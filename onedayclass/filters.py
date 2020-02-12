from django_filters import FilterSet
from django_filters import ChoiceFilter, ModelMultipleChoiceFilter, NumberFilter
from django_filters import MultipleChoiceFilter, NumericRangeFilter, CharFilter
from .models import OnedayClass
from django import forms

class OnedayClassFilter(FilterSet):
    type = MultipleChoiceFilter(choices=OnedayClass.TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple)
    gender = MultipleChoiceFilter(choices=OnedayClass.GENDER_CHOICES,
        widget=forms.CheckboxSelectMultiple)
    day = MultipleChoiceFilter(choices=OnedayClass.DAY_CHOICES,
        widget=forms.CheckboxSelectMultiple)
    theme = MultipleChoiceFilter(choices=OnedayClass.THEME_CHOICES,
        widget=forms.CheckboxSelectMultiple)

    #price = NumberFilter(field_name='price', lookup_expr='price')
    #price__gt = NumberFilter(field_name='price', lookup_expr='price__gt')
    price__lt = NumberFilter(field_name='price', lookup_expr='lte')

    place = CharFilter(lookup_expr='icontains')

    class Meta:
        model = OnedayClass
        fields = ['type', 'gender', 'day', 'theme', 'price', 'place',]
