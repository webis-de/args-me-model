import unittest

from args_me_model import Argument, Claim, Source

class TestParsing(unittest.TestCase):

    def test_simple(self):
        claim = Claim(id="C0123456789abcdef", text="Foo", sources=[
          Source(text="Bar", method="Intuition")
        ])
        self.assertEqual(claim, Claim.model_validate_json(claim.model_dump_json()))



if __name__ == '__main__':
    unittest.main()

