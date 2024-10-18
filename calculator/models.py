from django.db import models
import sys
from settings import CALCULATOR_FIELDS

class Nutrition(models.Model):
	nutr_kinds = {0: 'водянистый', 1: 'концентрированный', 2: 'зеленый', 3: 'грубый', 4: 'сочный', 5: 'минеральная добавка'}

	name = models.CharField(max_length=110, unique=True, verbose_name='Корм')
	kind = models.SmallIntegerField(choices=nutr_kinds, default=1, verbose_name='Тип корма')
	feed_unit = models.FloatField(verbose_name="Корм. ед.", default=0)
	energy_krs_mj = models.FloatField(verbose_name="Обмен. энерг. КРС, МДж", default=0)
	dry_matter_g = models.FloatField(verbose_name="Сухое в-во, г", default=0)
	crude_protein_g = models.FloatField(verbose_name="Сырой протеин, г", default=0)
	digestible_protein_g = models.FloatField(verbose_name="Перев. протеин, г", default=0)
	crude_fat_g = models.FloatField(verbose_name="Сыр. жир, г", default=0)
	crude_fiber_g = models.FloatField(verbose_name="Сыр. клетчатка, г", default=0)
	starch_g = models.FloatField(verbose_name="Крахмал, г", default=0)
	sugar_g = models.FloatField(verbose_name="Сахар, г", default=0)
	lysine_g = models.FloatField(verbose_name="Лизин, г", default=0)
	methionine_cystine_g = models.FloatField(verbose_name="Метионин+цистин, г", default=0)
	calcium_g = models.FloatField(verbose_name="Кальций, г", default=0)
	phosphorus_g = models.FloatField(verbose_name="Фосфор, г", default=0)
	magnesium_g = models.FloatField(verbose_name="Магний, г", default=0)
	potassium_g = models.FloatField(verbose_name="Калий, г", default=0)
	sulfur_g = models.FloatField(verbose_name="Сера, г", default=0)
	iron_mg = models.FloatField(verbose_name="Железо, мг", default=0)
	copper_mg = models.FloatField(verbose_name="Медь, мг", default=0)
	zinc_mg = models.FloatField(verbose_name="Цинк, мг", default=0)
	manganese_mg = models.FloatField(verbose_name="Марганец, мг", default=0)
	cobalt_mg = models.FloatField(verbose_name="Кобальт, мг", default=0)
	iodine_mg = models.FloatField(verbose_name="Йод, мг", default=0)
	carotene_mg = models.FloatField(verbose_name="Каротин, мг", default=0)
	vitamin_d_me = models.FloatField(verbose_name="Вит. Д, МЕ", default=0)
	vitamin_e_mg = models.FloatField(verbose_name="Вит. Е, мг", default=0)

	class Meta:
		verbose_name = "Корм"
		verbose_name_plural = "Корма"

	def __str__(self):
		return f"Корм {self.name} типа {self.kind} (корм. ед.: {self.feed_unit}, обмен. энергия: {self.energy_krs_mj} МДж)"

	def to_list(self):
		return [getattr(self, field) for field in CALCULATOR_FIELDS]

class Norm(models.Model):
	target = models.CharField(max_length=70, unique=True, verbose_name='Корм')
	feed_unit = models.FloatField(verbose_name="Корм. ед.", default=0)
	energy_krs_mj = models.FloatField(verbose_name="Обмен. энерг. КРС, МДж", default=0)
	dry_matter_g = models.FloatField(verbose_name="Сухое в-во, г", default=0)
	crude_protein_g = models.FloatField(verbose_name="Сырой протеин, г", default=0)
	digestible_protein_g = models.FloatField(verbose_name="Перев. протеин, г", default=0)
	crude_fat_g = models.FloatField(verbose_name="Сыр. жир, г", default=0)
	crude_fiber_g = models.FloatField(verbose_name="Сыр. клетчатка, г", default=0)
	starch_g = models.FloatField(verbose_name="Крахмал, г", default=0)
	sugar_g = models.FloatField(verbose_name="Сахар, г", default=0)
	calcium_g = models.FloatField(verbose_name="Кальций, г", default=0)
	phosphorus_g = models.FloatField(verbose_name="Фосфор, г", default=0)
	magnesium_g = models.FloatField(verbose_name="Магний, г", default=0)
	potassium_g = models.FloatField(verbose_name="Калий, г", default=0)
	sulfur_g = models.FloatField(verbose_name="Сера, г", default=0)
	iron_mg = models.FloatField(verbose_name="Железо, мг", default=0)
	copper_mg = models.FloatField(verbose_name="Медь, мг", default=0)
	zinc_mg = models.FloatField(verbose_name="Цинк, мг", default=0)
	manganese_mg = models.FloatField(verbose_name="Марганец, мг", default=0)
	cobalt_mg = models.FloatField(verbose_name="Кобальт, мг", default=0)
	iodine_mg = models.FloatField(verbose_name="Йод, мг", default=0)
	carotene_mg = models.FloatField(verbose_name="Каротин, мг", default=0)
	vitamin_d_me = models.FloatField(verbose_name="Вит. Д, МЕ", default=0)
	vitamin_e_mg = models.FloatField(verbose_name="Вит. Е, мг", default=0)
	salt_g = models.FloatField(verbose_name='соль повар., г', default=0)

	class Meta:
		verbose_name = "Норма"
		verbose_name_plural = "Нормы"

	def __str__(self):
		return f"Группа животных {self.target} (корм. ед.: {self.feed_unit}, обмен. энергия: {self.energy_krs_mj} МДж)"

	def to_list(self):
		return [getattr(self, field) for field in CALCULATOR_FIELDS]

class Ration(models.Model):
	components = models.ManyToManyField(Nutrition, related_name='rations')
	target = models.ForeignKey(Norm, on_delete=models.CASCADE, related_name='rations')

	@property
	def total(self):
		return [models.Sum('components__{}'.format(field)) for field in CALCULATOR_FIELDS]

	@property
	def diff(self):
		return [models.Sum('components__{}'.format(field)) - models.F('target__{}'.format(field)) for field in CALCULATOR_FIELDS]
