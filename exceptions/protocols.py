from http_status import HttpStatus


class AbstractException(Exception):
    def __init__(
        self,
        http_status: HttpStatus = HttpStatus(200),
        message="",
        notice=None,
        data: dict = {},
        token=None,
    ) -> None:
        super().__init__(message)
        self._http_status = http_status
        self._notice = notice
        self._data = data
        self._message = message
        self._token = token

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        self._token = token

    @property
    def data(self) -> dict:
        return self._data

    @data.setter
    def data(self, value) -> None:
        self._data = value

    @property
    def notice(self):
        return self._notice

    @notice.setter
    def notice(self, value):
        self._notice = value

    @property
    def http_status(self):
        return self._http_status

    @http_status.setter
    def http_status(self, value):
        self._http_status = value
