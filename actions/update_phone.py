from logging import getLogger
from decorator import http_action


class UpdatePhone:
    @http_action(
        logger=getLogger(), origin_call="function_to_be_decorated", use_token=True
    )
    async def function_to_be_decorated(self, request, account_data={"a": 42}):
        print(f"A nice request {request}")
        print(f"The account_data: {account_data}")

        return "Perfect"
