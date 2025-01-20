import unittest


from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq2(self):
        node = TextNode("132456", TextType.CODE)
        node2 = TextNode("132456", TextType.CODE)
        self.assertEqual(node, node2)
    def test_noteq(self):
        node = TextNode("112456", TextType.CODE)
        node2 = TextNode("132456", TextType.CODE)
        self.assertNotEqual(node, node2)
    def test_true(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        self.assertTrue(node)
    def test_noteq3(self):
        node = TextNode("123456", TextType.CODE, "https://www.boot.dev/lessons/")
        node2 = TextNode("132456", TextType.CODE, "https://www.boot.dev/lesson/")
        self.assertNotEqual(node, node2)
    def test_badinput(self):
        self.assertRaises(TypeError, TextNode, "123")

if __name__ == "__main__":
    unittest.main()