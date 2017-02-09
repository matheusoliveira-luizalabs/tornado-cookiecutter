import socket

import tornado.web

import app

from contrib.db.session import session

from .exceptions import MethodNotImplemented


class SerializerMixin(object):

    def serialize_list(self, data):
        return self.schema().dump(data, many=True)

    def serialize_detail(self, data):
        return self.schema().dump(data)


class MetaMixin(object):

    def set_meta(self, data):
        return self.meta_schema(data)

    def hostname(self, use_hostname=False):
        hostname = socket.gethostname()

        if use_hostname:
            return hostname

        return socket.gethostbyname(hostname)

    def data_count(self, data):
        count = 0

        if isinstance(data, list):
            count = len(data)
        else:
            count = 1
        return count

    def meta_schema(self, data):
        schema = {
            'name': app.Application.info('name'),
            'server': self.hostname(),
            'version': app.Application.info('version'),
            'record_count': self.data_count(data)
        }
        return schema

    def write(self, chunck):
        chunck['meta'] = self.set_meta(chunck['objects'])
        super(MetaMixin, self).write(chunck)


class BaseRestHandler(SerializerMixin, MetaMixin):

    def wrap_list_response(self, data):
        serialize = self.serialize_list(data)
        return serialize.data

    def wrap_object_response(self, data):
        serialize = self.serialize_detail(data)
        return serialize.data

    def wrap_response(self, data):
        objects = []

        if isinstance(data, list):
            objects = self.wrap_list_response(data)
        else:
            objects.append(self.wrap_object_response(data))

        response = {
            'objects': objects
        }
        return response

    def write(self, chunck, meta=True):
        if meta:
            data = self.wrap_response(chunck)
        else:
            data = chunck
        super(BaseRestHandler, self).write(data)


class RestHandler(BaseRestHandler, tornado.web.RequestHandler):

    def get(self, id=None):
        if not id:
            return self.list()
        else:
            return self.detail(id)

    def list(self):
        raise MethodNotImplemented()

    def detail(self, id):
        raise MethodNotImplemented()

    def get_or_404(self, id):
        obj = session.query(self.model).get(id)
        if obj:
            return obj
        else:
            self.set_status(404)
            self.write('{0} Not Found'.format(self.model.__name__), meta=False)
