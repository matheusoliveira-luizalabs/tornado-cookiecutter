import tornado.web


# class BaseException(tornado.web.HTTPError):
#     status_code = 500
#     reason = 'Internal Server Error'
# 
#     def __init__(self, status_code=None, reason=None):
#         self.status_code = status_code or self.status_code
#         self.reason = reason or self.reason
# 
#     def write_error(self, reason):
#         reason = self.wrap_error(self.reason)
#         super(BaseException, self).write_error(reason)
# 
#     def wrap_error(self):
#         return {
#             'statusCode': self.status_code,
#             'message': self.message
#         }
# 
# 
# class MethodNotImplemented(BaseException):
#     status_code = 405 
#     message = 'Method Not Implemented'
# 
# 
# class NotFound(BaseException):
#     status_code = 404
#     message = 'Resource Not Found'


class BaseException(tornado.web.HTTPError):
    status = 500
    reason = 'Internal Server Error'

    def prepare(self):
        self.write_error(self.status, self.reason)
        self.finish()


class MethodNotImplemented(BaseException):
    status = 405
    reason = 'Method Not Implemented'


class NotFound(BaseException):
    status = 404
    reason = 'Resource Not Found'
