from django import forms
from SuperTeacher.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text", "rating"]

        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add comment...'}),
            'rating': forms.NumberInput(attrs={'placeholder': 'Rate...'}),
        }


class SearchForm(forms.Form):
    teacher_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by teacher name...',
            }
        )
    )

    teacher_type = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by teacher type...',
            }
        )
    )