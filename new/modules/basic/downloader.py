#!/usr/bin/python
# -*- coding: utf8 -*-

import argparse
import json
import finance
import rss

def main():
    ''' Parsing command line args '''
    parser = argparse.ArgumentParser(description='Spyder-quote, the terrific botnet')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s v0.8.1 Licence GPLv3', help='Print program version')
    parser.add_argument('-f', '--file', action='store', required=True, help='Config file path')
    parser.add_argument('-d', '--database', action='store', required=True, help='Config file path')
    args = parser.parse_args()

    ''' Parsing configuration file '''
    config = json.load(open(args.file, 'r'))

    ''' Execute financial stuff '''
    q = finance.Quote(config['name'], args.database)
    #q.download(int(config['share']['days']), int(config['share']['precision']))
    #q.updateDb()

    ''' Execute rss stuff '''
    print '[DEBUG] Retrieving rss news from', q.rss
    channel = rss.Rss(q.rss)
    rval = channel.getFeeds(config['rss']['description'], config['rss']['link'], config['rss']['update'])
    for i in range(0, len(channel.title)):
        print '\t', channel.title[i], '-', channel.update[i]
        #print '\t', channel.description[i].strip()



if __name__ == '__main__':
    main()
