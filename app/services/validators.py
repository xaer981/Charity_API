from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.constants import (DUPLICATE_PROJECT_MESSAGE,
                           MIN_AMOUNT_TO_CHECK_INVESTED,
                           PROJECT_AMOUNT_LESS_INVESTED_MESSAGE,
                           PROJECT_CLOSED_CANT_EDIT_MESSAGE,
                           PROJECT_INVESTED_CANT_REMOVE_MESSAGE)
from app.crud.charity_project import charityproject_crud
from app.models import CharityProject


async def check_name_duplicate(project_name: str,
                               session: AsyncSession) -> None:
    project_id = await charityproject_crud.get_project_id_by_name(project_name,
                                                                  session)

    if project_id is not None:

        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail=DUPLICATE_PROJECT_MESSAGE)


async def check_charityproject_not_invested(
        charityproject: CharityProject) -> None:
    if charityproject.invested_amount > MIN_AMOUNT_TO_CHECK_INVESTED:

        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail=PROJECT_INVESTED_CANT_REMOVE_MESSAGE)


async def check_charityproject_not_closed(
        charityproject: CharityProject) -> None:
    if charityproject.close_date:

        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail=PROJECT_CLOSED_CANT_EDIT_MESSAGE)


async def check_charityproject_amount_not_less_than_invested(
        obj_in,
        charityproject: CharityProject) -> None:
    if obj_in.full_amount:
        if obj_in.full_amount < charityproject.invested_amount:

            raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                                detail=PROJECT_AMOUNT_LESS_INVESTED_MESSAGE)