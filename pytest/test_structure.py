import pytest


tested_dict = {'1': 1, '2': 2, '3': 3}
tested_str = 'Hello, world!'


@pytest.mark.parametrize(
    ('key', 'value'),
    (
        ('1', 1),
        ('4', None),
    )
)
def test_dict_get(key, value):
    assert tested_dict.get(key) == value


def test_dict_key_error():
    with pytest.raises(KeyError) as error:
        tested_dict['4']
    assert '4' == error.value.args[0]


def test_dict_values():
    assert tuple(tested_dict.values()) == (1, 2, 3, )


def test_str_upper():
    assert tested_str.upper() == 'HELLO, WORLD!'


def test_str_lower():
    assert tested_str.lower() == 'hello, world!'


def test_str_split():
    assert tested_str.split(' ') == ['Hello,', 'world!']


if __name__ == '__main__':
    pytest.main()
