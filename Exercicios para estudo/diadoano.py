
def is_leap_year(year: int) -> bool:
    """Verifica se o ano é bissexto."""
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def month_length(month: int, year: int) -> int:
    """Devolve o número de dias de um mês."""

    # Meses com 31 dias
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31

    # Meses com 30 dias
    elif month in [4, 6, 9, 11]:
        return 30

    # Fevereiro
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28


def is_date_valid(day: int, month: int, year: int) -> bool:
    """Verifica se a data é válida."""

    # Verifica se o mês existe
    if month < 1 or month > 12:
        return False

    # Verifica se o dia é válido
    if day < 1 or day > month_length(month, year):
        return False

    return True


def day_order(day: int, month: int, year: int) -> int:
    """Calcula o número do dia dentro do ano."""

    total_dias = day

    for mes in range(1, month):
        total_dias += month_length(mes, year)

    return total_dias


def main() -> None:

    day = int(input("Dia: "))
    month = int(input("Mês: "))
    year = int(input("Ano: "))

    if is_date_valid(day, month, year):
        print("Dia do ano:", day_order(day, month, year))
    else:
        print("DATA INVÁLIDA")


main()
