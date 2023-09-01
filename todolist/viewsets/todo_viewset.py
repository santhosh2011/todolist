from rest_framework import viewsets, mixins

from todolist.models import Todo
from todolist.serialisers.todo_serialiser import TodoSerializer


class TodoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """

    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
