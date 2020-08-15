#!/usr/bin/env python3

import os
import sys

class Entry:
    def __init__(self, project_name, github_link, gitignore_path):
        self.project_name = project_name
        self.github_link = github_link
        self.gitignore_path = gitignore_path
        self.gitignore_file = file_to_binary(gitignore_path)

    def file_to_binary(self, file_path):
        with open(file_path, 'rb') as file:
            blobData = file.read()

        return blobData


