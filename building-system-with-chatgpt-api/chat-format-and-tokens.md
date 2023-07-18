## word vs token

token is less than word, tokenized by LLM

for example, llm can't reverse word `lollipop`
but it can correctly reverse it when input is `l-o-l-l-i-p-o-p`

## message roles

- system
- user
- assistant

```python
message=[
    {"role": "system", "content": "you are an assistant.."},
    {"role": "user", "content": "tell me a joke.."},
    {"role": "assistant", "content": "what is .."},
]
```

system(Set tone/behavior of assistant) -> assistant (LLM response) -> user (prompt)

chatgpt max limit 4000 token