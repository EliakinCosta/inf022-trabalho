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
                    datetime.datetime(1998, 12, 31, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2009, 5, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2009, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((2, datetime.datetime(1999, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(1999, 12, 31, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2010, 5, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2010, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((3, datetime.datetime(2000, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2000, 12, 31, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2011, 5, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2011, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((4, datetime.datetime(2001, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2001, 12, 31, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2012, 5, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2012, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((5, datetime.datetime(2002, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2002, 12, 31, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2013, 6, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2013, 9, 27, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((6, datetime.datetime(2003, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2003, 12, 31, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2014, 5, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2014, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((7, datetime.datetime(2004, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2004, 12, 31, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2015, 5, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2015, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((8, datetime.datetime(2005, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2005, 12, 31, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2016, 5, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2016, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((9, datetime.datetime(2006, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2006, 12, 31, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2016, 5, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2016, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((10, datetime.datetime(2007, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2007, 12, 31, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2016, 5, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2016, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))
    windows.append((11, datetime.datetime(2008, 1, 1, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2008, 12, 31, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2016, 5, 1, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia')),
                    datetime.datetime(2016, 9, 7, tzinfo=pytz.timezone('America/Bahia')), datetime.datetime(1970, 9, 7, tzinfo=pytz.timezone('America/Bahia'))))

    return windows
