# ChrisPy - Better Function Defaults

> :warning: I do not recommend using this package anywhere, especially not inside other packages!

Install with `pip install chrispy`

```python
import chrispy

chrispy.BETTER_DEFAULTS["numpy.meshgrid"] = {
    "kwargs": {
        "indexing"="yx"
    }
}
```
