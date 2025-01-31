import unittest


from textnode import TextNode, TextType, text_node_to_html_node, extract_markdown_images, extract_markdown_url
from splitdelimiter import split_nodes_delimiter


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
        node = TextNode("Just plain text", TextType.TEXT)
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
    
    def test_basic_code_block(self):
        node = TextNode("This is `code` here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" here", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_multiple_code_blocks(self):
        node = TextNode("Here is `more` and `more code`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("more", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("more code", TextType.CODE)
        ]
        self.assertEqual(result, expected)

    def test_bold_text(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

    def test_already_formatted_node(self):
        node = TextNode("Already bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [node]  # Should remain unchanged
        self.assertEqual(result, expected)

    def test_unmatched_delimiter(self):
        node = TextNode("This is `incomplete", TextType.TEXT)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(context.exception), "Unmatched delimiter")
    
    def test_extract_markdown_images(self):
        text_1 = "some text ![alt_text](imageurl) some more text"
        text_2 = "some text [alt_text](imageurl) some more text"
        text_3 = "some text ![alt[]_text](imageurl) some more text"
        text_4 = "some text ![alt_text](ima()geurl) some more text"
        text_5 = "(some text ![alt_text](imageurl) some more text)"
        text_6 = "some text ![alt_text](imageurl) some more text ![alt_text2](imageurl2)"
        self.assertEqual(extract_markdown_images(text_1), [("alt_text", "imageurl")])
        self.assertEqual(extract_markdown_images(text_2), [])
        self.assertEqual(extract_markdown_images(text_3), [])
        self.assertEqual(extract_markdown_images(text_4), [])
        self.assertEqual(extract_markdown_images(text_5), [("alt_text", "imageurl")])
        self.assertEqual(extract_markdown_images(text_6), [("alt_text", "imageurl"), ("alt_text2", "imageurl2")])
    
    def test_extract_markdown_url(self):
        text_1 = "some text [alt_text](url) some more text"
        text_2 = "some text ![alt_text](url) some more text"
        text_3 = "some text [alt[]_text](url) some more text"
        text_4 = "some text [alt_text](()url) some more text"
        text_5 = "(some text [alt_text](url) some more text)"
        text_6 = "some text [alt_text](url) some more text [alt_text2](url2)"
        self.assertEqual(extract_markdown_url(text_1), [("alt_text", "url")])
        self.assertEqual(extract_markdown_url(text_2), [])
        self.assertEqual(extract_markdown_url(text_3), [])
        self.assertEqual(extract_markdown_url(text_4), [])
        self.assertEqual(extract_markdown_url(text_5), [("alt_text", "url")])
        self.assertEqual(extract_markdown_url(text_6), [("alt_text", "url"), ("alt_text2", "url2")])

if __name__ == "__main__":
    unittest.main()