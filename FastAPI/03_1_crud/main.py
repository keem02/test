from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
 
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
 
class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None


app = FastAPI()
 
# 메모리 내 데이터 저장소
items = {}


@app.post("/items/{item_id}", response_model=Item)
async def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = item
    return item

@app.get("/items", response_model=)



# put 전체 업데이트
# patch 일부 업데이트

@app.put("/items/{item_id}", respondse_model=Item)
async def 