'''Auth Exception module'''
class InvalidPasswordExceptions(Exception):
    '''Invalid password'''
    status_code = 401
    message = "Invalid Password"

    def __init__(self, message=None, status_code=None, payload=None):
        super(InvalidPasswordExceptions, self).__init__()
        self.message = message or self.message
        self.status_code = status_code or self.status_code
        self.payload = payload

    def to_dict(self):
        '''Change message to dict'''
        exception = dict(self.payload or ())
        exception['message'] = self.message

        return exception
