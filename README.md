# HTTP Action Exception Handling

Demonstrative repository to showcase how to handle HTTP action methods and tackle exceptions based on pre-defined http exceptions.

## The Idea

Python is heavily influenced by the usage of exceptions. However, oftenly developers rely on using such exceptions as flux control or as a manner to handle inumerous scenarios when commonly those scenarios are mapped to the known HTTP statuses. 

Ex:
```python
def function(request):
    try:
        body = parse_request_body(request)

        return do_something_wuth_request_body(body)
    except CaseA:
        pass
    
    except CaseB:
        pass
    
    except CaseC:
        pass
    
    except CaseD:
        pass
    
    finally:
        exit()
```

This leads to poorly implemented logic, which tends to focus more on exception scenarios than in the excepted flux of control. Not only that, code as the above is expected to bloat as time passes and comes to a point where a function or file describes many more details about exception handling than the expected behaviour. In that way, this repository introduces indirect exception handling by catching exceptions that are self-described in a decorator that acts as focal point, i.e, exceptions will bubble to the decorator and then will be managed accordingly. 

```python
    @http_action(
        logger=getLogger(), origin_call="function_to_be_decorated", use_token=True
    )
    async def function_to_be_decorated(self, request: Request)
        print(f"A nice request {request}")
        print(f"The account_data: {account_data}")

        return "OK
```

Exceptions can be narrowed by simply extend previously defined exceptions, such as:

```python
class UserNotFound(ElementNotFoundException):
  pass
  
def fetch_user():
  user = retrieve_user('hash')
  if not user:
    raise UserNotFound
```

Which will be mapped to a not found status. 
