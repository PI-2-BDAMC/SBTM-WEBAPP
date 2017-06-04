from django.conf.urls import include, url
from django.contrib import admin
import sbtmApp.views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^startEngine/', sbtmApp.views.startEngine, name="startEngine"),
    url(r'^$', sbtmApp.views.index, name='index'),
    url(r'^previousTests/', sbtmApp.views.previousTests, name="previousTests"),
    url(r'^graphs/', sbtmApp.views.graphs, name="graphs"),
]
