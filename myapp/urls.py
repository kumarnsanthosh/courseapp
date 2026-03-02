from .views import home
from django.urls import path

app_name = 'myapp'

urlpatterns = [ path('', home)

]