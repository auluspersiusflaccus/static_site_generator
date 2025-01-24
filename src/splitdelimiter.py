from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_of_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            # Check for unmatched delimiters
            if len(parts) % 2 == 0:
                raise ValueError("Unmatched delimiter")
            for i, part in enumerate(parts):
                if part:
                    if i % 2 == 0:
                        list_of_nodes.append(TextNode(parts[i], TextType.TEXT))
                    else:
                        list_of_nodes.append(TextNode(parts[i], text_type))
        else:
            list_of_nodes.append(node)
    return list_of_nodes