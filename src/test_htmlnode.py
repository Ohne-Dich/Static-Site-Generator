import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_not_eq(self):
        node = HTMLNode("This is a text node")
        node2 = HTMLNode("This is a text node", "2")
        self.assertNotEqual(node, node2) 

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            None,
            "What a strange world",
            "some",
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode (tag=None, value=What a strange world, children=some, props={'class': 'primary'})"
        )


if __name__ == "__main__":
    unittest.main()           

