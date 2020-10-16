import csv
from .DateManager import DateConverter


class CalendarDate(object):
    def __init__(self, month, day):
        self._month = month
        self._day = day

    def __repr__(self):
        return '{}/{}'.format(self._month, self._day)

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

class CSVGetter(CalendarDate):
    FIELD_NAMES = ('Subject', 'Start Date', 'End Date', 'All Day Event',
                   'Private')
    def __init__(self, subject, first_year, last_year, month, day):
        super(CSVGetter, self).__init__(month, day)
        self._subject = subject
        self._first_year = first_year
        self._last_year = last_year
        self._dates = []
        self._dates = []

    def get_solar_days(self):
        for year in range(self._first_year, self._last_year):
            converter = DateConverter(year, self._month, self._day, True)
            self._dates.append(converter.solar_day)

    def get_lunar_days(self):
        for year in range(self._first_year, self._last_year):
            converter = DateConverter(year, self.month, self._day, False)
            self._dates.append(converter.lunar_day)

    def write_csv(self, path):
        calendar = {}
        with open(path, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=self.FIELD_NAMES)
            writer.writeheader()
            for date in self._dates:
                year = date[:4]
                month = date[5:7]
                day = date[8:10]
                calendar['Subject'] = self._subject
                calendar['Start Date'] = "{}/{}/{}".format(month, day, year)
                calendar['End Date'] = "{}/{}/{}".format(month, day, year)
                calendar['All Day Event'] = True
                calendar['Private'] = True
                writer.writerow(calendar)
