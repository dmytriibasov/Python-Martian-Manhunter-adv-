import os
import requests
import re

r = requests.get('http://socrates.vsau.org/wiki/index.php/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B0%D0%B4%D1%80%D0%B5'
                 '%D1%81_%D0%B5%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%B8%D1%85_%D0%BF%D0%BE%D1%88%D1%82'
                 '%D0%BE%D0%B2%D0%B8%D1%85_%D1%81%D0%BA%D1%80%D0%B8%D0%BD%D1%8C_%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1'
                 '%83%D1%80%D0%BD%D0%B8%D1%85_%D0%BF%D1%96%D0%B4%D1%80%D0%BE%D0%B7%D0%B4%D1%96%D0%BB%D1%96%D0%B2_%D1'
                 '%83%D0%BD%D1%96%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82%D1%83')

file_path = r'html_page.html'

if r.status_code == 200:
    if not os.path.isfile(file_path):
        with open(r'html_page.html', 'w') as html_page:
            html_page.writelines(r.text)

    else:
        with open(r'html_page.html', 'r') as html_page:
            page = ''.join(html_page.readlines())

else:
    print('Status code ERROR')

pattern = re.compile(r'\<p\>(?P<status>.*?)\<b\>'
                     r'(?P<email>\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)\<\/b\>\n\<\/p\>')

pattern_2 = re.compile(r'\s?\\t')
matches = re.findall(pattern, page)

results = []

for match in matches:
    updated_match = re.sub(pattern=pattern_2, repl='', string=str(match))
    results.append(updated_match)

print(results)