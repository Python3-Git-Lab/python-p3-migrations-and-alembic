from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String
from datetime import datetime

engine = create_engine('sqlite:///students.db')

Base= declarative_base()

class Student(Base):
    __tablename__='students'

    id = Column (Integer(), primary_key= True)
    name= Column(String())
    email =Column(Integer())
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now)

    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.grade}"