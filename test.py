from service_functions import number_years_repr
import pandas
from pprint import pprint
from collections import defaultdict

num_list = [1, 11, 14, 15, 17, 21, 31, 2, 20, 22, 32, 3, 23, 4, 24, 5, 10, 69, 667, 1000, 1001, 1014]

"""for num_years in num_list:
    years_repr = number_years_repr(num_years)
    print(f"{num_years} {years_repr}")"""

# excel_data_df = pandas.read_excel('wine.xlsx') #sheet_name='Employees'
# excel_data_df = pandas.read_excel('wine.xlsx', names=['wine_name', 'grape_variety', 'price', 'image_name']) #sheet_name='Employees'
excel_data_df = pandas.read_excel(
    'wine2.xlsx',
    names=['category', 'wine_name', 'grape_variety', 'price', 'image_name'],
    keep_default_na=False)  # sheet_name='Employees'
# print(excel_data_df)
#print('Excel Sheet to Dict:', excel_data_df.to_dict(orient='records'))
wine_card = excel_data_df.to_dict(orient='records')
"""wine_card_by_category = {}
for wine in wine_card:
    category_name = wine['category']
    wine_card_by_category[category_name] = wine_card_by_category.get(category_name, [])
    wine_properties = {
        wine_property: wine[wine_property] for wine_property in wine.keys() if wine_property != 'category'
    }
    wine_card_by_category[category_name].append(wine_in_category)"""

wine_card_by_category = {}
for wine in wine_card:
    category_name = wine['category']
    category_content = wine_card_by_category.setdefault(category_name, [])
    wine_properties = {
        wine_property: wine[wine_property] for wine_property in wine.keys() if wine_property != 'category'
    }
    category_content.append(wine_properties)



wine_card_by_category = defaultdict(list)
for wine in wine_card:
    category_name = wine['category']
    category_content = wine_card_by_category[category_name]
    wine_properties = {
        wine_property: wine[wine_property] for wine_property in wine.keys() if wine_property != 'category'
    }
    category_content.append(wine_properties)

pprint(wine_card_by_category)

# print('Excel Sheet to Dict:', excel_data_df.to_dict(orient='record'))
"""Using short name for 'orient' is deprecated. Only the options: ('dict', list, 'series', 'split', 'records', 'index')
 will be used in a future version. Use one of the above to silence this warning.
print('Excel Sheet to Dict:', excel_data_df.to_dict(orient='record'))"""
