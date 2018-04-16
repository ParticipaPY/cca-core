# cca-core
cca-core  (Civic CrowdAnalytics Core) offers machine learning and natural language processing utilities for processing civic text input.

# Requirements
- scipy >= 0.19.1
- nltk >= 3.2.4
- scikit-learn >= 0.18.2
- beautifulsoup4 >= 4.6.0
- googletrans >= 2.2.0
- pandas >= 0.20.3

# Classes and Usage

 ## SentimentAnalyzer
Analyzes the sentiment polarity of a collection of documents.
    It determines wether the feeling about each doc is positive,
    negative or neutral.

### Parameters:

- **neu_inf_lim** : float, *-0.3* by default
        If a doc's polarity score is lower than this paramenter, then the sentiment is considered negative. Use values greater than -1 and lower than 0.
 - **neu_sup_lim** : float, *0.3* by default
        If a doc's polarity score is greater than this parameter, then the sentiment is considered positive. Use values greater than 0 and lower than 1.
 - **language**: string, *'english'*; by default
        Language on which documents are written. There are 2 languages supported natively:
        - *'english'*: through the ntlk_vader algorithms
        - *'spanish'*: through the ML_SentiCon algorithm
        If you use another language, the module will first translate each  document to english (using Google Translate AJAX API), so it can late re-use ntlk_vader algorithm for english docs.
### Methods
- **analyze_docs**:
    - **Description**: It takes as input a list of strings. For each document on that list, a sentiment label and a polarity score is assigned. The possible values for the label are 'pos' (for positive), 'neu' (for neutral), and 'neg' (for negative). The score is a float number.
    - **Method Parameters**:
        - *docs*: list of strings.
### Attributes
- **tagged_docs**: list of tuples on which each tuple consists of three elements:
    - the original text document. Data type: string
    - the sentiment label of that document. Data type: string
    - the polarity score of that document. Data type: float


 ## ConceptExtractor
Extract the most common concepts from a collection of documents.
### Parameters:
- **num_concepts** : int, *5* by default.
        The number of concepts to extract.
 - **context_words** : list, empty list by default.
        List of context-specific words that should notbe considered in the analysis.
 -  **ngram_range**: tuple, *(1,1)* by default.
        The lower and upper boundary of the range of n-values for different n-grams to be extracted. All values of n such that min_n <= n <= max_n will be used.
  - **pos_vec**: list, only words tagged as nouns (i.e., *['NN', 'NNP']*) are considered by default. 
  List of tags related with the part-of-speech that should be considered in the analysis. Please check [this link](http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html) for a complete list of tags.
- **consider_urls**: boolean, *False* by default
         Whether URLs should be removed or not.
 - **language**: string, *'english'* by default
        Language of the documents. Only the languages supported by the
        library NLTK are supported.
### Methods
- **extract_concepts**:
    - **Description**: Extract the most common concepts in the collection of documents.
    - **Method Parameters**:
        - *docs*: list of strings.
### Attributes
- **common_concepts**: list of tuples on which each tuple consists of two elements:
    - A concept, represented by a text n-gram . Data type: string.
    - The number of occurrences of the concept within the document collection . Data type: integer.
        
 ## DocumentClustering
 Cluster documents by similarity using the k-means algorithm.
 ### Parameters:
 -  **num_clusters** : int, *5* by default
        The number of clusters in which the documents will be grouped.
 - **context_words** : list, empty list by default
        List of context-specific words that should notbe considered in the 
        analysis.
 - **ngram_range**: tuple, *(1,1)* by default
        The lower and upper boundary of the range of n-values for different 
        n-grams to be extracted. All values of n such that 
        min_n <= n <= max_n will be used.
 - **min_df**: float in range [0.0, 1.0] or int, default=*0.1*
        The minimum number of documents that any term is contained in. It 
        can either be an integer which sets the number specifically, or a 
        decimal between 0 and 1 which is interpreted as a percentage of all 
        documents.
 - **max_df**: float in range [0.0, 1.0] or int, default=*0.9*
        The maximum number of documents that any term is contained in. It 
        can either be an integer which sets the number specifically, or a 
        decimal between 0 and 1 which is interpreted as a percentage of all 
        documents.
- **consider_urls**: boolean, *False* by default
        Whether URLs should be removed or not.
- **language**: string, *'english'* by default
        Language of the documents. Only the languages supported by the
        library NLTK are supported.
- **algorithm**: string, *'k-means'* by default
        Clustering algorithm use to group documents
        Currently available: k-means and agglomerative (hierarchical)
-  **use_idf**: boolean, *False* by default
        If true, it will use TF-IDF vectorization for feature extraction.
        If false it will use only TF.
### Methods
- **clustering**:
    - **Description**: Cluster, by similarity, a collection of documents into groups.
    - **Method Parameters**:
        - *docs*: list of strings.
### Attributes
- **num_docs_per_cluster**: dict where the keys are cluster labels, while the values are the number of docs in a cluster.
    
 ## DocumentClassifier
 Train a classifier with labeled documents and classify new documents 
    into one of the labeled clases.
   ### Parameters:
   
   - **train_p** : float, *0.8* by default
        The proportion of the 'dev docs' used as 'train docs'.
        Use values greater than 0 and lower than 1.
        The remaining docs will be using as 'test docs'
-  **n_folds** : integer, *10* by default
        Number of folds to be used in k-fold cross validation technique for choosing different sets as 'train docs'
- **vocab_size** : integer, *500* by default
        This is the size of the vocabulary set that will be used for extracting
        features out of the docs
- **t_classifier** : string, *'NB'* by default
        This is the type of classifier model used. Available types are *'NB'* (Naive Bayes), *'DT'* (decision tree), *'RF'* (Random Forest), and *'SVM'* (Support Vector Machine)
- **language**: string, *'english'* by default
        Language on which documents are written
- **train_method**: string, *'all_class_train'* by default
        Choose the method to train the classifier. There are two options:
        *'all_class_train'* and *'cross_validation'*
### Methods
- **classify_docs**:
    - **Description**: First train the classifier with the labeled data.
        Then classifies the unlabeled data.
    - **Method Parameters**:
        - *docs*: list of tuples (t,c), where t is text document, and c is the category label of t. Both, t and c, are strings. If c is an empty string, it means that t is unlabeled and is ment to be classified.
### Attributes
- **classified_docs**:  list of tuples (t,c), where t is text document, and c is the category label of t. Both, t and c, are strings. All t's are those that where unlabeled when calling classify_docs method. The ones that were already labeled are not included in this list.