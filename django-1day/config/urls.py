from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import Http404
from users import views as users_views

from todo.views import todo_list, todo_info

# 임시 유저 데이터 (딕셔너리로 직접 정의)
user_db = {}

# 내부에서 참조할 수 있도록 별도 변수로 저장
_db = user_db

def user_list(request):
    names = [{'id': key, 'name': value['이름']} for key, value in _db.items()]
    return render(request, 'user_list.html', {'data': names})

def user_info(request, user_id):
    if user_id not in _db:
        raise Http404('User not found')
    info = _db[user_id]
    return render(request, 'user_info.html', {'data': info})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', user_list, name='user_list'),
    path('users/<int:user_id>/', user_info, name='user_info'),
    path('todo/', todo_list, name='todo_list'),
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),
    path('accounts/login/', users_views.login, name='login'),
    path('accounts/signup/', users_views.sign_up, name='signup')
]