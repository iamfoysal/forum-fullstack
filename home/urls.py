from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('signup/', views.register, name='register'),
  path('login/', views.login, name='login'),
  path('logout-view/' , views.logout_view, name="logout_view"),
  path('add-blog/', views.add_blog, name='add_blog'),
  # path("<int:id>/",views.add_blog, name= "blog_update"),
  path('blog_detail/<slug>' , views.blog_detail, name="blog_detail"),
  path('see-blog/' , views.see_blog, name="see_blog"),
  path('blog-delete/<id>' , views.blog_delete, name="blog_delete"),
  path('blog-update/<slug>/' , views.blog_update, name="blog_update"),
  path('verify/<token>/' , views.verify, name="verify")
]
