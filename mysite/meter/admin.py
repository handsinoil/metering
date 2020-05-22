from django.contrib import admin

from .models import UnitValue, Rate, Meter, UsersSNT, News


class AdminUsersSNT(admin.ModelAdmin):
	list_display = ('id', 'name_user', 'login_user', 'parole_user', 'created_at')
	list_display_links = ('id', )
	search_fields = ('login_user', 'name_user')
	list_editable = ('name_user', 'login_user', 'parole_user')
	list_filter = ('name_user',)


class MeterAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'when_rec', 'updated_at', 'gas', 'light', 'water')
	list_display_links = ('id', 'user')
	search_fields = ('user', 'when_rec', 'updated_at')
	list_editable = ('gas', 'light', 'water')
	list_filter = ('user',)


class RateAdmin(admin.ModelAdmin):
	list_display = ('id', 'created_at', 'r_gas', 'r_light', 'r_water')
	list_display_links = ('id',)
	search_fields = ('created_at',)
	list_editable = ('r_gas', 'r_light', 'r_water')
	list_filter = ('created_at',)


class UnitValueAdmin(admin.ModelAdmin):
	list_display = ('id', 'when_rec', 'updated_at', 'gas', 'light', 'water')
	list_display_links = ('id',)
	search_fields = ('when_rec', 'updated_at')
	list_editable = ('gas', 'light', 'water')
	list_filter = ('when_rec',)


class NewsAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'created_at', 'updated_at', 'content')
	list_display_links = ('id',)
	search_fields = ('title', 'content')
	list_editable = ('content', 'title')


admin.site.register(UsersSNT, AdminUsersSNT)
admin.site.register(Meter, MeterAdmin)
admin.site.register(Rate, RateAdmin)
admin.site.register(UnitValue, UnitValueAdmin)
admin.site.register(News, NewsAdmin)
