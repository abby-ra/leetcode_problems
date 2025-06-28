class Solution:
    def dayOfTheWeek(self, day, month, year):
        import datetime
        date = datetime.date(year, month, day)
        return date.strftime("%A")
