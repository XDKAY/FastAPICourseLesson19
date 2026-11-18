import secrets


def compare_value(first_value: str, second_value: str) -> bool:
    return secrets.compare_digest(
        first_value.encode("utf-8"),
        second_value.encode("utf-8")
    )
