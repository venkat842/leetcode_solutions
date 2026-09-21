import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date_obj = datetime.date(year,month,day)
        week = datetime.datetime.strftime(date_obj,"%A")
        return week