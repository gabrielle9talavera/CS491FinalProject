import unittest
from Path import Path


class TestPathMethods(unittest.TestCase):

    def setUp(self):
        self.path = Path()

    def test_find_node_probs(self):
        self.node_fail.find_node_probs(5)
        self.assertEqual(len(self.node_fail.node_probs), 5)

    def test_calculate_failure_low_prob(self):
        self.node_fail.fail_prob = .2
        self.node_fail.node_probs = [.5, .6, .3, .7, .4]
        self.node_fail.calculate_failure(5, 2)
        self.assertEqual(self.node_fail.failure, [])

    def test_calculate_failure_high_prob(self):
        self.node_fail.fail_prob = .8
        self.node_fail.node_probs = [.2, .3, .1, .4, .5]
        self.node_fail.calculate_failure(5, 3)
        self.assertNotEqual(self.node_fail.failure, [])


if __name__ == '__main__':
    unittest.main()

