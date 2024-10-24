import textnode

def main():
    dummy_node = textnode.TextNode("this is a text node", textnode.TextType.BOLD_TEXT, "https://www.boot.dev")
    print(dummy_node)


if __name__ == "__main__":
    main()