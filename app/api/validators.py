from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.constants import PROJECT_NOT_FOUND_MESSAGE
from app.crud.charity_project import charityproject_crud
from app.models import CharityProject


async def check_charityproject_exists(
        project_id: int, session: AsyncSession) -> CharityProject:
    charityproject = await charityproject_crud.get(project_id, session)

    if not charityproject:

        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=PROJECT_NOT_FOUND_MESSAGE)

    return charityproject
