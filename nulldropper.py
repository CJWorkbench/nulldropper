import io
import re

# ---- SelectColumns ----

@staticmethod
def __init__(self):
    pass


class Importable:
    @staticmethod
    def event():
        pass

    @staticmethod
    def render(wf_module, table):
        buf = io.StringIO()
        table.info(buf=buf)
        s = buf.getvalue()
        info_values = [re.split("\\s\\s+", x) for x in s.split("\n")]
        info_values = [x for x in info_values if len(x) > 1]
        info_values = [x[0] for x in info_values if x[1].startswith('0 non-null')]
        df = table.drop(info_values, axis=1)
        return df