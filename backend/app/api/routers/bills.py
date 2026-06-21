from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.api.deps import get_db, jinjax
from app.models.bill import Bill, BillCreate, BillPublic, BillUpdate

router = APIRouter(prefix="/bills", tags=["bills"])


@router.get("/", response_model=list[BillPublic])
def get_bills(db: Session = Depends(get_db)) -> list[Bill]:
    return list(db.exec(select(Bill)).all())


@router.get("/{bill_id}", response_model=BillPublic)
def get_bill(bill_id: int, db: Session = Depends(get_db)) -> Bill:
    bill = db.get(Bill, bill_id)
    if not bill:
        raise HTTPException(status_code=404, detail="Bill not found")
    return bill


@router.post("/", response_model=BillPublic, status_code=201)
def create_bill(bill_in: BillCreate, db: Session = Depends(get_db)) -> Bill:
    bill = Bill.model_validate(bill_in)
    db.add(bill)
    db.commit()
    db.refresh(bill)
    return bill


@router.put("/{bill_id}", response_model=BillPublic)
@jinjax.page("bill.html")
def update_bill(
    bill_id: int, bill_in: BillUpdate, db: Session = Depends(get_db)
) -> Bill:
    bill = db.get(Bill, bill_id)
    if not bill:
        raise HTTPException(status_code=404, detail="Bill not found")
    update_data = bill_in.model_dump(exclude_unset=True)
    bill.sqlmodel_update(update_data)
    db.add(bill)
    db.commit()
    db.refresh(bill)
    return bill


@router.delete("/{bill_id}", status_code=204)
def delete_bill(bill_id: int, db: Session = Depends(get_db)) -> None:
    bill = db.get(Bill, bill_id)
    if not bill:
        raise HTTPException(status_code=404, detail="Bill not found")
    db.delete(bill)
    db.commit()
