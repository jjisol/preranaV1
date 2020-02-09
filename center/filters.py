from django_filters import FilterSet
from django_filters import ChoiceFilter, ModelMultipleChoiceFilter
from django_filters import ModelChoiceFilter
from .models import Center
from django import forms

class CenterFilter(FilterSet):
    SI = [(si, si) for si in ('서울특별시')]
    GU = [(gu, gu) for gu in ('용산구', '종로구', '중구', '서대문구')]
    type = ModelMultipleChoiceFilter(choices=Center.TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple)
    detail = ModelMultipleChoiceFilter(choices=Center.CENTER_CHOICES,
        widget=forms.CheckboxSelectMultiple)
    address = ChoiceFilter(choices=GU, lookup_expr='icontains')

    class Meta:
        model = Center
        fields = ['type', 'detail', 'address', ]
