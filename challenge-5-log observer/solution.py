import re

DATE_REGEX = r"Started (GET|POST|HEAD|POST|PUT|DELETE|TRACE|CONNECT) "\
    ".* at ([0-9]{4}\-[0-9]{2}\-[0-9]{2})"
IP_REGEX = r"for ([0-9]{,3}\.[0-9]{,3}\.[0-9]{,3}\.[0-9]{,3}) at"


def requests_per_day(log):
    days = re.findall(DATE_REGEX, log)
    days = [d[1] for d in days]
    return {day: days.count(day) for day in days}


def ips_set(log):
    return set(re.findall(IP_REGEX, log))