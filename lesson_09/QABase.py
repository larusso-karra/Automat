from sqlalchemy import create_engine
from sqlalchemy.sql import text


class QABase:

    def __init__(self, db_connection_string):
        self.db = create_engine(db_connection_string)

    def db_connection(self):
        names = self.db.table_names()
        return names

    def get_info_group_student(self):
        sql_statement = text("select * from group_student;")
        return self.db.execute(sql_statement).fetchall()

    def get_info_subject(self):
        sql_statement = text("select * from subject;")
        return self.db.execute(sql_statement).fetchall()

    def get_info_subject_by_subject_id(self, subject_id):
        sql_statement = text(
            "select * from subject where subject_id = :subject_id;"
            )
        params = {
            "subject_id": subject_id
        }
        return self.db.execute(sql_statement, params).fetchall()

    def get_info_subject_by_subject_title(self, subject_title):
        sql_statement = text(
            "select * from subject where subject_title = :subject_title;"
            )
        params = {
            "subject_title": subject_title
        }
        return self.db.execute(sql_statement, params).fetchall()

    def count_from_subject(self):
        sql_statement = ("select count(*) from subject")
        row = self.db.execute(sql_statement).fetchall()
        count = row[0]["count"]
        return count

    def insert_into_subject(self, subject_id, subject_title):
        sql_statement = text(
            "insert into subject values (:subject_id, :subject_title)"
            )
        params = {
            "subject_id": subject_id,
            "subject_title": subject_title
        }
        self.db.execute(sql_statement, params)

    def update_subject_title(self, subject_title, subject_id):
        sql_statement = text(
            "update subject set subject_title = :subject_title where subject_id = :subject_id"
            )
        params = {
            "subject_title": subject_title,
            "subject_id": subject_id
        }
        self.db.execute(sql_statement, params)

    def update_subject_id(self, subject_id, subject_title):
        sql_statement = text(
            "update subject set subject_id = :subject_id where subject_title = :subject_title"
            )
        params = {
            "subject_id": subject_id,
            "subject_title": subject_title
        }
        self.db.execute(sql_statement, params)

    def delete_from_subject(self, subject_id):
        sql_statement = text(
            "delete from subject where subject_id = :subject_id"
            )
        params = {
            "subject_id": subject_id
        }
        self.db.execute(sql_statement, params)