from django import forms
from django.utils.translation import gettext_lazy as _
from subscribe.models import Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'
        labels={
            'first_name':_('Enter first name'),
            'last_name':_('Enter last name'),
            'email':_('Enter email'),
        }
        error_messages={
            'first_name': {
                'required':_('enter first name')
        }
        }



# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError('Commas are not allowed')
#     return value

# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100, required=False, label="Enter first name", validators=[validate_comma])
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=100)


