from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('task.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]
