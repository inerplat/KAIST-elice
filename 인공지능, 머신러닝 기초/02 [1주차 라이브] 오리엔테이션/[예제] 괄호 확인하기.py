def main():
    tc = int(input("testcases > "))
    for i in range(tc):
        text = input("text > ")
        if check_parenthesis(text) == True:
            print("통과")
        else:
            print("거부")

def check_parenthesis(text):

    stack = []
    level = 3
    for now in text:
        if now=='[':
            if level>=3:
                stack.append('[')
                level=3
            else:
                return False
        elif now=='{':
            if level>=2:
                stack.append('{')
                level=2
            else:
                return False
        elif now=='(':
            if level>=1:
                stack.append('(')
                level=1
            else:
                return False
        elif len(stack):
            if now==')':
                nownow=stack.pop()
                if nownow != '(':
                    return False
            elif now=='}':
                nownow=stack.pop()
                if nownow != '{':
                    return False
            elif now==']':
                nownow=stack.pop()
                if nownow != '[':
                    return False
            if len(stack):
                prev=stack.pop()
                if prev=='(':
                    level=1
                elif prev=='{':
                    level=2
                elif prev=='[':
                    level=3
                stack.append(prev)
        else:
            return False
    if len(stack):
        return False
    return True

if __name__ == "__main__":
    main()
