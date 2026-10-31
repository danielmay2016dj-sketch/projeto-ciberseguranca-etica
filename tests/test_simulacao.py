import unittest

import simulacao_controle


class LockoutSimulationTests(unittest.TestCase):
    def test_lockout_is_simulated_after_threshold(self):
        result = simulacao_controle.simulate_lockout(attempts=5, threshold=3)
        self.assertTrue(result["locked"])
        self.assertEqual(result["failures"], 3)
        self.assertEqual(len(result["events"]), 5)

    def test_no_lockout_below_threshold(self):
        result = simulacao_controle.simulate_lockout(attempts=2, threshold=3)
        self.assertFalse(result["locked"])
        self.assertEqual(result["failures"], 2)

    def test_invalid_parameters_are_rejected(self):
        with self.assertRaises(ValueError):
            simulacao_controle.simulate_lockout(attempts=-1)
        with self.assertRaises(ValueError):
            simulacao_controle.simulate_lockout(threshold=0)


if __name__ == "__main__":
    unittest.main()
