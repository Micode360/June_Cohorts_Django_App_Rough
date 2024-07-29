import os
import json
from django.http import HttpResponse
from django.conf import settings # or from my_app.settings import MEDIA_ROOT


def message (request):
    return HttpResponse("Hello from the server",content_type="text/plain")


def another_func (request):
    return HttpResponse("Hello from another functionality",content_type="text/plain")

def get_html(request):
    return HttpResponse("<h1>I am from the hmtl view function</h1>", content_type="text/html")


def json_func(request):
    data = {'message': 'This is JSON data'}
    return HttpResponse(json.dumps(data), content_type="application/json")

def xml_func(request):
    return HttpResponse("<transport>i am a data</transport>", content_type="application/xml")

def csv_func(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'

    data = '''
        Name, Age, Gender
        King, 26, Male
        Alice, 22, Female
    '''
    response.write(data)
    return response


def download_pdf(request):

    # get the pdf inside the media folder
    pdf_path = os.path.join("media", "the_story_of_the_boy.pdf")

    # Open file in binary mode. rb means read binary
    with open(pdf_path, 'rb') as pdf_file:
        pdf_content = pdf_file.read()

    # create a http response with the pdf content
    response = HttpResponse(pdf_content, content_type="application/pdf")

    return response


def video_func(request):
    video_path = os.path.join(settings.MEDIA_ROOT, "video.mp4")

    with open(video_path, 'rb') as video_file:
        response = HttpResponse(video_file.read(), content_type="video/mp4")
        return response
