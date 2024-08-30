#!/usr/bin/python3
'''
Log parsing
'''
import sys


if __name__ == "__main__":
    '''
    Run only when not imported
    '''
    status_code = {'200', '301', '400', '401', '403', '404', '405', '500'}
    line_count = 0
    total_size = 0

    def print_res(status, size):
        '''
        Print result
        '''
        print("File size: {}".format(size))
        for code in sorted (status_codes.keys()):
            if status_code[code] > 0:
                print("{}: {}".format(code, status_codes[code]))

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            try:
                file_size = int(parts[-1])
                status_code = parts[-2]
            except (IndexError, ValueError):
                continue

            total_size += file_size

            if status_code in status_codes:
                status_codes[status_code] +=1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)
