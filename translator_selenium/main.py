from pathlib import Path

from definitions import DATA_IN, DATA_OUT
from translator import translate
from utils import remove_google_tags


def main():
    translated_files = [
        x.relative_to(DATA_OUT) for x in DATA_OUT.rglob('*.html')
    ]

    for en_file in DATA_IN.rglob('*.html'):
        if en_file.relative_to(DATA_IN) not in translated_files:
            html_code = translate(en_file)
            html_code = remove_google_tags(html_code)

            f_path = (DATA_OUT / en_file.relative_to(DATA_IN))
            # f_path = f_path.with_suffix('.xhtml')
            Path(f_path).parent.mkdir(parents=True, exist_ok=True)
            with open(f_path, 'w', encoding='utf-8') as f_out:
                f_out.write(html_code)


if __name__ == '__main__':
    main()
