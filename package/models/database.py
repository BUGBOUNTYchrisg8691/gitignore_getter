#!/usr/bin/env python3

import os
import sqlite3
import sys

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.dbname = os.path.basename(db_path)
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def add_entry(self, project_name, github_link, gitignore_path,
                  **entry_info):
        sql_statement = '''INSERT INTO gitignore_entries(
        project_name, github_link, gitignore_file)
        VALUES(?, ?, ?);'''

        gitignore_file = convert_to_binary(gitignore_path)

        self.cursor.execute(sql_statement, (project_name, github_link,
                                            gitignore_file))
        
        self.conn.commit()

    def del_entry(self, project_id):
        sql_statement = '''DELETE FROM gitignore_entries
        WHERE project_id = ?;'''

        self.cursor.execute(sql_statement, (project_id))
        self.conn.commit()

    def edit_entry(self, option, project_id, new_item):
        if option.lower() == 'name':
            sql_statement = '''UPDATE gitignore_entries
        SET
            project_name = ?,
        WHERE
            project_id = ?;'''

        elif option.lower() == 'link':
            sql_statement = '''UPDATE gitignore_entries
        SET
            github_link = ?,
        WHERE
            project_id = ?;'''

        elif option.lower() == 'file':
            sql_statement = '''UPDATE gitignore_entries
        SET
            gitignore_file = ?
        WHERE
            project_id = ?;'''

        self.cursor,execute(sql_statement, (new_item))
        self.conn.commit()

    def get_project_id(self, project_name):
        sql_query = '''SELECT (project_id) FROM gitignore_entries
        WHERE project_name = ?;'''

        self.cursor.execute(sql_statement, (project_name))
        pro_id = self.cursor.fetchone()[0]

        return pro_id
