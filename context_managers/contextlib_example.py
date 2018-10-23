"""Demonstrates uasge of contextmanager from contextlib
"""


from contextlib import contextmanager


class HtmlHelper:

    def __init__(self):
        self.__indent = -1

    @property
    def indent(self):
        return self.__indent

    def indenttabs(self, indent):
        """Returns \t\t... depending upon indent count"""
        tabs = ''
        for _ in range(indent):
            tabs += '\t'
        return tabs

    def printwithindent(self, text, indent, printformat='{}{}'):
        """Prints a formatted string with text and indentation
            Example:
                '{} {}'.format(text, indent)
                where indent is resolved as \t\t... from self.indenttabs(indent)
        """
        if indent == None:
            indent = self.indent + 1
        print(printformat.format(self.indenttabs(indent), text))

    @contextmanager
    def tag(self, tag, indent=0):
        # For each tag __enter__ increase the indentation
        self.__indent += 1
        # Print the opening tag
        self.printwithindent(tag, self.__indent, '{}<{}>')
        # yield the control back for user to print content
        yield
        # Print the closing tag
        self.printwithindent(tag, self.__indent, '{}<\\{}>')
        # On __exit__ decrease the indentation
        self.__indent -= 1


def main():
    # Below code will output
    # <html>
    #         <div>
    #                 <h1>
    #                         Fun with Context Manager
    #                 <\h1>
    #                 <p>
    #                         This is cool
    #                 <\p>
    #         <\div>
    # <\html>
    
    htmlhelper = HtmlHelper()

    # Add level for each nesting of HTML tag
    with htmlhelper.tag('html'):

        with htmlhelper.tag('div'):

            with htmlhelper.tag('h1'):
                htmlhelper.printwithindent('Fun with Context Manager', None)

            with htmlhelper.tag('p'):
                htmlhelper.printwithindent('This is cool', None)

    # The code in tag after yield is executed in reverse to the top


if __name__ == '__main__':
    main()
