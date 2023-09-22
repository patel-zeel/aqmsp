import os


def set_verbose(verbose: bool):
    assert isinstance(verbose, bool), "verbose must be a boolean"
    os.environ["AQMSP_VERBOSE"] = str(verbose)


def get_verbose():
    verbose = os.environ.get("AQMSP_VERBOSE")
    if verbose is None:
        return False
    elif verbose == "True":
        return True
    elif verbose == "False":
        return False
    else:
        raise ValueError("AQMSP_VERBOSE must be either True or False")


def verbose_print(*args, **kwargs):
    verbose = get_verbose()
    if verbose:
        print(*args, **kwargs)
