import os
from dotenv import load_dotenv

load_dotenv()


def get_chat_response(message: str, context: str | None = None, topic_title: str | None = None) -> str:
    try:
        from openai import OpenAI
    except ImportError:
        return "Error: Missing 'openai' package"

    api_key = os.environ.get("LLM_API_KEY") or os.environ.get("OPENROUTER_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return "Error: Missing API key. Please set LLM_API_KEY, OPENROUTER_API_KEY or OPENAI_API_KEY."

    base_url = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
    model = os.environ.get("CHAT_MODEL", "openai/gpt-4o-mini")
    client = OpenAI(api_key=api_key, base_url=base_url)

    system_prompt = (
        "Bạn là VLearn Tutor - một Trợ lý AI hỗ trợ Giảng viên trả lời câu hỏi của sinh viên. "
        "Hãy đóng vai Giảng viên để viết phản hồi mẫu cho sinh viên. "
        "Giọng điệu: Sư phạm, thân thiện, rõ ràng, ngắn gọn và mạch lạc. "
        "Nếu có thông tin ngữ cảnh về chủ đề (Topic), hãy trả lời xoay quanh chủ đề đó."
    )

    user_prompt = f"Tin nhắn từ Giảng viên/Yêu cầu: {message}"
    if topic_title:
        user_prompt += f"\nNgữ cảnh Chủ đề (Topic): {topic_title}"
    if context:
        user_prompt += f"\nChi tiết nội dung/Câu hỏi sinh viên: {context}"

    try:
        resp = client.chat.completions.create(
            model=model,
            temperature=0.7,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )
        return resp.choices[0].message.content or ""
    except Exception as exc:
        return f"Error calling LLM: {exc}"
