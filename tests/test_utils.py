import pytest

from openweather_api.utils import build_full_url


@pytest.mark.parametrize('base_url, endpoint, expected_full_url', [
    ('https://test.com/1/', '2/3', 'https://test.com/1/2/3'),
    ('https://test.com/1/', '/2/3', 'https://test.com/1/2/3'),
    ('https://test.com/1', '/2/3', 'https://test.com/1/2/3'),
    ('https://test.com/1', '2/3', 'https://test.com/1/2/3')
])
def test_build_full_url(base_url, endpoint, expected_full_url):
    assert build_full_url(base_url, endpoint) == expected_full_url
