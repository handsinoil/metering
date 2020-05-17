from django.db import models


class UsersSNT(models.Model):
	login_user = models.EmailField(max_length=254, verbose_name='Логин')
	parole_user = models.PositiveSmallIntegerField(verbose_name='Пароль')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
	name_user = models.CharField(max_length=254, db_index=True, verbose_name='Имя члена СНТ')

	def __str__(self):
		return self.name_user

	class Meta:
		verbose_name = 'Пользователи'
		verbose_name_plural = 'Список пользователей'
		ordering = ['name_user']


class Meter(models.Model):
	user = models.ForeignKey(UsersSNT, on_delete=models.PROTECT, verbose_name='Пользователь')
	when_rec = models.DateTimeField(auto_now_add=True, verbose_name='Дата внесения')
	updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
	gas = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Газ')
	light = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Свет')
	water = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Вода')

	class Meta:
		verbose_name = 'Показания'
		verbose_name_plural = 'Показания'
		ordering = ['-when_rec']


class Rate(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
	r_gas = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Тариф за Газ')
	r_light = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Тариф за Свет')
	r_water = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Тариф за Вода')

	class Meta:
		verbose_name = 'Тариф'
		verbose_name_plural = 'Тарифы'
		ordering = ['-created_at']


class UnitValue(models.Model):
	when_rec = models.DateTimeField(auto_now_add=True, verbose_name='Дата внесения')
	updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
	gas = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Газ')
	light = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Свет')
	water = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Вода')

	class Meta:
		verbose_name = 'Показания'
		verbose_name_plural = 'Общие показания'
		ordering = ['-when_rec']


class News(models.Model):
	title = models.CharField(max_length=150, verbose_name='Наименование')
	content = models.TextField(blank=True, verbose_name='Контент')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
	updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'
		ordering = ['-created_at']
