from django import forms

class AddPointForm(forms.Form):
    mobile_number = forms.CharField(label="Mobile Number", max_length='10')
    point = forms.CharField(label="Point")

    def save(self):
        return self