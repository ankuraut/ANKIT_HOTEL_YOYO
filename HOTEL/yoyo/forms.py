from django import forms

class AvailableForm(forms.Form):
    ROOM_TYPES={
        ('NOR','NORMAL'),
        ('ACC','AC'),
        ('NAC','NON-AC'),
        ('KIG','KING'),
        ('QUE','QUEEN'),
        ('XYX','COUPLE-FRIENDLY'),
    }
    room_type = forms.ChoiceField(choices=ROOM_TYPES, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M",])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M",])