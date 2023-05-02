from logging import Logger, getLogger
import traceback
from pydantic import ValidationError
from typing import Callable
from exceptions import (
    InvalidTypesException,
    ValidationException,
    ServerErrorException,
    AbstractException,
    generate_exception_response
)


def http_action(logger: Logger = getLogger(), origin_call: str = "", use_token=False):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur

    @param logger: The logging object
    @param origin_call: The function or endpoint from where this method is called
    @use_token: force token inclusion in response and errors
    """

    def decor(func: Callable):
        origin_call_function = origin_call or func.__name__

        print(f"Calling from decor {origin_call_function}")

        async def executor_wrapper(*args, **kwargs):
            print("Calling from executor_wrapper")
            error = None
            response = None
            token = None

            if use_token:
                account_data = args[-1] if type(args[-1]) == dict else {}
                account_data = (
                    account_data if bool(account_data) else kwargs.get("account_data")
                )
                token = account_data.get("token")
                if not token:
                    raise Exception(
                        "Account_data is not present or does not have a token key"
                    )

            try:
                response = await func(*args, **kwargs)
            except TypeError:
                error = InvalidTypesException(func.__name__)
            except ValidationError as e:
                error = ValidationException(data={"errors": e.errors})
            except AbstractException as e:
                error = e
            except Exception as e:
                error = ServerErrorException(
                    message=str(e),
                    notice=traceback.format_exc(),
                    data={"cause": e.__cause__},
                )

            else:
                logger.info(f"Finishing {origin_call_function} successfully")
            finally:
                if error is not None:
                    error.token = token if use_token else None
                    logger.error(
                        f"{origin_call_function} {error.__class__.__name__} - {error}"
                    )
                    return generate_exception_response(error)

                return response

        return executor_wrapper

    return decor
