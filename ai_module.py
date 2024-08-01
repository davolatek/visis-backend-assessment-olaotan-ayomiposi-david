from transformers import pipeline

# Load pre-trained summarization model from Hugging Face
summarizer = pipeline("summarization", model="t5-small")


def generate_summary_from_text(
    text: str, max_length: int = 150, min_length: int = 30
) -> str:
    # Generate summary using the AI model
    # Optionally, handle large texts by chunking
    chunk_size = 512  # This may vary depending on the model's max input length
    text_chunks = [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]

    summaries = []
    for chunk in text_chunks:
        summary = summarizer(
            chunk, max_length=max_length, min_length=min_length, do_sample=False
        )
        summaries.append(summary[0]["summary_text"])

    # Join all the chunk summaries
    full_summary = " ".join(summaries)
    return full_summary
