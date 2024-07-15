import os
import pytest
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture
def numbers():
    return {1, 2, 3}
