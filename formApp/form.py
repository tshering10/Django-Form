from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, error_messages={'required': 'Name is required.'})
    email = forms.EmailField(error_messages = {'required': 'Email is required.'})
    message = forms.CharField(widget=forms.Textarea, required = False)
    
    
    def send_email(self):
        print(f"Sending email from {self.cleaned_data['email']} with message: {self.cleaned_data['message']}")