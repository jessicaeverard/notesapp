from django.forms import ModelForm, Textarea
from .models import Notes

class NoteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update(
                            {'class': 'form-control'})

    class Meta:
        model = Notes
        fields = ['text']    
        widgets = {
            'text': Textarea(attrs={'rows': 4}),
        }