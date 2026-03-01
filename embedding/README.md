# Embeddings

This folder stores the vector embeddings used for retrieval in the Radiology RAG Copilot system.

The embeddings are generated from both image and text modalities.

## Types of embeddings

### Image Embeddings
Generated using a CLIP image encoder from chest X-ray images.

Example file:

```
image_embeddings_2696.npy
```

Each image is converted into a **512-dimensional vector representation**.

---

### Text Embeddings
Generated from the radiology report impressions using the CLIP text encoder.

These embeddings represent the semantic meaning of the report.

---

### Multimodal Fusion Embeddings

Image and text embeddings are combined using weighted fusion.

```
fused_embedding = α * image_embedding + (1-α) * text_embedding
```

Best performing value:

```
α = 0.5
```

Example file:

```
fused_embeddings_alpha_0.5.npy
```

---

## Why embeddings are not included

The embedding files are large and therefore not stored in the repository.

They can be regenerated using the notebooks in:

```
Notebook/
```

Relevant notebooks:

```
day3_image_embeddings.ipynb
day4_multimodal_fusion.ipynb
```
