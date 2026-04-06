from marshmallow import fields, validate
from extensions import ma
from models.task import Task

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        load_instance = False 

    title = fields.String(required=True, validate=validate.Length(min=1))
    priority = fields.String(required=True, validate=validate.OneOf(['low', 'medium', 'high']))
    status = fields.String(required=True, validate=validate.OneOf(['todo', 'in_progress', 'done', 'archived']))
    due_date = fields.Date(allow_none=True)

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)