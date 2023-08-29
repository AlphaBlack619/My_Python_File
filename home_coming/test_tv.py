import unittest
from tv import TV


class TestTV(unittest.TestCase):
    def setUp(self):
        self.nero = TV()

    def test_turn_on(self):
        self.nero.turn_on()
        self.assertTrue(self.nero.on)

    def test_turn_off(self):
        self.nero.turn_on()
        self.assertTrue(self.nero.on_status())
        self.nero.turn_off()
        self.assertFalse(self.nero.on_status())

    def test_channel(self):
        self.nero.turn_on()
        self.nero.set_channel(10)
        self.assertTrue(self.nero.on_status())
        self.assertEqual(10, self.nero.get_channel())

    def test_channel_down(self):
        self.nero.turn_on()
        self.assertTrue(self.nero.on_status())
        self.nero.set_channel(10)
        self.assertEqual(10, self.nero.channel)
        self.nero.channel_down()
        self.assertEqual(9, self.nero.get_channel())

    def test_channel_up(self):
        self.nero.turn_on()
        self.assertTrue(self.nero.on_status())
        self.nero.set_channel(10)
        self.assertEqual(10, self.nero.channel)
        self.nero.channel_up()
        self.assertEqual(11, self.nero.get_channel())

    def test_volume(self):
        self.nero.turn_on()
        self.assertTrue(self.nero.on_status())
        self.nero.set_volume(10)
        self.assertEqual(10, self.nero.get_volume())

    def test_volume_down(self):
        self.nero.turn_on()
        self.assertTrue(self.nero.on_status())
        self.nero.set_volume(10)
        self.assertEqual(10, self.nero.get_volume())
        self.nero.volume_down()
        self.assertEqual(9, self.nero.get_volume())

    def test_volume_up(self):
        self.nero.turn_on()
        self.assertTrue(self.nero.on_status())
        self.nero.set_volume(10)
        self.assertEqual(10, self.nero.get_volume())
        self.nero.volume_up()
        self.assertEqual(11, self.nero.get_volume())


if __name__ == '__main__':
    unittest.main()
