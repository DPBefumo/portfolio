from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name='index'),
    path('resume/', core_views.resume_detail, name='resume_detail'),
    path('projects/', core_views.project_detail, name='project_detail'),
    path('projects/dog_adoption', core_views.dog_adoption, name='dog_adoption'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)