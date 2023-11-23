import unittest
from src.Assignment_1.util import process_commands
class TestListCommands(unittest.TestCase):
    def test_process_commands(self):
        # Example test case
        the_list = []
        commands = ['append 1', 'append 2', 'print']
        process_commands(the_list, commands)
        self.assertEqual(the_list, [1, 2])

if __name__ == '__main__':
    unittest.main()
    
