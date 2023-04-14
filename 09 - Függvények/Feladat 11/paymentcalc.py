def howMuchPayment(hours: int) -> int:
    payment: int = None
    if(hours == 40 or hours < 40):
        payment = hours * 1000
    if(hours > 40):
        payment = (hours - 40) * 1500 + 40 * 1000 
    return payment
