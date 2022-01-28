"""
MIT License
Copyright (C) 2021-2022, NkSama
Copyright (C) 2021-2022 Moezilla
Copyright (c) 2021, Sylviorus, <https://github.com/Sylviorus/BlueMoonVampireBot>
This file is part of @BlueMoonVampireBot (Antispam Telegram Bot)
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import json
from operator import index
from re import S
from pymongo import MongoClient
import os


class DATABASE:

    def __init__(self, db_url) -> None:
        self.db_url = db_url
        self.role_db = MongoClient(self.db_url)['Sylviorus']['CUSTOM_ROLES']

    def already_exists(self, user_id):
        return bool(x := self.db.find_one({"user_id": user_id}))

    def add_role(self, user_id, role):
        if self.role_db.find_one({"user_id": user_id}):
            self.role_db.update_one({"user_id": user_id},
                                    {"$set": {
                                        "role": role
                                    }})
        else:
            self.role_db.insert_one({"user_id": user_id, "role": role})

    def get_role(self, user_id):
        if self.role_db.find_one({"user_id": user_id}):
            role = self.role_db.find_one({"user_id": user_id})
            return {
                "user_id": role['user_id'],
                "role": role['role'],
                "status": True,
            }
        else:
            return {"status": False}


class LocalDb:

    def __init__(self, db_name) -> None:
        self.db_name = f"{db_name}.json"

    def create_db(self):
        with open(self.db_name, "w+") as x:
            x.write("""{\"hello" : "world\"}""")

    def add_reason(self, key, value):
        if os.path.exists(self.db_name):
            with open(self.db_name) as f:
                db = json.load(f)

            db.update({key: value})

            with open(self.db_name, "w") as f:
                json.dump(db, f)
        else:
            return "Create db first"

    def get_reason(self, key):
        if os.path.exists(self.db_name):
            with open(self.db_name, "r") as f:
                db = json.load(f)

            return db[key]

        else:
            return "No Data"
