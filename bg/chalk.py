def green(text):
    return '\033[42m' + text + '\033[0m'
    
def blue(text):
    return '\033[44m' + text + '\033[0m'

def yellow(text):
    return '\033[43m' + text + '\033[0m'

def red(text):
    return '\033[41m' + text + '\033[0m'

def white(text):
    return '\u001b[47m' + text + '\033[0m'

def black(text):
    return '\u001b[40m' + text + '\033[0m'

def magenta(text):
    return '\u001b[45m' + text + '\033[0m'

def cyan(text):
    return '\u001b[46m' + text + '\033[0m'

    
# Decorations

def bold(text):
    return '\033[1m' + text + '\033[0m'

def underline(text):
    return '\033[4m' + text + '\033[0m'

def reversed(text):
    return '\033[7m' + text + '\033[0m'