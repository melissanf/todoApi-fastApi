from sqlalchemy import column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base            

class Category(Base):
    __tablename__ = "categories"
    name = column(String , primary_key= True , index = True)
    
    
    tasks = relationship("Task" , back_populates="category")