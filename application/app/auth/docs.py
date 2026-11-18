from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from application.app.core.config.settings import settings
from application.app.core.utils.compare_value import compare_value

__all__ = ("auth_docs", )


_security = HTTPBasic()


def auth_docs(credentials: Annotated[HTTPBasicCredentials, Depends(_security)]) -> None:

    if compare_value(credentials.username, settings.docs_user) and \
        compare_value(credentials.password, settings.docs_password):
        return

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect credentials",
        headers={"WWW-Authenticate": "Basic"},
    )
