from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import User
from app.schemas.donation import DonationCreate, DonationDB, DonationRead
from app.services.main import DonationLogic

router = APIRouter()


@router.get('/',
            response_model=list[DonationDB],
            response_model_exclude_none=True,
            dependencies=[Depends(current_superuser)])
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session)):
    """Только для суперюзеров."""

    return await donation_crud.get_multi(session)


@router.get('/my',
            response_model=list[DonationRead],
            response_model_exclude_none=True)
async def get_my_donations(session: AsyncSession = Depends(get_async_session),
                           user: User = Depends(current_user)):

    return await donation_crud.get_by_user(session, user)


@router.post('/',
             response_model=DonationRead,
             response_model_exclude_none=True)
async def create_donation(donation: DonationCreate,
                          session: AsyncSession = Depends(get_async_session),
                          user: User = Depends(current_user)):

    return await DonationLogic.create(donation, session, user)
