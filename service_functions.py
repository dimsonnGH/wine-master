def number_years_repr(number_years):
    remainder100 = number_years % 100
    remainder10 = number_years % 10
    if remainder100 >= 11 and remainder100 <= 14:
        years_repr = "лет"
    elif remainder10 == 1:
        years_repr = "год"
    elif remainder10 >= 2 and remainder10 <= 4:
        years_repr = "года"
    else:
        years_repr = "лет"
    return years_repr
