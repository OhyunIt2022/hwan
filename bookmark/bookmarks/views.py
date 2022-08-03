from multiprocessing import context
from urllib.robotparser import RequestRate
from django.shortcuts import render

from bookmarks.models import Bookmark
def bookmark_list(request):
    bookmark_list = Bookmark.objects.all()
    # bookmark_list = Bookmark.objects.all()  북마크 데이터 베이스에 있는 데이터 들을 모두 갖고 와서 bookmark_list에 저장 해줘라
    context = {'bookmark_list':bookmark_list} #딕셔너리
    return render(request, 'templates/bookmark_list.html',context) #reder -> html로 바꿔줌


def bookmark_detail(request, pk):
    bookmark = Bookmark.objects.get(id=pk)
    context = {'bookmark':bookmark}
    return render(request, 'templates/bookmark_detail.html',context)