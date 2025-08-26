from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from datetime import datetime
import uuid
import debugpy

app = FastAPI(
    title="TODO API",
    description="A simple TODO API built with FastAPI",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class Todo(TodoBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# In-memory storage (replace with database in production)
todos_db = {}

@app.get("/")
async def root():
    return {"message": "Welcome to TODO API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}

@app.get("/todos", response_model=List[Todo])
async def get_todos():
    """Get all todos"""
    return list(todos_db.values())

@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: str):
    """Get a specific todo by ID"""
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos_db[todo_id]

@app.post("/todos", response_model=Todo, status_code=201)
async def create_todo(todo: TodoCreate):
    """Create a new todo"""
    todo_id = str(uuid.uuid4())
    now = datetime.now()
    
    new_todo = Todo(
        id=todo_id,
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        created_at=now,
        updated_at=now
    )
    
    todos_db[todo_id] = new_todo
    return new_todo

@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: str, todo_update: TodoUpdate):
    """Update a todo"""
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    existing_todo = todos_db[todo_id]
    
    # Update only provided fields
    update_data = todo_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(existing_todo, field, value)
    
    existing_todo.updated_at = datetime.now()
    todos_db[todo_id] = existing_todo
    
    return existing_todo

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str):
    """Delete a todo"""
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    del todos_db[todo_id]
    return {"message": "Todo deleted successfully"}

@app.patch("/todos/{todo_id}/toggle")
async def toggle_todo(todo_id: str):
    """Toggle todo completion status"""
    if todo_id not in todos_db:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo = todos_db[todo_id]
    todo.completed = not todo.completed
    todo.updated_at = datetime.now()
    
    return todo

if __name__ == "__main__":
    # Enable remote debugging
    debugpy.listen(("0.0.0.0", 5678))
    print("⏳ Debugger is listening on port 5678...")
    # debugpy.wait_for_client()  # Uncomment to wait for debugger

    uvicorn.run(app, host="0.0.0.0", port=8000)
