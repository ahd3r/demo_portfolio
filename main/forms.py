from django import forms

class Mes(forms.Form):
	title_f=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Theme of your letter'}))
	name_f=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
	message_f=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message'}))
