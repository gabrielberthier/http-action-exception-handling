from asyncio import run
from actions.create_todo import CreateTodo
from actions.should_fail import ShouldFail
from actions.update_phone import UpdatePhone


async def main():
    u = UpdatePhone()

    response = await u.function_to_be_decorated(
        request={"hi": "i'm a request to update a phone"},
        account_data={"token": 42},
    )

    print(response)

    u = CreateTodo()

    response = await u.create_todo(
        request={"POST": "i'm a request to create a TODO"},
    )

    print(response)
    
    u = ShouldFail()

    response = await u.function_to_fail(
        request={"POST": "i'm a request to create a TODO"},
    )

    print(response)


if __name__ == "__main__":
    run(main())