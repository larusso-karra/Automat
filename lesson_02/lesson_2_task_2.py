def is_year_leap(year):
    """Проверяет, является ли год високосным."""
    if year % 4 == 0 :
        return True
    else:
        return False
is_year_leap(int(input("Введите год:")))