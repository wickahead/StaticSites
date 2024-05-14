class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    # def props_to_html(self):
    #     print("inside props_to_html")
    #     str = ""
    #     ctr = 1
    #     for prop in self.props:
    #         # print(f"prop is {prop}") 
    #         print(f"str is {str}") 
    #         str = str + f'"{prop}": "{self.props[prop]}"'
    #         if ctr < len(self.props):
    #             str = str + ", "
    #         ctr +=1
    #     print(f"str is {str}")

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
        else:
            children1 = "'" + self.children + "'"

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

