"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from bookmarks import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmark/', views.bookmark_list),
    path('bookmark/<int:pk>/', views.bookmark_detail)
]

"""
bookmark/?/
북마크 리스트
- 북마크 제목(네이버)
- 북마크 제목
.
.
.
.

bookmark/?/
네이버
- url:www.naver.com
- memo: 네이버 홈페이지 입니다.

"""

# 드래그 하고 컨트롤 물음표 눌러서 주석처리 가능