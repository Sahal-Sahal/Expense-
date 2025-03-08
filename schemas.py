from pydantic import BaseModel
from typing import List
class ExpenseBase(BaseModel):
    name:str
    amount:float
    category:str
    
class ExpenseCreate(ExpenseBase):
    pass

class ExpneseResponse(ExpenseBase):
    id:int
    
    class Config:
        orm_mode=True
