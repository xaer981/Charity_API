from typing import Optional

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(self,
                                     project_name: str,
                                     session: AsyncSession) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id)
            .where(CharityProject.name == project_name))

        return db_project_id.scalars().first()

    async def get_projects_by_completion_rate(self, session: AsyncSession):
        stmt = (
            select(CharityProject.name,
                   (func.julianday(CharityProject.close_date) -
                    func.julianday(CharityProject.create_date))
                   .label('time_passed'),
                   CharityProject.description)
            .where(CharityProject.fully_invested == 1)
            .order_by('time_passed')
        )
        closed_projects = await session.execute(stmt)

        return closed_projects.all()


charityproject_crud = CRUDCharityProject(CharityProject)
