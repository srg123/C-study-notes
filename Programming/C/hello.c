
//----------第一个程序----------

// 说明：main函数注释部分入门，后面多看多写多留意细节

#include <stdio.h> // 引入标准输入输出库

int main()
{ // 主函数，程序入口

    // 打印例子
    printf("Hello, World!\n");
    printf("%d\n", 10);        // 整数
    printf("%f\n", 3.14);      // 浮点
    printf("%.2f\n", 3.14159); // 保留2位小数
    printf("%c\n", 'A');       // 字符
    printf("%s\n", "hello");   // 字符串      //C 语言没有专门的字符串类型

    // 变量使用
    int n;
    scanf("%d", &n); // 注意 & 取地址符

    // -----------------基本数据类型

    //  类型	     说明	       示例
    //  int	     整数	      int a = 10;
    //  float	  单精度浮点	float f = 3.14f;
    //  double	 双精度浮点	   double d = 314159;
    //  char	     单个字符	   char c = 'A';
    //  void	     无类型	       函数无返回值时用
    //  修饰符：short、long、signed、unsigned

    // -----------------变量与常量

    //  int x = 5;              // 变量
    //  const int MAX = 100;    // 常量（不可修改）
    //  #define PI 3.14159      // 宏定义常量

    // -----------------运算符

    //   +  -  *  /  %      // 算术（% 取余，仅整数）
    //  == != >  < >= <=   // 比较
    //  && || !            // 逻辑
    //  = += -= *= /=      // 赋值
    //  ++ --              // 自增自减
    // 注意：整数相除会截断，5 / 2 == 2。要得到小数需 5.0 / 2。

    // -----------------流程控制

    //      if (score >= 90) {
    //      printf("优秀\n");
    //  } else if (score >= 60) {
    //      printf("及格\n");
    //  } else {
    //      printf("不及格\n");
    //  }

    // switch (day) {
    // case 1: printf("周一"); break;
    // case 2: printf("周二"); break;
    // default: printf("其他");

    // for (int i = 0; i < 10; i++) {
    // printf("%d ", i);
    // }
    //}

    //     int i = 0;
    // while (i < 5) { printf("%d", i); i++; }

    // do {
    //     printf("%d", i);
    //     i++;
    // } while (i < 5);   // 至少执行一次

    // break / continue
    // break：跳出循环
    // continue：跳过本次，进入下一次

    //-----------------数组

    //     int arr[5] = {1, 2, 3, 4, 5};
    // int arr2[] = {1, 2, 3};        // 自动推断长度
    // int arr3[5] = {0};             // 全部初始化为 0

    // 遍历
    // for (int i = 0; i < 5; i++) {
    //     printf("%d ", arr[i]);
    // }

    // 二维数组
    // int matrix[2][3] = {{1,2,3}, {4,5,6}};
    // C 语言数组不检查越界，务必自己保证下标合法。

    //-----------------字符串

    // C 语言没有专门的字符串类型，用 char 数组表示，以 '\0' 结尾。
    //  #include <string.h>

    // char str1[] = "hello";       // 自动加 '\0'
    // char str2[20];

    // strcpy(str2, str1);          // 复制
    // strcat(str2, " world");      // 拼接
    // int len = strlen(str1);      // 长度（不含 '\0'）
    // int cmp = strcmp(str1, str2); // 比较，0 表示相等

    //-----------------函数

    // 声明（原型）
    // int add(int a, int b);

    // 定义
    // int add(int a, int b) {
    //     return a + b;
    // }

    // int main() {
    //     int sum = add(3, 5);
    //     printf("%d\n", sum);
    //     return 0;
    // }

    // 递归示例：
    //  int factorial(int n) {
    //      if (n <= 1) return 1;
    //      return n * factorial(n - 1);
    //  }

    //-----------------指针     （重点*代表指针，&代表地址）
    // 指针存的是内存地址。

    // int a = 10;
    // int *p = &a;      // p 指向 a 的地址

    // printf("%d\n", *p);   // 10，解引用
    // *p = 20;              // 通过指针修改 a
    // printf("%d\n", a);    // 20

    // 指针与数组
    //  int arr[3] = {1, 2, 3};
    //  int *p = arr;         // 数组名即首地址
    //  printf("%d", *(p + 1)); // 2
    //  printf("%d", p[1]);     // 2，等价写法

    // 函数传参（交换两数）：
    //  void swap(int *a, int *b) {
    //      int t = *a;
    //      *a = *b;
    //      *b = t;
    //  }

    // int main() {
    //     int x = 1, y = 2;
    //     swap(&x, &y);   // 传地址
    //     printf("%d %d\n", x, y);  // 2 1
    // }

    //-----------------结构体

    // struct Student {
    //     char name[20];
    //     int age;
    //     float score;
    // };

    // int main() {
    //     struct Student s = {"Tom", 18, 95.5};
    //     printf("%s %d %.1f\n", s.name, s.age, s.score);

    //     struct Student *p = &s;
    //     printf("%s\n", p->name);   // 指针用 ->
    //     return 0;
    // }

    // typedef 简化：
    //  typedef struct {
    //      int x, y;
    //  } Point;

    // Point p = {1, 2};

    //-----------------动态内存

    // #include <stdlib.h>

    // int *arr = (int*)malloc(5 * sizeof(int));  // 分配
    // if (arr == NULL) return -1;                // 检查

    // for (int i = 0; i < 5; i++) arr[i] = i;

    // free(arr);      // 释放，必须！
    // arr = NULL;     // 避免野指针

    // malloc：分配但不初始化

    // calloc：分配并清零

    // realloc：调整大小

    //-----------------文件操作

    // #include <stdio.h>

    // 写文件
    // FILE *fp = fopen("test.txt", "w");
    // fprintf(fp, "hello %d\n", 123);
    // fclose(fp);

    // 读文件
    // fp = fopen("test.txt", "r");
    // char buf[100];
    // while (fgets(buf, sizeof(buf), fp)) {
    //     printf("%s", buf);
    // }
    // fclose(fp);

    // 模式：r 读、w 写（覆盖）、a 追加、rb/wb 二进制

    // -----------------常见坑
    // 忘记分号 ;

    // scanf 忘记 &

    // 数组越界不报错但会崩溃

    // 字符串不能用 == 比较，要用 strcmp

    // malloc 后忘记 free → 内存泄漏

    // 局部变量未初始化值随机

    // printf 与 scanf 格式符不匹配

    //----------------学习路线建议
    // 基础语法（本文档）→ 刷题巩固（洛谷、LeetCode C）

    // 指针与内存 → 手写链表、栈、队列

    // 文件与结构体 → 做小项目（学生管理系统、通讯录）

    // 进阶：多文件编译、Makefile、gdb 调试、valgrind 查内存

    return 0; // 返回 0 表示正常结束
}