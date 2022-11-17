from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
import datetime
from service_functions import get_number_years_repr
from collections import defaultdict
from environs import Env
import os
import sys
import argparse
import pathlib


def get_wine_card_from_excel(excel_file_path):
    excel_data_df = pandas.read_excel(
        excel_file_path,
        names=['category', 'wine_name', 'grape_variety', 'price', 'image_name', 'promo'],
        keep_default_na=False)

    wine_card = excel_data_df.to_dict(orient='records')

    wine_card_by_category = defaultdict(list)

    for wine in wine_card:
        wine_card_by_category[wine['category']].append(wine)

    return wine_card_by_category


def main():
    parser = argparse.ArgumentParser(description='Wine-master site')
    parser.add_argument('-f', type=pathlib.Path, help='Wine card excel file path')
    args = parser.parse_args()

    excel_file_path = args.f

    base_dir = os.path.dirname(os.path.abspath(__file__))

    env_path = os.path.join(base_dir, 'venv', '.env')
    env = Env()
    env.read_env(env_path)

    if not excel_file_path:
        excel_file_path = env.str('EXCEL_FILE_PATH', '')

    try:
        wine_card_by_category = get_wine_card_from_excel(excel_file_path)
    except FileNotFoundError as e:
        print(f'Define the file name in -f argument or in EXCEL_FILE_PATH parameter in the file venv{os.sep}.env')
        sys.exit(1)

    today = datetime.date.today()
    foundation_year = env.int('FOUNDATION_YEAR', today.year - 1)
    winery_age = today.year - foundation_year

    jinja_env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = jinja_env.get_template('template.html')

    rendered_page = template.render(
        winery_age=winery_age,
        years_repr=get_number_years_repr(winery_age),
        wine_card=wine_card_by_category,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
