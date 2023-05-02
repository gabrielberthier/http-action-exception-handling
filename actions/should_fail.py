from decorator import http_action
from exceptions.common_exceptions import ElementNotFoundException


class ShouldFail:
    @http_action()
    async def function_to_fail(self, request):
        print(f"A nice request {request} to fail")

        raise ElementNotFoundException("OOPS. Not found")

        return "Perfect"
