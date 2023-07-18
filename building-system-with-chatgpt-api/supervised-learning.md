监督学习
==

## process

get labeled data -> train ai model and data -> deploy & call model

## types of LLM

- base LLM
- instruction tuned LLM

Train a base LLM on a lot of data

Further train the model
- Fine-tune on examples of where the output follows an input instruction
- obtain human-rating of the quality of different LLM outputs, on criteria such as whether it is helpful
- tune LLM to increase probability that it generates the more highly rated outputs(using RLHF: reinforcement 
  learning from human feedback)

## prompting is revolutionizing AI app dev

prompt-based ai

specify prompt -> call model