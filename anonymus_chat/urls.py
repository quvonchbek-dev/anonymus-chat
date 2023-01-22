
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from chat.views import index, message_delete

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor", include("ckeditor_uploader.urls")),
    path("", index),
    path(r'^delete/(?P<pk>[0-9]+)/$', message_delete, name='message_delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
