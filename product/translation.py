from modeltranslation.translator import translator, TranslationOptions
from .models import Product,Comment,Category,Option

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
translator.register(Product, NewsTranslationOptions)

    
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
translator.register(Category, CategoryTranslationOptions)


class OptionTranslationOptions(TranslationOptions):
    fields = ('title',)
translator.register(Option, OptionTranslationOptions)


class CommentTranslationOptions(TranslationOptions):
    fields = ('content',)
translator.register(Comment, CommentTranslationOptions)