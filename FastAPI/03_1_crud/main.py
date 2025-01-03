# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List, Optional
 
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
 
# class ItemUpdate(BaseModel):
#     name: str | None = None
#     description: str | None = None
#     price: float | None = None


# app = FastAPI()
 
# # 메모리 내 데이터 저장소
# items = {}


# @app.post("/items/{item_id}", response_model=Item)
# async def create_item(item_id: int, item: Item):
#     if item_id in items:
#         raise HTTPException(status_code=400, detail="Item already exists")
#     items[item_id] = item
#     return item

# @app.get("/items", response_model=)



# # put 전체 업데이트
# # patch 일부 업데이트

# @app.put("/items/{item_id}", respondse_model=Item)
# async def 


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# 메모리 내 데이터 저장소
items = {}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float


class ItemUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None


@app.post("/items/{item_id}", response_model=Item)
async def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = item
    return item


@app.get("/items", response_model=List[Item])
async def read_items():
    return list(items.values())


# PUT 메서드로 /items/{item_id} 경로를 처리하는 엔드포인트
# response_model=Item: 응답이 Item 모델의 형식을 따르도록 지정
@app.put("/items/{item_id}", response_model=Item)
async def update_item(
    item_id: int,  # URL에서 추출한 아이템 ID (경로 매개변수)
    item: ItemUpdate,  # 요청 본문에서 전달받은 업데이트할 데이터 (ItemUpdate 모델 기반)
):
    # 주어진 item_id가 현재 저장된 아이템 목록에 없는 경우
    if item_id not in items:
        # HTTP 404 에러를 발생시키고 "Item not found" 메시지를 포함
        raise HTTPException(status_code=404, detail="Item not found")

    # 현재 저장된 아이템 데이터를 가져옴
    stored_item = items[item_id]

    # exclude_unset=True: 클라이언트가 전송한 필드만 포함하여 딕셔너리로 변환
    # 즉, 업데이트되지 않은 필드는 제외됨
    update_data = item.dict(exclude_unset=True)

    # stored_item을 복사하고 update_data의 내용으로 업데이트
    # .copy(update=...): Pydantic 모델의 메서드로, 기존 데이터를 유지하면서
    # 전달받은 필드만 업데이트
    updated_item = stored_item.copy(update=update_data)

    # 업데이트된 아이템을 저장소에 저장
    items[item_id] = updated_item

    # 업데이트된 아이템 정보를 응답으로 반환
    # response_model=Item에 의해 Item 모델 형식으로 자동 변환됨
    return updated_item