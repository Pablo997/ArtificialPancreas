import pandas as pd


def saveCSV():
	entries.to_csv('entries.csv')
	deviceStatus.to_csv('devicestatus.csv')
	treatments.to_csv('treatments.csv')

entries = pd.read_json('entries.json', lines=True)
deviceStatus = pd.read_json('devicestatus.json', lines=True)
treatments = pd.read_json('treatments.json', lines=True)

deviceStatus = pd.concat([deviceStatus.drop(['pump'], axis=1), deviceStatus['pump'].apply(pd.Series)], axis=1)
deviceStatus = pd.concat([deviceStatus.drop(['iob'], axis=1), deviceStatus['iob'].apply(pd.Series)], axis=1)
deviceStatus = pd.concat([deviceStatus.drop(['status'], axis=1), deviceStatus['status'].apply(pd.Series)], axis=1)
deviceStatus = deviceStatus.drop([0], axis=1)

#saveCSV()