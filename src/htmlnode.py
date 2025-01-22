class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        results = []
        for key, value in self.props.items():
            results.append(f" {key}=\"{value}\"") 
        return "".join(results)
    def __repr__(self):
        return f"""tag: {self.tag}, 
            value: {self.value}, 
            children: {self.children}, 
            props: {self.props}"""

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and 
                self.value == other.value and 
                self.props == other.props and 
                self.children == other.children)
        
    