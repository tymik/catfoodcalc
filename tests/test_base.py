import unittest


def get_results(method, used_object):
    return method(used_object)


def run_one_method(method_name, function, tested_class, test_data, test_results):
    for test_object, value in test_data.items():
        used_object = tested_class(*value)
        expected = test_results[test_object][method_name]
        actual = get_results(function, used_object)
        print("Testing method {0} with test item {1}".format(function.__name__, test_object))
        unittest.TestCase().assertEqual(actual, expected,
                                        "Failed testing method {0} for test item {1}".format(function, test_object))


class TestBase(unittest.TestCase):

    def runTest(self):
        for method_name, function in self.methods_to_test.items():
            run_one_method(method_name, function, self.tested_class, self.test_data, self.test_results)