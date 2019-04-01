# -*- coding:utf-8 -*-

import sys
import json

def main():
    data = open(sys.argv[-1], 'rb')
    log_file = open("/Users/onpajapan27/test/fluentd_test/log_server//log/fluentd_test.json", "ab")
    log_file.write(data)
    log_file.close()

if __name__ == "__main__":
    main()
