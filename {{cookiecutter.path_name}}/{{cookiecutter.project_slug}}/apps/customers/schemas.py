from marshmallow import Schema, fields


class CustomerSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    created_at = fields.Date()
