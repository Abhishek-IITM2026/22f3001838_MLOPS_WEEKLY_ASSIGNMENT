import re
from datetime import datetime

BLOCKLIST = [
    "ignore previous instructions",
    "system prompt",
    "repeat everything above",
    "print your context",
    "what instructions were you given",
    "you are now",
    "forget your task",
    "act as",
    "jailbreak"
]

VALID_SPECIES = [
    "setosa",
    "versicolor",
    "virginica"
]


def log_event(filename, reason, content):
    with open(filename, "a") as f:
        f.write(
            f"{datetime.now()},{reason},{content}\n"
        )


def input_guardrail(prompt):

    lower = prompt.lower()

    # Rule-based detection
    for phrase in BLOCKLIST:

        if phrase in lower:

            log_event(
                "blocked_inputs.log",
                phrase,
                prompt
            )

            return {
                "blocked": True,
                "reason": phrase
            }

    # Structural validation
    if (
        "sepal_length" not in lower
        and
        "flower specimen" not in lower
    ):

        log_event(
            "blocked_inputs.log",
            "invalid_schema",
            prompt
        )

        return {
            "blocked": True,
            "reason": "invalid_schema"
        }

    return {
        "blocked": False
    }


def output_guardrail(response):

    text = response.lower().strip()

    leakage_terms = [
        "system prompt",
        "training examples",
        "context window",
        "instruction"
    ]

    for term in leakage_terms:

        if term in text:

            log_event(
                "blocked_outputs.log",
                "leakage",
                response
            )

            return "BLOCKED_OUTPUT"

    import re

    for species in VALID_SPECIES:
        if re.search(rf"\b{species}\b", text):
            return species


    log_event(
        "blocked_outputs.log",
        "format_violation",
        response
    )

    return "INVALID_FORMAT"
