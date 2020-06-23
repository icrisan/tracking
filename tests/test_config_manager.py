from config_util.config_manager import read_config_file, parse_config_file


def test_config_manager():
    read_config_file()
    dictionary = parse_config_file('Email')
    print(dictionary)
