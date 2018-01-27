from rest_framework_simplify.views import SimplifyView

from ft_api.domain.models import FitnessPlanType


class FitnessPlanTypeHandler(SimplifyView):

    def __init__(self):
        super().__init__(FitnessPlanType, supported_methods=['GET', 'GET_LIST'])
