from django.db import models
from wagtail.core.models import  Page
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel # доавили импорт MultiFieldPanel

from modelcluster.fields import ParentalKey # Импортируем ParentalKey

class EquipmentOperator(models.Model): # Добавим модель фрагмента - сниппета
    """Оператор оборудования"""

    name = models.CharField(max_length=100, blank=False, null=False) # добавим поле имя оператора
    email = models.EmailField() # добавим поле адреса электронной почты

    equipment = ParentalKey( # Связываем EquipmentOperator (ParentalKey
        # как и Page наследуется от  ClusterableModel)
        # с EquipmentPage через ParentalKey
        'equipment.EquipmentPage', # Указываем что в приложении equipment
        # есть страница EquipmentPage с которой нужно установить связь
        on_delete=models.CASCADE, # Если EquipmentPage будет удалена,
        # то EquipmentPage тоже удаляется
        related_name='operators' # имя по которому можно обращаться к
        # EquipmentOperator из EquipmentPage
    )


class EquipmentPage(Page):
    """Страница с финформацией о единице оборудования"""

    description = RichTextField( # добавляем поле описание
        blank=True,
        null=True,
        features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', # разрешаем использование функций редактора
                  'hr', 'bold', 'italic', 'ol', 'ul', 'link'],
    )

    content_panels = Page.content_panels + [
        FieldPanel('description'), # добавляем возможность отображения поля в админпанели
        MultiFieldPanel([ # добавляет вывод красной полосы с заголовком heading
            InlinePanel('operators', label="оператора")], # через InlinePanel добавим
            # возможность вывода фрагмента в админпанели и именование кнопки
            heading="Операторы",) # Заголовок
    ]

    subpage_types = [] # ограничиваем дочерние стриницы
    parent_page_types = ['equipment.EquipmentIndexPage'] # ограничиваем родительские страницы

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"

class  EquipmentIndexPage(Page):
    """Страница для вывода списка оборудования"""

    max_count = 1 # ограничиваем число страниц одной
    subpage_types = ['equipment.EquipmentPage'] # ограничиваем дочерних страниц
    parent_page_types = ['home.HomePage'] # ограничиваем родительских страниц