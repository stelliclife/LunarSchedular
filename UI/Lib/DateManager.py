from korean_lunar_calendar import KoreanLunarCalendar


class DateConverter(object):
    def __init__(self, year, month, day, lunar):
        self._year = year
        self._month = month
        self._day = day
        self._lunar = lunar
        self._intercalation = None
        self._calendar = KoreanLunarCalendar()

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    @property
    def intercalation(self):
        return self._get_intercalation()

    @property
    def solar_day(self):
        return self._get_solar_day()

    @property
    def lunar_day(self):
        return self._get_lunar_day()

    def _get_intercalation(self):
        if self._lunar == True:
            if self._date.year % 4 == 0 or self._date.year % 400 == 0:
                self._intercalation = True
            else:
                self._intercalation = False
        else:
            self._intercalation = None
        return self._intercalation

    def _get_solar_day(self):
        self._calendar.setLunarDate(self._year, self._month, self._day,
                                    self._intercalation)
        solar_date = self._calendar.SolarIsoFormat()
        return solar_date

    def _get_lunar_day(self):
        self._calendar.setSolarDate(self._year, self._month, self._day)
        lunar_date = self._calendar.LunarIsoFormat()
        return lunar_date

    def __del__(self):
        del self._calendar
