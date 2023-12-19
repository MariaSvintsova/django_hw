from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from main.views import contact, home, catalog

urlpatterns = [
    path('', home),
    path('catalog/', catalog, name='catalog'),
    path('contacts/', contact, name='contact')
]
