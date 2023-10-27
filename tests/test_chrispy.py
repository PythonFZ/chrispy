import numpy as np
import numpy.testing as npt

def test_chrispy():
    linspace = np.linspace(0, 9, 10)
    npt.assert_equal(linspace, list(range(10)))
    import chrispy
    linspace = np.linspace(0, 10, 10)
    npt.assert_equal(linspace, list(range(10)))

def test_update_chrispy():
    arange = np.arange(stop=10)
    npt.assert_equal(arange, list(range(10)))
    import chrispy
    chrispy.BETTER_DEFAULTS["numpy.arange"] = {
        "kwargs": {
            "step": 2,
        }
    }
    arange = np.arange(stop=10)
    npt.assert_equal(arange, list(range(0, 10, 2)))
