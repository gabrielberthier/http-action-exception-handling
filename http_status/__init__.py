from enum import Enum

class HttpStatus(Enum):
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    BAD_REQUEST = 400
    NOT_ALLOWED = 401
    VALIDATION_ERROR = 401
    VERIFICATION_ERROR = 401
    UNAUTHENTICATED = 401
    INSUFFICIENT_PRIVILEGES = 403
    FORBIDDEN = 403
    RESOURCE_NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    CONFLICT = 409
    GONE = 410
    UNPROCESSABLE_ENTITY = 422
    SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    
if __name__ == '__main__':
    a = HttpStatus(400)
    print(a)
    print(type(a))
    