# Question:

    Given 2 tables compare them for data consistency

    You are given 2 tables
    One shows patient, test number and the corresponding results. An example is shown below:

    Table 1:
    patient data:
    patient_data

    patient_id | test_no | result
    ----------------------------
        1      |   2     |Positive
        1      |   1     |Positive
        2      |   4     |Negative
        2      |   2     |Positive
        2      |   1     |Negative

    Another table shows test counts for each patient


    Table 2:
    reference data:
    ref_data

    patient_id | tests_performed
    ----------------------------
        1      |   2
        2      |   3

Your goal is to compare these 2 tables and ensure that the first table has the correct number of test results as expected in the second table.
Your function check_test_num(table1, table2) will return True or False based on the above criteria.
From the given example, Patient 1 is expected to have 2 test results and patient 2 is expected to have 3 test results on the above criteria.
The check would return True for the sample data above.
