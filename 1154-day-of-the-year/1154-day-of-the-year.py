class Solution:
    def dayOfYear(self, date: str) -> int:
        date = list(map(int,date.split("-")))
        date_obj_1 = datetime.date(date[0],date[1],date[2])
        date_obj_2 = datetime.date(date[0],12,31)
        diff = date_obj_2 - date_obj_1
        year = date_obj_1.year 
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return (366 - diff.days)
        else:
            return (365 - diff.days)