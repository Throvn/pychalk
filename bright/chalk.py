def green(text):
    return '\033[92m;1m' + text + '\033[0m'
    
def blue(text):
    return '\033[94m;1m' + text + '\033[0m'

def yellow(text):
    return '\033[93m;1m' + text + '\033[0m'

def red(text):
    return '\033[91m;1m' + text + '\033[0m'

def white(text):
    return '\u001b[37m;1m' + text + '\033[0m'

def black(text):
    return '\u001b[30m;1m' + text + '\033[0m'

def magenta(text):
    return '\u001b[35m;1m' + text + '\033[0m'

def cyan(text):
    return '\u001b[36m;1m' + text + '\033[0m'

# Decorations

def bold(text):
    return '\033[1m' + text + '\033[0m'

def underline(text):
    return '\033[4m' + text + '\033[0m'

def reversed(text):
    return '\033[7m' + text + '\033[0m'