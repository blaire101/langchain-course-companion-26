# Exercise Guidance

These are guidance points, not fixed answers.

1. Add a `Literal["positive", "neutral", "negative"]` field to the Pydantic schema.
2. Store user and assistant messages under a stable thread ID; production storage should be persistent.
3. Implement `summary_prompt | model | translation_prompt | model`, or use two explicit functions for clarity.
4. Smaller chunks may improve precision but lose context; larger chunks may add noise and cost.
5. Include an expected `answerable: false` flag and test for refusal or an insufficient-information phrase.
6. Give the new tool a precise name, typed arguments, and a description that clearly distinguishes it from the simple cost tool.
