from wagtail.core.blocks import StructBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock


class FigCaptionBlock(StructBlock): # В данном блоке будет храниться
# изображение и подпись к нему, он наследуется от исходного StructBlock
    figure = ImageChooserBlock(label="Картинка") # Картинка и название субблока
    caption = CharBlock() #  Подпись к рисунку


    class Meta: # в классе Meta устанавливается то как будет выглядеть наш
        # блок FigCaptionBlock в административной панели
        icon = 'spinner' # мы задаем иконку (название ее берем из гида по стилям
        template = 'blocks/fig_caption_block.html' # укажем путь к нашему шаблону
        # (создадим его чуть позже) его имя необходимо указывать в нижнем регистре
        # и он должен совпадать по содержанию с название нашего класс и быть
        # записанным в нижнем регистре через подчеркивание, давайте
        # сравним FigCaptionBlock - fig_caption_block
        label = "Картинка с подписью" # подпись к блоку