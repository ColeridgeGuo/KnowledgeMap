# 知识图谱
用StanfordCoreNLP构建知识图谱

## 文档预处理

- `/code/text_processing.py `

- 对文章文档进行预处理，包括去掉无用信息保留摘要部分。

- 处理前的文件在`/data/original texts`里；处理完的文件保存在`/data/cleaned_texts`里。

## 句子核心抽取

- `/code/sentence_core_extraction.py`

- 抽取句子核心（主谓宾）用来构建实体关系。
- 从`/data/original_texts`里读取文件，抽取完的句子核心在`/output`里。

## 命名实体识别demo

- `/code/stanford_ner_demo.py`

- 一个使用 `nltk` 包中的 `StanfordNERTagger` 进行命名实体识别的demo

- TO-DO: 避免使用 `nltk.tag` 中的 Stanford NER 和 POS 标注器，以及 `nltk.tokenize` 里的tokenizer，因为它们即将被弃用。
  
- 使用 `nltk.parse.corenlp.CoreNLPParser`替代 ，详情看[这里](https://github.com/nltk/nltk/wiki/Stanford-CoreNLP-API-in-NLTK)。

