"""UI tests. `darkmode-toggle` is only referenced here — production code no
longer uses it, but the tests were never cleaned up."""
from app import flags


def setup_function(fn):
    flags.reset_overrides()


