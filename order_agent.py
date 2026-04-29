from config import get_llm, CUSTOMER_SERVICE_PROMPT
from agents.order_agent import run_order_agent
from agents.after_sale_agent import run_after_sale_agent
from langchain_core.prompts import ChatPromptTemplate

llm = get_llm()

def route_intent(user_input):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "只返回：订单查询/物流查询/退货退款/客服咨询/其他"),
        ("user", "{input}")
    ])
    chain = prompt | llm
    return chain.invoke({"input": user_input}).content.strip()

def run_customer_service(user_input, history):
    intent = route_intent(user_input)
    
    if "订单" in intent or "物流" in intent:
        return run_order_agent(user_input, history)
    elif "退货" in intent or "退款" in intent or "售后" in intent:
        return run_after_sale_agent(user_input, history)
    else:
        prompt = ChatPromptTemplate.from_messages([
            ("system", CUSTOMER_SERVICE_PROMPT),
            ("placeholder", "{chat_history}"),
            ("user", "{input}")
        ])
        chain = prompt | llm
        return chain.invoke({
            "chat_history": history,
            "input": user_input
        }).content