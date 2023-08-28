import os


def debug_print(*args, **kwargs):
    debug_mode = os.environ.get("AQMSP_DEBUG", False)
    if debug_mode:
        print(*args, **kwargs)
    else:
        pass
