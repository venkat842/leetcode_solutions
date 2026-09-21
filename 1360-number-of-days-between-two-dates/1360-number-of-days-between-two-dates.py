import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
       import datetime
       date1 = list(map(int,date1.split("-")))
       date2 = list(map(int,date2.split("-")))
       date_obj_1 = datetime.date(date1[0],date1[1],date1[2])
       date_obj_2 = datetime.date(date2[0],date2[1],date2[2])
       diff = date_obj_2 - date_obj_1
       return abs(diff.days)