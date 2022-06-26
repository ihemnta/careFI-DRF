from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Swagger')


sub_patterns = [
    path('v1/auth/', include('authenticate.urls')),
    path('v1/', include('bitcoin_api.urls')),
    path('swagger/', schema_view, name="schema_api"),
    # path(r'^swagger/', schema_view),
]


urlpatterns = [
    path('api/', include(sub_patterns)),
]