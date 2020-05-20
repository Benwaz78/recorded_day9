from django import forms
from classwork_app.models import Category, Post
from backend.models import ContactModel
from django.contrib.auth.models import User
from backend.options import REFERER_FIELD, GENDER_FIELD, CHOOSE
from django.core import validators
from backend.functions import check_for_c

# Four ways of validating forms in Django
# 1. Using inbuilt Django Validators
# 2. Validating each field
# 3. Validating two fields
# 4. Creating our own custom validation function



class CategoryForm(forms.ModelForm):
	cat_name = forms.CharField(label='Category Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Category'}))
	desc = forms.CharField(label='Description', required=False, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}))
	botcatcher = forms.CharField(widget=forms.HiddenInput(), required=False, validators=[validators.MaxLengthValidator(0)])

	def clean_cat_name(self):
		my_cat_name = self.cleaned_data.get('cat_name')
		if Category.objects.filter(cat_name=my_cat_name).exists():
			raise forms.ValidationError('Category name {} already exist'.format(my_cat_name))
		return my_cat_name

	class Meta():
		model = Category
		fields = ('cat_name', 'desc')

class PostForm(forms.ModelForm):
	pst_title = forms.CharField(label='Post Title',  widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title'}))
	pst_img = forms.ImageField(widget=forms.ClearableFileInput())
	content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'class':'form-control'}))
	category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple())
	user = forms.ModelChoiceField(empty_label="Choose User", queryset=User.objects.all(),   widget=forms.Select(attrs={'class':'form-control'}))

	class Meta():
		model = Post
		# fields = '__all__'
		# fields = ('pst_title', 'pst_img', 'content', 'category', 'user')
		exclude = ('create_date', 'update_date')


class ContactForm(forms.ModelForm):
	name = forms.CharField(validators=[check_for_c], widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Name'}))
	subject = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Subject', 'max_length':10}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
	verify_email = forms.EmailField(label='Email Again', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}))
	gender = forms.ChoiceField(widget=forms.RadioSelect(), choices=GENDER_FIELD)
	referer = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class':'form-control'}), choices=REFERER_FIELD)
	message = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
	botcatcher = forms.CharField(widget=forms.HiddenInput(), required=False, validators=[validators.MaxLengthValidator(0)])


	# To validate just one field
	def clean_subject(self):
		subt = self.cleaned_data.get('subject')
		if 'Hello' not in subt:
			raise forms.ValidationError('You must include "Hello" in your subject')
		return subt

	# TO validate two fields (Fields that depend on each other)
	def clean(self):
		cleaned_data = super().clean()
		email1 = cleaned_data.get('email')
		email2 = cleaned_data.get('verify_email')
		if email1 != email2:
			self.add_error('email', 'The two emails must match')
		elif not email1.endswith('@alabiansolutions.com'):
			self.add_error('email', 'Your email must end with "@alabiansolutions"')
			
	class Meta():
		model = ContactModel
		fields = ('name', 'subject', 'email', 'verify_email', 'gender', 'referer', 'message')




