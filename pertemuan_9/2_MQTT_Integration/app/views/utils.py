from datetime import timedelta
import re

def parse_time(time_str):
    regex = re.compile(r'((?P<days>\d+?)d)?'
                            r'((?P<hours>\d+?)h)?'
                            r'((?P<minutes>\d+?)m)?'
                            r'((?P<seconds>\d+?)s)?')
    str_code = time_str[-1]
    if str_code == 'M': 
        num_days = int(time_str[:-1])*30
        time_str = str(num_days) + 'd'
    if str_code == 'y':
        num_days = int(time_str[:-1])*30*12 
        time_str = str(num_days) + 'd'

    parts = regex.match(time_str)
    if not parts:
        return
    parts = parts.groupdict()

    time_params = {}
    for name, param in parts.items():
        if param:
            time_params[name] = int(param)
    return timedelta(**time_params)