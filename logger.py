_FP = open("log.txt", "w")

def log_(*args):
    for line in args:
        _FP.write(str(line))
        _FP.write('\n')
        pass
    return

def log_close():
    _FP.close()
    return
