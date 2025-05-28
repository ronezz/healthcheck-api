import psutil
import time

boot_time = psutil.boot_time()

def get_uptime():

    uptime_seconds= time.time() - boot_time
    uptime_hours = round(uptime_seconds/3600, 2)
    return f"{uptime_hours} hours"

def get_system_status():
    return{
        "cpu_percent": psutil.cpu_percent(interval=0.5),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
        "uptime": get_uptime(),
        "services": {
            "nginx": "OK",
            "mysql": "DOWN"
        }
    }
