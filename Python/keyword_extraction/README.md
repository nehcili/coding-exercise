The purpose of this project is to extract key words from news articles from Feb 20 to Feb 27 from https://www.jiqizhixin.com/dailies

The result and the main source code for the project is contained in keyword_search.ipynb. An open source keyword extraction algorithm (RAKE_For_Chinese) is used in this project with modification. The original code is written by Cryptum169 and can be found at https://github.com/Cryptum169/Rake_For_Chinese. In summary, it uses jieba to tokenize Chinese sentences and perform the RAKE algorithm on the resulting tokens.

A version of https://www.jiqizhixin.com/dailies where actual parsing/article extraction took place is the file news.html. This file is most easily obtained in chrome by selecting "Inspect" on any Feb 19 article and copying the html code into the news.html file.

