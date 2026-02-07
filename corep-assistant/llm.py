def generate_corep_output(reg_text, scenario):
    return {
        "template": "C 01.00",
        "fields": [
            {
                "row": "010",
                "column": "010",
                "label": "Ordinary shares",
                "value": scenario["ordinary_shares"],
                "justification": ["PRA OF 2.1", "EBA C01 r010"]
            },
            {
                "row": "030",
                "column": "010",
                "label": "Retained earnings",
                "value": scenario["retained_earnings"],
                "justification": ["PRA OF 2.2", "EBA C01 r030"]
            },
            {
                "row": "060",
                "column": "010",
                "label": "Intangible assets (deduction)",
                "value": -scenario["intangible_assets"],
                "justification": ["PRA OF 3.1", "EBA C01 r060"]
            }
        ]
    }
