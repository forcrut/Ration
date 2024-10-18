from settings import DB_EXCEL, NUTR_FIELDS, NORM_FIELDS
import pandas as pd
from calculator.models import Nutrition, Norm

def rebuild():
	df_nutr = pd.read_excel(DB_EXCEL, sheet_name='Корма', usecols='A:AA').fillna(0).round(2)
	df_nutr.columns = NUTR_FIELDS
	df_nutr['kind'] = df_nutr['kind'].map({v: k for k, v in Nutrition.nutr_kinds.items()})
	df_nutr_norm = pd.read_excel(DB_EXCEL, sheet_name='Нормы', usecols='A:Y').fillna(0).round(2)
	df_nutr_norm.columns = NORM_FIELDS

	Nutrition.objects.bulk_create([Nutrition(**row.to_dict()) for _, row in df_nutr.iterrows()], ignore_conflicts=True)
	Norm.objects.bulk_create([Norm(**row.to_dict()) for _, row in df_nutr_norm.iterrows()], ignore_conflicts=True)
