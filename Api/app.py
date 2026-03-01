from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Radiology RAG Copilot API running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Placeholder prediction
    return {
        "status": "generated",
        "confidence": 0.98,
        "draft": "IMPRESSION: Mild left basal atelectasis.",
        "retrieved_cases": []
    }
