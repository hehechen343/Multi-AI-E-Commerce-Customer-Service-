from config import get_llm, AFTER_SALE_PROMPT
from tools.after_sale_tools import create_refund_order
from langchain_core.prompts import ChatPromptTemplate

llm = get_llm()

def run_after_sale_agent(user_input, history):
    prompt = ChatPromptTemplate.from_messages([
        ("system", AFTER_SALE_PROMPT),
        ("placeholder", "{chat_history}"),
        ("user", "输入：{input}，提取订单号、原因、是否退货")
    ])
    chain = prompt | llm
    resp = chain.invoke({"chat_history": history, "input": user_input}).content

    order_id = ""
    for w in resp.split():
        if w.startswith("DD"):
            order_id = w

    if not order_id:
        return "请告诉我要退款的订单号~"

    result = create_refund_order(order_id, "七天无理由", need_return=True)
    if result.get("success"):
        return f"✅ {result['msg']}"
    else:
        return f"❌ {result.get('error', '退款失败')}"