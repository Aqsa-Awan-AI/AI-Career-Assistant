import os
from google import genai


# Models tried in order — if one fails (retired, rate-limited, etc.),
# the next one is automatically tried instead of crashing the app.
MODEL_FALLBACK_CHAIN = [
    "gemini-flash-latest",   # auto-updates to newest Flash model, always current
    "gemini-3.6-flash",      # current stable model (as of mid-2026)
    "gemini-2.5-flash",      # older stable, kept as a last-resort fallback
]


def generate_with_fallback(prompt):
    """
    Tries each model in MODEL_FALLBACK_CHAIN in order.
    Returns the response text from the first one that works.
    Raises the last error only if ALL models fail.
    """

    client = genai.Client(
        api_key=os.getenv("GEMINI_API_KEY")
    )

    last_error = None

    for model_name in MODEL_FALLBACK_CHAIN:

        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            return response.text

        except Exception as e:
            last_error = e
            continue

    raise last_error