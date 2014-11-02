# -*- coding: utf-8 -*-
"""
Created on Nov 1, 2014
@author: daniel

Usage:
    client --server <ip> --user <username> --password <password> --exec <program>
"""
from docopt import docopt
from trex import TrexClient, TrexMsg

if __name__ == '__main__':
    args = docopt(__doc__)
    trexClient = TrexClient(args['<ip>'])
    msg = TrexMsg(args['<username>'], args['<password>'], args['<program>'])
    trexClient.send(msg)
