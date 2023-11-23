from datetime import datetime

def time_delta(t1, t2):
    format_ = '%a %d %b %Y %H:%M:%S %z'
    return str(int(abs((datetime.strptime(t1, format_) - datetime.strptime(t2, format_)).total_seconds())))
