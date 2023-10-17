from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charityproject_crud
from app.crud.donation import donation_crud
from app.models import CharityProject, Donation, User
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectUpdate)
from app.schemas.donation import DonationCreate
from app.services.investment import invest
from app.services.validators import (
    check_charityproject_amount_not_less_than_invested,
    check_charityproject_not_closed, check_charityproject_not_invested,
    check_name_duplicate)


class CharityProjectLogic:

    @staticmethod
    async def create(charityproject: CharityProjectCreate,
                     session: AsyncSession) -> CharityProject:
        await check_name_duplicate(charityproject.name, session)
        charityproject = await charityproject_crud.create(charityproject,
                                                          session)

        await invest(session)

        return charityproject

    @staticmethod
    async def remove(charityproject: CharityProject,
                     session: AsyncSession) -> CharityProject:
        await check_charityproject_not_invested(charityproject)

        return await charityproject_crud.remove(charityproject, session)

    @staticmethod
    async def update(charityproject: CharityProject,
                     obj_in: CharityProjectUpdate,
                     session: AsyncSession) -> CharityProject:
        await check_name_duplicate(obj_in.name, session)
        await check_charityproject_not_closed(charityproject)
        await check_charityproject_amount_not_less_than_invested(
            obj_in, charityproject)

        charityproject = await charityproject_crud.update(charityproject,
                                                          obj_in,
                                                          session)

        await invest(session)

        return charityproject


class DonationLogic:

    @staticmethod
    async def create(donation: DonationCreate,
                     session: AsyncSession,
                     user: User) -> Donation:
        donation = await donation_crud.create(donation, session, user)

        await invest(session)

        return donation
