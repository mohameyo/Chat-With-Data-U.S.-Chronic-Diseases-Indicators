
DROP TABLE IF EXISTS StratificationCategories, Stratifications, Locations, DataSource, Questions, Topics, DataTypes, SurveyData;

CREATE TABLE Locations (
    LocationID SERIAL PRIMARY KEY,
    LocationAbbr VARCHAR(10),
    LocationDesc VARCHAR(255),
    GeoLocation VARCHAR(255)
);

CREATE TABLE DataTypes (
    DataTypeID SERIAL PRIMARY KEY,
    DataValueType VARCHAR(100),
    DataValueUnit VARCHAR(100)
);

CREATE TABLE Topics (
    TopicID SERIAL PRIMARY KEY,
    Topic VARCHAR(255)
);

CREATE TABLE Questions (
    QuestionID SERIAL PRIMARY KEY,
    Question VARCHAR(500),
    TopicID INT REFERENCES Topics(TopicID)
);

CREATE TABLE DataSource (
    DataSourceID SERIAL PRIMARY KEY,
    DataSource VARCHAR(255)
);

CREATE TABLE StratificationCategories (
    StratificationCategoryID SERIAL PRIMARY KEY,
    StratificationCategory VARCHAR(255)
);

CREATE TABLE Stratifications (
    StratificationID SERIAL PRIMARY KEY,
    Stratification VARCHAR(255),
    StratificationCategoryID INT REFERENCES StratificationCategories(StratificationCategoryID)
);

CREATE TABLE SurveyData (
    SurveyDataID SERIAL PRIMARY KEY,
    YearStart INT,
    YearEnd INT,
    LocationID INT REFERENCES Locations(LocationID),
    DataSourceID INT REFERENCES DataSource(DataSourceID),
    QuestionID INT REFERENCES Questions(QuestionID),
    DataValue VARCHAR(100),
    DataValueAlt NUMERIC,
    DataValueFootnoteSymbol VARCHAR(10),
    DatavalueFootnote TEXT,
    LowConfidenceLimit NUMERIC,
    HighConfidenceLimit NUMERIC,
    DataTypeID INT REFERENCES DataTypes(DataTypeID),
    StratificationID INT REFERENCES Stratifications(StratificationID)
);


-- select * FROM chronic_disease_indicators where topic like 'Cancer' LIMIT 10;