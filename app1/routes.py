from dash_app.base.urls import Url

from app1.pages.page1.view import page1_layout
from app1.pages.page2.view import page2_layout

app1_urlpatterns = [
    Url('/app/1', page1_layout),
    Url('/app/2', page2_layout),
]
