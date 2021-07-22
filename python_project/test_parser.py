import parser
import tests_base


def test_parser():

    tests_base.set_keyboard_input(["2019/12/01, 00:00:00", "2019/12/02, 12:53:21", "gunicorn.log2"])

    parser.parse_lines()

    output = tests_base.get_display_output()

    assert output == ["Podaj datę początkową[rrrr/mm/dd, hh:mm:ss]: ",
                      "Podaj datę końcową[rrrr/mm/dd, hh:mm:ss]: ",
                      "Podaj nazwę pliku z folderu ze skryptem lub ścieżkę[absolute] do pliku: ",
                      ]


def test_parser_wrong_date():

    tests_base.set_keyboard_input(["2019/12/01 00:00:00", "2019/12/02, 12:53:21", "gunicorn.log2"])

    parser.parse_lines()

    output = tests_base.get_display_output()

    assert output == ["Podaj datę początkową[rrrr/mm/dd, hh:mm:ss]: ",
                      "Podaj datę końcową[rrrr/mm/dd, hh:mm:ss]: ",
                      "Podaj nazwę pliku z folderu ze skryptem lub ścieżkę[absolute] do pliku: ",
                      "Coś poszło nie tak, sprawdź format daty"
                      ]


def test_parser_wrong_file():

    tests_base.set_keyboard_input(["2019/12/01, 00:00:00", "2019/12/02, 12:53:21", "gunicorn.l2"])

    parser.parse_lines()

    output = tests_base.get_display_output()

    assert output == ["Podaj datę początkową[rrrr/mm/dd, hh:mm:ss]: ",
                      "Podaj datę końcową[rrrr/mm/dd, hh:mm:ss]: ",
                      "Podaj nazwę pliku z folderu ze skryptem lub ścieżkę[absolute] do pliku: ",
                      "Wygląda na to, że podany plik nieistnieje, lub ścieżka jest niepoprawna "
                      ]


def test_statistics():
    lines = ['Pierwsza linia', 'druga linia', 'trzecia linia', 'czwarta linia']
    requests_time = 4000000
    out = parser.statistics(lines, requests_time)

    assert out == 'No. of requests: 4\nrequests/sec:1.0'
