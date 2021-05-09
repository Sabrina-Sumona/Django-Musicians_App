from django import forms
# here forms is bulit in library & CharField(), EmailField() etc are library FUNCTIONS
from django.core import validators

def even(val):
    if val % 2 != 0:
        raise forms.ValidationError("It must be an even number!")

class user_form(forms.Form):

    # we can set max & min length of a char field
    # user_name = forms.CharField(max_length=20, min_length=5, label="Full Name", widget = forms.TextInput( attrs= {'placeholder':'Enter your full name','style':'width:300px'} ) )
    # we can validate a input by using validators
    user_name = forms.CharField(validators=[validators.MaxLengthValidator(20),validators.MinLengthValidator(5)], label="Full Name", widget = forms.TextInput( attrs= {'placeholder':'Enter your full name','style':'width:300px'} ) )

    user_dob = forms.DateField(label="Date of Birth", widget = forms.TextInput( attrs={'type':'date'}))

    # in case of char field 'length' term is used but in case of num 'value' term is used for max / min count
    user_age = forms.IntegerField(validators=[validators.MaxValueValidator(100),validators.MinValueValidator(1)], label="Current Age")

    # user defined validators
    num_field = forms.IntegerField(validators=[even], label="Enter an even number")

    user_email = forms.EmailField(label="Email", widget = forms.TextInput( attrs= {'placeholder':'Enter your email address',} ))

    user_vemail = forms.EmailField(label="Confirm Email", widget = forms.TextInput( attrs= {'placeholder':'Enter your email again',} ))

    def clean(self):
        all_cleaned_data = super().clean()
        user_emai = all_cleaned_data['user_email']
        user_vemail = all_cleaned_data['user_vemail']

        if user_emai != user_vemail:
            raise forms.ValidationError("Emails Don't Match!!!!")

    # boolean field returns true or false wuth checkbox
    agreement = forms.BooleanField(required=False)

    # choices in drop down
    choices = (('','--Options--'), ('1', 'Worst'), ('2', 'Bad'), ('3', 'Not Bad'), ('4', 'Good'), ('5', 'Excellent!'))
    rating = forms.ChoiceField(choices=choices, required=False)

    # radio buttons choices
    choices = (('F','Female'),('M','Male'))
    gender = forms.ChoiceField(choices=choices, widget=forms.RadioSelect(attrs= {'class': "custom-radio-list"}))

    # # multiple choices
    # choices = (('r','Red'),('b','Blue'),('p','Pink'),('g','Green'),('w','White'))
    # color = forms.MultipleChoiceField(choices=choices, required=False)

    # multiple choices with checkbox
    choices = (('r','Red'),('b','Blue'),('p','Pink'),('g','Green'),('w','White'))
    color = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple(attrs= {'class': "custom-radio-list"}))


    # all fields are required by default
    # but can make it false
    # initial is similar as value of input field
    # please_enter_your_name = forms.CharField(required=False, initial="Sabrina Sumona")
    # automatically creates label by removing _ and converting the 1st char into Uppercase
    # but we can modify it
    # django does not provide place holder as core argument
    # but we can create it by using widget
    # we can also add style using widget
    # user_email = forms.EmailField(label="Please enter your email", widget = forms.TextInput(attrs = {'placeholder':'Enter a valid email address which belongs to you', 'style':'width: 300px'}))
    # we can also add date type using widget to show the calender
    # user_dob = forms.DateField(label="Date of Birth", widget = forms.TextInput( attrs={'type':'date'}))
