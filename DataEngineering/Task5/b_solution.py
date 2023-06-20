import pandas as pd

# def check_test_num(patient_data, ref_data):
#     df = patient_data.groupby("patient_id").size().reset_index(name="test_count")
#     df = df.merge(ref_data, on="patient_id", how="outer")
#     df["test_count"] = df["test_count"].fillna(0).astype(int)
#     df["tests_performed"] = df["tests_performed"].fillna(0).astype(int)
#     df["consistent"] = df["test_count"] == df["tests_performed"]
#     return df["consistent"].all()


def check_test_num_pos(patient_data, ref_data):
    df = (
        patient_data.groupby("patient_id")
        .apply(lambda x: (x["result"] == "Positive").sum())
        .reset_index(name="Positive_tests")
    )
    df = df.merge(ref_data, on="patient_id", how="outer")
    df["Positive_tests"] = df["Positive_tests"].fillna(0).astype(int)
    df["tests_performed"] = df["tests_performed"].fillna(0).astype(int)
    df["consistent"] = df["Positive_tests"] == df["tests_performed"]
    return df["consistent"].all()


def test3():
    test_df = pd.DataFrame(
        {
            "patient_id": ["1", "1", "2", "2", "2"],
            "test_no": ["2", "1", "4", "2", "1"],
            "result": ["Positive", "Positive", "Negative", "Negative", "Negative"],
        }
    )

    ref_df = pd.DataFrame({"patient_id": ["1", "2"], "tests_performed": ["2", "0"]})

    return check_test_num_pos(test_df, ref_df)


def test4():
    test_df = pd.DataFrame(
        {
            "patient_id": ["1", "1", "2", "2", "2"],
            "test_no": ["2", "1", "4", "2", "1"],
            "result": ["Positive", "Negative", "Negative", "Positive", "Positive"],
        }
    )

    ref_df = pd.DataFrame({"patient_id": ["1", "2"], "tests_performed": ["1", "2"]})

    return check_test_num_pos(test_df, ref_df)


def test_suite2():
    assert test3()
    assert test4()
    print("test_suite2 PASSED")


if __name__ == "__main__":
    test_suite2()
