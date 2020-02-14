from django_filters import FilterSet
from django_filters import ChoiceFilter, ModelMultipleChoiceFilter, NumberFilter
from django_filters import MultipleChoiceFilter, NumericRangeFilter, CharFilter
from django_filters import filters, widgets
from .models import OnedayClass
from django import forms
#import django_filters.rest_framework
#from myapp.serializers import OnedayClassSerializer
#from rest_framework import generics

class OnedayClassFilter(FilterSet):
    ADDR = [(addr, addr) for addr in ('종로구', '중구', '용산구', '성동구',
        '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구',
        '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구',
        '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구')]

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

    place = ChoiceFilter(choices=ADDR, lookup_expr='icontains')

    o = filters.OrderingFilter(
        fields=['price', 'date'],
        field_labels={
            '-price':'높은가격순',
            'price':'낮은가격순',
            'date':'마감임박순',
            '-date':'최신순',
        },
        widget=forms.RadioSelect,
        )

    class Meta:
        model = OnedayClass
        fields = ['type', 'gender', 'day', 'theme', 'price', 'place', 'date',]


#class OnedayClassListView(generics.ListAPIView):
#    queryset = OnedayClass.objects.all()
#    serializer_class = OnedayClassSerializer
#    filter_backends = [DjangoFilterBackend, OrderingFilter]
#    filterset_class = OnedayClassFilter
