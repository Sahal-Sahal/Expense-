from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from .import models,schemas


def create_expense(db:Session,expense:schemas.ExpenseCreate):
    db_expense=models.Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    
    
def get_expense(db:Session):
    return db.query(models.Expense).all()

def get_expenses_by_month(db:Session,year:int,month:int):
    return db.query(models.Expense.filter(func.extract('year',models.Expense.craeted_at)==year,func.extract('month',models.Expense.craeted_at)==month).all())

def get_total_expenses(db:Session):
    total_expense=db.query(func.sum(models.Expense.amount)).scalar or 0
    return {"total_expense":total_expense}
    