import unittest
import vim_qunit_special_blend as sut


class VimQunitSpecialBlendTests(unittest.TestCase):

    def test_get_line_num_of_current_module_returns_correct_value(self):
        current_line1 = 7
        current_line2 = 15
        current_buffer = self.build_buffer_helper()
        self.assertEqual(2, sut.get_line_num_of_current_module(current_line1, current_buffer))
        self.assertEqual(12, sut.get_line_num_of_current_module(current_line2, current_buffer))

    def test_get_line_num_of_current_module_returns_false_when_not_in_module(self):
        current_buffer = self.build_buffer_helper()
        self.assertEqual(False, sut.get_line_num_of_current_module(2, current_buffer))

    def test_sub_current_module_with_singleModule_returns_the_proper_string(self):
        current_buffer = self.build_buffer_helper()
        line_num = sut.get_line_num_of_current_module(7, current_buffer)
        returned_string = sut.sub_current_module_with_singleModule(line_num, current_buffer)
        self.assertEqual('singleModule("Module 1");\n', returned_string)

    def test_sub_singleModule_with_module_returns_the_proper_string(self):
        current_buffer = self.build_buffer_helper()
        line_num = sut.get_line_num_of_current_module(7, current_buffer)
        current_buffer[line_num] = sut.sub_current_module_with_singleModule(line_num, current_buffer)
        self.assertEqual('singleModule("Module 1");\n', current_buffer[line_num])
        returned_string = sut.sub_singleModule_with_module(line_num, current_buffer)
        self.assertEqual('module("Module 1");\n', returned_string)

    def test_get_line_num_of_current_test_returns_correct_value(self):
        current_line1 = 7
        current_line2 = 15
        current_buffer = self.build_buffer_helper()
        self.assertEqual(4, sut.get_line_num_of_current_test(current_line1, current_buffer))
        self.assertEqual(14, sut.get_line_num_of_current_test(current_line2, current_buffer))

    def test_get_line_num_of_current_test_returns_false_when_not_in_test(self):
        current_buffer = self.build_buffer_helper()
        self.assertEqual(False, sut.get_line_num_of_current_test(2, current_buffer))

    def test_sub_current_test_with_singleTest_returns_the_proper_string(self):
        current_buffer = self.build_buffer_helper()
        line_num = sut.get_line_num_of_current_test(7, current_buffer)
        returned_string = sut.sub_current_test_with_singleTest(line_num, current_buffer)
        self.assertEqual('singleTest("test example1a", function() {\n', returned_string)

    def test_sub_singleTest_with_test_returns_the_proper_string(self):
        current_buffer = self.build_buffer_helper()
        line_num = sut.get_line_num_of_current_test(7, current_buffer)
        current_buffer[line_num] = sut.sub_current_test_with_singleTest(line_num, current_buffer)
        self.assertEqual('singleTest("test example1a", function() {\n', current_buffer[line_num])
        returned_string = sut.sub_singleTest_with_test(line_num, current_buffer)
        self.assertEqual('test("test example1a", function() {\n', returned_string)

    def build_buffer_helper(self):
        with open("dummy_test_file.js", "r") as f:
            current_buffer = []
            for line in f.readlines():
                current_buffer.append(line)
        return current_buffer
