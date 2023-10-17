from datetime import datetime
from typing import Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import CharityProject, Donation


async def get_not_fully_invested(model: Union[CharityProject, Donation],
                                 session: AsyncSession):
    objs = await session.execute(
        select(model)
        .where(model.fully_invested == 0)
        .order_by(model.create_date)
    )

    return objs.scalars().first()


async def invest(session: AsyncSession):
    latest_not_invested_proj = await get_not_fully_invested(CharityProject,
                                                            session)
    latest_not_invested_donate = await get_not_fully_invested(Donation,
                                                              session)

    if latest_not_invested_proj and latest_not_invested_donate:
        clean_proj_balance = (latest_not_invested_proj.full_amount -
                              latest_not_invested_proj.invested_amount)
        clean_donate = (latest_not_invested_donate.full_amount -
                        latest_not_invested_donate.invested_amount)

        if clean_proj_balance > clean_donate:
            latest_not_invested_proj.invested_amount += clean_donate
            latest_not_invested_donate.invested_amount += clean_donate
            latest_not_invested_donate.fully_invested = True
            latest_not_invested_donate.close_date = datetime.now()

        elif clean_proj_balance == clean_donate:
            latest_not_invested_proj.invested_amount += clean_donate
            latest_not_invested_donate.invested_amount += clean_donate
            latest_not_invested_proj.fully_invested = True
            latest_not_invested_donate.fully_invested = True
            latest_not_invested_proj.close_date = datetime.now()
            latest_not_invested_donate.close_date = datetime.now()

        else:
            latest_not_invested_proj.invested_amount += clean_proj_balance
            latest_not_invested_donate.invested_amount += clean_proj_balance
            latest_not_invested_proj.fully_invested = True
            latest_not_invested_proj.close_date = datetime.now()

        session.add(latest_not_invested_proj)
        session.add(latest_not_invested_donate)
        await session.commit()

        await session.refresh(latest_not_invested_proj)
        await session.refresh(latest_not_invested_donate)

        await invest(session)
