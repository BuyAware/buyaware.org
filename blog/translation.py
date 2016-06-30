from modeltranslation.translator import translator, TranslationOptions
from .models import PostModel

# Provide fields to translate blog posts in the registered languages
class PostModelTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'abstract')

translator.register(PostModel, PostModelTranslationOptions)
