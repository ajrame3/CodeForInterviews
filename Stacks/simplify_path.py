# 71
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        path_items = path.split("/")

        for item in path_items:
            if item == "." or not item: # when '//' split we will get empty string, so don't do anything
                continue
            elif item == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        
        return "/" + "/".join(stack)

        