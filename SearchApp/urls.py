
from django.contrib import admin
from django.urls import path
from Search import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.search),
    path('posts/<int:id>/',views.dynamicPage,name="post"),
    path('posts',views.dynamic,name="post"),
    # path('posts/<int:post_id>',views.posts)
    # path('resultPage',views.resultPage),
    # path('post1',views.post1,name="post1")
    # path('search',views.search),
]
