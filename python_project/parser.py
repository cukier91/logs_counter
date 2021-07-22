from datetime import datetime


def dict_printer(status_response):
    return f'responses: {status_response}'


def statistics(lines, request_time):
    # Function that provides statistics
    if len(lines) == 0:
        string_lines = f'No. of requests: 0'
        string_request_times = f'requests/sec: 0'
        return f'Nie znaleziono wyników w podanym zakresie\n{string_lines}\n{string_request_times}'
    else:
        string_lines = f'No. of requests: {len(lines)}'
        string_request_times = f'requests/sec:{round((request_time / 1000000) / len(lines), 2)}'
        return f'{string_lines}\n{string_request_times}'


def parse_lines():
    # Parsers function- main function in the script
    global start_date, end_date
    start = input("Podaj datę początkową[rrrr/mm/dd, hh:mm:ss]: ")
    end = input("Podaj datę końcową[rrrr/mm/dd, hh:mm:ss]: ")
    file_name = input("Podaj nazwę pliku z folderu ze skryptem lub ścieżkę[absolute] do pliku: ")

    try:
        # Taking care of data format error
        start_date = datetime.strptime(start, "%Y/%m/%d, %H:%M:%S")
        end_date = datetime.strptime(end, "%Y/%m/%d, %H:%M:%S")
    except ValueError:
        print("Coś poszło nie tak, sprawdź format daty")
        return
    try:
        # Taking care of file name or file path error
        file = open(f'{file_name}')
    except FileNotFoundError:
        print("Wygląda na to, że podany plik nieistnieje, lub ścieżka jest niepoprawna ")
        return

    lines = []
    request_time = 0
    status_response = {}

    for line in file:
        # Iterating through every line in files
        if 'gunicorn' in line:
            # checking condition that skips not need lines-- need to be changed if not gunicorn server
            if datetime.strptime(line.split()[8].lower(), "[%d/%b/%Y:%H:%M:%S") >= start_date and datetime.strptime(
                    line.split()[8].lower(), "[%d/%b/%Y:%H:%M:%S") <= end_date:
                # For every line checking if filling condition of limited dates start and end, if yes adding to
                # list(lines) and adding to variable request time: request connection time
                lines.append([line])
                request_time += int(line.split()[-1])

                if f'{line.split()[13]}' in status_response.keys():
                    # If server status is already in dict than increment by 1
                    status_response[f'{line.split()[13]}'] = status_response[f'{line.split()[13]}'] + 1

                else:
                    status_response[f'{line.split()[13]}'] = 1
                    # If it's not in dict add it to dict and assign value 1

            elif datetime.strptime(line.split()[8].lower(), "[%d/%b/%Y:%H:%M:%S") > end_date:
                # If date in line is after defined end date, than stop iterating
                break

    return statistics(lines, request_time), dict_printer(status_response)
    # return no. of request, requests/sec, and all noted server statuses


try:
    if __name__ == '__main__':
        for parsed_line in parse_lines():
            print(parsed_line)
except NameError:
    print("Spróbujmy jeszcze raz! ")
except TypeError:
    print("Spróbujmy jeszcze raz! ")
