def convert_time_in_seconde(time_string: str) -> int:
    houres, minutes, seconde = map(int, time_string.split(':'))
    return houres*3600 + minutes*60 + seconde


print(convert_time_in_seconde('1:30:00'))
