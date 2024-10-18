from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Nutrition, Norm, Ration

admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
	list_display = ('name', 'kind', 'feed_unit', 'energy_krs_mj')
	list_filter = ('kind',)
	ordering = ('name',)
	search_fields = ('name', 'kind')
	fieldsets = (
		('Корм', {
			'fields': ('name', 'kind'),
		}),
		('Характеристики', {
			'fields': (
				'feed_unit', 'energy_krs_mj', 'dry_matter_g', 'crude_protein_g', 'digestible_protein_g', 
				'crude_fat_g', 'crude_fiber_g', 'starch_g', 'sugar_g', 'lysine_g', 'methionine_cystine_g', 
				'calcium_g', 'phosphorus_g', 'magnesium_g', 'potassium_g', 'sulfur_g', 'iron_mg', 'copper_mg',
				'zinc_mg', 'manganese_mg', 'cobalt_mg', 'iodine_mg', 'carotene_mg', 'vitamin_d_me', 'vitamin_e_mg',
				),
			'classes': ('collapse',),
		}),
	)

@admin.register(Norm)
class NormAdmin(admin.ModelAdmin):
	list_display = ('target', 'feed_unit', 'energy_krs_mj')
	ordering = ('target',)
	search_fields = ('targe',)
	fieldsets = (
		('Группа животных', {
			'fields': ('target',),
		}),
		('Характеристики', {
			'fields': (
				'feed_unit', 'energy_krs_mj', 'dry_matter_g', 'crude_protein_g', 'digestible_protein_g', 
				'crude_fat_g', 'crude_fiber_g', 'starch_g', 'sugar_g', 
				'calcium_g', 'phosphorus_g', 'magnesium_g', 'potassium_g', 'sulfur_g', 'iron_mg', 'copper_mg',
				'zinc_mg', 'manganese_mg', 'cobalt_mg', 'iodine_mg', 'carotene_mg', 'vitamin_d_me', 'vitamin_e_mg', 'salt_g',
				),
			'classes': ('collapse',),
		})
	)

@admin.register(Ration)
class RationAdmin(admin.ModelAdmin):
	list_display = ('target', 'count_components')
	ordering = ('target',)
	search_fields = ('target',)
	fieldsets = (
		('Группа животных', {
			'fields': ('target',)
		}),
		('Компоненты', {
			'fields': ('components',),
			'class': ('collapse',),
		}),
	)

	def count_components(self):
		return self.components.count()
	
