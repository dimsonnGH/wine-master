from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
import datetime
from service_functions import number_years_repr
from collections import defaultdict


def get_wine_card_from_excel(excel_file_name):
    excel_data_df = pandas.read_excel(
        excel_file_name,
        names=['category', 'wine_name', 'grape_variety', 'price', 'image_name', 'promo'],
        keep_default_na=False)

    wine_card = excel_data_df.to_dict(orient='records')

    wine_card_by_category = defaultdict(list)
    for wine in wine_card:
        category_name = wine['category']
        category_content = wine_card_by_category[category_name]
        wine_properties = {
            wine_property: wine[wine_property] for wine_property in wine.keys() if wine_property != 'category'
        }
        category_content.append(wine_properties)

    return wine_card_by_category

def main():
    excel_file_name = 'wine.xlsx'

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    today = datetime.date.today()
    foundation_date = datetime.datetime(year=1920, month=1, day=1)
    winery_age = (today.year - foundation_date.year)
    wine_card_by_category = get_wine_card_from_excel(excel_file_name)

    rendered_page = template.render(
        winery_age=winery_age,
        years_repr=number_years_repr(winery_age),
        wine_card=wine_card_by_category,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()