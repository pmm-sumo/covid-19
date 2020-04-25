#!/usr/bin/env python3

import csv, json
import sys
import datetime
import requests
import os


r0_path = 'data/rt.csv'
verbose = os.getenv('VERBOSE', False)
dump_all = os.getenv('ALL', False)
url = os.getenv('URL')

if url is None:
    print("URL env variable is required")
    sys.exit(1)

class Dumper:
    MAX_RECORDS_IN_POST = os.getenv('MAX_RECORDS_IN_POST', 50)

    def __init__(self, url, dump_all, verbose):
        self.url = url
        self.dump_all = dump_all
        self.verbose = verbose
        self.data = []
        self.today = datetime.date.today().strftime("%Y-%m-%d")

    def sumo_json(self, data):
        rows = []
        for record in self.data:
            rows.append(json.dumps(record))
        return "\n".join(rows)

    def dump_maybe(self, force=False):
        if len(self.data) > Dumper.MAX_RECORDS_IN_POST or force:
            if Dumper.MAX_RECORDS_IN_POST == 1:
                payload = json.dumps(self.data[0])
            else:
                payload = self.sumo_json(self.data)
            print("Sending a payload of %d records to %s" % (len(self.data), self.url))
            if verbose:
                print(payload)
            response = requests.post(url=self.url, data=payload)
            print(response)
            self.data = []

    def is_today(self, row):
        return row['date'] == self.today

    def process(self, csv_path):
        with open(csv_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                record = {
                    'Country': row['country'],
                    'Date': row['date'],
                    'Ro': row['ML'],
                    'Ro_Low90': row['Low_90'],
                    'Ro_High90': row['High_90'],
                    'Ro_Low50': row['Low_50'],
                    'Ro_High50': row['High_50']
                }
        
                if self.dump_all or self.is_today(row):
                    self.data.append(record)
                self.dump_maybe()

            self.dump_maybe(True)


Dumper(url, dump_all, verbose).process(r0_path)
