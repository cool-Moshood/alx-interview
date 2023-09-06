import sys
import re

def parse_log_line(line):
    """Parse a log line and return the status code and file size"""
    match = re.match(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6})\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$', line)
    return (int(match.group(3)), int(match.group(4))) if match else (None, None)

def print_statistics(file_details):
    """Print the current statistics"""
    print("File size:", file_details['size'])
    for key, value in sorted(file_details['codes'].items(), key=lambda x: int(x[0])):
        if value:
            print(f"{key}: {value}")

if __name__ == '__main__':
    file_details = {'codes': {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}, 'size': 0}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            status_code, file_size = parse_log_line(line.strip())
            if status_code is not None and status_code in file_details['codes']:
                file_details['codes'][str(status_code)] += 1
                file_details['size'] += file_size

            if count % 10 == 0:
                print_statistics(file_details)

    except KeyboardInterrupt:
        pass

    finally:
        print_statistics(file_details)
