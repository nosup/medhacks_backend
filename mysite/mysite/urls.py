from django.conf import settings

from django.conf.urls.static import static
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from django.contrib import admin
from .views import SignupView, LoginView


urlpatterns = [
   path("", TemplateView.as_view(template_name="homepage.html"), name="home"),
   path("admin/", admin.site.urls),
   path('account/signup/', SignupView.as_view(), name="account_signup"),
   path('account/login/', LoginView.as_view(), name="account_login"),
   path('account/', include('account.urls')),
]

# urlpatterns = patterns(
#     "",
#     url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
#     url(r"^admin/", include(admin.site.urls)),
#     url(r"^account/signup/$", SignupView.as_view(), name="account_signup"),
#     url(r"^account/", include("account.urls")),
# )
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
