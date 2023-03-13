"""for sorting planner list by datetime: https://www.techiedelight.com/sort-list-of-objects-python/"""

import datetime

class item:
    def __init__(self, _name, _year, _month, _day, _time, _desc=""):
        self.name = _name
        self.date = _month + "/" + _day + "/" + _year
        self.time = _time
        self.desc = _desc
        self.status = "TO-DO"
        self.due_date = self.date + " at " + _time

        self.year = int(_year)
        self.month = int(_month)
        self.day = int(_day)
        
        self.hour = int(_time.split(":")[0])
        self.min = int(_time.split(":")[1])
        self.sec = int(_time.split(":")[2])


    def printItem(self):
        self.checkStatus()
        if self.desc == "":
            print(f"{self.name}\n{self.status:5} - {self.due_date}")
        else:
            print(f"{self.name}\n{self.status:5} - {self.due_date}\n{self.desc}")
    
    def editDate(self, newYear, newMonth, newDay, newTime):
        self.date = newMonth + "/" + newDay + "/" + newYear
        self.year = int(newYear)
        self.month = int(newMonth)
        self.day = int(newDay)
        self.due_date = self.date + " at " + self.time

    def editTime(self, newTime):
        self.time = newTime

    def editDesc(self, newDesc):
        self.desc = newDesc

    def checkStatus(self):
        d = datetime.datetime(self.year, self.month, self.day)
        n = datetime.datetime.now()
        if d < n:
            self.status = "PASSED"

    def getDateTime(self):
        return datetime.datetime(self.year, self.month, self.day, self.hour, self.min, self.sec)

class planner:
    def __init__(self, _name):
        self.items = []
        self.name = _name

    def addItem(self, _name, _year, _month, _day, _time, _desc=""):
        self.items.append(item(_name, _year, _month, _day, _time, _desc))

    def sortPlanner(self):
        self.items.sort(key=lambda x: x.getDateTime())
        pass

    def printPlanner(self):
        self.sortPlanner()
        for i, it in enumerate(self.items):
            print(str(i+1) + ". ", end='')
            it.printItem()
            print()

if __name__ == "__main__":
    example = item("Grocery shopping", "2022", "12", "05", "19:00:00", "Go to the store! The wife says we need to eat")
    example.printItem()
    print(example.getDateTime())
    
    print("\n\n")
    
    p = planner("PUMP")
    p.addItem("cheese time", "2023", "3", "25", "13:05:00", "i love cheese")
    p.addItem("John's Birthday Party", "2023", "1", "5", "13:00:00")
    p.addItem("Grocery shopping", "2022", "12", "05", "19:00:00", "Go to the store! The wife says we need to eat")
    p.addItem("baseball game", "2023", "3", "25", "13:00:00", "LETS GO RED SOX")
    p.printPlanner()

