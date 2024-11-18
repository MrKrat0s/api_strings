import uuid
import random
from string import ascii_lowercase, digits

from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse


class String:
    def __init__(self, string: str):
        self.result = string
        self.id = str(uuid.uuid4())


STRINGS = []

app = FastAPI()


@app.get("/")
async def main():
    print("START")
    return FileResponse("index.html")


@app.get("/api/string")
def get_string():
    return STRINGS


@app.get("/api/string/{id}")
def get_string_id(id):
    string = find_string(id)
    if string is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"message": "Строка не найдена"}
        )
    return {'result': string.result}


@app.post("/api/string")
def post_string(data=Body()):
    string = String(string=create_string(palindrome=data["palindrome"]))
    STRINGS.append(string)
    return string


def find_string(id):
    for string in STRINGS:
        if string.id == id:
            return string
    return None


def create_string(palindrome: bool):
    def is_palindrome(x):
        return str(x) == str(x)[::-1]

    i = ''
    if palindrome:
        i = "".join(random.choices(ascii_lowercase + digits, k=5))
        i += i[::-1]
    else:
        while is_palindrome(i):
            i = "".join(random.choices(ascii_lowercase + digits, k=10))
    return i