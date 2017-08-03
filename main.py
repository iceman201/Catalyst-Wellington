import csv, sys
import pymysql

db = pymysql.connect(
    host="sql12.freemysqlhosting.net",
    user="sql12188392",
    passwd="C11pJQ86vy",
    db="sql12188392"
)

cursor = db.cursor()

def checkVersion():
    # This is a free sql host just for demo this project.
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print ("Database version : %s " % data)
    db.close()

def createTable(firstname, lastname, email):
    sql = "INSERT INTO USERS(FIRST_NAME, \
           LAST_NAME, EMAIL) \
           VALUES ('%s', '%s', '%s')" % \
          (firstname, lastname, email)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()




def main():
    fileName = 'users.csv'
    with open(fileName, 'rb') as csvfile:
        fileReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        try:
            #skip first line
            next(fileReader)
            for row in fileReader:
                # row[0] first name
                # row[1] last name
                # row[2] email
                createTable(row[0],row[1],row[2])
                print row
            db.close()
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (fileName, fileReader.line_num, e))


if __name__ == '__main__':
    main()