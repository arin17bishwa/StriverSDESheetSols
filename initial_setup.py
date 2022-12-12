from typing import List
from slugify import slugify
import json
import os
import sys
import striver_sde_sheet_scraper


def create_dir_structure(topic_name: str, topic_contents: List[dict], force_overwrite: bool = False) -> None:
    os.mkdir(topic_name)
    os.chdir(topic_name)
    topic_dir = os.getcwd()
    for problem in topic_contents:
        os.chdir(topic_dir)
        create_problem_dir(problem)


def create_problem_dir(problem_data: dict) -> None:
    dir_name = slugify(problem_data['name'], separator='_', replacements=(("'", ""),))
    lines = [
        '"""',
        'Problem Name: {}'.format(problem_data['name']),
        'TUF Link: {}'.format(problem_data.get('editorial', 'N/A')),
        '"""\n',
    ]
    os.mkdir(dir_name)
    os.chdir(dir_name)
    for file_number in range(1, 5):
        with open('solution_{}.py'.format(file_number), 'w') as file:
            file.writelines('\n'.join(lines[:-1] + ['Solution {}'.format(file_number)] + [lines[-1]]))


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
