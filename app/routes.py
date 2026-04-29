from fastapi import APIRouter
from app.models import Ticket
from app.services import create_ticket_service

router = APIRouter()

@router.post("/tickets")
def create_ticket(ticket: Ticket):
    return create_ticket_service(ticket)