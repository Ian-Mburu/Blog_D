from django import forms
from .models import User
from .models import RecipeDescription, UserPosted


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



class BlogForm(forms.ModelForm):
    # Define the author field as a dropdown menu of authors
    postedBy = forms.ModelChoiceField(queryset=UserPosted.objects.all(), empty_label='Select User', required=False)

    class Meta:
        model = RecipeDescription
        fields = ['image', 'postedBy', 'recipeTitle', 'recipeDescription', 'is_published' ] 
        widgets = {
            'recipeTitle': forms.TextInput(attrs={'required': True}),
            'recipeDescription': forms.Textarea(attrs={'required': True}),
        }

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        # Customize the form's appearance or behavior here if needed

    def clean(self):
        cleaned_data = super().clean()
        # Additional form validation can be performed here
        return cleaned_data
