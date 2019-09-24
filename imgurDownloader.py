#! python3
# imgurDownloader.py - This project takes an argument and searches imgur with the user input
#   and proceeds to download all image search results.

import bs4, sys, requests, os

# Get user input
tag = sys.argv[1]

# Make a directory for the images to be stored
directory = 'imgurSearch(' + tag + ')'
os.makedirs(directory, exist_ok=True)

# Connect to imgur with tag from arguement and search
for x in range(10):
    website = 'https://imgur.com/search/score/all/page/' + str(x+1) + '?scrolled&q=' + tag + '&'
    try:
        res = requests.get(website)
            # print(website)
        print('Connecting to imgur...')
        res.raise_for_status()


        # Get the soup to find the image links from search results
        soupy = bs4.BeautifulSoup(res.text, 'lxml')
            # print(soupy)
        imgElem = soupy.select('img')

        for i in range(len(imgElem)):  
            imgSrc = 'https:' + imgElem[i].get('src')
            # print(imgSrc)

            # Download the image     
            res = requests.get(imgSrc)
            res.raise_for_status()
            
            # Save image to folder
            imageFile = open(os.path.join(directory,  os.path.basename(imgSrc)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

    except Exception as exc:
        print('There was a problem: %s' % (exc))

print('Could not find any more images.')