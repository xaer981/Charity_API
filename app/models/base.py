from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer

from app.constants import INVESTED_AMOUNT_DEFAULT


class InvestInfoAndCreateCloseDateTime(object):
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=INVESTED_AMOUNT_DEFAULT)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)
