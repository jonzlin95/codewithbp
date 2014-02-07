from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def login_check(user):
    if user is not None and user.is_active:
        return True
    return False

class LoginView(FormView):
    template_name = 'login/login.html'
    form_class = AuthenticationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.request = request
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'],
            password = form.cleaned_data['password'])
            if login_check(user):
                login(request, user)
                next = request.POST.get('next')
                if next != None:
                    return self.form_valid(form, next)
                else:
                    return self.form_valid(form, '/')
            return self.form_invalid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, next):
        return HttpResponseRedirect(next)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)