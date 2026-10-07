# todo-cli
一个跑在终端里的轻量待办工具，可直接在终端添加、查看、标记完成、删除待办任务，数据自动持久化保存。

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
请输入:add 学习git分支重命名
待办已添加
请输入:add 部署code-server
待办已添加
请输入:list
1. [ ] 学习git分支重命名
2. [ ] 部署code-server
已完成 0/2
请输入:done 1
已标记第 1 条完成
请输入:list
1. [x] 学习git分支重命名
2. [ ] 部署code-server
已完成 1/2
请输入:clear
请输入:list
1. [ ] 部署code-server
已完成 0/1
请输入:q
程序退出中...
```
123jhagsdjgasjdgajhsgdjha