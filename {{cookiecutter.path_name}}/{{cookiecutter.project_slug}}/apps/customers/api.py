import tornado.web
import tornado.gen

from contrib.handlers import RestHandler

from contrib.db import session
from contrib.db.utils import get_or_404

from .models import Customer
from .schemas import CustomerSchema


class CustomerHandler(RestHandler):
    schema = CustomerSchema
    model = Customer

    @tornado.gen.coroutine
    def list(self):
        customers = session.query(self.model).slice(0, 10).all()
        self.write(customers)

    @tornado.gen.coroutine
    def detail(self, id):
        self.get_or_404(id)
