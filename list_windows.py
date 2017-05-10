import datetime
import pytz

# windows.append((1, datetime.datetime(1998, 4, 9, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1999, 4, 9, tzinfo=pytz.timezone('America/Bahia'))))
# windows.append((2, datetime.datetime(1999, 4, 9, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2000, 4, 9, tzinfo=pytz.timezone('America/Bahia'))))
# windows.append((3, datetime.datetime(2000, 4, 9, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2001, 4, 9, tzinfo=pytz.timezone('America/Bahia'))))
# windows.append((4, datetime.datetime(2001, 4, 9, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2002, 4, 9, tzinfo=pytz.timezone('America/Bahia'))))
# windows.append((5, datetime.datetime(2002, 4, 9, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2003, 4, 9, tzinfo=pytz.timezone('America/Bahia'))))
# windows.append((6, datetime.datetime(2003, 4, 9, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2004, 4, 9, tzinfo=pytz.timezone('America/Bahia'))))
# windows.append((7, datetime.datetime(2004, 4, 9, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2005, 4, 9, tzinfo=pytz.timezone('America/Bahia'))))
# windows.append((8, datetime.datetime(2005, 4, 9, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2006, 4, 9, tzinfo=pytz.timezone('America/Bahia'))))
# windows.append((9, datetime.datetime(2006, 4, 9, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2007, 4, 9, tzinfo=pytz.timezone('America/Bahia'))))
# windows.append((10, datetime.datetime(2007, 4, 9, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(2008, 4, 9, tzinfo=pytz.timezone('America/Bahia'))))

def list_windows():
    windows = []


    windows.append((1, datetime.datetime(1998, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1999, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((2, datetime.datetime(1999, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2000, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((3, datetime.datetime(2000, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2001, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((4, datetime.datetime(2001, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2002, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((5, datetime.datetime(2002, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2003, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 27, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((6, datetime.datetime(2003, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2004, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((7, datetime.datetime(2004, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2005, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((8, datetime.datetime(2005, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2006, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((9, datetime.datetime(2006, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2007, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((10, datetime.datetime(2007, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2008, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((11, datetime.datetime(2008, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2009, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((12, datetime.datetime(2009, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2010, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((13, datetime.datetime(2010, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2011, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((14, datetime.datetime(2011, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2012, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((15, datetime.datetime(2012, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2013, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((16, datetime.datetime(2013, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2014, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((17, datetime.datetime(2014, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2015, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((18, datetime.datetime(2015, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2016, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((19, datetime.datetime(2016, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2017, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1980, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1981, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    return windows
