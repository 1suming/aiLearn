import unittest

from xor_classifier import train_xor


class XorClassifierTest(unittest.TestCase):
    def test_trained_model_classifies_all_xor_inputs(self):
        predictions = train_xor(epochs=1_500)

        self.assertEqual(predictions.tolist(), [0, 1, 1, 0])


if __name__ == "__main__":
    unittest.main()
