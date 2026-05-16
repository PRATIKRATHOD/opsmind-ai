import ollama


def generate_retrieval_query(incident):

    prompt = f"""
    Convert this production incident into an optimized
    semantic troubleshooting search query.

    Incident:
    Application: {incident["application"]}
    Issue: {incident["issue"]}

    Return ONLY the optimized search query.
    """

    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    query = response["message"]["content"]

    print(f"Optimized Retrieval Query: {query}")

    return query