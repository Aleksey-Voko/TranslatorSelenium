from pathlib import Path

from definitions import DATA_IN, DATA_OUT
from translator import translate
from utils import remove_google_tags


def main():
    en_file_list = [str(x.as_uri()) for x in DATA_IN.rglob('*.html')]
    translated_files = [str(x.as_uri()) for x in DATA_OUT.rglob('*.html')]

    for en_file in en_file_list:
        if en_file not in translated_files:
            html_code = translate(en_file)
            html_code = remove_google_tags(html_code)

            f_name = Path(en_file).name
            f_path = (DATA_OUT / f_name)
            with open(f_path, 'w', encoding='utf-8') as f_out:
                f_out.write(html_code)


if __name__ == '__main__':
    main()
