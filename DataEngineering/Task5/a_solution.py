import pandas as pd


def check_test_num(patient_data, ref_data):
    merged_data = (
        patient_data.groupby("patient_id").size().reset_index(name="test_count")
    )
    merged_data = merged_data.merge(ref_data, on="patient_id", how="outer")
    merged_data["test_count"] = merged_data["test_count"].fillna(0).astype(int)
    merged_data["tests_performed"] = (
        merged_data["tests_performed"].fillna(0).astype(int)
    )
    merged_data["consistent"] = (
        merged_data["test_count"] == merged_data["tests_performed"]
    )
    return merged_data["consistent"].all()


def test1():
    test_df = pd.DataFrame(
        {
            "patient_id": ["1", "1", "2", "2", "2"],
            "test_no": ["2", "1", "4", "2", "1"],
            "result": ["Positive", "Positive", "Negative", "Negative", "Negative"],
        }
    )

    ref_df = pd.DataFrame({"patient_id": ["1", "2"], "tests_performed": ["2", "3"]})

    return check_test_num(test_df, ref_df)


def test2():
    test_df = pd.DataFrame(
        {
            "patient_id": ["1", "1", "2", "2", "2"],
            "test_no": ["2", "1", "4", "2", "1"],
            "result": ["Positive", "Positive", "Negative", "Negative", "Negative"],
        }
    )

    ref_df = pd.DataFrame({"patient_id": ["1", "2"], "tests_performed": ["2", "4"]})

    return check_test_num(test_df, ref_df)


def test_suite1():
    assert test1()
    assert not test2()
    print("test_suite1 PASSED")


if __name__ == "__main__":
    test_suite1()
