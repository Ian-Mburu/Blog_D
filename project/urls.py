
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),

]


urlpatterns += staticfiles_urlpatterns()
handler404 = 'app.views.error_404'