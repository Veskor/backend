from mongoengine.fields import ObjectId
from ..models import Task
from .fields.task import fields
from .namespaces import ns_task
from .resources import ProtectedResource


@ns_task.route('', endpoint='tasks')
class TaskListAPI(ProtectedResource):
    @ns_task.marshal_with(fields)
    def get(self):
        return [task for task in Task.objects.all()]


@ns_task.route('/<id>', endpoint='task')
class TaskAPI(ProtectedResource):
    @ns_task.marshal_with(fields)
    def get(self, id):
        task = Task.objects.get(pk=id)
        return task
