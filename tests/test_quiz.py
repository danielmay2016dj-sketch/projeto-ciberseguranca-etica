import unittest

import quiz
import simulacao_controle


class QuizDataTests(unittest.TestCase):
    def test_question_bank_is_not_empty(self):
        self.assertGreaterEqual(len(quiz.QUESTIONS), 8)

    def test_each_question_has_valid_answer_and_four_options(self):
        for item in quiz.QUESTIONS:
            with self.subTest(question=item["question"]):
                self.assertEqual(len(item["options"]), 4)
                self.assertIn(item["answer"], {"A", "B", "C", "D"})
                self.assertTrue(item["explanation"].strip())

    def test_all_options_start_with_answer_letter(self):
        for item in quiz.QUESTIONS:
            labels = {option[0] for option in item["options"]}
            self.assertEqual(labels, {"A", "B", "C", "D"})


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
