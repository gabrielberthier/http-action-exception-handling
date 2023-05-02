from decorator import http_action


class CreateTodo:
    @http_action()
    async def create_todo(self, request):
        print(f"A nice request {request}")
        print("Creating todo")

        return "Perfect"
