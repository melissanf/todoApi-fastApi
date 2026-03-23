from sqlalchemy import column , Integer , String , Boolean , ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = column(Integer , primary_key= True , index = True)
    title = column(String , index = True)
    description = column(String , index = True)
    category_name = column(String , ForeignKey("categories.name"))
    completed = column(Boolean , default = False)
    owner_id = column(Integer , ForeignKey("users.id"))
    
    
    category = relationship("Category" , back_populates="tasks")
    owner = relationship("User" , back_populates="tasks")
