from django import forms

class OnedayClassFilterForm(forms.Form):
    options = [('1', '높은가격순'), ('2', '낮은가격순'),
        ('3', '마감임박순'), ('4',  '최신순'),]
    select = forms.ChoiceField(choices=options, label='')
