from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from .import schemas,crud
from .database import get_db
import models

app=FastAPI()

@app.post("/expenses/",response_model=schemas.ExpneseResponse)
def create_expense(expense:schemas.ExpenseCreate, db:Session=Depends(get_db)):
    return crud.create_expense(db=db,expense=expense)

@app.get("/expenses/",response_model=list[schemas.ExpneseResponse])
def get_expenses(db:Session=Depends(get_db)):
    return crud.get_expenses(db=db)

@app.get("/expenses/month/{year}/{month}/",response_model=list[schemas.ExpneseResponse])
def get_expenses_by_month(year:int,month:int,db:Session=Depends(get_db)):
    return crud.get_expenses_by_month(db=db,year=year,month=month)

@app.get("/totals/")
def get_total_expenses(db:Session=Depends(get_db)):
    return crud.get_total_expenses(db=db)
