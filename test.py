import pandas as pd
from datetime import datetime
import xlwt

xls = pd.read_excel("horarios.xls", sheet_name="Hoja 1")
for col in xls["Dia"]:

    if str(col) == "06/05/2021:19:30:00":
        fecha = xls.at[2,"Dia"]
        fecha_obj = datetime.strptime(fecha,"%d/%m/%Y:%H:%M:%S")
        xls.at[2,"Dia"] = datetime.strftime(fecha_obj + pd.Timedelta("5 minutes"),"%d/%m/%Y:%H:%M:%S")
        print(xls.head(3))
        print("hola")
xls = pd.DataFrame(xls)
print(xls)
xls.to_excel('horarios.xls', sheet_name='Hoja 1', index=False)

#import schedule, time
#def hola():
#    print("toma")

#schedule.every().day.at("00:56").do(hola)
#while True:
#    schedule.run_pending()
#    time.sleep(1)

