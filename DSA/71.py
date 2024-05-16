'''
Example 1:

Input: path = "/home/"

Output: "/home"

Explanation:

The trailing slash should be removed.

 
Example 2:

Input: path = "/home//foo/"

Output: "/home/foo"

Explanation:

Multiple consecutive slashes are replaced by a single one.

Example 3:

Input: path = "/home/user/Documents/../Pictures"

Output: "/home/user/Pictures"

Explanation:

A double period ".." refers to the directory up a level.

Example 4:

Input: path = "/../"

Output: "/"

Explanation:

Going one level up from the root directory is not possible.

Example 5:

Input: path = "/.../a/../b/c/../d/./"

Output: "/.../b/d"


To solve this problem we can easy solve by below steps
1:fristly split the path by '/' it gives us list items exculding / in the path
2:iterate the components list anf appy two condition
frist on =e if the component is '..' it means we need to go one directory backward so will pop the last item in the list
second one if the component is exits and component is not equal to '.' it means we need to add the item into list so will append the item into the list
finally we join the path by using join method of list and return the soecified_path string
'''


class Solution(object):
    def simplifyPath(self, path):
        components = path.split('/')
        specified_components = []
        for component in components:
            if component == '..':
                if specified_components:
                    specified_components.pop()
            elif component and component != '.':
                specified_components.append(component)
        
        specified_path = '/' + '/'.join(specified_components)
        return specified_path
