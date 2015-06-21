from django.contrib import admin

import authors.models as m

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'slug')
    readonly_fields = ('slug',)

## Registered administrative pages.
admin.site.register(m.Author, AuthorAdmin)

