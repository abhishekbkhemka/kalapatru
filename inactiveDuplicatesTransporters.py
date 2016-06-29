import os
import MySQLdb


DB = os.environ.get('PRODUCTION_DB', None)
if DB:
    db = MySQLdb.connect(DB, os.environ.get('DB_USER', ''), os.environ.get('DB_PASS', ''),
                         os.environ.get('DB_NAME', ''))
else:

    db = MySQLdb.connect('127.0.0.1', 'root', 'root', os.environ.get('DB_NAME', 'kalptaru1'))

query = '''SELECT address_ptr_id,name FROM  LR_transporter;

    '''

mapDict={}

cursor = db.cursor()
cursor.execute(query)
fetchAptResult = cursor.fetchall()
for obj in fetchAptResult:
    id= obj[0]
    name= str(obj[1])

    if not name in mapDict:
        updateQuery='''UPDATE LR_transporter set isActive=1 WHERE  address_ptr_id = '{id}' '''.format(id=id)
        cursor.execute(updateQuery)
        db.commit()
        mapDict[name]=True
    else:
        print id,name