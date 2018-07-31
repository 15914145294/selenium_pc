"""
根据已知的dict object 更新字典的属性
从更新后的属性中获取value
"""


class LookupDict(dict):
    """Dictionary lookup object."""

    def __init__(self, name=None):
        self.name = name
        super(LookupDict, self).__init__()

    def __repr__(self):
        return '<lookup \'%s\'>' % (self.name)

    def __getitem__(self, key):
        # We allow fall-through here, so values default to None
        return self.__dict__.get(key, None)

    def get(self, key, default=None):
        return self.__dict__.get(key, default)

_codes={500: ('internal_server_error', 'server_error', '/o\\', '✗'),
    501: ('not_implemented',),
    502: ('bad_gateway',),
    503: ('service_unavailable', 'unavailable'),
    504: ('gateway_timeout',),
    505: ('http_version_not_supported', 'http_version'),
    506: ('variant_also_negotiates',),
    507: ('insufficient_storage',),
    509: ('bandwidth_limit_exceeded', 'bandwidth')}
codes = LookupDict(name='status_codes')

for code, titles in _codes.items():
    for title in titles:
        setattr(codes, title, code)
        if not title.startswith('\\'):
            setattr(codes, title.upper(), code)

if __name__ == '__main__':

	print codes.__dict__
	print codes.get("reset")
