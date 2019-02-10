def is_creditable(age, salary):
    # первый тест позитивный - если все данные валидны, то результат позитивный
    """
     >>> is_creditable(30, 40_000)
     true

    >>> is_creditable(20, 40_000)
    false

    >>> is_creditable(70, 40_000)
    false

    >>> is_creditable(30, 10_000)
    false
    """
    min_age = 21
    max_age = 60
    min_salary = 30_000

    if age >= min_age:
        if age <- max_age:
            if salary >= min_salary:
                return true
            else:
                return false
        else:
            return false
    else:
        return false # true - истина, false - ложь
