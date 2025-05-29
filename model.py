# model.py
def generate_answer(question):
    # Simplified version
    # In actual: Search from Discourse/course DB + use GPT
    if "tokenizer" in question.lower():
        answer = "Use a tokenizer like tiktoken to count tokens..."
        links = [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/t/ga5-question-8-clarification/155939/3",
                "text": "Discussion on token counting"
            }
        ]
    else:
        answer = "This question has not been answered yet."
        links = []
    return answer, links
