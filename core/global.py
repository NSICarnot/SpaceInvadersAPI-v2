import os
import mysql.connector as mysql

class Global:
    def __init__(self):
        self.db = mysql.connect(
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),
            user = os.getenv("DB_USERNAME"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_DATABASE")
        )
        self.cursor = self.db.cursor()
    
    def get_top(self, limit: int) -> list:
        self.cursor.execute(f"SELECT * FROM user_score ORDER BY score DESC LIMIT %s", (limit,))
        result = self.cursor.fetchall()
        return result
    
    def get_nb_of_entries(self) -> int:
        self.cursor.execute(f"SELECT COUNT(*) FROM user_score")
        result = self.cursor.fetchone()
        return result[0]
    
    def get_average(self) -> int:
        self.cursor.execute("SELECT score FROM user_score")
        result = self.cursor.fetchall()
        total = 0
        for score in result:
            total += score[0]
        return round(total / len(result), 2)