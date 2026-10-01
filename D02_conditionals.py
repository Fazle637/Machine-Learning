#Loan approval logic
credit_score = 680
income = 45000
has_debt = True

if credit_score >= 7500:
    approval = "Approved - Excellent credit"

elif credit_score >= 650 and income >= 40000 and has_debt:
    approval = "Approved - Good credit, low risk"

elif credit_score >= 650 and income >= 40000 and has_debt:
    approval = "Conditionally approved - needs manual review"

else:
     approval = "Rejected - Does not meet minimum criteria"

print(f"Loan Status: {approval}")


#Day 2 Challenge: Conditionals
score = 67

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"

else:
    grade = "F"

#Special Handling for failing grades
if grade == "F" and score < 60:
    print(f"Score: {score} - Close - consider a retake")
else:
    print(f"Score: {score} - Grade: {grade}")


