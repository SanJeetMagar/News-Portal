from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

api_prefix: str = "api"
version: str = "v1"

if version:
    api_prefix = f"{api_prefix}/{version}/"

urlpatterns = [
    path("admin/", admin.site.urls),

    path(f"{api_prefix}", include([
        path("auth/", include("src.apps.auth.urls")),
        path("news/",include("src.apps.news.urls")),
        path("interactions/",include('src.apps.interactions.urls')),
        path("news_media/", include("src.apps.news_media.urls")),
    ])),
]
if settings.DEBUG:
    urlpatterns += [
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path("", SpectacularSwaggerView.as_view(), name="swagger-ui"),
        path("redoc/", SpectacularRedocView.as_view(), name="redoc"),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
