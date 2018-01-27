from rest_framework_simplify.views import SimplifyView

from ft_api.domain.models import User


class UserHandler(SimplifyView):

    def __init__(self):
        super().__init__(User, supported_methods=['GET', 'GET_LIST'])
