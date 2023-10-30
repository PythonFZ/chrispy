import importlib
import functools
import logging

log = logging.getLogger(__name__)


class CustomDict(dict):
    def __setitem__(self, full_name, defaults) -> None:
        module, func_name = full_name.split(".", 1)
        module = importlib.import_module(module)
        func = getattr(module, func_name)
        # setattr(module, f"_chrispy_{func_name}", old_func)

        @functools.wraps(func)
        def new_func(*args, **kwargs):
            if "kwargs" in defaults:
                for k, v in defaults["kwargs"].items():
                    if k not in kwargs:
                        kwargs[k] = v
            if "args" in defaults:
                for i, v in enumerate(defaults["args"]):
                    if i >= len(args):
                        args.append(v)
            return func(*args, **kwargs)

        log.critical(f"Using ChrisPy for {full_name} - modifying defaults!")

        setattr(module, func_name, new_func)
        super().__setitem__(full_name, defaults)

    def update(self, other: dict) -> None:
        for k, v in other.items():
            self[k] = v


BETTER_DEFAULTS = CustomDict()
