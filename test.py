from utils import format_not_completed_status_history, get_not_completed_status_history, group_keys_by_value


test_list =[
    {"A08": "Clear/No conflict"},
    {"D39": "Not complete/In progress (Responded per folder placement.)"},
    {"Xjdo": "Not yet responded"},
    {"RX99": "Not yet responded"},
    {"RX123": "Not yet responded"},
]

a = "Not complete/In progress (Responded per folder placement.)" 
b = "Not yet responded"
c = "24-hour delay (Response by Utiliquest)"
d = "COMDC, VDC, WASA02 & WGL07 - Not yet responded & DCDOT01 - 	Not complete/In progress"


not_complete = get_not_completed_status_history(test_list)
group_by = group_keys_by_value(not_complete)
f = format_not_completed_status_history(not_complete)
print(f)


def is_expired_ticket(days_to_expire: int) -> bool:
    return days_to_expire < 0

