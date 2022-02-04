from dash_app.base.urls import Url

from credentialing.pages.page1.view import layout


credentialing_urlpatterns = [
    Url('/credentialing', layout),

]
