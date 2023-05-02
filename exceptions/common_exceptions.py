from http_status import HttpStatus
from .protocols import AbstractException


class ElementNotFoundException(AbstractException):
    def __init__(self, message="", notice=None, data: dict = {}) -> None:
        super().__init__(HttpStatus.RESOURCE_NOT_FOUND, message, notice, data)


class ForbiddenException(AbstractException):
    def __init__(self, message="", notice=None, data: dict = {}) -> None:
        super().__init__(HttpStatus.FORBIDDEN, message, notice, data)


class ValidationException(AbstractException):
    def __init__(self, data: dict = {}) -> None:
        super().__init__(
            HttpStatus.UNPROCESSABLE_ENTITY,
            message=f'{"code": "E004", "message": "Validation failed"}',
            data=data,
        )


class InvalidTypesException(AbstractException):
    def __init__(self, func_name: str) -> None:
        super().__init__(
            HttpStatus.BAD_REQUEST, message=f"{func_name} wrong data types"
        )


class ServerErrorException(AbstractException):
    def __init__(self, message="", notice=None, data: dict = {}) -> None:
        super().__init__(HttpStatus.SERVER_ERROR, message, notice, data)
