class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        # print("inside props_to_html")
        str = ""
        if self.props is None:
            return ""
        for prop in self.props:
            # print(f"prop is {prop}") 
            # print(f"str is {str}") 
            str = str + f' {prop}="{self.props[prop]}"'
        # print(f"final str is {str}")    
        return str


    def __repr__(self):
        if self.tag == None:
            tag1 = "None"
        else:
            tag1 = "'" + self.tag + "'"

        if self.value == None:
            value1 = "None"
        else:
            value1 = "'" + self.value + "'"

        if self.children == None:
            children1 = "None"
        # elif type(self.children) == 
        else:
            # print(f"type(self.children) is {type(self.children)}")
            # print(f"type(self.children) == 'htmlnode.LeafNode' evaluates to {type(self.children) == 'htmlnode.LeafNode'}")
            # print(f"type(self.children) == 'htmlnode.LeafNode' evaluates to {type(self.children) == LeafNode}")
            # print(f"type(self.children) == list evaluates to {type(self.children) == list}")
            # children1 = "'" + self.children + "'"
            children1 = ""

        if self.props == None:
            props1 = "None"
        else:
            # props1 = "'" + self.props + "'"                    
            props1 = "'{"
            for prop in self.props:
                print(f"prop is {prop}")
                props1 = props1 + prop + ": " + self.props[prop] + ", "
            props1 = props1 + "}'"

        return_str = "HTMLNode(tag=" + tag1 + ", value=" + value1 + ", children=" + children1 + ", props=" + props1 + ")"
        # print (return_str)
        return return_str

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        str = ""
        if self.value == None:
            raise ValueError("All leaf nodes require a value.")
        # print(f"self is {self}")
        # str_props = ""
        # for prop in self.props:
        #     str_
        if self.tag is None:
            open_tag = ""
            close_tag = ""
        else:
            open_tag = "<" + self.tag + self.props_to_html() + ">"
            close_tag = "</" + self.tag + ">"

        str = str + open_tag + self.value + close_tag
        # print (f"about to return '{str}'")
        return str

class ParentNode(HTMLNode):
    result_str = ""
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        # print("inside ParentNode.to_html()")
        # print(f"children are {self.children}")
        # print(f"type(self.children) is {type(self.children)}")
        # print(f"type(self.children) == 'htmlnode.LeafNode' evaluates to {type(self.children) == LeafNode}")

        #Need inner recursive loop. Need to set parent tag first, then recurse thru children.
        #Current status is 'inner' text (all but outer tag) is working as expected.

        #base case
        if self.children == None:
            return result_str
        #recursive case
        for child in self.children:
            # print(f"type(child) is {type(child)}")
            # print(f"type(child) == 'htmlnode.LeafNode' evaluates to {type(child) == LeafNode}")
            if type(child) == LeafNode:
                self.result_str = self.result_str + child.to_html()
            elif type(child) == ParentNode:
                return child.to_html() #Hope this is right
        print(f"result_str is {self.result_str}")



    # def to_html(self):
    #     str = ""
    #     if self.tag == None:
    #         raise ValueError("All ParentNode objects require a tag.")

    #     if self.children == None:
    #         raise ValueError("All ParentNode objects require children.")

    #     if self.tag is None:
    #         open_tag = ""
    #         close_tag = ""
    #     else:
    #         open_tag = "<" + self.tag + self.props_to_html() + ">"
    #         close_tag = "</" + self.tag + ">"

    #     str = str + open_tag + self.value + close_tag
    #     # print (f"about to return '{str}'")
    #     return str

