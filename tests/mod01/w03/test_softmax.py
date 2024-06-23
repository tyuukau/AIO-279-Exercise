import unittest
import torch
import torch.nn.functional as F

from mod01.w03.softmax import Softmax, SoftmaxStable


class TestSoftmaxFunctions(unittest.TestCase):

    def setUp(self):
        """
        Set up instances of Softmax and SoftmaxStable for testing.
        """
        self.softmax = Softmax()
        self.softmax_stable = SoftmaxStable()

    def test_softmax_output(self):
        """
        Test the output of the custom Softmax function.
        """
        x = torch.tensor([1.0, 2.0, 3.0])
        output = self.softmax(x)
        expected_output = F.softmax(x, dim=0)
        self.assertTrue(torch.allclose(output, expected_output, atol=1e-6))

    def test_softmax_stable_output(self):
        """
        Test the output of the custom numerically stable Softmax function.
        """
        x = torch.tensor([1.0, 2.0, 3.0])
        output = self.softmax_stable(x)
        expected_output = F.softmax(x, dim=0)
        self.assertTrue(torch.allclose(output, expected_output, atol=1e-6))

    def test_softmax_stable_large_values(self):
        """
        Test the numerically stable Softmax function with large input values.
        """
        x = torch.tensor([1000.0, 1001.0, 1002.0])
        output = self.softmax_stable(x)
        expected_output = F.softmax(x, dim=0)
        self.assertTrue(torch.allclose(output, expected_output, atol=1e-6))


if __name__ == "__main__":
    unittest.main()
