from datetime              import *

def getServerDateFromStr(dateStr):
     if dateStr != '' and dateStr != None:
        try:    return datetime.strptime(dateStr,"%m-%d-%Y")
        except: return datetime.strptime(dateStr,"%m-%d-%Y %H:%M:%S")
     else: return None
