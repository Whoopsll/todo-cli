import json

def load_data(path):
    """读取 JSON 文件,文件不存在时范围空列表"""
    try:
        with open(path,"r",encoding="utf-8")as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(path,data):
    """把数据写入 JSON 文件"""
    with open(path,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)

if __name__ == "__main__":
    print("test")