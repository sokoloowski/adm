def _print_color(color: str = '\033[0m', *args, **kwargs):
    # FAIL      = '\033[91m'
    # OKGREEN   = '\033[92m'
    # WARNING   = '\033[93m'
    # OKBLUE    = '\033[94m'
    # HEADER    = '\033[95m'
    # OKCYAN    = '\033[96m'
    # ENDC      = '\033[0m'
    # BOLD      = '\033[1m'
    # UNDERLINE = '\033[4m'
    print(color + ' '.join(args) + '\033[0m', **kwargs)


def error(*args, critical=True, **kwargs):
    _print_color('\033[91m', *args, **kwargs)
    if critical:
        raise ValueError(*args)


def success(*args, **kwargs):
    _print_color('\033[92m', *args, **kwargs)


def warning(*args, **kwargs):
    _print_color('\033[93m', *args, **kwargs)


def bold(text: str) -> str:
    return f'\033[1m{text}\033[0m'
