from bs4 import BeautifulSoup


def remove_google_tags(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')

    html_tag = soup.find('html', {'class': 'translated-ltr'})
    if html_tag and html_tag['class']:
        del html_tag['class']
    translate_tag = soup.find(
        'link',
        {'href': 'https://translate.googleapis.com/translate_static/css/translateelement.css'})
    if translate_tag:
        translate_tag.decompose()
    skip_translate = soup.find('div', {'class': 'skiptranslate'})
    if skip_translate:
        skip_translate.decompose()
    goog_te_spinner_pos = soup.find('div', {'class': 'goog-te-spinner-pos'})
    if goog_te_spinner_pos:
        goog_te_spinner_pos.decompose()

    font_tags = soup.find_all('font', {'style': 'vertical-align: inherit;'})
    for font_tag in font_tags:
        font_tag.unwrap()

    html_code = str(soup)
    html_code += '\n'

    return html_code
