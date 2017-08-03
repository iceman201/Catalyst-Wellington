import csv, sys, re, pymysql, argparse

# MySQL server login at http://www.phpmyadmin.co/index.php
db = pymysql.connect(
    host="sql12.freemysqlhosting.net",
    user="sql12188392",
    passwd="C11pJQ86vy",
    db="sql12188392"
)

cursor = db.cursor()

def valid_email(email):
    return bool(re.search('\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+', email))

def checkVersion():
    # This is a free sql host just for demo this project.
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print ("Database version : %s " % data)

def create_table():
    sql = "CREATE TABLE USERS(ID int(11) NOT NULL AUTO_INCREMENT, NAME varchar(32), SURNAME varchar(32), EMAIL varchar(32), PRIMARY KEY(ID)) \
ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 "
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.InternalError as error:
        code, message = error.args
        print ">>>>>>>>>>>>>", code, message
        db.rollback()

def insertUser(firstname, surname, email):
    sql = "INSERT INTO USERS(NAME, SURNAME, EMAIL) VALUES ('%s', '%s', '%s')" % \
          (firstname, surname, email)
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.InternalError as error:
        code, message = error.args
        print ">>>>>>>>>>>>>", code, message
        db.rollback()

def main():
    fileName = 'users.csv'
    create_table()
    with open(fileName, 'rb') as csvfile:
        fileReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        try:
            #skip first line
            next(fileReader)
            checkVersion()
            for row in fileReader:
                email = row[2]
                if valid_email(email):
                    firstName = row[0].replace("'", "\\'").title()
                    lastName = row[1].replace("'", "\\'").title()
                    email = email.replace("'", "\\'").lower()
                    insertUser(firstName, lastName, email)
            db.close()
            print "Insertion success"
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (fileName, fileReader.line_num, e))


if __name__ == '__main__':
    main()