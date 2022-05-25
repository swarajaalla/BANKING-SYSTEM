
import pandas as pd
from db_connect import Db_connect


curs = Db_connect()
# curs.display('SELECT * FROM BANK_DETAILS')
# curs.display('SELECT * FROM BRANCH_DETAILS')
# curs.display('SELECT * FROM CUSTOMERS')
'''
Group 5 - Banking

1. How many banks have branches more than 6 in Bangalore?

2. Rank the banks based on the number of customers. Most customers in a bank comes first. Least customers in a bank comes last.

3. How many corporate clients are there with ICICI bank? 

4. How many retail clients are there with HDFC bank and who is their employer?

5. Get the list of all the corporate cients and their corresponding retail customers.

6. Which corporate client has the least number of employees (retail clients in bank's branch) in each bank.
'''

# 1. How many banks have branches more than 6 in Bangalore?
curs.display('SELECT * FROM (SELECT BID,COUNT(BID) AS TOT FROM BRANCH_DETAILS GROUP BY BID) K WHERE K.TOT >6')

# 2. Rank the banks based on the number of customers. Most customers in a bank comes first. Least customers in a bank comes last.
curs.display('''SELECT * , DENSE_RANK() OVER( ORDER BY TOTAL_CUSTOMERS DESC) FROM (
 SELECT BID, COUNT(*) AS TOTAL_CUSTOMERS
 FROM CUSTOMERS C JOIN BRANCH_DETAILS BR ON C.BRID = BR.BRID GROUP BY BID )X;''')

# 3. How many corporate clients are there with ICICI bank? 
curs.display("SELECT COUNT(*) N0_OF_ICICI_CORPORATE_CLIENTS FROM CUSTOMERS WHERE CTYPE = 'C' AND BRID LIKE 'ICICI%' ")

# 4. How many retail clients are there with HDFC bank and who is their employer?
curs.display("SELECT PAR_ACC AS EMPLOYER,COUNT(PAR_ACC) NO_OF_RETAIL_CLIENTS FROM CUSTOMERS WHERE CTYPE = 'R' AND BRID LIKE 'HDFC%' GROUP BY PAR_ACC")

# 5. Get the list of all the corporate cients and their corresponding retail customers.
curs.display('''SELECT K.CNAME AS RETAIL_CUSTOMERS,K.PAR_ACC AS CORPORATE_CLIENTS,K.CTYPE FROM 
            (SELECT *,ROW_NUMBER() OVER(PARTITION BY PAR_ACC ) FROM CUSTOMERS WHERE CTYPE = 'R') K''')

# 6. Which corporate client has the least number of employees (retail clients in bank's branch) in each bank.
curs.display('''SELECT Z.BID,Z.PAR_ACC AS CORP_ACCOUNT,MIN(Z.TOTAL_EMP) NO__OFEMP  FROM (SELECT *,COUNT(K.CTYPE) OVER(PARTITION BY K.BID,K.PAR_ACC) AS TOTAL_EMP FROM 
            (SELECT C.CNAME,C.CTYPE,C.PAR_ACC,B.BID FROM CUSTOMERS C JOIN BRANCH_DETAILS B ON C.BRID = B.BRID) K
            WHERE K.CTYPE = 'R') Z
            GROUP BY Z.BID,Z.PAR_ACC 
            ''')
