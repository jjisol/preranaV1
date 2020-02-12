from django_filters import FilterSet
from django_filters import ChoiceFilter, ModelMultipleChoiceFilter
from django_filters import MultipleChoiceFilter, CharFilter
from .models import Center
from django import forms
from django.db.models import Q

class CenterFilter(FilterSet):
    type = MultipleChoiceFilter(choices=Center.TYPE_CHOICES,
        method='type_filter',
        widget=forms.CheckboxSelectMultiple)
    detail = MultipleChoiceFilter(choices=Center.CENTER_CHOICES,
        widget=forms.CheckboxSelectMultiple)
    address = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Center
        fields = ['type', 'detail', 'address', ]

    def type_filter(self, queryset, name, type):
        if len(type) == 2:
            return queryset.filter(Q(type__icontains='1')|Q(type__icontains='2'))
        else:
            return queryset.filter(type__icontains=type[0])
