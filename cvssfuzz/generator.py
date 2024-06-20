import logging
from itertools import product
from . import settings
from . import log_settings

log_settings.setup_logging()
LOG = logging.getLogger(__name__)

class CVSSGenerate():
    def __init__(self, category, version):
        self.category = category
        self.version = version

    def run(self):
        values = settings.metrics[self.version]['values']
        categories = settings.metrics[self.version]['categories'][self.category]
        
        # Generate canonical, Cartesian product of values
        for vector_values in product(*(values[cat] for cat in categories)):
            yield f'CVSS:{self.version}/' + '/'.join([f"{k}:{v}" for k, v in dict(zip(categories, vector_values)).items()])

#

    def __call__(self):
        self.run()