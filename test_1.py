from datetime import datetime

first_lst = list(range(1, 1000001, 1))
second_lst = list(range(1, 1000001, 2))

init_time = datetime.now()
print(f"FIRST LIST LENGTH BEFORE REMOVE:\t{len(first_lst)}")
print(f"START\t{init_time.strftime('%y-%m-%d %H:%M:%S')}")
first_lst = list(set(first_lst) - set(second_lst))
finish_time = datetime.now()
print(f"FIRST LIST LENGTH AFTER REMOVE:\t{len(first_lst)}")
print(f"FINISH\t{finish_time.strftime('%y-%m-%d %H:%M:%S')}")
print(f"DURATION\t{(finish_time-init_time).seconds}")
