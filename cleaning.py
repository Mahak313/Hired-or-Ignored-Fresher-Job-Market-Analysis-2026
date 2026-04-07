import pandas as pd 

# LOAD DATA 1 - SURVEY DATA
#----------------------------------------------
survey = pd.read_csv(r'D:\Data Analyst\Fresher Skills Gap Analysis\Fresher_Survey_Data.csv')
print(survey.head())


# LOAD DATA 2 - JOBS DATA
#----------------------------------------------
jobs = pd.read_csv(r'D:\Data Analyst\Fresher Skills Gap Analysis\job_dataset.csv')
print(jobs.head())
print("Survey Data:", survey.shape)
print("Jobs Data:", jobs.shape)


# HERE WE WILL EXTRACT ONLY DATA-RELATED ROLES FROM THE JOBS DATA
data_roles = [
    'Data Analyst',       # DA roles
    'Business Analyst',   # BA roles
    'Data Scientist',     # DS roles
    'Data Engineer',      # DE roles
    'MIS Analyst',        # MIS roles
    'Reporting Analyst',  # Reporting roles
    'BI Analyst',         # BI roles
    'Analytics'           # Any analytics role
]
# Create a regex pattern to match any of the data roles in the job titles
pattern = '|'.join(data_roles)
jobs_filtered = jobs[
    jobs['Title'].str.contains(pattern, case=False, na=False)
]


print("\nTotal Jobs Before Filter:", jobs.shape[0])
print("Data Role Jobs After Filter:", jobs_filtered.shape[0])

print("\nJob Titles Found:")
print(jobs_filtered['Title'].value_counts())

jobs_filtered.to_csv(
    r'D:\Data Analyst\Fresher Skills Gap Analysis\jobs_data_roles.csv',
    index=False
)

print("\n✅ Data roles filter ho gaye!")
print("✅ New file save hui: jobs_data_roles.csv")


# ============================================
# SURVEY DATA CLEANING
# ============================================
# Step 1 - CHNAGE COLUMN NAMES 
# ============================================
survey.columns = [
    'Timestamp',
    'Graduation_Year',
    'Degree',
    'Job_Search_Duration',
    'Applications_Per_Day',
    'Interview_Calls',
    'Skills',
    'Biggest_Challenge',
    'Resume_Reviewed',
    'Total_Companies_Applied',
    'Platforms_Used',
    'Target_Role'
]

print(survey.columns.tolist())

# Step 2 -  CHECK  FOR MISSING VALUES 
# ============================================
print("\nMissing Values:")
print(survey.isnull().sum())

# Step 3 - Duplicate rows check karo
# ============================================
print("\nDuplicate Rows:", survey.duplicated().sum())

# Step 4 - Data ka overview dekho
# ============================================
print("\nSurvey Data Overview:")
print(survey.head())

# Step 5 - delete empty rows
# ============================================
survey=survey.dropna(how='all')
print("\n✅ Empty rows deleted!", survey.shape)

# Step 6 - fill missing values with 'Unknown' 
# ============================================
survey=survey.fillna('UnKnown')
print("\n✅ Missing values filled with 'Unknown'!", survey.isnull().sum())

# Step 7 - save cleaned survey data
# ============================================
survey.to_csv(
    r'D:\Data Analyst\Fresher Skills Gap Analysis\survey_cleaned.csv',index=False)
print("\n✅ survey cleaned and saved as survey_cleaned.csv!")





# ============================================
# jobs data role  DATA CLEANING
# ============================================
# Step 1 - jobs_data_roles (LOAD DATA)
# ============================================
jobs_clean=pd.read_csv(r'D:\Data Analyst\Fresher Skills Gap Analysis\jobs_data_roles.csv')
print(jobs_clean.head())





# Step 2 - CHECK FOR MISSING VALUES
# ============================================
print("\n missing values:", jobs_clean.isnull().sum())


# Step 3- CHECK FOR DUPLICATE ROWS AND DELETE THEM
# ============================================
print("\n duplicate rows before deletion :",jobs_clean.duplicated().sum())
jobs_clean=jobs_clean.drop_duplicates()
print("\n duplicate rows after deletion :",jobs_clean.duplicated().sum())
print("\n✅ jobs after removing duplicaates:",jobs_clean.shape[0])

# Step 4- REMOVE UNNECESSARY COLUMNS
# ============================================
jobs_clean=jobs_clean.drop(
    columns=['JobID','Responsibilities']
)
print("\n ✅ jobs columns after cleaning ")
print(jobs_clean.columns .tolist())



# Step 5 - save cleaned jobs data
# ============================================
jobs_clean.to_csv(r'D:\Data Analyst\Fresher Skills Gap Analysis\jobs_data_roles_cleaned.csv',index=False)
print("\n jobs cleaned and saved as jobs_cleaned.csv")