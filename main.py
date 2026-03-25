from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from datetime import datetime


app = FastAPI()


@app.get("/{date_path}/")
async def get_date(date_path: str):
    today = datetime.now()

    expected = today.strftime("%d%m%y")

    if date_path != expected:
        return JSONResponse(
            status_code=404,
            content={"error": "Not found"}
        )

    return {
        "date": today.strftime("%d-%m-%Y"),
        "login": "seerb",
    }


@app.get("/api/rv/{text}/")
async def reverse_text(text: str):
    for symb in text:
        if symb not in "abcdefghijklmnopqrstuvwxyz":
            return JSONResponse(
                status_code=400,
                content={"error": "only small engl sybmls"}
            )
    
    return PlainTextResponse(text[::-1])
