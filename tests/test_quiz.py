import unittest

import quiz


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


if __name__ == "__main__":
    unittest.main()
