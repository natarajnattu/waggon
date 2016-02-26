from django.conf.urls import include, url
from registration.backends.simple.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

urlpatterns = [
    url(
        r'^register/$',
        RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
        name='registration_register',
    ),

    url(r'', include('registration.backends.simple.urls')),

]
