import pandas
import itertools
from tqdm import tqdm

from baserow.client import BaserowClient


class BaserowIO(BaserowClient):

    def get_fields(self, table_id):
        fields = lambda table_id: self._request('GET', path=f'/api/database/fields/table/{table_id}/').json()
        return {'field_'+str(field['id']): field['name'] for field in fields(table_id)}

    def get_table(self, table_id, get_values=True, progress=True):
        """
        :table_id: database table id
        :get_values: set to False to leave listed JSON 'values' as is
        :progress: set to False to not use tqdm

        Note: field names are in df.attrs, and useful when inserting/updating.
        """

        records = lambda table_id: itertools.chain.from_iterable(
          [[row for row in page.results]
            for page in (progress and tqdm(self.paginated_database_table_rows(table_id))
                         or self.paginated_database_table_rows(table_id))]
        )

        fields = self.get_fields(table_id)

        df = pandas.DataFrame.from_records(records(table_id))
        df.attrs = fields

        if get_values:
            df.rename(columns=fields, inplace=True)
            get_val = lambda x: x[0].get('value') if x and isinstance(x, list) and isinstance(x[0], dict) else x
            return df.applymap(get_val)


        return df

    def add_record(self, table_id, record, fields):
        """
        Example write:
        fields = io.get_fields(123)
        io.add_record(123, {'Name': 'hello', 'Description': 'Notes': 'world'}, fields)

        df = io.get-table(123)
        io.add_records(123, {'Name': 'hello', 'Description': 'Notes': 'world'}, df.attrs)
        """
        reverse_fields = dict(zip(fields.values(), fields.keys()))
        record = dict((reverse_fields[key], value) for (key, value) in record.items())

        return self.create_database_table_row(table_id, record)

