from trialmatch.schema import PatientProfile


def test_profile_schema() -> None:
    p = PatientProfile(free_text_summary="demo")
    assert p.free_text_summary == "demo"
    assert p.biomarkers == []
