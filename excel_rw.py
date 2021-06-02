import pytz #libreria para la timezone de todo el mundo
import pandas as pd #libreria para leer el excel
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from datetime import datetime
import os
TIME_ZONE = os.getenv('TIME_ZONE')
tz_bsas = pytz.timezone(TIME_ZONE) #timezone de argentina

def start():
    datetime_bsas = datetime.now(tz_bsas)  # guarda la hora de bsas
    # formatea la hora y la guarda en la variable hora
    hora = datetime_bsas.strftime("%d/%m/%Y:%H:%M")
    #AL FORMATO HAY QUE AÑADIRLE LOS SEGUNDOS ASI NO ESTA TODO EL MINUTO ENTERO ENVIANDO EL MENSAJE HACER ESTO ES LO PROXIMO
    #POR AHORA ESTA ES LA FUNCIÓN QUE ESTOY EDITANDO, ESTA IGUAL A "start", SOLO POR LO COMENTADO ARRIBA. LO QUE FALTA ES
    #ACTUALIZAR EL EXCEL UNA VEZ QUE HAYA MANDADO EL MENSAJE. LO ESTOY INTENTANDO EN ./test.py
    #-----------------FIX-----------------
    #El error de arriba lo arreglé updateando la fecha del excel que valida la equidad por la nueva fecha, entonces
    #encuentra la equidad y la cambia.
    print(hora, "hora actual")
    xls = pd.read_excel("horarios.xlsx", sheet_name="Hoja 1", )
    wb = Workbook()
    ws = wb.active
    c = -1
    for col in xls["Dia"]:
        c = c+1
        print(col)
        if str(col) == hora:
            fecha = xls.at[c, "Dia"]
            fecha_obj = datetime.strptime(fecha, "%d/%m/%Y:%H:%M")
            xls.at[c, "Dia"] = datetime.strftime(
            fecha_obj + pd.Timedelta("2 W"), "%d/%m/%Y:%H:%M")
            xls = pd.DataFrame(xls)
            for r in dataframe_to_rows(xls, index=False, header=True):
                ws.append(r)
                ws.title = "Hoja 1"
                wb.save(filename='horarios.xlsx')
            return (200,str(xls.at[c,"Materia"]),str(xls.at[c,"Hora"])) 

def getDates():
    xls = pd.read_excel("horarios.xlsx", sheet_name="Hoja 1", )
    xls = pd.DataFrame(xls)
    return xls.to_string(index=False)
