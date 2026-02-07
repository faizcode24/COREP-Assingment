def render_corep_table(report):
    return [
        {"Row": f.row, "Description": f.label, "Amount": f.value}
        for f in report.fields
    ]
