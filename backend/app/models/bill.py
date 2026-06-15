from datetime import date
from decimal import Decimal
from typing import Optional

from sqlmodel import Field, SQLModel


class BillBase(SQLModel):
    name: str
    deadline: date
    amount: Decimal
    done: bool = False


class Bill(BillBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class BillCreate(BillBase):
    pass


class BillUpdate(SQLModel):
    name: Optional[str] = None
    deadline: Optional[date] = None
    amount: Optional[Decimal] = None
    done: Optional[bool] = None


class BillPublic(BillBase):
    id: int
