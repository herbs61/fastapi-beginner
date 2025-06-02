from tortoise.models import Model
from tortoise import fields


class Todo(Model):
    id = fields.IntField(pk=True)
    task = fields.CharField(max_length=100)
    done = fields.BooleanField(default=False, null=False)