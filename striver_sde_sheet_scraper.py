"""
Scrapes the SDE sheet page of the TUF website and writes relevant data into a JSON file named
"striver_sde_sheet_data.json".
"""

from bs4 import BeautifulSoup
import requests
import json


def unicode_to_ascii(text: str, replacements: dict = None) -> str:
    if not replacements:
        replacements = {
            '\u2019': "'",
            '\u2013': '-'
        }
    for key, val in replacements.items():
        text = text.replace(key, val)
    return text


def main():
    url = 'https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/'

    soup = BeautifulSoup(requests.get(url).text, features="html.parser")

    data = {}
    for topic in soup.find_all(name='details')[:-4]:
        curr_topic_data = []
        curr_topic_name = topic.summary.text.split(':')[-1].strip()
        for row in topic.find_all(name='tr'):
            if row.find('th'):
                continue
            cols = row.find_all('td')
            name = cols[1].text
            curr_row = {'name': name}
            if cols[1].a:
                curr_row['editorial'] = cols[1].a.get('href')
            for col in cols[2:]:
                txt = col.text
                if txt == 'Link 1' and col.a:
                    curr_row['practice_link_1'] = col.a.get('href')
                elif txt == 'Link 2' and col.a:
                    curr_row['practice_link_2'] = col.a.get('href')
                elif ('YT' in txt) or ('YouTube' in txt):
                    curr_row['video_links'] = [i.get('href') for i in col.find_all('a')]
            for key, val in curr_row.items():
                if isinstance(val, list):
                    curr_row[key] = list(map(unicode_to_ascii, val))
                elif isinstance(val, str):
                    curr_row[key] = unicode_to_ascii(val)
                else:
                    raise NotImplementedError('The JSON data is not expected to contain any other types.')

            curr_topic_data.append(curr_row)
        data[curr_topic_name] = curr_topic_data[:]

    with open('striver_sde_sheet_data.json', 'w') as file_handler:
        json.dump(data, file_handler, indent=4)


if __name__ == '__main__':
    main()
