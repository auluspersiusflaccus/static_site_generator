import unittest


from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node1 = LeafNode(None, "Hello world")
        node2 = "Hello world"
        self.assertEqual(node1.to_html(), node2)

        node3 = LeafNode("p", "Some text")
        node4 = "<p>Some text</p>"
        self.assertEqual(node3.to_html(), node4)

        node5 = LeafNode("a", "Click me!", {"href": "https://example.com"})
        node6 = '<a href="https://example.com">Click me!</a>'
        self.assertEqual(node5.to_html(), node6)

        

if __name__ == "__main__":
    unittest.main()