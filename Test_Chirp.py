import unittest

class TestChirp(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    def test_reply_public_chirp_creation(self):
        source = User("Mac", "The Knife")
        chirp = Chirp   (
                        message="Test chirp for public reply.",
                        user=source.user_id,
                        private=False
                        )

    def test_new_public_chirp_creation(self):
        source = User("Mac", "The Knife")
        chirp = Chirp   (
                        message="Test new public chirp.",
                        user=source.user_id,
                        private=False
                        )

        self.assertEqual(chirp.message, "This is a chirp.")
        self.assertEqual(chirp.user_id, source.user_id)
        self.assertEqual(chirp.private, False)
        self.assertIsInstance(chirp, Chirp)
        self.assertIsNotNone(chirp.chirp_id)


    def test_private_chirp_creation(self):
        source = User("Mac", "The Knife")
        target = User("Bobby", "The Chin")
        chirp = Chirp(
                      message="Hi everyone",
                      user=source.user_id,
                      private=True,
                      receiver=target.user_id
                      )
    self.assertIsInstance(chirp, Chirp)


if __name__ == '__main__':
    unittest.main()
