from datetime              import *

def getServerDateFromStr(dateStr):
     if dateStr != '' and dateStr != None:
        try:    return datetime.strptime(dateStr,"%d-%m-%Y")
        except: return datetime.strptime(dateStr,"%d-%m-%Y %H:%M:%S")
     else: return None
