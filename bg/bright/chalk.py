def green(text):
    return '\033[42m;1m' + text + '\033[0m'
    
def blue(text):
    return '\033[44m;1m' + text + '\033[0m'

def yellow(text):
    return '\033[43m;1m' + text + '\033[0m'

def red(text):
    return '\033[41m;1m' + text + '\033[0m'

def white(text):
    return '\u001b[47m;1m' + text + '\033[0m'

def black(text):
    return '\u001b[40m;1m' + text + '\033[0m'

def magenta(text):
    return '\u001b[45m;1m' + text + '\033[0m'

def cyan(text):
    return '\u001b[46m;1m' + text + '\033[0m'
