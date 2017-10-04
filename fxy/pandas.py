import pandas
import sklearn

class DataFrame(pandas.DataFrame):
    @property
    def _constructor(self, *args, **kwargs):
        return DataFrame

    def classify(self):
        """
        This would work like .groupby, e.g.:

        df.classify(columns=[], how='kmeans', {'threshold': '', 'metric': ''})

        # ref: https://maciejjaskowski.github.io/2016/01/22/pandas-scikit-workflow.html
        """
        return 'This method will run a classification algorithm on the data in the DataFrame.'
