from marshmallow import Schema, fields, validates, ValidationError

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    role = fields.Str(required=True)

    @validates('role')
    def validate_role(self, value):
        if value not in ['intern', 'manager', 'CEO']:
            raise ValidationError("Invalid role")

user_schema = UserSchema()

class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()

project_schema = ProjectSchema()
