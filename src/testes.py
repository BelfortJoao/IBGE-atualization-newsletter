import sidrapy

data = sidrapy.get_table(
        table_code="5459",
        territorial_level="1",
        ibge_territorial_code="all",
        classifications={"11278": "33460", "166": "3067,3327"},
        period="202002",
        header='n',
        format='list'
    )