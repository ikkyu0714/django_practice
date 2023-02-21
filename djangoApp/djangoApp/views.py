from django.http import HttpResponse

def index(request):
    #return HttpResponse("Hello World")
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="utf-8"/>
                <link rel="stylesheet" href="/static/style.css"/>
        </head>
        <body>
        <h1>Hello World</h1>
        </body>
    </html>
    """)

def hoge(request):
    return HttpResponse("Hoge")

def fuga(request):
    return HttpResponse("Fuga")