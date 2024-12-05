#imports

#models
# with open("lgb.pkl", "rb") as f:
#     lgb_model = pickle.load(f)
# test_data=pd.read_csv("test_data.csv")
# if 'Unnamed: 0' in test_data.columns:
#     test_data = test_data.drop(columns=['Unnamed: 0'])
# test_labels=pd.read_csv("test_labels.csv")
# if 'Unnamed: 0' in test_labels.columns:
#     test_labels = test_labels.drop(columns=['Unnamed: 0'])
# row_count = len(test_data)
# test_val=randint(0,row_count-1)
# data=test_data.iloc[test_val] 
# data_2d= np.array(data).reshape(1, -1)
# label=test_labels.iloc[test_val]

def predict(model,row):
    val=True if model.predict(row)==True else False
    return val
# # #predictions
# # lgb_val=1 if lgb_model.predict(data_2d)==True else 0
# # log_val=1 if log_model.predict(data_2d)==True else 0
# rfc_val=True if rfc_model.predict(data_2d)==True else False
# weight=(rfc_val)
# print(weight)
# print("\n",label['Churn_Yes'])