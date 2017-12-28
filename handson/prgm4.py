emp_id=int(input("Enter emp id:"))
emp_bs=int(input("Enter basic salary"))
emp_al=int(input("Enter allowance"))
gross_salary=emp_bs+emp_al
print("The gross salary is:",gross_salary)
if gross_salary>=5001&gross_salary<=10000:
    tax=gross_salary*0.1
    print("tax:",tax)
elif gross_salary>=10001&gross_salary<=20000:
    tax=gross_salary*0.2
    print("tax:",tax)
elif gross_salary>=20001:
    tax=gross_salary*0.3
    print("tax:",tax)
else:
    print("no tax")
net_salary=gross_salary-tax
print("The net salary is:",net_salary)
