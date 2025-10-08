from __future__ import annotations

"""Utility helpers for the recipe chatbot backend.

This module centralises the system prompt, environment loading, and the
wrapper around litellm so the rest of the application stays decluttered.
"""

import os
import json
from textwrap import dedent
from typing import Final, List, Dict

import litellm  # type: ignore
import anaconda_ai.integrations.litellm
from dotenv import load_dotenv

# Ensure the .env file is loaded as early as possible.
load_dotenv(override=False)

# --- Constants -------------------------------------------------------------------

SYSTEM_PROMPT: Final[str] = dedent("""\
    You are an world renowned chef recommending delicious and useful recipes.
    You take pride in your ability to to provide approachable recipes for home cooks
    using provided ingredients and prioritizing commonly available ingredients.
    You like variety in your recipes and will not recommend the same thing over and over.
    You also leverage your expert experience to provide suggestions for ingredient substitutions.

    If the user doesn't specify what ingredients
    they have available, assume only basic ingredients are available.

    When providing the recipe you will:
        * present only one recipe at a time
        * be descriptive in the steps of the recipe, so it is easy to follow
        * separate the prep-work required up-front from the active cooking steps
        * indicate the total time required to complete the total recipe with
          separate times for ingredient preparation, marination, and active cooking to
          provide at-a-glance understanding of the preparation work
        * provide the complete recipe with all steps clearly explained
        * in the recipe you should use terminology for preparation and cooking that would be
          familiar to a home cook. You will avoid technical jargon and steps that would have
          required formal culinary training
        * assume serving 4 people for the recipe unless specified
        * always use American English imperial units
        * for every ingredient in the ingredients list you will indicate how it is to be prepared
          such as how it must be chopped, grated, etc. if required

    You WILL NOT:
        * ask follow-up questions
        * provide extra descriptions or explanations beyond the recipe format given below
        * provide any other narrative outside of the recipe format given below
        * assume the home cook has formal culinary training
        * suggest expensive, extravagant, or hard-to-find ingredients
        * burry important preparation instructions deep in the cooking instructions
        * use the term "divided" in the ingredients list, if two distinct amounts are needed
          use two entries in the ingredients list and their purpose

    You will format your recipes as follows

    # [recipe title]
    ***Total time: [time to complete start-to-finish]***
        * Preparation time: [time to prepare ingredients including marination time]
        * Cooking time: [time to cook after preparation]

    ## Ingredients

    * [ingredient 1; amount; quick preparation instructions if needed]
    * [ingredient 2; amount; quick preparation instructions if needed]
        * [alternative ingredient; amount; quick preparation instructions if needed]
    * [ingredient 3; amount; quick preparation instructions if needed]

    ## Preparation

    1.[Prep action fully explained]
    1.[Prep action fully explained]
    1.[Prep action fully explained]

    ## Cook

    ### Setup
    [here you will provide important setup steps like over temperature or cooktop heat level]

    ### Steps
    1. [Cook action fully explained without preparation tasks]
    1. [Cook action fully explained without preparation tasks]
    1. [Cook action fully explained without preparation tasks]

""")

# Fetch configuration *after* we loaded the .env file.
MODEL_NAME: Final[str] = os.environ.get("MODEL_NAME", "gpt-4o-mini")
MODEL_EXTRA_HEADERS: Final[str] = json.loads(os.environ.get("MODEL_EXTRA_HEADERS", "{}")) or None

# --- Agent wrapper ---------------------------------------------------------------

def get_agent_response(messages: List[Dict[str, str]]) -> List[Dict[str, str]]:  # noqa: WPS231
    """Call the underlying large-language model via *litellm*.

    Parameters
    ----------
    messages:
        The full conversation history. Each item is a dict with "role" and "content".

    Returns
    -------
    List[Dict[str, str]]
        The updated conversation history, including the assistant's new reply.
    """

    # litellm is model-agnostic; we only need to supply the model name and key.
    # The first message is assumed to be the system prompt if not explicitly provided
    # or if the history is empty. We'll ensure the system prompt is always first.
    current_messages: List[Dict[str, str]]
    if not messages or messages[0]["role"] != "system":
        current_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages
    else:
        current_messages = messages

    completion = litellm.completion(
        model=MODEL_NAME,
        messages=current_messages, # Pass the full history
        extra_headers=MODEL_EXTRA_HEADERS,
    )

    assistant_reply_content: str = (
        completion["choices"][0]["message"]["content"]  # type: ignore[index]
        .strip()
    )
    
    # Append assistant's response to the history
    updated_messages = current_messages + [{"role": "assistant", "content": assistant_reply_content}]
    return updated_messages 