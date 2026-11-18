from fastapi import HTTPException, status

from application.app.core.utils.deployment import is_production


def production() -> None:
    if is_production():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resourse Not Found",
        )
