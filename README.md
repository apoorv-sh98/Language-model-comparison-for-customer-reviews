# Language-model-comparison-for-customer-reviews

Considering how online buying is preferred everywhere and an important factor, in buying things online, is the customer reviews from people who have already bought the same product. It is hard to know whether the reviews submitted are actually written by people or is it computer generated.
Analyzing how we can differentiate between the two types of text - original text and paraphrased text, is the motivation behind this project.

## Dataset
In this project we consider two datasets in our work, namely, a publicly available human-generated dataset containing actual Amazon Alexa customer reviews, and other dataset containing reviews generated (paraphrased) by ChatGPT (OpenAi API).

## ML Model
Experimented with couple of transformer models such as 'Distilbert', 'Bert-Base' and  'Roberta-Base'. In this study, after implementing the above mentioned three models, we found that the performance of Roberta-Base was better than the other two (F1 score of 0.965). So, for our implementations of explainable AI, we used the Roberta model to predict the text classification between human and AI.

## Evaluation and Comparison
we used SHAP (a python package that employs the concept of Shapely values to provide explanations for the results) so that we can leverage the 'feature attribution' by considering each feature as a player in a game and computing its shapely value, which represents contribution of that feature to the predicted outcome.


## Conclusion
From the results of SHAP framework, we found that ChatGPT paraphrases tend to have slightly bigger and uncommon words. We also observed that the paraphrases were full of punctuation marks. Moreover, because the words used by ChatGPT are sophisticated, the language seems to be more formal. All these observations are based on the assumption that humans have simply asked ChatGPT to paraphrase a sentence and without giving any constraints for the paraphrasing task such as - "paraphrase in simple words", "paraphrase in 10 words", etc.