#ch 10.1

from fastapi import FastAPI #importing FastAPI class from FastAPI package
from pydantic import BaseModel, Field #helps validate data and check whether it matches a defined structure

app = FastAPI(title="Student API")

class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    division: str

@app.get("/")
def home():
    return {
        "message":"Welcome to Student API"
        }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "student-api"
        }

@app.post("/students", status_code=201)
def create_student(student: StudentCreate):
    return {
        "message": "Student received successfully",
        "student" : student
    }