import os
from dotenv import load_dotenv

load_dotenv()


def get_chat_response(message: str, context: str | None = None, topic_title: str | None = None) -> str:
    try:
        import google.generativeai as genai
    except ImportError:
        return "Error: Missing 'google-generativeai' package — run: pip install google-generativeai"

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "Error: Missing GEMINI_API_KEY in .env"

    genai.configure(api_key=api_key)

    model_name = os.environ.get("CHAT_MODEL", "gemini-2.5-flash")
    model = genai.GenerativeModel(
        model_name=model_name,
        system_instruction=(
            "Bạn là VLearn Assistant - một Trợ lý AI đắc lực dành riêng cho Giảng viên. "
            "Người đang trò chuyện với bạn là Giảng viên, KHÔNG PHẢI là sinh viên. "
            "Nhiệm vụ của bạn là hỗ trợ Giảng viên phân tích, tổng hợp câu hỏi, và soạn thảo câu trả lời mẫu khi được yêu cầu. "
            "Hãy xưng hô tôn trọng là 'Thầy/Cô' và xưng là 'Tôi' hoặc 'Trợ lý'. Luôn tuân thủ nghiêm ngặt các chỉ thị và cung cấp thông tin chính xác, súc tích."
        ),
    )

    user_prompt = f"Tin nhắn từ Giảng viên/Yêu cầu: {message}"
    if topic_title:
        user_prompt += f"\nNgữ cảnh Chủ đề (Topic): {topic_title}"
    if context:
        user_prompt += f"\nChi tiết nội dung/Câu hỏi sinh viên: {context}"

    try:
        resp = model.generate_content(user_prompt)
        return resp.text or ""
    except Exception as exc:
        return f"Error calling Gemini: {exc}"
