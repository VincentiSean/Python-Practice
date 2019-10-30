import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import calendar
import datetime

weekdays = ["M", "Tu", "W", "Th", "F", "Sa", "Su"]
currentMonth = 0
currentYear = 0

class Clndr(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        global weekdays
        global currentMonth
        global currentYear

        # Set global variables to current date
        currentDate = str(datetime.datetime.now()).split("-")
        currentYear = currentDate[0]
        currentMonth = currentDate[1]

        # Display current month on launch
        currMonthText = datetime.datetime.now().strftime("%B")
        currMonthLabel = QLabel(currMonthText, self)
        currMonthLabel.resize(1000, 75)
        currMonthLabel.move(0, 10)
        currMonthLabel.setAlignment(Qt.AlignCenter)
        monthFont = QFont("Times", 36, QFont.Bold) 
        currMonthLabel.setFont(monthFont)

        # Set up left and right arrow buttons
        leftArrow = QPushButton("<", self)
        leftArrow.resize(50, 50)
        leftArrow.move(100, 25)
        leftArrow.clicked.connect(self.LeftArrow)

        rightArrow = QPushButton(">", self)
        rightArrow.resize(50, 50)
        rightArrow.move(860, 25)
        rightArrow.clicked.connect(self.RightArrow)

        # Set up weekday letters
        posX = 150
        for weekday in range(0, 7):
            weekdayLabel = QLabel(weekdays[weekday], self)
            weekdayLabel.resize(50, 20)
            weekdayLabel.setAlignment(Qt.AlignLeft)
            weekdayFont = QFont("Times", 12, QFont.Bold) 
            weekdayLabel.setFont(weekdayFont)
            weekdayLabel.move(posX, 110)
            posX += 115

        # TODO: set up on a loop to update after arrow clicks?
        # Get current month/year for calendar
        nowDate = datetime.datetime.now()
        nowDate = str(nowDate).split("-")
        nowMonth = nowDate[1]
        nowYear = nowDate[0]

        # Get the current month's days with calendar module
        cal = calendar.Calendar()

        posX = 100
        posY = 135
        counter = 1
        for day in cal.itermonthdays(int(nowYear), int(nowMonth)):
            dayLabel = QLabel(self)
            dayLabel.resize(115, 100)
            dayLabel.move(2 + posX, posY)
            dayLabel.setStyleSheet("border: 1px solid grey;")
            dayLabel.setAlignment(Qt.AlignTop)
            if day == 0:
                dayLabel.setText("")
            else:
                dayLabel.setText(str(day))

            if counter < 7:
                posX += 115
            elif counter == 7:
                counter = 0
                posX = 100
                posY += 100

            counter += 1
        

        self.setGeometry(400, 200, 1000, 700)
        self.setWindowTitle("Calendar")
        self.setFixedSize(1000, 700)
        self.show()

    # TODO: Clean up  this code into more bite sized chunksrepeated code)
    def LeftArrow(self):
        global currentMonth
        global currentYear

        newDay = 1
        currDate = datetime.datetime(int(currentYear), int(currentMonth), int(newDay))
        currDate = str(currDate).split("-")
        currMonth = currDate[1]
        currYear = currDate[0]
        newMonth = 0
        newYear = 0

        if (int(currMonth) - 1 < 1):
            newYear = int(currYear) - 1
            newMonth = 12
        else:
            newYear = currYear
            newMonth = int(currMonth) - 1

        newDate = datetime.datetime(int(newYear), int(newMonth), int(newDay))
        currentMonth = str(newDate).split("-")[1]
        currentYear = str(newDate).split("-")[0]
        print(currentMonth)
        print(currentYear)

    def RightArrow(self):
        global currentMonth
        global currentYear

        newDay = 1
        currDate = datetime.datetime(int(currentYear), int(currentMonth), int(newDay))
        currDate = str(currDate).split("-")
        currMonth = currDate[1]
        currYear = currDate[0]
        newMonth = 0
        newYear = 0

        if (int(currMonth) + 1 > 12):
            newYear = int(currYear) + 1
            newMonth = 1
        else:
            newYear = currYear
            newMonth = int(currMonth) + 1

        newDate = datetime.datetime(int(newYear), int(newMonth), int(newDay))
        currentMonth = str(newDate).split("-")[1]
        currentYear = str(newDate).split("-")[0]
        print(currentMonth)
        print(currentYear)


def main():
    app = QApplication(sys.argv)
    main = Clndr()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()