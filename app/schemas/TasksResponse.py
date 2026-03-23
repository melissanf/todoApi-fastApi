from pydantic import BaseModel
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    category_name: str
    completed: bool
    owner_id: int
    class Config :
        orm_mode = True
        