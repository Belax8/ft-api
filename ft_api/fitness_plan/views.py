from rest_framework_simplify.views import SimplifyView

from ft_api.domain.models import FitnessPlan, User


class FitnessPlanHandler(SimplifyView):

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
        super().__init__(FitnessPlan, supported_methods=['GET', 'GET_LIST_SUB', 'PUT', 'POST'], linked_objects=linked_objects)
