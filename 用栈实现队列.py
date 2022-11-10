class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        # 有新元素进来，就往in里面push
        self.stack_in.append(x)

    def pop(self) -> int:
        # 从队列前面移除元素并返回该元素
        if self.empty():
            return None

        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        # 获取前面的元素
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        # 只要in或者out有元素，说明队列不为空
        return not (self.stack_in or self.stack_out)


# Your MyQueue object will be instantiated and called as such:
x = 1
obj = MyQueue()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
