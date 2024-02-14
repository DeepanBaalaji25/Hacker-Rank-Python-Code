if __name__ == '__main__':
    N = int(input())
    l1 = []
    for i in range(N):
        cmd = map(str, input().split())
        cmd_list = list(cmd)
        if cmd_list[0] == 'insert':
            l1.insert(int(cmd_list[1]), int(cmd_list[2]))
        elif cmd_list[0] == 'print':
            print(l1)
        elif cmd_list[0] == 'remove':
            l1.remove(int(cmd_list[1]))
        elif cmd_list[0] == 'append':
            l1.append(int(cmd_list[1]))
        elif cmd_list[0] == 'sort':
            l1.sort()
        elif cmd_list[0] == 'pop':
            l1.pop()
        elif cmd_list[0] == 'reverse':
            l1.reverse()
