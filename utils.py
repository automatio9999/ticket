from re import compile, match
import json
from time import sleep
from random import uniform
from datetime import datetime, timedelta
from typing import List, Dict
from collections import defaultdict


def overdue_date(expire_date_str: str):
    date_format = "%m/%d/%y %I:%M %p"
    expire_date = datetime.strptime(expire_date_str, date_format)
    now = datetime.now()
    delta = expire_date - now
    return f"{delta}"


def cleared_date() -> str:
    date_format = "%m/%d/%y %I:%M %p"
    yesterday = datetime.now() - timedelta(days=1)
    return yesterday.strftime(date_format) 


def expire_date_days(expire_date_str: str):
    date_format = "%m/%d/%y %I:%M %p"
    expire_date = datetime.strptime(expire_date_str, date_format)
    now = datetime.now()
    delta = expire_date - now
    return delta.days


def is_expired_ticket(days_to_expire: int) -> bool:
    return days_to_expire < 0

def group_keys_by_value(data: List[Dict[str, str]]) -> Dict[str, List[str]]:
    grouped = defaultdict(list)
    for item in data:
        for key, value in item.items():
            grouped[value].append(key)
    return dict(grouped)


def is_clear_or_marked(status: str) -> bool:
    is_clear_or_marked = compile(r"marked|clear")
    return True if is_clear_or_marked.match(status.lower()) else False


def get_not_completed_status_history(status_history: list[dict]) -> list[dict]:
    not_completed = []
    for sh in status_history:
        for s in sh.values():
            if not is_clear_or_marked(s):
                not_completed.append(sh)
    return not_completed


def is_completed_status_history(status_history: list[dict]) -> bool:
    status = []
    for sh in status_history:
        for s in sh.values():
            status.append(s)
    for s in status:
        if not is_clear_or_marked(s):
            return False
    return True


def delay(min: float, max: float) -> None:
    sleep(uniform(min, max))


def extract_without_parenthesis(text: str) -> str:
    pattern = r'^(.*?)\s*\(.*\).*$'
    res = match(pattern, text)
    if res:
        return res.group(1).strip()
    return text.strip()


def format_not_completed_status_history(status_history: list[dict]) -> str:
    group_by = group_keys_by_value(status_history)
    f = []
    for k, v in group_by.items():
        if len(v) > 1:
            s = f'{", ".join(v[:len(v)-1])} & {v[len(v)-1]}'
        else:
            s = f'{", ".join(v)}'
        e = extract_without_parenthesis(k)
        f.append(f"{s} - {e}")
    return " & ".join(f)


def check_ticket_type(former_id_ticker: str) -> str:
    return "New" if len(former_id_ticker) == 0 else "Update-Renewal"

