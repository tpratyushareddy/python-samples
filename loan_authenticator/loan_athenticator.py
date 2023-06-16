# importing variables
import random
import string

# Loan engine function
def loan_engine(master_data,customer_data):
    for cust in customer_data:
        Approved = {}
        Denied = {}
        LoanApplicationStatus = ""
        for rule in master_data:
            # Comparing the Data
            if cust["CustCreditScore"] >= rule["min_cs"] and cust["CustCreditScore"] <= rule["max_cs"] and cust["CustLoanAmount"] >= rule["min_loan_amt"] and cust["CustLoanAmount"] <= rule["max_loan_amt"]:
                LoanApplicationStatus = "Approved"
                InterestRate = rule["interest"]
                DurationInMonths = rule["duration"]
                Approved['Custname'] = (cust["CustName"])
                Approved['CustCreditScore'] = (cust["CustCreditScore"])
                Approved['CustLoanAmount'] = (cust["CustLoanAmount"])
                Approved['Status'] = LoanApplicationStatus
                Approved['InterestRate'] = InterestRate
                Approved['DurationInMonths'] = DurationInMonths
                Approved['Message'] = "Congrats"
        if LoanApplicationStatus == "Approved":
            print(Approved)
        else:
            LoanApplicationStatus = "Denied"
            Denied['Custname'] = cust["CustName"]
            Denied['CustCreditScore'] = cust["CustCreditScore"]
            Denied['CustLoanAmount'] = cust["CustLoanAmount"]
            Denied['Status'] = LoanApplicationStatus
            Denied['Message'] = "sorry"
            print(Denied)



# Master data
master_loan_rules = [
 {"min_cs":200, "max_cs":299, "min_loan_amt":10000, "max_loan_amt":19999, "interest":5, "duration":72}
,{"min_cs":200, "max_cs":299, "min_loan_amt":20000, "max_loan_amt":29999, "interest":5.5, "duration":72}
,{"min_cs":200, "max_cs":299, "min_loan_amt":30000, "max_loan_amt":39999, "interest":6, "duration":72}
,{"min_cs":200, "max_cs":299, "min_loan_amt":40000, "max_loan_amt":50000, "interest":.65, "duration":72}
,{"min_cs":300, "max_cs":399, "min_loan_amt":10000,"max_loan_amt":19999, "interest":5, "duration":72}
,{"min_cs":300, "max_cs":399, "min_loan_amt":20000,"max_loan_amt":29999, "interest":5.5, "duration":72}
,{"min_cs":300, "max_cs":399, "min_loan_amt":30000,"max_loan_amt":39999, "interest":6, "duration":72}
,{"min_cs":300, "max_cs":399, "min_loan_amt":40000,"max_loan_amt":50000, "interest":.65, "duration":72}
,{"min_cs":400, "max_cs":500, "min_loan_amt":10000,"max_loan_amt":19999, "interest":5, "duration":72}
,{"min_cs":400, "max_cs":500, "min_loan_amt":20000,"max_loan_amt":29999, "interest":5.5, "duration":72}
,{"min_cs":400, "max_cs":500, "min_loan_amt":30000,"max_loan_amt":39999, "interest":6, "duration":72}
,{"min_cs":400, "max_cs":500, "min_loan_amt":40000,"max_loan_amt":50000, "interest":.65, "duration":72}
]


# Customer data

customer = [{"CustName":"AA", "CustCreditScore":35, "CustLoanAmount":22450}
            ,{"CustName":"BB", "CustCreditScore":375, "CustLoanAmount":46756}
            ,{"CustName":"CC", "CustCreditScore":5, "CustLoanAmount":244}
            ]
# calling function
#loan_engine(master_loan_rules,customer)

# Bulk data
for c1 in range(3): # range can be changed as per requirement
    customer_random = {}
    cr = []
    CustName = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))# generates a random string
    CustCreditScore = random.randint(100, 505)
    CustLoanAmount = random.randint(10000, 50000)
    customer_random['CustName'] = CustName
    customer_random['CustCreditScore'] = CustCreditScore
    customer_random['CustLoanAmount'] = CustLoanAmount
    cr.append(customer_random)
    # calling function
    loan_engine(master_loan_rules,cr)


