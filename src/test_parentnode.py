import unittest


from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_basic_parent_with_single_leaf_child(self):
        node = ParentNode("div", [
            LeafNode("p", "Hello")
        ])
        expected = "<div><p>Hello</p></div>"
        self.assertEqual(node.to_html(), expected)

    def test_parent_with_multiple_child(self):
        node = ParentNode("div", [
            LeafNode("b", "Bold"),
            LeafNode(None, "Normal"),
            LeafNode("i", "Italic")
        ])
        expected = "<div><b>Bold</b>Normal<i>Italic</i></div>"
        self.assertEqual(node.to_html(), expected)

    def test_nested_parents(self):
        node = ParentNode("div", [
            ParentNode("p", [
                LeafNode("b", "Nested")
            ])
        ])
        expected = "<div><p><b>Nested</b></p></div>"
        self.assertEqual(node.to_html(), expected)

    def test_parent_with_props(self):
        node = ParentNode("div", [
            LeafNode("p", "Hello")
        ], {"class": "container"})
        expected = "<div class=\"container\"><p>Hello</p></div>"
        self.assertEqual(node.to_html(), expected)

    def test_Error_case_no_tag(self):
        node = ParentNode(None, [
            LeafNode("p", "Hello")
        ])
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "missing tag value")

    def test_Error_case_no_children(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "missing children value")

    def test_complex_nesting_with_props(self):
        node = ParentNode("section", [
            ParentNode("div", [
                LeafNode("p", "Text")
            ], {"class": "inner"}),
            LeafNode("b", "Bold")
        ], {"id": "main"})
        expected = "<section id=\"main\"><div class=\"inner\"><p>Text</p></div><b>Bold</b></section>"
        self.assertEqual(node.to_html(), expected)

    def test_mixed_content_types(self):
        node = ParentNode("div", [
            LeafNode(None, "Text"),
            ParentNode("p", [
                LeafNode("b", "Bold")
            ]),
            LeafNode(None, "More text")
        ])
        expected = "<div>Text<p><b>Bold</b></p>More text</div>"
        self.assertEqual(node.to_html(), expected)

    def test_multiple_props(self):
        node = ParentNode("div", [
            LeafNode("p", "Hello")
        ], {
            "class": "container",
            "id": "main",
            "data-test": "true",
            "style": "color: blue"
        })
        expected = "<div class=\"container\" id=\"main\" data-test=\"true\" style=\"color: blue\"><p>Hello</p></div>"
        self.assertEqual(node.to_html(), expected)


        

if __name__ == "__main__":
    unittest.main()