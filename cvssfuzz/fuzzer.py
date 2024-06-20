import base64
import random
import sys
import string
import logging

from urllib.parse import quote

from . import settings
from . import log_settings

log_settings.setup_logging()
LOG = logging.getLogger(__name__)

class CVSSFuzz:
    """CVSS Fuzzer. Test CVSS tooling robustness."""
    def __init__(self, **kwargs):
        self.config = kwargs.get('config') or settings.default_settings
        LOG.debug(f"Fuzzer Configuration: {self.config}")
        self.config['fuzzer'] = self.config.get('fuzzer')
        self.config['category'] = self.config.get('category')
        try:
            self.metrics_values = settings.metrics[self.config['version']]['values']
            self.metric_categories = settings.metrics[self.config['version']]['categories']
        except KeyError as kerr:
            LOG.critical(f"Invalid Config - CVSS Version: {self.config['version']} is not supported.")
            sys.exit(-1)

    def get_random_combination(self):
        """
        Generates a random combination in order of the spec. 
        Even though the spec defines out of order vector is acceptable, I prefer to keep it in order.
        """
        #VERSION 4.0 SUPPORT
        if self.config['version'] == '4.0':
            match self.config['category']:
                case 'all':  # CVSS-BTE (with S)
                    category_keys = self.metric_categories['base'] + \
                                    self.metric_categories['threat'] + \
                                    self.metric_categories['environmental'] + \
                                    self.metric_categories['supplemental']
                case 'base': # CVSS-B
                    category_keys = self.metric_categories['base']
                case 'threat': # CVSS-BT
                    category_keys = self.metric_categories['base'] + self.metric_categories['threat']
                case 'supplemental': # CVSS-BS
                    category_keys = self.metric_categories['base'] + self.metric_categories['supplemental']

                case 'environmental': # CVSS-BE
                    category_keys = self.metric_categories['base'] + self.metric_categories['environmental']
                case _:
                    category_keys = self.metric_categories['base'] + \
                                    self.metric_categories['threat'] + \
                                    self.metric_categories['environmental'] + \
                                    self.metric_categories['supplemental']

        #VERSION 3.1 SUPPORT
        elif self.config['version'] == '3.0' or self.config['version'] == '3.1':
            match self.config['category']:
                case 'all':
                    category_keys = self.metric_categories['base'] + \
                                    self.metric_categories['temporal'] + \
                                    self.metric_categories['environmental']
                case 'base':
                    category_keys = self.metric_categories['base']
                case 'temporal':
                    category_keys = self.metric_categories['base'] + self.metric_categories['temporal']
                case 'environmental':
                    category_keys = self.metric_categories['base'] + self.metric_categories['environmental']
                case _:
                    category_keys = self.metric_categories['base'] + \
                                    self.metric_categories['temporal'] + \
                                    self.metric_categories['environmental']
        
        elif self.config['version'] == '2.0':
            match self.config['category']:
                case 'all':
                    category_keys = self.metric_categories['base'] + \
                                    self.metric_categories['temporal'] + \
                                    self.metric_categories['environmental']
                case 'base':
                    category_keys = self.metric_categories['base']
                case 'temporal':
                    category_keys = self.metric_categories['base'] + self.metric_categories['temporal']
                case 'environmental':
                    category_keys = self.metric_categories['base'] + self.metric_categories['environmental']
                case _:
                    category_keys = self.metric_categories['base'] + \
                                    self.metric_categories['temporal'] + \
                                    self.metric_categories['environmental']

        random_combination = {key: random.choice(self.metrics_values[key]) for key in list(self.metrics_values.keys()) if key in category_keys}
        final_vector = f'CVSS:{self.config["version"]}/' + '/'.join([f"{k}:{v}" for k, v in random_combination.items()])
        LOG.debug(f"Random Vector: {final_vector}")
        return final_vector
    
    def shuffle_combination(self, combination):
        """
        Shuffles a combination.
        CVSS tools should be able to handle varied ordering of the vector string.
        CVSS 4.0 spec section 7 "A vector string must contain metrics in the order shown in Table 23, every other ordering is invalid."
        """
        kv_pairs = combination.split('/')
        first_kv = kv_pairs[0]
        other_kvs = kv_pairs[1:]
        random.shuffle(other_kvs)
        shuffled_kv_pairs = [first_kv] + other_kvs
        final_string = '/'.join(shuffled_kv_pairs)
        LOG.debug(f"Shuffled Vector: {final_string}")
        return final_string
        
    def invalid_combination(self, combination):
        """
        Generates an invalid combination by changing a random key-value pair to a random value that is abnormal for the specific metric.
        CVSS tools should recognize these as invalid.
        """
        kv_pairs = combination.split('/')
        first_kv = kv_pairs[0]
        other_kvs = kv_pairs[1:]
        random_index = random.randrange(len(other_kvs))
        key, _ = other_kvs[random_index].split(':')
        alphabet = [char for char in string.ascii_uppercase if char not in self.metrics_values[key]]
        new_value = random.choice(alphabet)
        other_kvs[random_index] = f'{key}:{new_value}'
        modified_kv_pairs = [first_kv] + other_kvs
        final_string = '/'.join(modified_kv_pairs)
        LOG.debug(f"Invalid Key: {random_index} - Vector: {final_string}")
        return final_string

    def missing_combination(self, combination):
        """
        Generates a combination with a random key-value pair missing.
        CVSS tools should recognize these as invalid if the removed item is one of the base metrics.
        """
        kv_pairs = combination.split('/')
        #random_pop_size = random.randint(0, len(kv_pairs))
        #random_size = len(kv_pairs) - random.randrange(len(kv_pairs))
        random_index = random.randrange(len(kv_pairs))
        kv_pairs.pop(random_index)
        final_string = '/'.join(kv_pairs)
        LOG.debug(f"Missing Key: {random_index} - Vector: {final_string}")
        return final_string

    def insane_combination(self, combination):
        """
        Generates an insane combination by changing a random key-value pair to a random value.
        CVSS tools should recognize these as invalid *most of the time*. It's possible for a insane random value to be valid.
        """
        insanity = ['hex', 'byte', 'keyboard', 'base64', 'url', 'backwards']
        kv_pairs = combination.split('/')
        random_index = random.randrange(len(kv_pairs))
        special_chars = '!@#$%^&*()-_=+[]{}|;:",.<>/?'
        keyboard_chars = [char for char in string.ascii_uppercase + string.digits + special_chars]
        new_value = random.choice(keyboard_chars)
        insane_choice = random.choice(insanity)

        match insane_choice:
            case 'hex':
                new_value = str(new_value.encode('utf-8').hex())
            case 'byte':
                new_value = str(new_value.encode('utf-8'))
            case 'keyboard':
                new_value = str(new_value)
            case 'base64':
                new_value = str(base64.b64encode(new_value.encode('utf-8')))
            case 'url':
                new_value = str(quote(new_value))
            case _:
                new_value = str(new_value)

        key, _ = kv_pairs[random_index].split(':')
        kv_pairs[random_index] = f'{key}:{new_value}'
        final_string = '/'.join(kv_pairs)
        LOG.debug(f"Insane Choice: {insane_choice} - Vector: {final_string}")
        return final_string

    def duplicate_entry_combination(self, combination):
        """
        Generates a combination with a duplicate key-value pair.
        CVSS tools should recognize these as invalid.
        CVSS 4.0 section 7 - "A vector string must not include the same metric more than once."
        """
        kv_pairs = combination.split('/')
        random_index = random.randrange(len(kv_pairs))
        kv_pairs.append(kv_pairs[random_index])
        final_string = '/'.join(kv_pairs)
        LOG.debug(f"Duplicate Key: {random_index} - Vector: {final_string}")
        return final_string

    def lowercase_combination(self, combination):
        """
        Generates a combination with a random key-value pair lowercase.
        CVSS tools should recognize these as invalid.
        """
        kv_pairs = combination.split('/')
        random_index = random.randrange(len(kv_pairs))
        key, value = kv_pairs[random_index].split(':')
        kv_pairs[random_index] = f'{key.lower()}:{value}'
        final_string = '/'.join(kv_pairs)
        LOG.debug(f"Lowercase Key: {random_index} - Vector: {final_string}")
        return final_string

    def missing_prefix_combination(self, combination):
        """
        Generates a combination with a random key-value pair missing the CVSS prefix.
        CVSS tools should recognize these as invalid.
        CVSS 4.0 spec section 7 - "vector string begins with the label “CVSS:” and a numeric representation of the current version"
        """
        # remove the first 5 characters from the string
        kv_pairs = combination.split('/')
        kv_pairs.pop(0)
        final_string = '/'.join(kv_pairs)
        return final_string

    def missing_metric_key_combination(self, combination):
        """
        Generates a combination with a random metric missing the metric _key_.
        CVSS tools should recognize these as invalid.
        The range starts at 1 to avoid removing the CVSS version.
        """
        kv_pairs = combination.split('/')
        random_index = random.randrange(1, len(kv_pairs))
        _, value = kv_pairs[random_index].split(':')
        kv_pairs[random_index] = f':{value}'
        final_string = '/'.join(kv_pairs)
        LOG.debug(f"Missing Key Key: {random_index} - Vector: {final_string}")
        return final_string

    def missing_metric_value_combination(self, combination):
        """
        Generates a combination with a random metric missing the _value_.
        CVSS tools should recognize these as invalid.
        The range starts at 1 to avoid removing the CVSS version.
        """
        kv_pairs = combination.split('/')
        random_index = random.randrange(1, len(kv_pairs))
        key, _ = kv_pairs[random_index].split(':')
        kv_pairs[random_index] = f'{key}:'
        final_string = '/'.join(kv_pairs)
        LOG.debug(f"Missing Value Key: {random_index} - Vector: {final_string}")
        return final_string


    def __fuzz(self):
        """
        Private method that calls the appropriate fuzzer based on the config.
        """
        vector_string = self.get_random_combination()
        match self.config['fuzzer']:
            case 'random':  # default to random combos
                return vector_string
            case 'shuffle':
                return self.shuffle_combination(vector_string)
            case 'invalid':
                return self.invalid_combination(vector_string)
            case 'missing':
                return self.missing_combination(vector_string)
            case 'insane':
                return self.insane_combination(vector_string)
            case 'duplicate':
                return self.duplicate_entry_combination(vector_string)
            case 'lowercase':
                return self.lowercase_combination(vector_string)
            case 'missing_prefix':
                return self.missing_prefix_combination(vector_string)
            case 'missing_metric_key':
                return self.missing_metric_key_combination(vector_string)
            case 'missing_metric_value':
                return self.missing_metric_value_combination(vector_string)
            case _:
                return vector_string

    def run(self):
        """
        Generator that yields fuzzed CVSS vectors one at a time.
        Caution: if you set count to 0, this will run forever and might use up all available memory on a system.
        """
        if self.config.get('count') > 0:
            for _ in range(self.config['count']):
                yield self.__fuzz()
        elif self.config.get('count') == 0: # run forever..... 
            while True:
                yield self.__fuzz()
    
    def __call__(self):
        self.run()