import uuid


def create_unique_code(length: int) -> str:
    return uuid.uuid4().__str__()
