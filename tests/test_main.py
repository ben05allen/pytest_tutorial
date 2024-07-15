from main import func


def test_func():
    assert func(3) == 5


if __name__ == "__main__":
    print(f"func(3) is {func(3)}")
