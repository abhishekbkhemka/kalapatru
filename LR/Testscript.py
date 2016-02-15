import datetime
# val='[datetime.datetime(2015, 12, 14, 0, 0, tzinfo=)]'.replace('=','=None').replace('[','').replace(']','')
# res=eval(val).strftime("%d-%m-%y")
# print res

res=eval('datetime.datetime(2015, 12, 14, 0, 0, tzinfo=None)').strftime("%d-%m-%y")
print res

