from rest_framework.exceptions import APIException
from rest_framework import status


class BetterLinkAPIException(APIException):
    def __init__(self, detail=None, code=None):
        super().__init__(detail=detail, code=code)
        self.code = code


class BadRequest(BetterLinkAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
