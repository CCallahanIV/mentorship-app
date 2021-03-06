"""mentorship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from mentorship_profile import views as profile_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('django.contrib.auth.urls')),
    url(r'^activate_account/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        profile_views.activate_account_view, name='activate_account'),
    url(r'^signup/mentor/', profile_views.register_mentor_view),
    url(r'^signup/mentee/', profile_views.register_mentee_view),
    url(
        r'^activate/',
        TemplateView.as_view(
            template_name="mentorship_profile/activate_notification.html"
        ),
        name="activate_notification"
    )
]
