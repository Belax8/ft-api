from rest_framework_simplify.views import SimplifyView

from ft_api.domain.models import ExerciseType


class ExerciseTypeHandler(SimplifyView):

    def __init__(self):
        super().__init__(ExerciseType, supported_methods=['GET', 'GET_LIST'])
