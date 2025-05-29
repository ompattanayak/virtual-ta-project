import json
import base64
from typing import List, Tuple
from difflib import get_close_matches

# Load Discourse + Course Content
with open("discourse.json", "r", encoding="utf-8") as f:
    discourse_posts = json.load(f)

with open("course_content.json", "r", encoding="utf-8") as f:
    course_pages = json.load(f)

def search_data(question: str) -> Tuple[str, List[dict]]:
    matches = []

    def search_in(data, key):
        for item in data:
            if question.lower() in item[key].lower():
                matches.append(item)

    search_in(discourse_posts, "content")
    search_in(course_pages, "content")

    # If nothing exact, use fuzzy matching
    if not matches:
        corpus = [item["content"] for item in discourse_posts + course_pages]
        best = get_close_matches(question, corpus, n=3, cutoff=0.3)
        for b in best:
            for item in discourse_posts + course_pages:
                if b in item["content"]:
                    matches.append(item)
                    break

    answer = "This might help you with your question:"
    links = []

    for m in matches[:2]:
        links.append({
            "url": m.get("url", "#"),
            "text": m.get("content", "")[:150] + "..."
        })

    if not links:
        answer = "Sorry, I couldn't find a relevant answer. Try rephrasing your question."

    return answer, links
