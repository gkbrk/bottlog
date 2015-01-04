import bottle
import time

def apache_logger(callback):
    """Logs in the combined log format"""
    def wrapper(*args, **kwargs):
        log_data = []
        log_data.append(bottle.request.remote_addr)
        log_data.append("-")
        log_data.append("-")
        log_data.append(time.strftime("[%d/%b/%Y:%H:%M:%S %z]"))
        log_data.append('"%s %s %s"' % (bottle.request.method, bottle.request.path, bottle.request.environ.get("SERVER_PROTOCOL", "")))
        log_data.append(bottle.response.status_code)
        log_data.append("-") #TODO: Fix content-length
        log_data.append(bottle.request.get_header("Referer", "-"))
        log_data.append(bottle.request.get_header("User-Agent", "-"))

        with open("server.log", "a+") as log_file:
            log_file.write(" ".join(log_data) + "\n")

    return wrapper

def common_logger(callback):
    """Logs in the common log format"""
    def wrapper(*args, **kwargs):
        log_data = []
        log_data.append(bottle.request.remote_addr)
        log_data.append("-")
        log_data.append("-")
        log_data.append(time.strftime("[%d/%b/%Y:%H:%M:%S %z]"))
        log_data.append('"%s %s %s"' % (bottle.request.method, bottle.request.path, bottle.request.environ.get("SERVER_PROTOCOL", "")))
        log_data.append(bottle.response.status_code)
        log_data.append("-") #TODO: Fix content-length

        with open("server.log", "a+") as log_file:
            log_file.write(" ".join(log_data) + "\n")

    return wrapper