import json
import os
from typing import Final
from textwrap import dedent
import pandas as pd
from random import choice
from tqdm import tqdm
import subprocess

import litellm  # type: ignore
import anaconda_ai.integrations.litellm

from dotenv import load_dotenv

# Ensure the .env file is loaded as early as possible.
load_dotenv(override=False)
# Fetch configuration *after* we loaded the .env file.
MODEL_NAME: Final[str] = os.environ.get("MODEL_NAME", "gpt-4o-mini")
MODEL_EXTRA_HEADERS: Final[str] = json.loads(os.environ.get("MODEL_EXTRA_HEADERS", "{}")) or None


dimensions = {
    "number_serving": lambda: choice([2, 6, 8]),
    "meal": lambda: choice(["breakfast", "lunch", "dinner"]),
    "dietary_restrictions": lambda: choice(["None", "eggs", "dairy", "gluten"]),
    "required_ingredients": lambda: choice(["None", "chicken", "beans", "pork", "beef"]),
    "total_time": lambda: choice([10, 30, 60, 120])
}

query_template = dedent("""\
    You are a prompt generator for error analysis of a recipe chatbot.
    You will be given the dimensions and values over which to generate the request for a recipe.
    You will return the prompt as a user of the recipe chatbot would write and nothing more.
    Here are the dimensions and values:
    {dims}
""")

tuples = []
for _ in tqdm(range(20)):
    data = {}
    for dim, sampler in dimensions.items():
        data[dim] = sampler()

    dims = "\n".join(f" - {k}: {v}" for k, v in data.items())
    query = query_template.format(dims=dims)
    completion = litellm.completion(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": query}],
        extra_headers=MODEL_EXTRA_HEADERS,
    )
    prompt = completion["choices"][0]["message"]["content"].strip()

    data["query_input"] = query
    data["query"] = prompt
    tuples.append(data)

tuples = pd.DataFrame(data=tuples).drop_duplicates()
tuples.index.name = "id"
tuples.to_csv("generated_queries.csv")
