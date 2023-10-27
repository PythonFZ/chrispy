class CustomDict(dict):
    def __setitem__(self, *args, **kwargs) -> None:
        super().__setitem__(*args, **kwargs)
        update_defaults()

BETTER_DEFAULTS = CustomDict({
    "numpy.linspace": {
        "kwargs": {
            "endpoint": False,
        }
    }
})

import importlib
import functools

def update_defaults():
    """Update the defaults of some functions in numpy."""
    for full_name, defaults in BETTER_DEFAULTS.items():
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
        
        setattr(module, func_name, new_func)

update_defaults()