from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', 'visible_to')

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__()
        self.fields['description'].widget.attrs.update({
            'placeholder':'Description',
            'class':'form-control'
        })
        self.fields['document'].widget.attrs.update({
            'class':'form-control'
        })
        self.fields['visible_to'].widget.attrs.update({
            'class':'form-control'
        })
