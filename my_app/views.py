from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Musician, Album
# here all forms of my_app will be imported
# from my_app.form import user_form
from my_app.form import MusicianForm

# Create your views here.

def index(request):
    # return render(request, 'my_app/index.html', context=diction)
    # DJNGO query
    musician_list = Musician.objects.order_by('first_name')
    # here we can get any value or release date from any album according to the index of that album object
    diction = {'text_1': "Live",'text_2':'This a list of Musicians', 'musician': musician_list, 'value': Album.objects.get(pk=4), 'value2':'Release'}
    return render(request, 'my_app/index.html', context=diction)

def contact(request):
    diction = {}
    return render(request, 'my_app/contact.html', context=diction)

def about(request):
    diction = {}
    return render(request, 'my_app/about.html', context=diction)

def form(request):
    new_form = MusicianForm()

    if request.method == 'POST':
        new_form = MusicianForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
    diction = {'test_form': new_form, 'heading_3':'Add New Musician'}
    return render(request, 'my_app/form.html', context=diction)


# def form(request):
#     # here initial form will be stored
#     new_form = user_form
#     # diction = {'test_form': new_form, 'heading_1': "This form is created using django forms library"}
#     diction = {'test_form': new_form, 'heading_2': "Django Form"}
#
#     if request.method == 'POST':
#         # here form with inputs will be stored
#         new_form = user_form(request.POST)
#         # to show error messages we must update the initial form with the new form to find error
#         diction.update({'test_form':new_form})
#         #here the validation of the inputs will be checked
#         if new_form.is_valid():
#             # if valid the values will be collected from new form
#             user_name = new_form.cleaned_data['user_name']
#             user_dob = new_form.cleaned_data['user_dob']
#             user_email = new_form.cleaned_data['user_email']
#             agreement = new_form.cleaned_data['agreement']
#
#             diction.update({'user_name':user_name})
#             diction.update({'user_dob':user_dob})
#             diction.update({'user_email':user_email})
#             diction.update({'agreement': agreement})
#
#             diction.update({'rating': new_form.cleaned_data['rating']})
#             diction.update({'gender': new_form.cleaned_data['gender']})
#             diction.update({'color': new_form.cleaned_data['color']})
#             diction.update({'user_age': new_form.cleaned_data['user_age']})
#             diction.update({'num_field': new_form.cleaned_data['num_field']})
#
#             diction.update({'user_vemail': 'Emails Match!!'})
#
#             diction.update({'form_submited':"Yes"})
#
#     return render(request, 'my_app/form.html', context=diction)

# def index(request):
# #     diction = {}
# #     return render(request, 'my_app/index.html', context=diction)
#
# # def index(request):
# #     return HttpResponse("<h1>Hello World<h1>")
#
# # def index(request):
# #         return HttpResponse("<h1>MY app<h1>")
#
# # def home(request):
# #     return HttpResponse("<h1>This is Homepage</h1> <a href='contact/'>Contact</a> <a href='about/'>About</a>")
# #
# # def contact(request):
# #     return HttpResponse("<h1>This is Contact Page</h1> <a href='/my_app'>Homepage</a> <a href='/my_app/about/'>About</a>")
# #
# # def about(request):
# #     return HttpResponse("<h1>About Us</h1> <a href='/my_app'>Homepage</a> <a href='/my_app/contact/'>Contact</a>")
#
# # def home(request):
# #     return HttpResponse("<h1>This is Homepage</h1> <a href='contact/'>Contact</a> <a href='about/'>About</a>")
# #
# # def contact(request):
#     # return HttpResponse("<h1>This is Contact Page</h1> <a href='/'>Homepage</a> <a href='/about/'>About</a>")
# #
# def about(request):
#     return HttpResponse("<h1>About Us</h1> <a href='/'>Homepage</a> <a href='/contact/'>Contact</a>")
