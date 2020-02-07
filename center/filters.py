from django_filters import FilterSet
from django_filters import ChoiceFilter, ModelMultipleChoiceFilter
from django_filters import ModelChoiceFilter
from .models import Center

class CenterFilter(FilterSet):
