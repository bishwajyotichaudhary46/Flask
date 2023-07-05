import mysql.connector
import json
import pandas as pd
class model:
    
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost",
                                            user="root",
                                            password="bishwa",
                                            database="pharmanuman")  
            self.cur = self.conn.cursor(dictionary=True)
            print("connection sucessfully")
        except:
            print("Error in connection")


    def user_signup_model(self):
        self.cur.execute("SELECT * FROM medicine_for_prediction")
        result = self.cur.fetchall()
        df = pd.DataFrame(result)
        df.to_csv("salesdata.csv",index=False)
        print(type(result[0]))

            

        