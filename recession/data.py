import pandas as pd
import pandas_datareader.data as web

import datetime
import os

from typing import List


class Data(object):
    """
    Get a data series from FRED
    """

    _fred_id = None
    _name = None
    _start_date = None
    _end_date = None
    _series = None

    def __init__(self, fred_id: str, name: str = None, *args, **kwargs):
        self._fred_id = fred_id
        self._name = fred_id if name == None else name
        self._start_date = kwargs.get('start_date', datetime.date(1913, 1, 1))
        self._end_date = kwargs.get('end_date', datetime.date.today())


    def _load_series(self) -> pd.Series:
        data = web.DataReader(self._fred_id, "fred",
                              self._start_date,
                              self._end_date)


        self._series = data.ix[:,0]
        self._series.name = self._name

    def get_series(self):
        if self._series is None:
            self._load_series()
        return self._series




def test():
    gdp = Data('GDPC1').get_series()
    print(gdp)


if __name__ == '__main__':
    test()