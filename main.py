from agents.customer_service import run_customer_service

def chat_loop():
    print("🤖 AI电商客服已启动（输入 退出 结束）")
    history = []
    while True:
        user_msg = input("你：")
        if user_msg in ["退出", "exit", "quit"]:
            print("🤖 感谢咨询，祝您生活愉快！")
            break
        
        reply = run_customer_service(user_msg, history)
        history.append(("user", user_msg))
        history.append(("assistant", reply))
        print(f"🤖 客服：{reply}\n")

if __name__ == "__main__":
    chat_loop()