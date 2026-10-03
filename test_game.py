import unittest
from unittest.mock import patch

import module


class GameTests(unittest.TestCase):
    def test_win_boundary(self):
        self.assertTrue(module.compare_values(100, 90))
        self.assertTrue(module.compare_values(100, 110))
        self.assertFalse(module.compare_values(100, 89))

    def test_bad_attack_does_not_consume_turn(self):
        with patch('builtins.input', side_effect=['bad', ' LITE ', 'lite', 'lite', 'lite', 'lite']):
            with patch.object(module, 'get_lite_attack', return_value=3):
                self.assertEqual(module.get_user_attack(), 15)

    def test_replay_prompt_retries(self):
        with patch.object(module, 'set_enemy_health', return_value=100), \
             patch.object(module, 'get_user_attack', return_value=100), \
             patch('builtins.input', side_effect=['?', ' N ']):
            self.assertFalse(module.run_game())


if __name__ == '__main__':
    unittest.main()
