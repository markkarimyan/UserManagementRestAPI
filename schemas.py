from marshmallow import Schema, fields, validate, ValidationError

class UserSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=2, max=100))
    email = fields.Email(required=True)

user_schema = UserSchema()