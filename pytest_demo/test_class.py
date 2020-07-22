# content of test_class.py
class TestClass:
    def test_one_LOMA0004(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")