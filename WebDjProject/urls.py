# Импортируем функцию admin из модуля django.contrib.admin
# admin позволяет работать с административной панелью Django
from django.contrib import admin

# Импортируем функции path и include из модуля django.urls
# path - для создания отдельных маршрутов
# include - для подключения маршрутов из других файлов (приложений)
from django.urls import path, include

# Создаем список urlpatterns для ВСЕГО проекта
# Этот список обрабатывает ВСЕ запросы к сайту
urlpatterns = [
    # Создаем маршрут для административной панели Django
    # Когда пользователь перейдет на URL /admin/
    # Django покажет стандартную админ-панель
    path('admin/', admin.site.urls),

    # Подключаем маршруты из нашего приложения myapp
    # Первый параметр '' - означает КОРЕНЬ сайта (после домена ничего нет)
    # Второй параметр include('myapp.urls') - говорит Django:
    # "Возьми все маршруты из файла urls.py приложения myapp"
    # Теперь маршруты из myapp будут работать в корне сайта
    path('', include('myapp.urls')),
]
