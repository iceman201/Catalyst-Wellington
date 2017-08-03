import csv, sys, re
import pymysql

db = pymysql.connect(
    host="sql12.freemysqlhosting.net",
    user="sql12188392",
    passwd="C11pJQ86vy",
    db="sql12188392"
)

cursor = db.cursor()

def valid_email(email):
  return bool(re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})', email))

def checkVersion():
    # This is a free sql host just for demo this project.
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print ("Database version : %s " % data)

def insertTable(firstname, lastname, email):
    sql = "INSERT INTO USERS(FIRST_NAME, LAST_NAME, EMAIL) VALUES ('%s', '%s', '%s')" % \
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
            checkVersion()
            for row in fileReader:
                firstName = row[0].replace("'","\\'").title()
                lastName = row[1].replace("'","\\'").title()
                email = row[2].replace("'","\\'")
                #insertTable(firstName, lastName, email)
            db.close()
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (fileName, fileReader.line_num, e))


if __name__ == '__main__':
    main()