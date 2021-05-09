from django import forms
# here forms is bulit in library & CharField(), EmailField() etc are library FUNCTIONS
class user_form(forms.Form):

    user_name = forms.CharField(label="Full Name", widget = forms.TextInput( attrs= {'placeholder':'Enter your full name','style':'width:300px'} ) )

    user_dob = forms.DateField(label="Date of Birth", widget = forms.TextInput( attrs={'type':'date'}))

    user_email = forms.EmailField(label="Email", widget = forms.TextInput( attrs= {'placeholder':'Enter your Email Address',} ))


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
