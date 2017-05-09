from datetime import datetime
import time

def timenow():
    return datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')