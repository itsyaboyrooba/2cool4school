import psutil

def total():
    return int(psutil.disk_usage('/').total / pow(1024, 3))
def free():
    return int(psutil.disk_usage('/').free / pow(1024, 3))
def used():
    return int(psutil.disk_usage('/').used / pow(1024, 3))
def used_pct():
    return used() / total() * 100