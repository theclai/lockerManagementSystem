import unittest
from io import StringIO
from unittest.mock import patch
from locker import Locker


class TestLocker(unittest.TestCase):
    # test if command invalid
    def test_error_when_invalid_command(self):
        error_message = "hello pilihan tidak ada ada.\n"
        test_input = "hello"
        locker = Locker(test_input)

        # run test
        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), error_message)

    # test if init have more than 1 arg   
    def test_init_more_than_1_argument(self):
        error_message = "init Hanya bisa 1 argument.\n"
        test_input = "init 123 123"
        interpreter = Locker(test_input)

        # run test
        with patch('sys.stdout', new=StringIO()) as fake_out:
            interpreter.run()
            self.assertEqual(fake_out.getvalue(), error_message)

    # test success init
    def test_init_accept_1_argument(self):
        test_input = "init 2"
        locker_data_output = [[1, None, None], [2, None, None]]

        locker = Locker(test_input)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(len(locker.locker_data), len(locker_data_output))
            self.assertEqual(locker.locker_data, locker_data_output)

    def test_init_must_contain_argument(self):
        error_message = "init Hanya bisa 1 argument.\n"
        test_input = "init"
        interpreter = Locker(test_input)

        # run test
        with patch('sys.stdout', new=StringIO()) as fake_out:
            interpreter.run()
            self.assertEqual(fake_out.getvalue(), error_message)

    def test_init_only_accept_number(self):
        error_message = "argument harus angka, mulai dari angka 1.\n"
        test_input = "init yy"
        locker = Locker(test_input)
        locker.locker_data = []

        # run test
        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), error_message)

    def test_init_only_accept_postive_number_and_gte_1(self):
        error_message = "argument harus angka, mulai dari 1.\n"
        test_input = "init -1"
        locker = Locker(test_input)
        locker.locker_data = []

        # run test
        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), error_message)

    def test_init_reinit(self):
        error_message = "Sukses membuat loker dengan jumlah 10.\n"
        test_input = "init 10"
        locker = Locker(test_input)
        locker.locker_data = [[1, None, None]]

        # run test
        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), error_message)

    def test_input_allow_2_arguments(self):
        error_message = "input Sukses membuat loker dengan jumlah.\n"
        test_input = "input SIM 123 123"
        locker = Locker(test_input)
        # mock self.locker_data
        locker.locker_data = [
            [1, 'KTP', '1234'],
            [2, None, None]
        ]

        # run test
        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), error_message)

    def test_input_must_initiate_first(self):
        error_message = "Anda belum memasukan jumlah loker.\n"
        test_input = "input SIM 123"
        locker = Locker(test_input)
        locker.locker_data = []

        # run test
        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), error_message)

    def test_input_locker_full(self):
        error_message = "Loker sudah terisi.\n"
        test_input = "input SIM 1234"
        locker = Locker(test_input)

        # mock self.locker_data
        locker.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'SIM', '4321']
        ]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), error_message)

    def test_input_locker_available(self):
        message = "Kartu identitas sudah tersimpan pada loker nomer 1.\n"
        test_input = "input SIM 1234"
        locker = Locker(test_input)

        # mock self.locker_data
        locker.locker_data = [[1, None, None]]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), message)

    def test_leave_with_valid_index_range(self):
        message = "Loker no 1 berhasil dikosongkan.\n"
        test_input = "leave 1"
        locker = Locker(test_input)
        output_locker_data = [[1, None, None], [2, 'SIM', '4321']]

        # mock self.locker_data
        locker.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'SIM', '4321']
        ]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), message)

        self.assertEqual(locker.locker_data, output_locker_data)

    def test_leave_error_if_out_of_locker_length(self):
        message = "Hanya bisa mengosongkan loker dari 1 - 2.\n"
        test_input = "leave 212"
        locker = Locker(test_input)

        # mock self.locker_data
        locker.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'SIM', '4321']
        ]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), message)

    def test_leave_must_1_argument(self):
        message = "leave Hanya bisa 1 argument.\n"
        test_input = "leave 212 1"
        locker = Locker(test_input)

        # mock self.locker_data
        locker.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'SIM', '4321']
        ]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), message)

    def test_search_must_1_argument(self):
        message = "search Hanya bisa 1 argument.\n"
        test_input = "search 212 1"
        locker = Locker(test_input)

        # mock self.locker_data
        locker.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'SIM', '4321']
        ]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), message)

    def test_search_valid_data(self):
        message = "No identitas dengan tipe KTP: 1234, 2233.\n"
        test_input = "search KTP"
        locker = Locker(test_input)

        # mock self.locker_data
        locker.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'SIM', '4321'],
            [3, 'KTP', '2233']
        ]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), message)

    def test_search_invalid_type_id(self):
        message = "Tipe identitas tidak ada.\n"
        test_input = "search UNKNOWN"
        locker = Locker(test_input)

        # mock self.locker_data
        locker.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'SIM', '4321'],
            [3, 'KTP', '2233']
        ]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), message)

    def test_exit_without_argument(self):
        message = "exit tidak bisa menerima argument.\n"
        test_input = "exit 1234"
        locker = Locker(test_input)
        locker.locker_data = [
            [1, 'KTP', '1234'],
            [2, None, None]
        ]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), message)

    def test_exit_run_normal(self):
        test_input = "exit"
        locker = Locker(test_input)
        with self.assertRaises(SystemExit) as cm:
            locker.run()

    def test_find_must_1_argument(self):
        message = "find Hanya bisa 1 argument.\n"
        test_input = "find 212 1"
        locker = Locker(test_input)
        locker.locker_data = [
            [1, 'KTP', '1234'],
            [2, None, None]
        ]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), message)

    def test_find_data_exist(self):
        message = "Kartu identitas 1234 berada pada loker nomer 1.\n"
        test_input = "find 1234"
        locker = Locker(test_input)

        # mock self.locker_data
        locker.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'SIM', '4321']
        ]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), message)

    def test_find_data_doesnot_exist(self):
        message = "Nomer identitas tidak ada.\n"
        test_input = "find 12342"
        locker = Locker(test_input)

        # mock self.locker_data
        locker.locker_data = [
            [1, 'KTP', '1234'],
            [2, 'SIM', '4321']
        ]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), message)

    def test_status_without_argument(self):
        message = "status tidak bisa menerima argument.\n"
        test_input = "status 1234"
        locker = Locker(test_input)
        locker.locker_data = [
            [1, 'KTP', '1234'],
            [2, None, None]
        ]

        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertEqual(fake_out.getvalue(), message)

    def test_status_show_valid_data(self):
        test_input = "status"
        locker = Locker(test_input)
        locker.locker_data = [[1, 'KTP', '1234'], [2, None, None]]
        contain_string = "1       KTP                      1234"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            locker.run()
            self.assertIn(contain_string, fake_out.getvalue())

    def test_status_must_initiate_first(self):
        test_input = "status"
        locker = Locker(test_input)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            result = locker.run()
            self.assertEqual(None, result)


if __name__ == '__main__':
    unittest.main()
