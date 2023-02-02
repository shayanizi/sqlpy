import mysql.connector

class DataBase:
    def __init__(
        
        self, 
        name,
        password,
        host,
        database):
        
        self.name = name
        self.password = password
        self.host = host
        self.database = database
    def connectDb(self):
        try:
            with mysql.connector.connect(
                user=self.name,
                password=self.password,
                host=self.host,
                database=self.database) as cnx:
                curser=cnx.cursor()
                getOrder=input("set Order >> ")
                if getOrder==("shel"):
                    curser.execute("SELECT * FROM coin;")
                    for i in curser:
                        print(i)
                elif getOrder==("cdb"):
                    nameDB = input("enter your name Database >> ")
                    curser.execute("CREATE DATABASE {}".format(nameDB))
                    print("create success!")
                elif getOrder==("shdb"):
                    curser.execute("SHOW DATABASES")
                    for i in curser:
                        print(i)

        except mysql.connector.Error as error:
            print(error)

infoDB = DataBase(
    input("insert username >> "),
    input("insert password >>"),
    input("insert host >>"),
    input("insert database >>"))
infoDB.connectDb()

