from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('team/', include('teams.urls')),
    path('question/', include('questions.urls'))
]
