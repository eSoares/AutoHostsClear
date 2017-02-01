#! /usr/bin/python2

import ipaddress


class Host:
    names = None
    crypto_algo = None
    crypto_sig = None
    hosts_line = None

    def __init__(self, line):
        self.hosts_line = line
        self.__parse_line()

    def is_local(self):
        # returns if is not local address
        for name in self.names.split(','):
            try:
                if ipaddress.ip_address(str(name).decode('utf-8')).is_private:
                    return True
            except ValueError:
                continue
        return False

    def __parse_line(self):
        line_parts = self.hosts_line.split(' ')
        if len(line_parts) > 0:
            self.names = line_parts[0]
            self.crypto_algo = line_parts[1]
            self.crypto_sig = line_parts[2]

    def __str__(self):
        return self.hosts_line
