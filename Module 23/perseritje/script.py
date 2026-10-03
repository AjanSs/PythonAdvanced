from typing import Optional
from pydentic import BaseModel
from fastapi import FastAPI

app=FastAPI

class User(BaseModel):
    id: int
    name: str
    age: conint(gt=0)
    email:constr(min_length=5)
    gender:Optional[str]=None


def main():
    user1:User=User(id=1,name="John",age=21,email="xyz@gmail.com",gender="Male")


if __name__=="__main__":
    main()