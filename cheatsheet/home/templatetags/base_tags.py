from ..models import Footer # Импортируем модель Footer

from django import template # Импортируем template из django для создания шаблонных тегов


register = template.Library() # Создаем декоратор для тегов

@register.inclusion_tag('home/tags/footer.html', takes_context=True) # Передаем созданному
# ранее декоратору register два аргумента. Первый шаблон html,
# второй служит для передачи контекста в нутри тега в строке 'request': context['request'],
def footer_tag(context): # создаем тег  принимающий контекст

    return { # Возвращаем объект, в его состав входит
        'request': context['request'], # контекст
        'footer': Footer.objects.first() # первая запись Footer из базы данных
    }


