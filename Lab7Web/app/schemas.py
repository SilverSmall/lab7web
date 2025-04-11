from pydantic import BaseModel

class RoomBase(BaseModel):
    number: str
    capacity: int

class RoomCreate(RoomBase):
    pass

class Room(RoomBase):
    id: int

    class Config:
        orm_mode = True
