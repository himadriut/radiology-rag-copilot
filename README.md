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
