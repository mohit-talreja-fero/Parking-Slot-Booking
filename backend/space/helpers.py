
def calculate_duration_hours(start_time=None, end_time=None):
    if start_time >= end_time:
        duration_in_time_difference = start_time - end_time
    else:
        duration_in_time_difference = end_time - start_time

    duration = duration_in_time_difference.seconds // (60 * 60)
    return duration


def calculate_payment_charge(hours: int):
    """
        Calculate Payment based on number of hours:
        1) less than 2 payment => 30
        2) between 2 and 6 hours payment => 50
        3) between 6 and 12 hours payment => 100
        4) greater than 12 hours payment => 150
    """

    if not hours:
        payment = 0

    elif hours < 2:
        payment = 30

    elif hours < 6:
        payment = 50

    elif hours < 12:
        payment = 100
    else:
        payment = 150

    return payment


def get_duration_and_payment_for_start_and_end_time(start_time=None, end_time=None):
    """ Calculate duration (in hours) and Payment for given start and end time """

    duration = hours = 0
    if not (start_time and end_time):
        return duration, hours
    duration = calculate_duration_hours(start_time=start_time, end_time=end_time)
    payment = calculate_payment_charge(hours=duration)
    return duration, hours
