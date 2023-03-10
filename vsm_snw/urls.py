from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from simple_robots.views import serve_robots
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtail.documents import urls as wagtaildocs_urls
from wagtail_tag_manager import urls as wtm_urls
from wagtail_transfer import urls as wagtailtransfer_urls

import private
from commons.views import Test404View, Test500View
from search import views as search_views

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.SearchView.as_view(), name="search"),
    path("robots.txt", serve_robots),
    path("sitemap.xml", sitemap),
    path("wtm/", include(wtm_urls)),
    path("hitcount/", include("hitcount.urls", namespace="hitcount")),
    path('', include('private.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    # Testing for 404 & 500 Responses
    urlpatterns.append(path("test_404/", Test404View.as_view()))
    urlpatterns.append(path("test_500/", Test500View.as_view()))

if settings.DEBUG or settings.SHOW_DEBUG_TOOLBAR:
    # Django Debug Toolbar
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("wagtail-transfer/", include(wagtailtransfer_urls)),
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
