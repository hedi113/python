def convertToJPY(a: int) -> float:
    JPYresult: float = None
    JPYresult = a * 0.3636
    return JPYresult
def convertToUSD(a: int) -> float:
    USDresult: float = None
    USDresult = a * 0.0027
    return USDresult
def convertToCHF(a: int) -> float:
    CHFresult: float = None
    CHFresult = a * 0.0025
    return CHFresult

def convertJPYtoEUR(JPYresult: float) -> float:
    JPYtoEURresult: float = None
    JPYtoEURresult = JPYresult * 0.75
    return JPYtoEURresult
def convertUSDtoEUR(USDresult: float) -> float:
    USDtoEURresult: float = None
    USDtoEURresult = USDresult * 0.8
    return USDtoEURresult
def convertCHFtoEUR(CHFresult: float) -> float:
    CHFtoEURresult: float = None
    CHFtoEURresult = CHFresult * 0.55
    return CHFtoEURresult
