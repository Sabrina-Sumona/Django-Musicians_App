from django import forms
# here forms is bulit in library & CharField(), EmailField() etc are library FUNCTIONS
class user_form(forms.Form):

    # we can set max & min length of a char field
    user_name = forms.CharField(max_length=20, min_length=5, label="Full Name", widget = forms.TextInput( attrs= {'placeholder':'Enter your full name','style':'width:300px'} ) )

    user_dob = forms.DateField(label="Date of Birth", widget = forms.TextInput( attrs={'type':'date'}))

    user_email = forms.EmailField(label="Email", widget = forms.TextInput( attrs= {'placeholder':'Enter your Email Address',} ))

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
