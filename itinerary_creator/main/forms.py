from django import forms
from .models import Feedback  # Ensure you have a Feedback model defined

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback  # Your feedback model
        fields = ['email', 'message']  # Adjust fields based on your model
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
