import hashlib
import json
import os
import mysql.connector as mysql

class Player:
    def __init__(self, pseudo: str):
        self.pseudo = pseudo
        self.db = mysql.connect(
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_DATABASE")
        )
        self.cursor = self.db.cursor()

    def change_score(self, score: int) -> None:
        if self.get_score() == None:
            self.cursor.execute(f"INSERT INTO user_score (pseudo, score) VALUES (%s, %s)", (self.pseudo, score))
            self.db.commit()
        else:
            self.cursor.execute(f"UPDATE user_score SET score = %s WHERE pseudo = %s", (score, self.pseudo))
            self.db.commit()

    def get_score(self) -> int | None:
        self.cursor.execute(f"SELECT score FROM user_score WHERE pseudo = %s", (self.pseudo,))
        result = self.cursor.fetchone()
        if result == None:
            return 0
        elif len(result) == 0:
            return 0
        else:
            return result[0]

    def get_md5(self) -> str:
        return hashlib.md5(self.pseudo.encode('utf-8')).hexdigest()