from storage import save_data,load_data

DATA_FILE = "todos.json"

def add(tasks,task):
    tasks.append({"task":task,"done":False})
    save_data(DATA_FILE,tasks)
    print("待办已添加")

def show_tasks(tasks):
    count = 0
    if not tasks:
        print("暂无待办")
        return
    for idx, task in enumerate(tasks,1):
        task_task = task.get('task')
        task_done = task.get('done')
        if task_done != False:
            count += 1
        print(f"{idx}. {'[x]'if task_done else'[ ]'} {task_task}")
    print(f"已完成 {count}/{len(tasks)}")

def delete_task(tasks,item):
    try:
        itemNum = int(item)
    except ValueError:
        print("请输入有效数字")
        return
    if itemNum < 1 or itemNum > len(tasks):
        print(f"请输入的序号大于0,小于{len(tasks)+1}")
        return
    tasks.pop(itemNum - 1)
    save_data(DATA_FILE, tasks)
    print(f"已删除第{itemNum}条待办")

def done(tasks,item):
    try:
        itemNum = int(item)
    except ValueError:
        print("请输入有效数字")
        return
    if itemNum < 1 or itemNum > len(tasks):
        print(f"请输入的序号大于0,小于{len(tasks)+1}")
        return
    
    if tasks[itemNum-1]["done"] == True:
        print("该项已标记为完成,请确认")
        return
    else:
        tasks[itemNum-1]["done"] = True
    save_data(DATA_FILE, tasks)


def clear(tasks):
    if not tasks:
        print("暂无待办")
        return
    tasks[:] = [task for task in tasks if not task["done"]]
    save_data(DATA_FILE, tasks)


# 先加载json文件中数据,以防后面被覆写
tasks = load_data(DATA_FILE)
while True:
    cmd = input("请输入:").split()
    if not cmd:
        continue 
    if cmd[0] == "add":
        if len(cmd) < 2:
            print("请输入待办内容!")
            continue
        add(tasks," ".join(cmd[1:]))
    elif cmd[0] == "list":
        if len(cmd) > 1:
            print("请重新输入指令!")
            continue
        show_tasks(tasks)
    elif cmd[0] == "done":
        if len(cmd) < 2:
            print("请重新输入指令!")
            continue
        done(tasks,cmd[1])
    elif cmd[0] == "del":
        if len(cmd) < 2:
            print("请重新输入指令!")
            continue
        delete_task(tasks,cmd[1])
    elif cmd[0] == "q":
        if len(cmd) > 1:
            print("请重新输入指令!")
            continue
        print("程序退出中...")
        break
    elif cmd[0] == "clear":
        if len(cmd) > 1:
            print("请重新输入指令!")
            continue
        clear(tasks)
    else:
        print("系统暂未支持此功能,请您重新确认")
        continue


        
    # print(json.dumps(tasks,ensure_ascii=False))





