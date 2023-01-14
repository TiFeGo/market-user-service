from typing import List, Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.models import user
from src.schemas import schemas
from src.core import tracing_tools


@tracing_tools.trace_it('Service', 'Create new user')
async def new_user_register(
        request: schemas.User,
        database: Session
) -> user.User:
    new_user = user.User(name=request.name, email=request.email, password=request.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


@tracing_tools.trace_it('Service', 'Get all users')
async def all_users(
        database: Session
) -> List[user.User]:
    users = database.query(user.User).all()
    return users


@tracing_tools.trace_it('Service', 'Get user by id')
async def get_user_by_id(
        user_id: int,
        database: Session
) -> Optional[user.User]:
    user_info = database.query(user.User).get(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found!")
    return user_info


@tracing_tools.trace_it('Service', 'Delete user by id')
async def delete_user_by_id(
        user_id: int,
        database: Session
) -> None:
    database.query(user.User).filter(user.User.id == user_id).delete()
    database.commit()
