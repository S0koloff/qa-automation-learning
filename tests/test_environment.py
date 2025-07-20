def test_python_version():
    import sys
    assert sys.version_info.major == 3
    assert sys.version_info.minor >= 10  # Проверяем Python 3.10+

def test_imports():
    try:
        import pytest
        import selenium
        import playwright
    except ImportError as e:
        assert False, f"Ошибка импорта: {e}"