# Hugging Face

Hugging face is a platform where organization and individuals publish there Machine Learning models. These models are open source and anyone can use them. That's why Hugging face is also called the github of ML models.

## List of available tasks

1. audio-classification
2. automatic-speech-recognition
3. conversational
4. depth-estimation
5. document-question-answering
6. feature-extraction
7. fill-mask
8. image-classification
9. image-segmentation
10. image-to-image
11. image-to-text
12. mask-generation
13. ner
14. object-detection
15. question-answering
16. sentiment-analysis
17. summarization
18. table-question-answering
19. text-classification
20. text-generation
21. text-to-audio
22. text-to-speech
23. text2text-generation
24. token-classification
25. translation
26. zero-shot-classification
27. zero-shot-image-classification
28. zero-shot-object-detection
29. translation_XX_to_YY

## Usage Example

## Sentiment Analysis

```python
from transformers import pipeline

sentiment = pipeline('sentiment-analysis',model='distilbert/distilbert-base-uncased-finetuned-sst-2-english')

response = sentiment('I bought a laptop from your organization but it was not working well.')

print(response)
```

## Pipeline

A pipeline refers to a sequence of data processing components that are connected in a linear manner . The output of one component serves as the input for the next component . These components can include data preprocessing, feature extraction, model training, and model evaluation . By organizing the different tasks into a pipeline, data scientists can easily experiment with different combinations of components

## Name Entity Recognition

NLP task, involves identifying and classifying named entities in text into predefined categories such as person names, organizations, locations, dates and more.

### Code Example

```python
from transformers import pipeline

recognition = pipeline('ner')

response = recognition('Muhammad was going to Makkah.')

print(response)
```

where `ner` is for **Name Entity Recognition**.

## Important Note

Working with hugging face requires lot of computational power and resources. It is recommended to use [Google Colab](https://colab.google/). It is a powerful jupyter environment that covers all the essential requirements. Jupyter files in this environment are added into the repository but was implemented at Colab.

Other reason to work on colab is that whenever a hugging face model is used it gets download and consumes a lot of memory, so for fast response use the Google Colab.

## Installations

```pip
!pip install transformers
```
