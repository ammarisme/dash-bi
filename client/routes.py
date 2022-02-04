from dash_app.base.urls import Url

from client.pages.summary.view import layout
from client.pages.claims.view import cliams_layout
from client.pages.charges.view import charges_layout
from client.pages.deposit.view import deposits_layout
from client.pages.ar.view import ar_layout
from client.pages.geo.view import geo_layout
from client.pages.denial.view import denial_layout
from client.pages.reimburse.view import reimburse_layout
from client.pages.cliam_detail.view import cliams_detail_layout
import urllib.parse


client_urlpatterns = [
    Url('/client', layout),
    Url('/client/cliams',cliams_layout),
    Url('/client/charges',charges_layout),
    Url('/client/deposits',deposits_layout),
    Url('/client/ar',ar_layout),
    Url('/client/geo',geo_layout),
    Url('/client/denial',denial_layout),
    Url('/client/reimburse',reimburse_layout),
    Url('/client/cliam_detail',cliams_detail_layout),

]