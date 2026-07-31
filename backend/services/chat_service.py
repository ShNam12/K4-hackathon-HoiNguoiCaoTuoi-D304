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

    model_name = os.environ.get("CHAT_MODEL", "gemini-2.0-flash")
    model = genai.GenerativeModel(
        model_name=model_name,
        system_instruction=(
            "Bạn là VLearn Tutor - một Trợ lý AI hỗ trợ Giảng viên trả lời câu hỏi của sinh viên. "
            "Hãy đóng vai Giảng viên để viết phản hồi mẫu cho sinh viên. "
            "Giọng điệu: Sư phạm, thân thiện, rõ ràng, ngắn gọn và mạch lạc. "
            "Nếu có thông tin ngữ cảnh về chủ đề (Topic), hãy trả lời xoay quanh chủ đề đó."
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
