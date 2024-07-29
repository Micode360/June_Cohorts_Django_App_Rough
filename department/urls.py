from django.urls import path
from .views import message, another_func, get_html, json_func, xml_func, csv_func, download_pdf, video_func


urlpatterns = [
    path('message/', message),
    path('another_func/', another_func),
    path('get_html/', get_html),
    path('json/', json_func),
    path('xml/', xml_func),
    path('csv/', csv_func),
    path('download_pdf/', download_pdf),
    path('video/', video_func)
,
]