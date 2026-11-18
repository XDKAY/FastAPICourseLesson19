from application.app.core.config.settings import settings
from application.app.core.utils.compare_value import compare_value


def is_production() -> bool:
    return compare_value(settings.mode, "PROD")
