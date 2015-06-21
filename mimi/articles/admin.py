from django.contrib import admin

import articles.models as m

class ArticleArticleTagInline(admin.TabularInline):
    model = m.ArticleArticleTag
    pass

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'published')
    prepopulated_fields = {"slug": ("headline",)}

class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(m.Article, ArticleAdmin)
admin.site.register(m.ArticleTag, ArticleTagAdmin)
