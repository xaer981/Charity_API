from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_charityproject_exists
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charityproject_crud
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectDB,
                                         CharityProjectUpdate)
from app.services.main import CharityProjectLogic

router = APIRouter()


@router.post('/',
             response_model=CharityProjectDB,
             response_model_exclude_none=True,
             dependencies=[Depends(current_superuser)])
async def create_charityproject(
        charityproject: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session)):

    return await CharityProjectLogic.create(charityproject,
                                            session)


@router.delete('/{project_id}',
               response_model=CharityProjectDB,
               dependencies=[Depends(current_superuser)])
async def delete_charityproject(
        project_id: int,
        session: AsyncSession = Depends(get_async_session)):
    charityproject = await check_charityproject_exists(project_id, session)

    return await CharityProjectLogic.remove(charityproject, session)


@router.patch('/{project_id}',
              response_model=CharityProjectDB,
              dependencies=[Depends(current_superuser)])
async def update_charityproject(
        project_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session)):
    charityproject = await check_charityproject_exists(project_id, session)

    return await CharityProjectLogic.update(charityproject,
                                            obj_in,
                                            session)


@router.get('/',
            response_model=list[CharityProjectDB],
            response_model_exclude_none=True)
async def get_all_charityprojects(
        session: AsyncSession = Depends(get_async_session)):

    return await charityproject_crud.get_multi(session)