from datetime import datetime

# start = input("Podaj datę początkową[rrrr/mm/dd]: ")
# end = input("Podaj datę końcową[rrrr/mm/dd]: ")

start = '2019/12/01, 00:00:00'
end = '2019/12/01, 11:54:22'


start_date = datetime.strptime(start, "%Y/%m/%d, %H:%M:%S")
end_date = datetime.strptime(end, "%Y/%m/%d, %H:%M:%S")


file = open(f'gunicorn.log2')
lines = []
request_time = 0
status_response = {}
for line in file:
    if '--' not in line:
        if datetime.strptime(line.split()[8].lower(), "[%d/%b/%Y:%H:%M:%S") >= start_date and datetime.strptime(
                line.split()[8].lower(), "[%d/%b/%Y:%H:%M:%S") <= end_date:
            lines.append([line])
            request_time += int(line.split()[-1])
            if f'{line.split()[13]}' in status_response.keys():
                status_response[f'{line.split()[13]}'] = status_response[f'{line.split()[13]}'] + 1
            else:
                status_response[f'{line.split()[13]}'] = 1
        elif datetime.strptime(line.split()[8].lower(), "[%d/%b/%Y:%H:%M:%S") > end_date:
            break
        else:
            continue
print(f'requests: {len(lines)}')
print(f'requests/sec: {round((request_time / 1000000) / len(lines), 2)}')
for k, v in status_response.items():
    print(f'response: {k} ilość: {v}')