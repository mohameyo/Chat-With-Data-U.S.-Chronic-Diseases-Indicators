from psycopg2 import sql
import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

df = pd.read_csv(
    '../data/U.S._Chronic_Disease_Indicators__CDI_.csv', low_memory=False)

# After you have created the database which we conviniently named "cdc_chronic_disease_indicators"
# load credentials from the .env file and Connect to the database
load_dotenv("../.env", override=True)
DBUSER = os.environ["DBUSER"]
DBPASS = os.environ["DBPASS"]
DBHOST = os.environ["DBHOST"]
DBNAME = os.environ["DBNAME"]


params = {
    'database': DBNAME,
    'user': DBUSER,
    'password': DBPASS,
    'host': DBHOST,
    'port': 5432
}

# Connect to your postgres DB
conn = psycopg2.connect(**params)

# Open a cursor to perform database operations
cur = conn.cursor()


# Populate Locations
locations_data = df[['LocationAbbr', 'LocationDesc', 'GeoLocation']
                    ].drop_duplicates().reset_index(drop=True).to_dict(orient='records')

for loc in locations_data:
    cur.execute(
        sql.SQL("INSERT INTO Locations (LocationAbbr, LocationDesc, GeoLocation) VALUES (%s, %s, %s) RETURNING LocationID;"),
        (loc['LocationAbbr'], loc['LocationDesc'], loc['GeoLocation'])
    )
    loc['LocationID'] = cur.fetchone()[0]

# Commit transaction
conn.commit()

print("Locations table populated")

# Populate data types
data_types = df[['DataValueType', 'DataValueUnit']].drop_duplicates(
).reset_index(drop=True).to_dict(orient='records')

for loc in data_types:
    cur.execute(
        sql.SQL(
            "INSERT INTO DataTypes (DataValueType, DataValueUnit) VALUES (%s, %s) RETURNING DataTypeID;"),
        (loc['DataValueType'], loc['DataValueUnit'])
    )
    loc['DataTypeID'] = cur.fetchone()[0]

# Commit transaction
conn.commit()
print("DataTypes table populated")
# Populate Topics

topics = df[['Topic']].drop_duplicates().to_dict(orient='records')
for loc in topics:
    cur.execute(
        sql.SQL("INSERT INTO Topics (Topic) VALUES (%s) RETURNING TopicID;"),
        (loc['Topic'],)
    )
    loc['TopicID'] = cur.fetchone()[0]

# Commit transaction
conn.commit()
print("Topics table populated")
# Populate Question
questions = df[['Question', 'Topic']].drop_duplicates(
).reset_index().to_dict(orient='records')

for loc in questions:
    # get topicId from Topics tablebased on topic
    topicID = cur.execute(
        sql.SQL("SELECT TopicID FROM Topics WHERE Topic = %s;"),
        (loc['Topic'],)
    )
    cur.execute(
        sql.SQL(
            "INSERT INTO Questions (Question, TopicID) VALUES (%s, %s) RETURNING QuestionID;"),
        (loc['Question'], topicID)
    )

    loc['QuestionID'] = cur.fetchone()[0]

# Commit transaction
conn.commit()
print("Questions table populated")

# populate DataSources
data_sources = df[['DataSource']].drop_duplicates(
).reset_index(drop=True).to_dict(orient='records')

for loc in data_sources:
    cur.execute(
        sql.SQL(
            "INSERT INTO DataSource (DataSource) VALUES (%s) RETURNING DataSourceID;"),
        (loc['DataSource'],)
    )
    loc['DataSourceID'] = cur.fetchone()[0]

# Commit transaction
conn.commit()
print("DataSources table populated")
# populate StratificationCategory1
stratification_categories = df[['StratificationCategory1']].drop_duplicates(
).reset_index(drop=True).to_dict(orient='records')

for loc in stratification_categories:
    cur.execute(
        sql.SQL("INSERT INTO StratificationCategories (StratificationCategory) VALUES (%s) RETURNING StratificationCategoryID;"),
        (loc['StratificationCategory1'],)
    )
    loc['StratificationCategoryID1'] = cur.fetchone()[0]

# Commit transaction
conn.commit()
print("StratificationCategories table populated")
# populate Stratification1
stratifications = df[['Stratification1', 'StratificationCategory1']].drop_duplicates(
).reset_index(drop=True).to_dict(orient='records')

for loc in stratifications:
    # get stratificationCategory1ID from StratificationCategories table based on StratificationCategory1
    stratificationCategoryID = cur.execute(
        sql.SQL("SELECT StratificationCategoryID FROM StratificationCategories WHERE StratificationCategory = %s;"),
        (loc['StratificationCategory1'],)
    )
    cur.execute(
        sql.SQL("INSERT INTO Stratifications (Stratification, StratificationCategoryID) VALUES (%s, %s) RETURNING StratificationID;"),
        (loc['Stratification1'], stratificationCategoryID)
    )
    loc['Stratification1ID'] = cur.fetchone()[0]

# Commit transaction
conn.commit()
print("Stratifications table populated")
# populate SurveyData
survey_data = df[['YearStart', 'YearEnd', 'LocationAbbr', 'DataSource', 'Question', 'DataValueType', 'DataValue', 'DataValueUnit', 'DataValueAlt', 'DataValueFootnoteSymbol',
                  'DatavalueFootnote', 'LowConfidenceLimit', 'HighConfidenceLimit', 'StratificationCategory1', 'Stratification1']].reset_index(drop=True).to_dict(orient='records')

for loc in survey_data:
    # get LocationID from Locations table based on LocationAbbr
    LocationID = cur.execute(
        sql.SQL("SELECT LocationID FROM Locations WHERE LocationAbbr = %s;"),
        (loc['LocationAbbr'],)
    )
    # get DataSourceID from DataSources table based on DataSource
    DataSourceID = cur.execute(
        sql.SQL("SELECT DataSourceID FROM DataSource WHERE DataSource = %s;"),
        (loc['DataSource'],)
    )
    # get QuestionID from Questions table based on Question
    QuestionID = cur.execute(
        sql.SQL("SELECT QuestionID FROM Questions WHERE Question = %s;"),
        (loc['Question'],)
    )
    # get DataTypeID from DataTypes table based on DataValueType
    DataTypeID = cur.execute(
        sql.SQL("SELECT DataTypeID FROM DataTypes WHERE DataValueType = %s;"),
        (loc['DataValueType'],)
    )
    # get StratificationID from Stratifications table based on Stratification
    Stratification1ID = cur.execute(
        sql.SQL(
            "SELECT StratificationID FROM Stratifications WHERE Stratification = %s;"),
        (loc['Stratification1'],)
    )
    cur.execute(
        sql.SQL("INSERT INTO SurveyData (YearStart, YearEnd, LocationID, DataSourceID, QuestionID, DataValue, DataValueAlt, DataValueFootnoteSymbol, DatavalueFootnote, LowConfidenceLimit, HighConfidenceLimit, DataTypeID, StratificationID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s) RETURNING SurveyDataID;"),
        (loc['YearStart'], loc['YearEnd'], LocationID, DataSourceID, QuestionID, loc['DataValue'], loc['DataValueAlt'], loc['DataValueFootnoteSymbol'],
         loc['DatavalueFootnote'], loc['LowConfidenceLimit'], loc['HighConfidenceLimit'], DataTypeID, Stratification1ID)
    )
# Commit transaction
conn.commit()
print('SurveyData table populated')
# Close communication with the database
cur.close()
conn.close()
