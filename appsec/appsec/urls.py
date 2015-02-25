from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', login_required(TemplateView.as_view(template_name="tracker/dashboard.html")), name='dashboard'),

    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    url(r'^tracker/', include('tracker.urls', namespace="tracker")),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
