# todo-cli
一个简单的终端待办工具，靠识别首单词执行对应操作，用来管理待办任务。

## 运行方法
需要 Python 3.10 以上。
```bash
# 创建虚拟环境（可选）
python3 -m venv .venv
source .venv/bin/activate

# 启动程序
python todo.py
```

## 命令
- `add 内容`：添加一条待办任务
- `list`：列出全部任务
- `done 序号`：将指定序号任务标记为已完成
- `del 序号`：删除指定序号任务
- `clear`：批量删除所有已完成任务
- `q`：退出程序

## 数据存储
任务持久化保存在 `todos.json`，程序下次启动会自动读取。

## 使用示例
```
$ python todo.py
请输入:待办已添加
请输入:待办已添加
请输入:1. [ ] 学习git分支重命名
2. [ ] 部署code-server
已完成 0/2
请输入:请输入:1. [x] 学习git分支重命名
2. [ ] 部署code-server
已完成 1/2
请输入:请输入:1. [ ] 部署code-server
已完成 0/1
请输入:程序退出中...
```