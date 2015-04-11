from multicorn import ForeignDataWrapper
from multicorn.utils import log_to_postgres, ERROR, WARNING, DEBUG

from parse_rest.connection import register
from parse_rest.datatypes import Object

class ParseFdw(ForeignDataWrapper):
    """
    A Parse foreign data wrapper.
    """

    def __init__(self, options, columns):
        super(ParseFdw, self).__init__(options, columns)
        self.columns = columns
        try:
            self.application_id = options['application_id']
            self.rest_api_key = options['rest_api_key']
            self.className = options['class_name']
        except KeyError:
            log_to_postgres("You must specify an application_id, rest_api_key and class_name options when creating this FDW.", ERROR)

        register(self.application_id, self.rest_api_key)
        self.object = Object.factory(self.className)

    def execute(self, quals, columns):
        result = self.object.Query.all().keys(*self.columns.keys())

        for row in result:
            yield row._to_native()
