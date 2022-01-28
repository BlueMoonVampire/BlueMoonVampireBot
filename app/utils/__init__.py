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

from requests import get, post
from config import DEV, LOGS
# from .. import LOGS


class Sylviorus:

    def __init__(self, token) -> None:
        self.devs = DEVS
        self.logs = LOGS
        self.base = "https://sylviorus-api.up.railway.app/"
        self.admin_token = token

    def check(self, user: int) -> dict:
        return get(f"{self.base}user/{user}").json()

    def ban(self, user: int, reason: str, enforcer: int) -> str:
        data = {
            "user": user,
            "reason": reason,
            "enforcer": enforcer,
            "admin_token": self.admin_token
        }
        res = post(f"{self.base}ban", json=data)
        return res.text

    def unban(self, user):
        data = {"user": user, "admin_token": self.admin_token}
        res = post(f"{self.base}unban", json=data)
        return res.text


def check_dev(user: int):
    return user in DEVS


