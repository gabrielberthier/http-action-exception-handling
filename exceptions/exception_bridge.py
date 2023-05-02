from .protocols import AbstractException


def generate_exception_response(exception: AbstractException) -> dict:
    return dict(
        {
            "message": exception._message,
            "notice": exception.notice,
            "data": exception.data,
            "token": exception.token,
        },
        status_code=exception.http_status,
    )
