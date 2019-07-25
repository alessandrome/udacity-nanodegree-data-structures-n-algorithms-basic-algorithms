# The Router class will wrap the Trie and handle
class RouterNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = {}

    def insert(self, listed_path, handler):
        self._insert_help(listed_path, handler)

    def _insert_help(self, listed_path, handler):
        if not listed_path:
            return
        partial_path = listed_path[0]
        child = None
        if partial_path in self.children:
            child = self.children[partial_path]
        if child:
            return child._insert_help(listed_path[1:], handler)
        child = RouterNode() if len(listed_path) > 1 else RouterNode(handler)
        self.children[partial_path] = child
        child._insert_help(listed_path[1:], handler)

    def get_handler(self):
        return self.handler

    def __repr__(self):
        return '{{hanlder: '+str(self.handler)+', chldren: '+str(list(self.children.items()))+'}}'


class Router:
    def __init__(self, root_handler, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root_node = RouterNode(root_handler)
        self.not_found_node = RouterNode(not_found_handler)

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        splitted_path = self.split_path(path)
        self.root_node.insert(splitted_path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        splitted_path = self.split_path(path)
        node = self.root_node
        if not splitted_path:
            handler = node.get_handler()
            if not handler:
                handler = self.not_found_handling()
            return handler
        string = ''
        for partial_path in splitted_path:
            if partial_path in node.children:
                node = node.children[partial_path]
            else:
                return self.not_found_handling()
        return node.get_handler() or self.not_found_handling()

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        splitted_path = path.split('/')
        if splitted_path[0] == '':
            splitted_path = splitted_path[1:]
        if splitted_path and splitted_path[-1] == '':
            splitted_path = splitted_path[:-1]
        return splitted_path

    def not_found_handling(self):
        return self.not_found_node.get_handler()


print("ROUTING WITH MISSING HANDLING")
# create the router and add a route
router = Router("root handler",
                "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler'
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup(
    "/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup(""))  # should print 'root handler' as it is another form of '/'


print()
print("ROUTING WITHOUT MISSING HANDLING")
# create the router that not manage 'not found' cases
not_found_router = Router("root handler")  # remove the 'not found handler' if you did not implement this
not_found_router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(not_found_router.lookup("/"))  # should print 'root handler'
print(not_found_router.lookup("/you/cant/see/me"))  # should print None
