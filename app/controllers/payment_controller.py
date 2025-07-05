from fastapi import APIRouter, Header, HTTPException
from app.utils.jwt_utils import decode_token
from app.services.payment_service import get_all_payments_logic

payment_router = APIRouter()


@payment_router.get("/all-payments")
def get_all_payments(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Formato Bearer inválido")

    token = authorization.replace("Bearer ", "")
    user = decode_token(token)

    roles = user.get("roles", [])
    if not isinstance(roles, list) or "admin" not in roles:
        raise HTTPException(
            status_code=403, detail="Acceso denegado: solo para administradores"
        )

    return get_all_payments_logic()
