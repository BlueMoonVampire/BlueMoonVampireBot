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
        data = get(f"{self.base}user/{user}").json()
        return data

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
    if user in DEVS:
        return True
    else:
        return False


