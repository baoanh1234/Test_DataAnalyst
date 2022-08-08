import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Data Analyst_Hiring Case Study")
st.header("Candidate: Nguyen Trung Bao Anh")
st.markdown("Python code here is basic and short, see file notebook to more detail. Thank you")

st.header("1. Read file")
url = 'https://drive.google.com/file/d/1ExC6u_yYoPbt4VevEzY9Rvijw2x8KGPG/view'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path, parse_dates = ["date_of_birth","txn_ts"])
st.code("import pandas as pd\n\
df = pd.read_csv(txn_history_dummysample.csv)")
st.text("Show dataframe")
st.code("df.head(5)")
st.dataframe(df.head(5))

st.header("2. Transaction per user")
st.text("Group by ID and then count by ID")
df_account_id = df.groupby(by=["account_id"], as_index = False).count()
df_account_id = df_account_id[["account_id", "txn_type_code"]].rename(columns = {"txn_type_code":"Count"})
data = df_account_id["Count"]

st.code('df_account_id = df.groupby(by=["account_id"], as_index = False).count()')
st.text("Average of Transactions:")
st.code("data.mean()")
st.text("The middle number in an ordered data set of Transactions:")
st.code("data.median()")
st.text("Transactions appear most often:")
st.code("data.mode()")
st.text("Visualize on chart to know the histogram of transaction per user")
fig, ax = plt.subplots()
ax.hist(data, bins=100, density=False, alpha=0.5, color='b',range = (0,200))
plt.title('Transactions per user')
plt.xlabel('Transactions')
plt.ylabel('Frequency of appearance')
plt.text(7,1500,"Average of Transactions: 29.23")
plt.text(7,1350,"The middle number in an ordered data set of Transactions: 8")
plt.text(7,1200,"Transactions appear most often: 2")
st.pyplot(fig)

st.subheader("Conclusion")
st.text(" - Almost transaction per user is between 0 and 100")
st.text(" - Transaction of each user > 100 rarely appear")

st.header("3. Average of amount per users")
st.text("Group by ID and then calculate mean by ID")
st.code('df_txn_amount = df.groupby(by=["account_id"], as_index = False).mean()')
st.text("Average of Amount per users: ")
st.code('data_amount.mean()')
st.text("The middle number in an ordered data set of average amount per users: ")
st.code('data_amount.median()')
st.text("Amount per users appear most often: ")
st.code('data_amount.mode()')
st.text("Visualize on chart to know the histogram of average amount per user")

df_txn_amount = df.groupby(by=["account_id"], as_index = False).mean()
df_txn_amount = df_txn_amount[["account_id", "txn_amount"]].rename(columns = {"txn_amount":"Amount"})
data_amount = df_txn_amount["Amount"]
fig, ax = plt.subplots()
ax.hist(data_amount, bins=100, density=False, alpha=0.5, color='b', range = (-100000,100000))
plt.title('Average of amount per user')
plt.xlabel('Average of amount')
plt.ylabel('Frequency of appearance')
plt.text(-100000,700,"Average of amount per users: 772776")
plt.text(-100000,600,"The middle number in an ordered data set of avg amount per users: 1333")
plt.text(-100000,500,"Avg Amount per users appear most often: 1000")
plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
plt.xticks(rotation = 90)
st.pyplot(fig)
st.subheader("Conclusion")
st.text(" - Almost amount per user is between -50000 and 50000")
st.text(" - 1000 is the most avg amount")

st.header("4. Frequency of transaction by age")
st.text("Creat new column 'year' from column 'date_of_birth ")
st.text("Group by year and then count by year")
st.code("df['year'] = df['date_of_birth'].dt.year\n\
df_year_count = df.groupby(by=['year'], as_index = False).count()")
df['year'] = df['date_of_birth'].dt.year
df_year_count = df.groupby(by=["year"], as_index = False).count()
df_year_count = df_year_count[["year","account_id"]].rename(columns = {"account_id":"Transactions"})

fig, ax = plt.subplots()
ax.bar(df_year_count["year"],df_year_count["Transactions"])
plt.title('Transactions per user by age')
plt.xlabel('Year of birth')
plt.ylabel('Transactions')
st.pyplot(fig)
st.subheader("Conclusion")
st.text(" - Transactions of people between 20 and 30 ages are more significant than people older than 30 ages")

st.header("5. Average amount of each transaction by age")
st.text("Group by year and then sum amount by year")
st.code("df_year_sum = df.groupby(by=['year'], as_index = False).sum()")
df_year_sum = df.groupby(by=["year"], as_index = False).sum()
df_year_sum = df_year_sum[["year","txn_amount"]].rename(columns = {"txn_amount":"Amount"})
st.text("Calculate average amount of each transaction by age")
st.code('df_avg["avg"] = df_avg["Amount"]/df_avg["Transactions"]')
df_avg = pd.merge(df_year_sum, df_year_count)
df_avg["avg"] = df_avg["Amount"]/df_avg["Transactions"]

fig, ax = plt.subplots()
ax.bar(df_avg["year"],df_avg["avg"])
plt.title('Average of each transaction by age')
plt.xlabel('Year of birth')
plt.ylabel('Amount')
plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
st.pyplot(fig)
st.subheader("Conclusion")
st.text(" - People older than 30 ages have big money transactions than younger people")

st.header("6. Fequency of type code")
df_type_count = df.groupby(by=["txn_type_code"], as_index = False).count()
df_type_count = df_type_count[["txn_type_code", "account_id"]].rename(columns = {"account_id":"Count"})
st.text("Group by type code and then count")
st.code('f_type_count = df.groupby(by=["txn_type_code"], as_index = False).count()')

fig, ax = plt.subplots()
ax.bar(df_type_count["txn_type_code"],df_type_count["Count"])
plt.title('Fequency of type code')
plt.xlabel('Type code')
plt.ylabel('Frequency')
st.pyplot(fig)
st.subheader("Conclusion")
st.text(" - The type code 1 and 2 that appear most often")

st.header("7. Transactions per month")
st.text("Creat new column 'month' from column 'txn_ts")
st.text("Group by month and then count by month")
st.code("df['month_of_transaction'] = df['txn_ts'].dt.month\n\
f_month = df.groupby(by=['month_of_transaction'], as_index = False).count()")
df['month_of_transaction'] = df['txn_ts'].dt.month
df_month = df.groupby(by=["month_of_transaction"], as_index = False).count()
df_month = df_month[["month_of_transaction", "account_id"]].rename(columns = {"account_id":"Count"})

fig,ax = plt.subplots()
plt.bar(df_month["month_of_transaction"], df_month["Count"], width = 0.3)
plt.title('Transactions per month')
plt.xlabel('Month')
plt.ylabel('Frequency')
st.pyplot(fig)
st.subheader("Conclusion")
st.text(" - Total transactions on march are higher than the others")

st.header("Conclusion")
st.text(" - Almost transaction per user is between 0 and 100")
st.text(" - Transaction of each user > 100 rarely appear")
st.text(" - Almost amount per user is between -50000 and 50000")
st.text(" - 1000 is the most avg amount per user")
st.text(" - Transactions of people between 20 and 30 ages are more significant than people older than 30 ages")
st.text(" - People older than 30 ages have big money transactions than younger people")
st.text(" - The type code 1 and 2 that appear most often")
st.text(" - Total transactions on march are higher than the others")


