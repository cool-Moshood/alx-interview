#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''


import sys
import re


def parse_log_line(line):
    """Parse a log line and return the status code and file size"""
    pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$'
    match = re.match(pattern, line)
    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))
        return status_code, file_size
    return None, None


def print_statistics(file_details):
    """Print the current statistics"""
    print("File size: {}".format(file_details['size']))
    for key, value in sorted(file_details['codes'].items(), key=lambda x: int(x[0])):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == '__main__':
    file_details = {'codes': {'200': 0, '301': 0, '400': 0,
                              '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}, 'size': 0}
    possible_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            status_code, file_size = parse_log_line(line.strip())
            if status_code is not None and file_size is not None and status_code in possible_codes:
                file_details['codes'][str(status_code)] += 1
                file_details['size'] += file_size

            if count % 10 == 0:
                print_statistics(file_details)

    except KeyboardInterrupt:
        pass

    finally:
        print_statistics(file_details)
