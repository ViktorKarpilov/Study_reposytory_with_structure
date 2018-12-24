
def translation():
    """Повертає кількість годин і хвилин , що пройшли після початку дня для заданої користувачем кількості хвилин
    Args:
    Return: Рядок , в якому вказана кількість годин і хвилин
    Examples:
    Enter pleas minutes: 1321313123123213
    10 Hours and 53 Minutes"""
    input_minutes = int(input("Enter pleas minutes: "))
    hours = input_minutes//60
    result_hours = hours - (hours//24)*24
    result_minutes = input_minutes - hours*60
    result = str(result_hours) +" Hours and "+str(result_minutes) +" Minutes"
    return result

def Run_translation():
    """Представляє собою інтерфейс для запуску программи
    Args:
    Return:
    Examples:
    Enter pleas minutes: 1321313123123213
    10 Hours and 53 Minutes"""
    try:
        print(translation())
    except:
        print("Something wrong")
        translation()
    return None

