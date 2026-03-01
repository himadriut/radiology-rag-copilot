# radiology-rag-copilot
Multimodal Retrieval-Augmented Generation for radiology report assistance using MIMIC-CXR
## System Architecture (High Level)

```text
Chest X-ray Image
        │
        ▼
CLIP Image Encoder
        │
        ▼
Image Embedding (512D)
        │
        │
Radiology Report ──► CLIP Text Encoder
        │
        ▼
Text Embedding (512D)
        │
        ▼
Multimodal Fusion (α-weighted)
        │
        ▼
FAISS Vector Index
        │
        ▼
Top-K Similar Studies
        │
        ▼
Retrieval-Augmented Generation
        │
        ▼
Draft Radiology Impression
        │
        ▼
Confidence Gate (anti-hallucination)
## Experiment Results

Retrieval performance comparison:

| Method | Recall@5 |
|------|------|
| Image only | 0.68 |
| Multimodal fusion | 0.973 |

The results show that combining image and text embeddings significantly improves retrieval performance for radiology studies.
## Quickstart

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the API

```bash
uvicorn api.app:app --host 0.0.0.0 --port 8000 --reload
```

### Test the API

```bash
curl -X POST http://localhost:8000/predict \
-F "file=@test.jpg"
```

Example response:

```json
{
  "status": "generated",
  "confidence": 0.98,
  "draft": "IMPRESSION: Mild left basal atelectasis.",
  "retrieved_cases": []
}
```
