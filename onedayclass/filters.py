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
    ADDR = [(addr, addr) for addr in ('서울특별시', '부산광역시', '대구광역시',
        '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시',
        '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도',
        '경상북도', '경상남도', '제주특별자치도')]

    ADDR1 = [(addr, addr) for addr in ('종로구', '중구', '용산구', '성동구',
        '광진구', '동대문구', '중랑구', '성북구', '강북구', '도봉구', '노원구',
        '은평구', '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구',
        '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구')]

    ADDR2 = [(addr, addr) for addr in ('수원시', '고양시', '성남시', '부천시',
        '안양시', '광명시', '평택시', '안산시', '과천시', '오산시', '시흥시',
        '군포시', '의왕시', '하남시', '용인시', '이천시', '안성시', '김포시',
        '화성시', '광주시', '의정부시', '동두천시', '구리시', '남양주시', '파주시',
        '양주시', '포천시', '여주시', '연천군', '가평군', '양평군')]


    type = MultipleChoiceFilter(choices=OnedayClass.TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple)
    gender = MultipleChoiceFilter(choices=OnedayClass.GENDER_CHOICES,
        widget=forms.CheckboxSelectMultiple)
    day = MultipleChoiceFilter(choices=OnedayClass.DAY_CHOICES,
        widget=forms.CheckboxSelectMultiple)
    theme = MultipleChoiceFilter(choices=OnedayClass.THEME_CHOICES,
        widget=forms.CheckboxSelectMultiple)

    price__lt = NumberFilter(field_name='price', lookup_expr='lte')

    place = ChoiceFilter(choices=ADDR, field_name='place', lookup_expr='icontains')
    place1 = ChoiceFilter(choices=ADDR1, field_name='place', lookup_expr='icontains')
    place2 = ChoiceFilter(choices=ADDR2, field_name='place', lookup_expr='icontains')

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

    def place_filter(self, queryset, place):
        if place == "서울특별시":
            return queryset.exclude('place2')
        elif place == "경기도":
            return queryset.exclude('place1')
        else:
            return queryset.exclude('place1', 'place2')
#class OnedayClassListView(generics.ListAPIView):
#    queryset = OnedayClass.objects.all()
#    serializer_class = OnedayClassSerializer
#    filter_backends = [DjangoFilterBackend, OrderingFilter]
#    filterset_class = OnedayClassFilter
