from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, PositiveInt

from app.constants import (DESCRIPTION_MIN_LENGTH, NAME_MAX_LENGTH,
                           NAME_MIN_LENGTH)


class CharityProjectCreate(BaseModel):
    name: str = Field(min_length=NAME_MIN_LENGTH,
                      max_length=NAME_MAX_LENGTH)
    description: str = Field(min_length=DESCRIPTION_MIN_LENGTH)
    full_amount: PositiveInt


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)


class CharityProjectUpdate(CharityProjectCreate):
    name: Optional[str] = Field(None,
                                min_length=NAME_MIN_LENGTH,
                                max_length=NAME_MAX_LENGTH)
    description: Optional[str] = Field(None,
                                       min_length=1)
    full_amount: Optional[PositiveInt]

    model_config = ConfigDict(extra='forbid')
