from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Event-Driven Ticket System")

@app.get("/")
def root():
    return {"message": "Event-driven ticket system is running"}

app.include_router(router)