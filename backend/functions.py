from django.contrib import messages
from django import forms

def calculate(val1, val2, name, sign):
    if name == sign:
        add = val1 + val2
        messages.success(request, add)
    elif name == sign:
        subt = val1 - val2
        messages.success(request, subt)
    elif name == sign:
        div = val1/val2
        messages.success(request, div)
    elif name == sign:
        mult = val1 * val2
        messages.success(request, mult)


def check_for_c(value):
    if value[0].capitalize() != 'C':
        raise forms.ValidationError('Name must start with "C"')


