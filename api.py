from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents.data_collector_agent import DataCollectorAgent
from agents.insight_agent import InsightAgent
from agents.idea_generator_agent import IdeaGeneratorAgent

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/")
def root():
    return {"status": "NeoAI backend is running ✅"}

# Input format
class ResearchRequest(BaseModel):
    query: str
    model: str = "llama3-8b-8192"

# Main POST route
@app.post("/generate/")
async def generate_report(form_data: ResearchRequest):
    try:
        collector = DataCollectorAgent()      # API key should be inside class
        insighter = InsightAgent()
        generator = IdeaGeneratorAgent()
        
        docs = collector.fetch_data(form_data.query)
        keywords = insighter.extract_keywords(docs)
        report = generator.generate_report(keywords, model=form_data.model)

        return {"keywords": keywords, "report": report}
    except Exception as e:
        return {"error": str(e), "keywords": [], "report": "Failed to generate report"}

# Run with: uvicorn api:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
print("✅ api.py loaded successfully")
