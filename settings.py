from pathlib import Path

# dirs
BASE_DIR = Path(__file__).resolve().parent
DJANGO_DIR = BASE_DIR
DJANGO_MANAGE_FILE = DJANGO_DIR / 'manage.py'
DB_EXCEL = BASE_DIR / 'db/Рацион_рабочая тетрадь_зоотехника_2011.xlsm'

# fields
NUTR_FIELDS_NAMES = ['Корм. ед.', 'Обмен.энерг. КРС, МДж', 'Сухое в-во, г.', 'Сырой протеин,г', 'Перев.протеин, г', 'сыр. жир, г', 'сыр.клетчатка,г', 'крахмал,г', 'Сахар,г', 'Лизин, г', 'метионин+цистин, г', 'кальций,г', 'Фосфор,г', 'Магний,г', 'Калий,г', 'Сера,г', 'Железо, мг', 'Медь, мг', 'Цинк, мг', 'Марганец, мг', 'Кобальт, мг', 'Йод, мг', 'Каротин, мг', 'Вит. Д, МЕ', 'Вит. Е, мг']
NORM_FIELDS_NAMES = ['Корм. ед.', 'Обмен.энерг. КРС, МДж', 'Сухое в-во, г.', 'Сырой протеин,г', 'Перев.протеин, г', 'сыр. жир, г', 'сыр.клетчатка,г', 'крахмал,г', 'Сахар,г', 'кальций,г', 'Фосфор,г', 'Магний,г', 'Калий,г', 'Сера,г', 'Железо, мг', 'Медь, мг', 'Цинк, мг', 'Марганец, мг', 'Кобальт, мг', 'Йод, мг', 'Каротин, мг', 'Вит. Д, МЕ', 'Вит. Е, мг', 'соль повар., г']
CALCULATOR_FIELDS_NAMES = ['Корм. ед.', 'Обмен.энерг. КРС, МДж', 'Сухое в-во, г.', 'Сырой протеин,г', 'Перев.протеин, г', 'сыр. жир, г', 'сыр.клетчатка,г', 'крахмал,г', 'Сахар,г', 'кальций,г', 'Фосфор,г', 'Магний,г', 'Калий,г', 'Сера,г', 'Железо, мг', 'Медь, мг', 'Цинк, мг', 'Марганец, мг', 'Кобальт, мг', 'Йод, мг', 'Каротин, мг', 'Вит. Д, МЕ', 'Вит. Е, мг']
NORM_FIELDS = ["target", "feed_unit", "energy_krs_mj", "dry_matter_g", "crude_protein_g", "digestible_protein_g", "crude_fat_g", "crude_fiber_g", "starch_g", "sugar_g", "calcium_g", "phosphorus_g", "magnesium_g",
	"potassium_g", "sulfur_g", "iron_mg", "copper_mg", "zinc_mg", "manganese_mg", "cobalt_mg", "iodine_mg", "carotene_mg", "vitamin_d_me", "vitamin_e_mg", "salt_g"]
NUTR_FIELDS = ["name", "kind", "feed_unit", "energy_krs_mj", "dry_matter_g", "crude_protein_g", "digestible_protein_g", "crude_fat_g", "crude_fiber_g", "starch_g", "sugar_g", "lysine_g", "methionine_cystine_g",
	"calcium_g", "phosphorus_g", "magnesium_g", "potassium_g", "sulfur_g", "iron_mg", "copper_mg", "zinc_mg", "manganese_mg", "cobalt_mg", "iodine_mg", "carotene_mg", "vitamin_d_me", "vitamin_e_mg"]
CALCULATOR_FIELDS = ["feed_unit", "energy_krs_mj", "dry_matter_g", "crude_protein_g", "digestible_protein_g", "crude_fat_g", "crude_fiber_g", "starch_g", "sugar_g", "calcium_g", "phosphorus_g", "magnesium_g",
	"potassium_g", "sulfur_g", "iron_mg", "copper_mg", "zinc_mg", "manganese_mg", "cobalt_mg", "iodine_mg", "carotene_mg", "vitamin_d_me", "vitamin_e_mg"]
