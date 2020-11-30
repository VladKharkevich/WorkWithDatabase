from typing import Dict, List, Tuple

import mysql.connector

from .iconnector import IConnector


class MySQLConnector(IConnector):
    def __init__(self, user, password, database, host="127.0.0.1"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        self.db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.db.cursor(dictionary=True)

    def insert_students_and_rooms_data(self, students_data: List[Dict], rooms_data: List[Dict]) -> None:
        # checking the table room for having data, just idempotent query

        query = "SELECT count(*) FROM room"
        self.cursor.execute(query)
        count_of_rooms: Dict = self.cursor.fetchone()
        if count_of_rooms["count(*)"] == 0:
            query = """
                     INSERT INTO room
                     (room_id, name)
                     VALUES (%(id)s, %(name)s)
                    """
            self.cursor.executemany(query, rooms_data)

        query = "SELECT count(*) FROM student"
        self.cursor.execute(query)
        count_of_students: Dict = self.cursor.fetchone()
        if count_of_students["count(*)"] == 0:
            query = """
                     INSERT INTO student
                     (student_id, name, birthday, sex, room_id)
                     VALUES (%(id)s, %(name)s, %(birthday)s, %(sex)s, %(room)s)
                    """
            self.cursor.executemany(query, students_data)

    def select_list_room_with_count_of_students(self) -> List[Dict]:
        query = """
                SELECT r.room_id, r.name, count(*) AS count
                FROM room r
                JOIN student st ON r.room_id = st.room_id
                GROUP BY 1, 2
                ORDER BY 3
                """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def select_top_5_rooms_with_the_smallest_average_age(self) -> List[Dict]:
        query = """
                SELECT r.room_id, r.name, avg(st.birthday) AS average_age 
                FROM room r
                JOIN student st ON r.room_id = st.room_id
                GROUP BY 1, 2
                ORDER BY 3 DESC
                LIMIT 5
                """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def select_top_5_rooms_with_the_biggest_age_difference(self) -> List[Dict]:
        query = """
                SELECT r.room_id, r.name, max(st.birthday) - min(st.birthday) AS age_difference
                FROM room r
                JOIN student st ON r.room_id = st.room_id
                GROUP BY 1, 2
                ORDER BY 3 DESC
                LIMIT 5
                """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def select_list_room_with_different_sex_of_students(self) -> List[Dict]:
        query = """
                SELECT DISTINCT r.room_id, r.name
                FROM room r
                WHERE EXISTS (
                    SELECT * FROM student st
                        WHERE st.sex = 'M'
                        AND st.room_id = r.room_id
                ) AND EXISTS (
                    SELECT * FROM student st
                        WHERE st.sex = 'F'
                        AND st.room_id = r.room_id
                )
                """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def disconnect(self):
        if self.db.is_connected():
            self.cursor.close()
            self.db.close()
