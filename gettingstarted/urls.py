from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
import coffee.views

import hobbies.views

from django.template import Context, loader
from django.conf.urls.static import static

import gettingstarted.settings
# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('coffee/',coffee.views.Coffee.as_view(),name='coffee'),
    path('illustrations/',hobbies.views.IllustrationsView.as_view(),name='illustrations'),
    path('illustrations/<int:pk>/',hobbies.views.IllustrationsDetails.as_view(),name='illustrations_detail'),
    path('photography/',hobbies.views.Photography.as_view(),name='photography'),
    path('photography/<int:pk>/',hobbies.views.PhotographyDetails.as_view(),name='photography_detail'),
    path('skate/',hobbies.views.Skate.as_view(),name='skate'),

]+static(gettingstarted.settings.STATIC_URL,document_root=gettingstarted.settings.STATIC_ROOT) 
