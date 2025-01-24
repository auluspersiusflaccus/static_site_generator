import unittest


from textnode import TextNode, TextType, text_node_to_html_node


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
    def test_text_node_to_html_node(self):
    # Test normal text
        node = TextNode("Just plain text", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "", "Normal text should have empty tag"
        assert html_node.value == "Just plain text", "Normal text value should be preserved"
        assert html_node.props == None, "Normal text should have no props"
    def test_btext_node_to_html_node(self):
    # Test bold text
        node = TextNode("Just plain text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "b", "Bold text should have a 'b' tag"
        assert html_node.value == "Just plain text", "Bold text value should be preserved"
        assert html_node.props == None, "Bold text should have no props"
    def test_itext_node_to_html_node(self):
    # Test italic text
        node = TextNode("Just plain text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "i", "Italic text should have a 'i' tag"
        assert html_node.value == "Just plain text", "Italic text value should be preserved"
        assert html_node.props == None, "Italic text should have no props"
    def test_ctext_node_to_html_node(self):
    # Test code text
        node = TextNode("Just plain text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "code", "Code text should have a 'code' tag"
        assert html_node.value == "Just plain text", "Code text value should be preserved"
        assert html_node.props == None, "Code text should have no props"
    def test_ltext_node_to_html_node(self):
    # Test link text
        node = TextNode("Just plain text", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "a", "LINK text should have a 'a' tag"
        assert html_node.value == "Just plain text", "Normal text value should be preserved"
        assert html_node.props == {"href": "https://www.boot.dev"}, "Link text should have a href prop"
    def test_imtext_node_to_html_node(self):
    # Test image text
        node = TextNode("this is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        assert html_node.tag == "img", "Image text should have an 'img' tag"
        assert html_node.value == "", "Image text is passed into an 'alt' prop"
        assert html_node.props == {"src": "https://www.boot.dev", "alt": "this is an image"}, "Image text should have a src props and and a alt prop"

    
if __name__ == "__main__":
    unittest.main()