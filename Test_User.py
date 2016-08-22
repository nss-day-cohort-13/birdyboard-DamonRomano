import unittest


class TestUser(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_user_creation(self):
    user = User("Mac", "The Knife")
    self.assertEqual("Mac", user.full_name)
    self.assertEqual("The Knife", user.screen_name)
    self.assertIsNotNone(user.user_id)
    self.assertIsInstance(user, User)


if __name__ == '__main__':
    unittest.main()
