def render(table, params):
    return table.dropna(how='all', axis='index')
