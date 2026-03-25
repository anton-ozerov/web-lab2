from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=[
        "x-test",
        "ngrok-skip-browser-warning",
        "Content-Type",
        "Accept",
        "Access-Control-Allow-Headers",
    ],
)


@app.api_route("/result4/", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
async def result4(request: Request):
    x_test = request.headers.get("x-test")

    body_bytes = await request.body()
    body = body_bytes.decode("utf-8") if body_bytes else ""

    return {
        "message": "seerb",
        "x-result": x_test,
        "x-body": body
    }
