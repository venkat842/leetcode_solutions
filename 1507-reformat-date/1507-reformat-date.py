from datetime import datetime
class Solution:
    def reformatDate(self, date: str) -> str:
        date = date.replace("th","")
        date = date.replace("nd","")
        date = date.replace("rd","")
        date = date.replace("st","")
        date_obj = datetime.strptime(date,"%d %b %Y")
        date_obj_2 = datetime.strftime(date_obj,"%Y-%m-%d")
        return (str(date_obj)[:10])