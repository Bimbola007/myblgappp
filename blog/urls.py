from  django.urls import path
from .views import HomeBlogView , DetailBlogView , CreatBlogView , EditBlogPost , DelBlogP

urlpatterns = [path('post/<int:pk>/delete', DelBlogP.as_view() , name = 'del_blogp' ),
               path('post/<int:pk>/edit', EditBlogPost.as_view() , name = 'edit_post' ),
               path('post/new' , CreatBlogView.as_view() , name = 'create_view'),
               path('', HomeBlogView.as_view(), name = 'home'),
               path('post/<int:pk>', DetailBlogView.as_view() , name = 'post_detail'),



]