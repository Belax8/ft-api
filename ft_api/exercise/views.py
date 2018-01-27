from rest_framework_simplify.views import SimplifyView

from ft_api.domain.models import Exercise, User


class ExerciseHandler(SimplifyView):

    def __init__(self):
        linked_objects = []
        user = {
            'parent_resource': 'users',
            'parent_cls': User,
            'parent_name': 'user',
            'linking_cls': None,
            'sub_resource_name': None
        }
        linked_objects.append(user)
        super().__init__(Exercise, supported_methods=['GET', 'GET_LIST_SUB'], linked_objects=linked_objects)
