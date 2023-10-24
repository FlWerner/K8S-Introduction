from _socket import gethostname

from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def root():
    return {"Mitteilung": "Hallo Demo: "f"{gethostname()}"}


@app.get("/add/")
async def say_hello(zahl1: int, zahl2: int):
    return {"ergebnis": f"{zahl1+zahl2}"}


