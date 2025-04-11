from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Room, summary="Створити кімнату")
def create_room(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    db_room = models.Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

@router.get("/", response_model=list[schemas.Room], summary="Отримати список кімнат")
def read_rooms(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Room).offset(skip).limit(limit).all()

@router.get("/{room_id}", response_model=schemas.Room, summary="Отримати кімнату за ID")
def read_room(room_id: int, db: Session = Depends(get_db)):
    room = db.query(models.Room).filter(models.Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@router.delete("/{room_id}", summary="Видалити кімнату")
def delete_room(room_id: int, db: Session = Depends(get_db)):
    room = db.query(models.Room).filter(models.Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    db.delete(room)
    db.commit()
    return {"message": "Room deleted"}
