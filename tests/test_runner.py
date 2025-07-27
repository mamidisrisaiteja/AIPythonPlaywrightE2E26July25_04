import pytest

if __name__ == '__main__':
    pytest.main([
        '--maxfail=2',
        '--disable-warnings',
        '--tb=short',
        'step_definitions/'
    ])
