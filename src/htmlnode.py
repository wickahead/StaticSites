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
        else:
            # for child in self.children:
            #     print(f"type(child) is {type(child)}")
            #     print(f"type(child) == LeafNode evaluates to {type(child) == LeafNode}")
            #     print(f"type(child) == ParentNode evaluates to {type(child) == ParentNode}")
            #     print(f"type(child) == list evaluates to {type(child) == list}")
            #     # children1 = "'" + self.children + "'"
            #     children1 = ""
            children1 = "Check input! There are children in LeafNode object, and there should be none."

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

    def to_html(self):
        # print("inside LeafNode.to_html()")
        str = ""
        if self.value == None:
            raise ValueError("All leaf nodes require a value.")
        if self.children is not None:
            raise ValueError("LeafNode objects cannot have children.")
       
        if self.tag is None:
            open_tag = ""
            close_tag = ""
        else:
            open_tag = "<" + self.tag + self.props_to_html() + ">"
            close_tag = "</" + self.tag + ">"

        str = str + open_tag + self.value + close_tag
        # print (f"LeafNode.to_html() about to return '{str}'")
        return str


class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        children1 = ""
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
        else:
            for child in self.children:
                children1 = children1 + repr(child)

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


    #TODO - fix when children are ParentNode types (the result_str needs to be 'reset' for recursive parent nodes.)
    def to_html(self):
        def __inner_to_html(self, result_str=""):
            #base case
            if self.children == None:
                return result_str #Might need to change to ""
            #recursive case
            for child in self.children:
                
                result_str = result_str + child.to_html()
            return result_str

        if self.tag is None:
            raise ValueError("Tag cannot be empty.")
        if self.children is None:
            raise ValueError("ParentNode objects must have children.")
        result_str = f"<{self.tag}>"  #start tag
        result_str = result_str + __inner_to_html(self)
        result_str = result_str + f"</{self.tag}>" #end tag
        return result_str
