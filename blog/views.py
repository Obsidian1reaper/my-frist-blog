from django.shortcuts import render

# Create your views here.


def post_list(request):
    return render(request, 'blog/post_list.html', {})

# render - ф-ция, которая соберет готовый шаблон для страницы
