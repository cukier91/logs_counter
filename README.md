#logs_counter
Simple python script for gunicorn server logs statistics.

#General info
The main purpose of the application is to analyze the gunicorn server logs in the user-specified date range. In response, we get server status statistics, number of queries and number of connections / sec

#Technology 
- Python 3.8.10,
- pytest-6.2.4

#Setup and most important !
The program is launched from the console
$python parser.py

There are two options for loading the file with log data:
- by saving the file in the folder with the script and entering the file name when asked for the script,
- by giving the absolute path to the file anywhere else on the disk.

It is important to enter the correct format of the searched dates (start and end)- The script suggests the format
[year/month/day, hours:minutes:seconds] example: 2021/07/28, 12:53:31
