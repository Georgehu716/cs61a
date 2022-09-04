def test_import_statement_of_frame():
    import time
    print('f1 frame now:', time.time())


if __name__ == '__main__':
    test_import_statement_of_frame()
    print('global frame:', time.time())
