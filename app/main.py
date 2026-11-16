#ch 5 
#creating first fastapi server

from fastapi import FastAPI #importing FastAPI class from FastAPI package
app = FastAPI(title="Student API") #creating FastAPI application

@app.get("/") #decorator telling when GET request arrives at the / path, call the function defined below

def home(): #defines a function called home
    return{ #returns a python dictionary 
        "message": "Welcome to Student API"
    }

#ch 6
#health check 

@app.get("/health")

def health_check():

    return {
        "status":"ok",
        "service":"student-api"
    }