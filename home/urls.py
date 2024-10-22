from django.urls import path
from .views import user_profile ,sponsor , select_category , search , user_register , announcement_list, announcement_detail, create_announcement, like_announcement, user_login, user_logout
urlpatterns = [
    path('', announcement_list, name='announcement_list'),
    path('announcement/<int:announcement_id>/', announcement_detail, name='announcement_detail'),
    path('announcement/', create_announcement, name='create_announcement'),
    path('announcement/<int:announcement_id>/like/', like_announcement, name='like_announcement'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('search/', search, name='search'),
    path('select_category/<category_id>', select_category, name='category'),
    path('sponsor/', sponsor, name='sponsor'),
    path('user/', user_profile, name='user_profile'),

]
