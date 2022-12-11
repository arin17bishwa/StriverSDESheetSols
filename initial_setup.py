from typing import List
from slugify import slugify
import json
import os
import sys
import striver_sde_sheet_scraper


def create_dir_structure(topic_name: str, topic_contents: List[dict], force_overwrite: bool = False) -> None:
    os.mkdir(topic_name)
    os.chdir(topic_name)
    for problem in topic_contents:
        create_file_details(problem)


def create_file_details(problem_data: dict) -> None:
    filename = '{}.py'.format(slugify(problem_data['name'], separator='_', replacements=(("'", ""),)))
    lines = [
        '"""',
        'Problem Name: {}'.format(problem_data['name']),
        'TUF Link: {}'.format(problem_data.get('editorial', 'N/A')),
        '"""\n',
    ]
    with open(filename, 'w') as file:
        file.writelines('\n'.join(lines))


def main(filename: str = 'striver_sde_sheet_data.json'):
    try:
        with open(filename, 'r') as data_file:
            js = json.load(data_file)
    except FileNotFoundError:
        '''if json data file DNE, then it calls the scraper to create that data file'''
        striver_sde_sheet_scraper.main()
        main()
        return
    try:
        os.makedirs('solutions')
        os.chdir('solutions')
        solutions_path = os.getcwd()
        for topic_name, topic_contents in js.items():
            os.chdir(solutions_path)
            create_dir_structure(topic_name, topic_contents)
    except FileExistsError:
        sys.exit('"solutions" directory already exists. Please remove it to create a fresh directory structure.')
    return


if __name__ == '__main__':
    main()
