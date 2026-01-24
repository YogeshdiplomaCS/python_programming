class date:
    def __init__(self,a,b,c):
        self.d=a
        self.m=b
        self.y=c
    def day(self):
        print("Day=",self.d)
    def month(self):
        print("Month=",self.m)
    def year(self):
        print("Year=",self.y)
    def monthName(self):
        months=["Unknown","January","February","March","April","May",
            "June","July","August","september","October","November","December"]
        print("Month_name=",months[self.m])
    def isLeapYear(self):
        if(self.y % 400 ==0) and (self.y % 100 == 0 ):
         print(" it is a Leap Year")
        elif(self.y % 4 ==0) and (self.y % 100 != 0 ):
         print(" it is a Leap Year")
        else:
            print(" it is not a Leap Year")

d1 = date(12,5,2009)
d1.day()
d1.month()
d1.year()
d1.isLeapYear()
