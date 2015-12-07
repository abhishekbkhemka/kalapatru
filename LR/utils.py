from datetime              import *

def getServerDateFromStr(dateStr):
     if dateStr != '' and dateStr != None:
        try:    return datetime.strptime(dateStr,"%d-%m-%Y")
        except: return datetime.strptime(dateStr,"%d-%m-%Y %H:%M:%S")
     else: return None


def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
    import signal

    class TimeoutError(Exception):
        pass

    def handler(signum, frame):
        raise TimeoutError()

    # set the timeout handler
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout_duration)
    try:
        result = func(*args, **kwargs)
    except TimeoutError as exc:
        result = default
    finally:
        signal.alarm(0)

    return result