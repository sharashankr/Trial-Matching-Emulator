from __future__ import annotations

import json
from trialmatch.pipeline import TrialMatchingPipeline


if __name__ == "__main__":
    patient = (
        "62-year-old woman with advanced endometrial cancer, ECOG 1, "
        "received prior chemotherapy, dMMR tumor."
    )
    pipeline = TrialMatchingPipeline(top_k=3)
    output = pipeline.run(patient)
    print(json.dumps(output, indent=2))
