from django.urls import path
from .views import ProfileView
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(ProfileView.as_view()), name='profile'), # добавим кэширование на главную
    # страницу. Раз в 1 минуту страница будет записываться в кэш для экономии ресурсов.
]
