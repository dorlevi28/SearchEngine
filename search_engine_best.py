import pandas as pd

from Glove import Glove
from Thesaurus import _Thesaurus
from Word2Vec import Word2Vec
from WordNet import WordNet
from _SpellCheck import _SpellChecker
from reader import ReadFile
from configuration import ConfigClass
from parser_module import Parse
from indexer import Indexer
from searcher import Searcher
import utils

# DO NOT CHANGE THE CLASS NAME
class SearchEngine:

    # DO NOT MODIFY THIS SIGNATURE
    # You can change the internal implementation, but you must have a parser and an indexer.
    def __init__(self, config=None):
        self._config = config
        self._parser = Parse()
        self._indexer = Indexer(config)
        self._model = None

    # DO NOT MODIFY THIS SIGNATURE
    # You can change the internal implementation as you see fit.
    def build_index_from_parquet(self, fn):
        """
        Reads parquet file and passes it to the parser, then indexer.
        Input:
            fn - path to parquet file
        Output:
            No output, just modifies the internal _indexer object.
        """
        df = pd.read_parquet(fn, engine="pyarrow")
        documents_list = df.values.tolist()
        # Iterate over every document in the file
        self._parser.curr_idx = self.parse_and_index_tweet_list(documents_list, 0)
        self._indexer.save_index('idx_bench.pkl')
        print('Finished parsing and indexing.')

    def parse_and_index_tweet_list(self, documents_list, idx):

        for document in documents_list:
            # parse the document
            self._parser.curr_idx = idx
            parsed_document = self._parser.parse_doc(document)
            # add the doucment to indexer here
            self._indexer.set_idx(idx)
            self._indexer.add_new_doc(parsed_document)
            idx += 1

        return idx-1
    # DO NOT MODIFY THIS SIGNATURE
    # You can change the internal implementation as you see fit.
    def load_index(self, fn):
        """
        Loads a pre-computed index (or indices) so we can answer queries.
        Input:
            fn - file name of pickled index.
        """
        self._indexer.load_index(fn)

    # DO NOT MODIFY THIS SIGNATURE
    # You can change the internal implementation as you see fit.
    def load_precomputed_model(self, model_dir=None):
        """
        Loads a pre-computed model (or models) so we can answer queries.
        This is where you would load models like word2vec, LSI, LDA, etc. and
        assign to self._model, which is passed on to the searcher at query time.
        """
        self._model = [_Thesaurus(), Glove()]

    # DO NOT MODIFY THIS SIGNATURE
    # You can change the internal implementation as you see fit.
    def search(self, query):
        """
        Executes a query over an existing index and returns the number of
        relevant docs and an ordered list of search results.
        Input:
            query - string.
        Output:
            A tuple containing the number of relevant search results, and
            a list of tweet_ids where the first element is the most relavant
            and the last is the least relevant result.
        """
        searcher = Searcher(self._parser, self._indexer, model=self._model)
        return searcher.search(query)
