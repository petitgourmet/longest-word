# tests/test_game.py

# [...]
def test_unknown_word_is_invalid(self):
      new_game = Game()
      new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
      self.assertIs(new_game.is_valid('FEUN'), False)

def test_empty_word_is_invalid(self):
    new_game = Game()
    self.assertIs(new_game.is_valid(''), False)

def test_is_valid(self):
    new_game = Game()
    new_game.grid = list('KWEUEAKRZ') # Force the grid to a test case:
    self.assertIs(new_game.is_valid('EUREKA'), True)
    self.assertEqual(new_game.grid, list('KWEUEAKRZ')) # Make sure the grid remained untouched

def test_is_invalid(self):
    new_game = Game()
    new_game.grid = list('KWEUEAKRZ') # Force the grid to a test case:
    self.assertIs(new_game.is_valid('SANDWICH'), False)
    self.assertEqual(new_game.grid, list('KWEUEAKRZ')) # Make sure the grid remained untouched
