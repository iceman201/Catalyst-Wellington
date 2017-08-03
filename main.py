import csv, sys
import pymysql.connections


def sqlSetup():
    # This is a free sql host just for demo this project.
    conn = pymysql.connect(
        host='sql12.freemysqlhosting.net',
        user='sql12188392',
        passwd='jiaoliguo',
        db='db',
        autocommit=True
    )




def read():
    fileName = 'users.csv'
    with open(fileName, 'rb') as csvfile:
        fileReader = csv.reader(csvfile, delimiter=',', quotechar='|')
        try:
            for row in fileReader:
                # row[0] first name
                # row[1] last name
                # row[2] email
                print row
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (fileName, fileReader.line_num, e))



read()