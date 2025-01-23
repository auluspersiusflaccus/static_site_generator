from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, "", children, props)
    def to_html(self):
        if not self.tag:
            raise ValueError("missing tag value")
        if not self.children:
            raise ValueError("missing children value")
        parentlist = []
        if self.props == None:
            parentlist.append(f"<{self.tag}>")
        else:
            parentlist.append(f"<{self.tag}{self.props_to_html()}>")
        for child in self.children:
            parentlist.append(child.to_html())
        parentlist.append(f"</{self.tag}>")
        return ''.join(parentlist)
        
"""if __name__ == "__main__":
    # Test LeafNode first
    leaf = LeafNode("b", "Bold")
    print("Leaf node output:", leaf.to_html())
    
    # Then test ParentNode
    node = ParentNode("div", [
        LeafNode("b", "Bold"),
        LeafNode(None, "Text")
    ]) 
    print("Parent node output:", node.to_html())"""