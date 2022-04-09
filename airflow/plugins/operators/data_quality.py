from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from helpers import SqlQueries



class DataQualityOperator(BaseOperator):
"""
This class will check quality of data by runnable of SQL query and a result expectation.
The parameters:
@redshift_conn_id: a Redshift connection ID
@sqls_be_validated: a list of json object as following structure:
{
"sql_be_validated": a SQL query which be validated from our Redshift cluster,
"result_expectation": a expected result for the query above
}

For example:
{
"sql_be_validated": "SELECT COUNT(*) FROM users WHERE user_id IS NULL",
"result_expectation": 0
}
"""
    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 sqls_be_validated=None, 
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table_targets = table_targets
       
        if sqls_be_validated is None:
            sqls_be_validated = []
            self.redshift_conn_id = redshift_conn_id
            self.validate = sqls_be_validated
            
    def execute(self, context):
        self.log.info('Processing to get aws credentials...')
        redshift_conn = PostgresHook.PostgresHook('redshift')

        self.log.info('Starting to validate the data...')
        
        for c in self.validate:
            sql_string = c['sql_be_validated']
            expected_result = c['result_expectation']
            records = redshift_conn.get_records(sql_string)
            # We will get the cell at [0][0] since the COUNT function will return only one row
            number_records = records[0][0]
            if number_records == expected_result:
                self.log.info('Passed on the SQL {} with {} records'.format(sql_string, number_records))
            else:
                raise ValueError("Failed on the SQL {}. Expected result is {} | Real is {}".format(sql_string, expected_result, number_records))