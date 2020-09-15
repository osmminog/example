from modeltranslation.translator import register, TranslationOptions
from .models import Category, Product


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'description')

