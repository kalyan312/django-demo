"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from datetime import datetime

def welcome(request):
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return HttpResponse(f"""
    <html>
      <head><title>Demo applicartion sync</title></head>
      <body style="font-family: Arial; padding: 24px;">
        <h1>✅ Welcome to Demo (Django)</h1>
        <p>Host: --</p>
        <p>Last render: <b>{now}</b></p>
        <p>If you see this, git-sync + Django reload is working, reloaded indicator: 1 .</p>
        <hr/>
        <a href="/admin/">Go to Admin</a>
      </body>
    </html>
    """)

urlpatterns = [
    path("", welcome),  
    path('admin/', admin.site.urls),
]
