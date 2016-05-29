import re
from dateutil import parser, tz

NGINX_LINE_REGEXP = re.compile(
    ('(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
     ' - - '
     '\[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] '
     '((\"(?P<method>GET|POST|CONNECT|HEAD) )'
     '(?P<url>.+)(http\/1\.(1|0)")) '
     '(?P<statuscode>\d{3}) '
     '(?P<bytessent>\d+) '
     '(["](?P<refferer>(\-)|(.+))["]) '
     '(["](?P<useragent>.+)["])'), re.IGNORECASE)

TIME_FORMAT = '%H:%M:%S'

status_code=[]
used_resources=[]
created_res=[]
succ_rate=0

def file_parse():
    i=0
    j=0
    count=0
    with open('logs.txt') as f:
        for line in f.readlines():
            match = re.match(NGINX_LINE_REGEXP, line)
            j=j+1
            if not match:
                continue
            status_code.append(match.group('statuscode'))
            if match.group('statuscode')=='403':
                used_resources.append(match.group('url'))
            if match.group('statuscode')=='201':
                created_res.append(match.group('url'))
            if match.group('statuscode')=='200':
                i=i+1
            log_datetime = match.group('dateandtime').replace(':', ' ', 1)
            log_datetime = parser.parse(log_datetime)
            utc_log_datetime = log_datetime.astimezone(tz.tzutc())
            if utc_log_datetime.strftime(TIME_FORMAT) >='15:11:00' and utc_log_datetime.strftime(TIME_FORMAT)<='15:26:00':
                count=count+1

    f.close()
    succ_rate=i*1.0/j
    distinct_status_codes=set(status_code)
    print(distinct_status_codes)
    print(used_resources)
    print(created_res)
    print(count)
    print(succ_rate)

if __name__== '__main__':
    file_parse()