from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, error_messages={'required': 'Name is required.'})
    email = forms.EmailField(error_messages={'required': 'Email is required.'})
    message = forms.CharField(widget=forms.Textarea, required=False)

    def clean(self):
        # Call the parent clean() method first to clean individual fields
        cleaned_data = super().clean()

        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')

        # Validate the name field
        if not name:
            raise forms.ValidationError({"name": "Name is required."})
        elif len(name) < 3:
            raise forms.ValidationError({"name": "Name cannot be less than 3 characters."})

        # Validate the email field
        if not email:
            raise forms.ValidationError({"email": "Email is required."})

        # Validate the message field
        if message and len(message) < 10:
            raise forms.ValidationError({"message": "Message should be at least 10 characters long."})

        # Return the cleaned data dictionary
        return cleaned_data
