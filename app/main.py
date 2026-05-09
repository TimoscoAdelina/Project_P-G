from fastapi import FastAPI

app = FastAPI(title="Manufacturing Quality API")

@app.get("/")
def home():
    return {"message": "Manufacturing Quality API is running"}
