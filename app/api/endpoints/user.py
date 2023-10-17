from http import HTTPStatus

from fastapi import APIRouter, HTTPException

from app.constants import (AUTH_PREFIX, AUTH_TAG, DELETE_NOT_ALLOWED_MESSAGE,
                           JWT_PREFIX, USERS_PREFIX, USERS_TAG)
from app.core.user import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead, UserUpdate

router = APIRouter()

router.include_router(fastapi_users.get_auth_router(auth_backend),
                      prefix=JWT_PREFIX,
                      tags=[AUTH_TAG])
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate),
                      prefix=AUTH_PREFIX,
                      tags=[AUTH_TAG])
router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate),
                      prefix=USERS_PREFIX,
                      tags=[USERS_TAG])


@router.delete('/users/{id}',
               tags=[USERS_TAG],
               deprecated=True)
def delete_user(id: str):
    """Не используйте удаление, деактивируйте пользователей."""

    raise HTTPException(status_code=HTTPStatus.METHOD_NOT_ALLOWED,
                        detail=DELETE_NOT_ALLOWED_MESSAGE)
