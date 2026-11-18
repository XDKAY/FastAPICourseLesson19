from fastapi import APIRouter

router = APIRouter(tags=["Users"])

@router.get("/users/{id}")
def get_user_by_id_endpoint(id: int) -> dict:
    return {
        "message": f"User id: {id}"
    }
