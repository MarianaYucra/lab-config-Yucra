def reserva_valida(horas):
    return isinstance(horas, int) and not isinstance(horas, bool) and 1 <= horas <= 6