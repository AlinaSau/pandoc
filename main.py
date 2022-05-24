from panflute import *
import sys

headers = []


def repeatedHeader(elem):
    if isinstance(elem, Header):
        if stringify(elem) in headers:
            sys.stderr.write("!!! Repeated header !!!" + stringify(elem))
        else:
            headers.append(stringify(elem))


def headerLevel(elem, _):
    if isinstance(elem, Header) and elem.level >= 3:
        return Header(Str(stringify(elem).upper()), level=elem.level)


def boldSearch(file, _):
    file.replace_keyword("BOLD", Strong(Str("BOLD")))


if __name__ == "__main__":
    run_filters([repeatedHeader, headerLevel], prepare=boldSearch)
