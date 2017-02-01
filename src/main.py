#! /usr/bin/python2

import cli.app
import os
from hosts import Host


def clear_hosts():
    hosts_file = os.path.expanduser("~/.ssh/known_hosts")
    hosts = []
    with open(hosts_file, 'r') as h:
        # let's read them all
        for line in h:
            hosts.append(Host(line))
        h.close()
    # now write out only the non local hosts
    with open(hosts_file, 'w') as h:
        for host in hosts:
            if not host.is_local():
                h.write(str(host))
        h.close()
    print("New hosts written")
    return


@cli.app.CommandLineApp
def app(_app):
    clear_hosts()

if __name__ == "__main__":
    app.run()
