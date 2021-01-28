from django import forms
from post.models import Contact,Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ContactForm(forms.ModelForm):
    
    class Meta:

        model = Contact
        fields =('name', 'email', 'message')

