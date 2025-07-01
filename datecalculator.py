class DateCalculator:
    def __init__(self, day: int, month: int, year: int):
        self.daysOfTheWeek = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.day = day

        if month < 3:
            self.month = month + 12
            self.year = year - 1
        else:
            self.month = month
            self.year = year

    def getDay(self):
        k = self.year % 100
        j = self.year // 100
        day_index = (self.day + (13 * (self.month + 1)) // 5 + k + (k // 4) + (j // 4) + 5 * j) % 7
        return self.daysOfTheWeek[day_index]

# Example 
datecalculator1 = DateCalculator(8, 7, 2006)
print(datecalculator1.getDay())  # Output: Saturday
