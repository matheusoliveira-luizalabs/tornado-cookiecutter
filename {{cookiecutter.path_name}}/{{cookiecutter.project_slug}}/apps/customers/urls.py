from tornado.web import URLSpec as url

from .api import CustomerHandler


urls = [
    url(r'', CustomerHandler),
    url(r'\/(?P<id>[\d]+)', CustomerHandler)
]
