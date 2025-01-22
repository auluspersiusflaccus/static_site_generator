import unittest


from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_constructor_equality(self):
        # Test with identical nodes
        node1 = HTMLNode(tag="a", value="Click me!", props={"href": "https://www.boot.dev"})
        node2 = HTMLNode(tag="a", value="Click me!", props={"href": "https://www.boot.dev"})
        self.assertEqual(node1, node2)

        # Maybe test with None values?
        node3 = HTMLNode()
        node4 = HTMLNode()
        self.assertEqual(node3, node4)

        # Test with different nodes
        node5 = HTMLNode(tag="p", value="Different!")
        self.assertNotEqual(node1, node5)
    def test_propstohtml(self):
        link_node = HTMLNode(
        tag="a",
        value="Click me!",
        props={"href": "https://www.boot.dev"}
        )
        result = link_node.props_to_html()
        self.assertEqual(result, " href=\"https://www.boot.dev\"")
    def test_repr(self):
        link_node = HTMLNode(
        tag="a",
        value="Click me!",
        props={"href": "https://www.boot.dev"}
        )
        result = link_node.__repr__()
        self.assertEqual(result, """tag: a, 
            value: Click me!, 
            children: None, 
            props: {'href': 'https://www.boot.dev'}"""
            )
    

if __name__ == "__main__":
    unittest.main()