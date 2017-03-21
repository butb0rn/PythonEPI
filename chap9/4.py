def simplifyPath(path):
    stack = []
    for p in path.split("/"):
      if p == ".." and stack:
          stack.pop()
      elif p and p != '.':
        stack.append(p)
    return "/" + "/".join(stack)


print simplifyPath("../Users/././ehsan/Code/../pythonEpi/chap13/..")
