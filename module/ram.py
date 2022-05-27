import psutil

def total():
    return int(psutil.virtual_memory().total / pow(1024, 2))
def available():
    return int(psutil.virtual_memory().available / pow(1024, 2))
def usage():
    return int(psutil.virtual_memory().used / pow(1024, 2))
def usage_pct():
    return int(psutil.virtual_memory().percent)