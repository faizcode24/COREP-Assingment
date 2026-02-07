from fastapi import FastAPI
from retriever import retrieve_regulatory_text
from llm import generate_corep_output
from schema import CorepReport
from renderer import render_corep_table

app = FastAPI(title="LLM-assisted COREP Reporting Assistant")

@app.post("/generate-corep")
def generate_corep(question: str, scenario: dict):
    regulatory_text = retrieve_regulatory_text(question)
    llm_output = generate_corep_output(regulatory_text, scenario)
    report = CorepReport(**llm_output)
    warnings = report.validate_report()
    table = render_corep_table(report)

    return {
        "template": report.template,
        "corep_extract": table,
        "audit_log": llm_output["fields"],
        "validation_warnings": warnings
    }
