



class FigCaptionBlock(StructBlock): # В данном блоке будет храниться
# изображение и подпись к нему, он наследуется от исходного StructBlock
    caption = CharBlock() #  Подпись к рисунку
    figure = ImageChooserBlock() # Картинка

    class Meta: # в классе Meta
        icon = 'image' # мы задаем иконку (название ее берем из
        template = 'blocks/fig_caption_block.html' #
