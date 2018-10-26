"""
User defined Exceptions
"""


class UserException(Exception):
    """Custom Exception"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message

try:
    raise UserException('Some User Exception')
except UserException as ue:
    print(ue)
