from django.urls import path
from .views import posts, quienessomos, postindividual, registrouser, CustomLogoutView, eliminar_post, nuevo_post, modificar_post
from django.contrib.auth import views as auth_views

urlpatterns = [
    path ('', posts, name = 'posts'),
    path('quienessomos/', quienessomos, name='quienessomos'), 
    path('post/<int:post_id>/', postindividual, name='postindividual'),
    path('registro/', registrouser, name='registro'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('post/eliminar/<int:post_id>/', eliminar_post, name='eliminar_post'),
    path('modificar_post/<int:id>/', modificar_post, name='modificar_post'),
    path('nuevo_post/', nuevo_post, name='nuevo_post'),
]