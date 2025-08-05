import groq

class IdeaGeneratorAgent:
    def __init__(self, api_key=None):
        # Replace with your real Groq API key or set via env variable
        api_key = api_key or "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"
        self.client = groq.Groq(api_key=api_key)

    def generate_report(self, keywords, model="llama3-8b-8192"):
        keyword_str = ", ".join([kw for kw, _ in keywords])
        prompt = f"""
Using the following trending topics in AI:
{keyword_str}

Suggest 3 innovative research directions.

Respond in **Markdown** with headings, justification, and clarity.
"""

        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=600
            )
            return response.choices[0].message.content
        except Exception as e:
            print("❌ Error in IdeaGeneratorAgent:", e)
            return "⚠️ Failed to generate report."
