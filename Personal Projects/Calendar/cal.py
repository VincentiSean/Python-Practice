import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import calendar
import datetime

weekdays = ["M", "Tu", "W", "Th", "F", "Sa", "Su"]
class Clndr(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        global weekdays

        currMonth = datetime.datetime.now().strftime("%B")
        self.currMonthLabel = QLabel(self)
        self.currMonthLabel.resize(1000, 75)
        self.currMonthLabel.move(0, 10)
        self.currMonthLabel.setText(currMonth)
        self.currMonthLabel.setAlignment(Qt.AlignCenter)
        monthFont = QFont("Times", 36, QFont.Bold) 
        self.currMonthLabel.setFont(monthFont)

        posX = 150
        for weekday in range(0, 7):
            self.weekdayLabel = QLabel(self)
            self.weekdayLabel.resize(50, 20)
            self.weekdayLabel.setAlignment(Qt.AlignLeft)
            weekdayFont = QFont("Times", 12, QFont.Bold) 
            self.weekdayLabel.setFont(weekdayFont)
            self.weekdayLabel.move(posX, 110)
            self.weekdayLabel.setText(weekdays[weekday])
            posX += 115

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
            self.dayLabel = QLabel(self)
            self.dayLabel.resize(115, 100)
            self.dayLabel.move(2 + posX, posY)
            self.dayLabel.setStyleSheet("border: 1px solid grey;")
            self.dayLabel.setAlignment(Qt.AlignTop)
            if day == 0:
                self.dayLabel.setText("")
            else:
                self.dayLabel.setText(str(day))

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

def main():
    app = QApplication(sys.argv)
    main = Clndr()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()