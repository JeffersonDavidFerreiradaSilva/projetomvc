import mysql.connector

class StudentModel:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="seu_usuario",
            password="sua_senha",
            database="seu_banco_de_dados"
        )
        self.cursor = self.db.cursor()

    def save_student(self, name, age, weight):
        query = "INSERT INTO students (name, age, weight) VALUES (%s, %s, %s)"
        values = (name, age, weight)
        self.cursor.execute(query, values)
        self.db.commit()

    def close(self):
        self.cursor.close()
        self.db.close()
