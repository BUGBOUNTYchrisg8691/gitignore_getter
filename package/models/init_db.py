#!/usr/bin/env python3

import os
import sqlite3
import sys
from package.models.database import Database


class NewDatabase(Database):
    def __init__(self, db_path):
        super().__init__('NewDatabase')

    def create_table(self):
        sql_statement = '''CREATE TABLE IF NOT EXISTS gitignore_entries(
        project_id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT NOT NULL, github_link TEXT NOT NULL,
        gitignore_file BLOB NOT NULL);'''

        self.cursor.execute(sql_statement)
        self.conn.commit()
