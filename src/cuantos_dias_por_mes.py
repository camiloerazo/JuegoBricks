def dias_en_mes(mes, year):
    if mes < 1 or mes > 12:
        raise ValueError("El mes debe estar entre 1 y 12")

    dias_por_mes = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    if mes == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return 29  # Leap year

    return dias_por_mes[mes]