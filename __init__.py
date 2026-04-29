from config import get_llm, ORDER_AGENT_PROMPT
from tools.order_tools import query_order_by_id, query_logistics
from langchain_core.prompts import ChatPromptTemplate

llm = get_llm()

def run_order_agent(user_input, history):
    prompt = ChatPromptTemplate.from_messages([
        ("system", ORDER_AGENT_PROMPT),
        ("placeholder", "{chat_history}"),
        ("user", "用户输入：{input}，只提取订单号，无则返回空")
    ])
    chain = prompt | llm
    order_id = chain.invoke({
        "chat_history": history,
        "input": user_input
    }).content.strip()

    if not order_id or "DD" not in order_id:
        return "请提供订单号，例如 DD2025001"

    order = query_order_by_id(order_id)
    logistics = query_logistics(order_id)
    res = f"📦 订单 {order_id} 查询结果：\n"

    if "error" in order:
        res += order["error"]
    else:
        res += f"商品：{order['goods']}\n状态：{order['status']}\n时间：{order['create_time']}\n"
        if logistics and "error" not in logistics:
            res += f"物流：{logistics['company']} {logistics['number']}\n{logistics['detail']}"
    return res