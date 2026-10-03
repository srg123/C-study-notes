# 八皇后


** ## 题目是什么

国际象棋棋盘 8 行 8 列，放**8 个皇后**。
皇后攻击规则：横向、纵向、两条斜线，都能无限远攻击。
要求：
✅ 一共放 8 个皇后
✅ **任意两个皇后，不能同行、不能同列、不能同斜线**

扩展：N 皇后，就是 N×N 棋盘放 N 个皇后。

## 解题思路（大白话）

核心：**回溯算法**（试探 + 反悔）

1. 一行只放 1 个皇后（直接解决同行问题，不用再判断行），我们一行一行放
2. 到当前行，逐个试每一列：
   - 如果这个位置安全（和前面已经放好的皇后，不同列、不同斜线），就放皇后
   - 然后进入下一行继续放
3. 如果当前行所有列试完都不能放 →**回溯**：回到上一行，把上一行的皇后拿掉，试上一行的下一列
4. 放完 8 行，代表找到 1 组解，记录结果。

> 斜线判断大白话：
> 两个皇后坐标 `(row1,col1)` 和 `(row2,col2)`
> 如果 `abs(row1-row2) == abs(col1-col2)` → 在同一条斜线上，会互相攻击。
 **

```python
def queen(n):
    """
    n皇后，用生成器yield返回每一组解
    :param n: 棋盘大小，八皇后就是n=8
    """
    # queens：列表，下标=行，值=皇后放在第几列
    def backtrack(row, queens):
        if row == n:
            # 全部行放完，找到一组解，yield吐出这组结果
            yield queens
            return
        # 遍历当前行每一列，尝试放皇后
        for col in range(n):
            # 判断col这一列是否安全
            safe = True
            for r, c in enumerate(queens):
                # c==col：同列；abs(r-row)==abs(c-col)同斜线
                if c == col or abs(r-row) == abs(c-col):
                    safe = False
                    break
            if safe:
                # 当前位置安全，放皇后，递归下一行
                yield from backtrack(row + 1, queens + [col])
    # 从第0行开始，已经放的皇后为空列表
    yield from backtrack(0, [])

if __name__ == "__main__":
    # 八皇后 n=8
    result_generator = queen(8)
    count = 0
    # 生成器逐个取出每一种摆放方案
    for solution in result_generator:
        count += 1
        print(f"方案{count}: {solution}")
    print(f"\n八皇后总共有 {count} 种解法")


```

### 用例总结
1. 整体用**生成器**，找到一组解就`yield`吐出，不用一次性算出全部方案存内存。
2. `queens = [1,3,0,2]`这种形式代表：
第 0 行皇后在第 1 列，第 1 行皇后在 3 列……
3. `yield from`：把子生成器产出的数据，继续往外传递。

