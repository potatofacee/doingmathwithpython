import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

DATA = 'CRND0103-2021-TX_Austin_33_NW.txt'


def parse_headers(DATA_HEADERS):
    '''
    takes an ascii block of headers from https://www.ncei.noaa.gov/pub/data/uscrn/products/daily01/headers.txt
    and returns a list of various weather measurements and their units.
    '''

    data_shape = DATA_HEADERS.split('\n')[1:]

    d_names = []
    d_units = {}
    n_cols = 0

    for field in data_shape:
        col, label, units = field.split()
        n_cols = col

        d_names.append(label.lower())
        d_units[label.lower()] = units



    return n_cols, d_names, d_units

def read_data(filename: str, column_headers: list) -> list:

    df = pd.read_fwf(DATA, header=None, delim_whitespace=True)
    # temps = pd.read_csv(DATA, header=None, delim_whitespace=True)
    # apparently in all the docs for pandas, the "main" tool (read_csv) has the information, and the secondaries
    # like read_fwf and read_table, only have things specific to those formats from csv (ex, delim_whitespace=True)

    df.columns = d_names
    # TODO type datetime column as datetime
    # TODO make a log file
    log = 'haha'
    return df, log


# TODO strip null columns from df
# TODO make plotting function
# TODO take a column name, plot it against datetime
# TODO



if __name__ == '__main__':
    data_shape = '''
            1    WBANNO                         XXXXX
            2    LST_DATE                       YYYYMMDD
            3    CRX_VN                         XXXXXX
            4    LONGITUDE                      Decimal_degrees
            5    LATITUDE                       Decimal_degrees
            6    T_DAILY_MAX                    Celsius
            7    T_DAILY_MIN                    Celsius
            8    T_DAILY_MEAN                   Celsius
            9    T_DAILY_AVG                    Celsius
            10   P_DAILY_CALC                   mm
            11   SOLARAD_DAILY                  MJ/m^2
            12   SUR_TEMP_DAILY_TYPE            X
            13   SUR_TEMP_DAILY_MAX             Celsius
            14   SUR_TEMP_DAILY_MIN             Celsius
            15   SUR_TEMP_DAILY_AVG             Celsius
            16   RH_DAILY_MAX                   %
            17   RH_DAILY_MIN                   %
            18   RH_DAILY_AVG                   %
            19   SOIL_MOISTURE_5_DAILY          m^3/m^3
            20   SOIL_MOISTURE_10_DAILY         m^3/m^3
            21   SOIL_MOISTURE_20_DAILY         m^3/m^3
            22   SOIL_MOISTURE_50_DAILY         m^3/m^3
            23   SOIL_MOISTURE_100_DAILY        m^3/m^3
            24   SOIL_TEMP_5_DAILY              Celsius
            25   SOIL_TEMP_10_DAILY             Celsius
            26   SOIL_TEMP_20_DAILY             Celsius
            27   SOIL_TEMP_50_DAILY             Celsius
            28   SOIL_TEMP_100_DAILY            Celsius'''

    n_cols, d_names, d_units = parse_headers(data_shape)
    print(f'Number of columns found: {n_cols}')
    temps, log = read_data(DATA, d_names)
    temps.info()
    temps.info()

## todo clean useless columns
## todo, capture these values somewhere
tstd = []
for col in d_names:
    try:
        std = temps[col].std()
        if std < 1e-10:
            tstd.append(col)
    except:
        tstd.append(col)
        pass

temps.drop(tstd, axis=1, inplace=True)


# datetime format here: https://strftime.org/
temps['lst_date'] = pd.to_datetime(temps['lst_date'], format='%Y%m%d')

x = []
for i in range(1,366):
    x.append(i)

t = temps['t_daily_avg'].tolist()
plt.plot(x, t)