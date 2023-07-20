#!/usr/bin/python3
"""Log parsing module"""
import sys
import re


if __name__ == '__main__':
    """Log parsing function"""
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s{1}-\s\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{6}\]\s"GET\s\/projects\/260\sHTTP\/1.1"\s(\d{3})\s(\d+)$'  # nopep8

    file_details = {'codes': {'200': 0, '301': 0, '400': 0,
                              '401': 0, '403': 0, '404': 0,
                              '405': 0,  '500': 0}, 'size': 0}
    possible_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    count = 0
    try:
        for x in sys.stdin:
            count += 1
            pattern = re.compile(pattern)
            match = re.match(pattern, str(x.strip()))
            if match:

                if int(match.group(1)) in possible_codes:
                    file_details['codes'][str(match.group(1))] += 1
                    file_details['size'] = file_details['size'] + \
                        int(match.group(2))

                if count % 10 == 0:
                    print("File size: {}".format(file_details['size']))
                    for key, value in sorted(file_details['codes'].items(),
                                             key=lambda x: int(x[0])):
                        if value != 0:
                            print("{}: {}".format(key, value))
    finally:
        print("File size: {}".format(file_details['size']))
        for key, value in sorted(file_details['codes'].items(),
                                 key=lambda x: int(x[0])):
            if value != 0:
                print("{}: {}".format(key, value))
