from gendiff.scripts.gendiff import generate_diff

PATH = 'tests/fixtures/json/'


def test_diff():
    file1_path = PATH + 'diff1.json'
    file2_path = PATH + 'diff2.json'
    assert generate_diff(file1_path, file2_path) == '''{
  - follow: false
  + verbose: true
}'''


def test_diff_values():
    file1_path = PATH + 'diff_values1.json'
    file2_path = PATH + 'diff_values2.json'
    assert generate_diff(file1_path, file2_path) == '''{
  - host: hexlet.io
  + host: yandex.ru
}'''


def test_equal():
    file_path = PATH + 'equal.json'
    assert generate_diff(file_path, file_path) == '''{
    host: hexlet.io
}'''


def test_add():
    file1_path = PATH + 'add1.json'
    file2_path = PATH + 'add2.json'
    assert generate_diff(file1_path, file2_path) == '''{
    host: hexlet.io
  + verbose: true
}'''


def test_diff_values_position():
    file1_path = PATH + 'diff_values_pos1.json'
    file2_path = PATH + 'diff_values_pos2.json'
    assert generate_diff(file1_path, file2_path) == '''{
    follow: false
  - host: hexlet.io
  + host: yandex.ru
}'''