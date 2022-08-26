# LDA-on-blogs
Contains the data and code necessary to run the LDA topic analysis on AK blogs.
Disclaimer. Any change to the parameters or to the source data may create different results, even if that is merely a different numbering of the same topics.
backup and backup_large contain txt files that can be copied directly to the "txtfiles\category_1_folder" but require preprocessing.py before LDA.py

## Requirements
- Python 3.10
### Python libraries
Following libraries were installed using:

* `pip install -r requirements.txt`.

Some of the libraries have dependencies of their own. However, they should be automatically installed.
If that is not the case, just install the required packages mentioned by the interpreter.

For the NLTK library we need to install the data:
Run the collowing code in the python interpreter.

```python
import nltk
nltk.download('popular')
```

## Running the program

### importer.py
To generate .txt files from blogs, either:
Run the importer.py without any arguments. This parses existing local copies of html files in the "htmlfiles" folder.
Run the importer.py with arguments <filename> <request_headers> <allow_redirection>
  
- filename is the name of .xlsx file where URLs are in first column, starting from row 2. Existing list is named "relevant_pages.xlsx"
- request_headers is the GET request headers if user prefers to not use defaults.
- allow_redirection, write yes if you want to allow get request redirections
  
As a result "txtfiles" folder will contain all parsed files.
If not using local files, a "import_results.xlsx" is created where second column contains a return code of the get request and third contains a txt file name.
  
### langtest.py
Will perform language testing for english language in the txtfiles folder. Any files that have more than 50% not recognized words will be listed in the terminal.
Manual checking and removal is required due to false positives.
  
### preprocess.py
Copy the contents of the "txtfiles" folder into "category_1_folder" subfolder. You may want to remove old files first. This 2 folder hierarchy is required by the LDA and "txtfiles" folder works as a backup for preprocess.py
To modify results of the preprocessing modify any of the sheets in the "preprocessing" folder to add compound words, ontology keywords etc.
  
### LDA.py
Performs LDA on the contents of the "txtfiles\category_1_folder" contents.
Modify the "TOP_WORDS" to adjust the amount of top words visible in the graph.
You can run the LDA.py without any arguments for the default settings or supply the following.
- MAX DF: int or float (either count or percentage)
- MIN DF: int or float (either count or percentage)
- MAX Features: int or None for default
- ALPHA : float
- BETA : float
- MAX iterations : int
- Amount of topics : int
- Tau_0 : float
  
LDA will print perplexity score to the terminal.
If topic count = 3. Topic density plot is generated.
Topics are plotted on the screen. Manual saving is required. ctrl+s with small screen size and large topic+top words count.
Next average top topic ratio per generated topic group prints to the terminal.
file "lda_result_names.xlsx" is generated. First column contains topic category, second the document file name and finally, third column has the top topic ratio.
  
## Extra
  
### coherence.py
Requires installing gensim library.

Is used to get coherence score of different topic counts. Prints score on the screen. Uses gensim as scikit-learn lacks the said functionality.
Prints coherence score per topic count alongside top words.
  
### source_topic_matcher.py
Requires running importer.py with a blog list rather than local files. Matches URLs to the generated topics (rather than matching the txt files). Used for making sampling easier. Generates "match_topic_types.xlsx" file.
  
### plot_sources.py
Generates discrete bubble chart and boxplots. Uses "BlogTypes.xlsx" to match with "match_topic_types.xlsx"

## Replicate the results
### Default arguments should suffice. Either option is valid for replicating the results.
- 1 directly run the python LDA.py command. 
- Delete all txt files in the txtfiles/category_1_folder and copy files in the txtfiles there. Followed by running python preprocess.py and python LDA.py.

### To follow original process run the following.
- importer.py "relevant_pages.xlsx"
  - Manually download missing pages and remove not blogs that were downloaded.
- run the langtest.py
  - Manually remove non english pages
  - copy files to category_1_folder
- run the preprocess.py
- run the LDA.py
