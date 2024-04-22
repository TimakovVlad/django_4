from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Section, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_scopes_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_scopes_count += 1

        if main_scopes_count == 0:
            raise ValidationError('Укажите основной раздел')
        elif main_scopes_count > 1:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
