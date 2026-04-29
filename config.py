from langchain_openai import ChatOpenAI

# 请在这里填入你的API信息
LLM_API_KEY = "你的API密钥"
LLM_BASE_URL = "https://api.deepseek.com/v1"
LLM_MODEL_NAME = "deepseek-chat"

def get_llm():
    return ChatOpenAI(
        api_key=LLM_API_KEY,
        base_url=LLM_BASE_URL,
        model=LLM_MODEL_NAME,
        temperature=0.1,
        max_tokens=1024
    )

# 提示词
CUSTOMER_SERVICE_PROMPT = """
你是专业电商智能客服，负责接待用户、识别意图、分配任务。
要求：礼貌、简洁、记住上下文、不编造信息。
"""

ORDER_AGENT_PROMPT = "你是订单查询专员，负责查询订单和物流。"
AFTER_SALE_PROMPT = "你是售后审核专员，处理退货退款，自动审核订单。"