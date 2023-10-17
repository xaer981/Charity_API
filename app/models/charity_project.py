from sqlalchemy import Column, String, Text

from app.constants import NAME_MAX_LENGTH
from app.core.db import Base
from app.models.base import InvestInfoAndCreateCloseDateTime


class CharityProject(InvestInfoAndCreateCloseDateTime, Base):
    name = Column(String(NAME_MAX_LENGTH), unique=True, nullable=False)
    description = Column(Text, nullable=False)
