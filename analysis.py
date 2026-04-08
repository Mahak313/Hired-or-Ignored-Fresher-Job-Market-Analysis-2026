import pandas as pd 



# STEP 1 LOAD DATA (survey_cleaned.csv)
survey=pd.read_csv(r'D:\Data Analyst\Fresher Skills Gap Analysis\survey_cleaned.csv')




# STEP 2 LOAD DATA (jobs_data_roles_cleaned.csv)
jobs=pd.read_csv(r'D:\Data Analyst\Fresher Skills Gap Analysis\jobs_data_roles_cleaned.csv')


#STEP 3 DATA LOAD CONFIRMATION
print("Survey data loaded successfully.", survey.shape[0])
print("Jobs data loaded successfully.", jobs.shape[0])
print("both files loaded successfully.")



# ============================================
# ANALYSIS 1 - INTERVIEW REALITY
# Calculate the percentage of freshers who got an interview
# ============================================

interview_count=survey["Interview_Calls"].value_counts()
interview_percentage=survey['Interview_Calls'].value_counts(normalize=True)*100
print("="*50)
print("ANALYSIS 1- INTERVIEW REALITY")
print("="*50)
print("how many freshers got an interview:",interview_count)
print("percentage of freshers who got an interview:",interview_percentage.round(2))
#Insight 🎯
# "38% freshers ko ek bhi interview nahi aaya — despite months of applying!"


# ============================================
# ANALYSIS 2 - JOB SEARCH DURATION
# ============================================

duration_counts=survey['Job_Search_Duration'].value_counts()
duration_percent=survey['Job_Search_Duration'].value_counts(normalize=True)*100
print("="*50)
print("ANALYSIS 2 - JOB SEARCH DURATION")
print("="*50)
print("Job search duration distribution:")
print(duration_counts)
print("Percentage of freshers by job search duration:")
print(duration_percent.round(2))
#Insight 🎯

#"46% freshers sirf 0-3 months se search kar rahe hain — but 38% ko abhi bhi koi interview nahi aaya!"


# ============================================
# ANALYSIS 3 - PLATFORMS USED

# ============================================
all_platforms=survey['Platforms_Used'].str.split(',').explode().str.strip()

platform_counts=all_platforms.value_counts()
platform_percent=all_platforms.value_counts(normalize=True)*100
print("="*50)
print("ANALYSIS 3 - PLATFORMS USED")
print("="*50)

print("Most used platforms for job search:",platform_counts)
print("Percentage of freshers using each platform:",platform_percent.round(2))
#Insight 🎯
#"LinkedIn sabse popular platform hai — 28% freshers use karte hain — followed by Naukri at 22.86%"



# ============================================
# ANALYSIS 4 - RESUME REVIEW IMPACT
# ============================================

print("="*50)
print("ANALYSIS 4 - RESUME REVIEW IMPACT")
print("="*50)

# Resume reviewed vs interview calls
resume_impact=survey.groupby('Resume_Reviewed')['Interview_Calls'].value_counts()
resume_percent=survey.groupby('Resume_Reviewed')['Interview_Calls'].value_counts(normalize=True)*100
print("Resume review vs interview calls:")
print(resume_impact)

print("Percentage distribution of interview calls by resume review status:")
print(resume_percent.round(2))
#Insight 🎯
#"Jo freshers ne resume professionally review karaya — unhe 78% interview calls aaye! Jo nahi karaya — 58% ko koi interview nahi aaya!"




# ============================================
# ANALYSIS 5 - MARKET SKILLS DEMAND

# ============================================


print("="*50)
print("ANALYSIS 5 - MARKET SKILLS DEMAND")
print("="*50)

print("Skills column sample:")
print(jobs['Skills'].head(3))

skills_split = []

for skill_row in jobs['Skills']:
    individual_skills = str(skill_row).split(';')
    for skill in individual_skills:
        clean_skill = skill.strip().lower()
        if clean_skill != '' and clean_skill != 'nan':
            skills_split.append(clean_skill)

import pandas as pd
skills_series = pd.Series(skills_split)

job_skills_count = skills_series.value_counts().head(15)

print("\nTop 15 Skills Market Demand:")
print(job_skills_count)

#Insight 🎯
#"SQL, Power BI, Tableau aur Python — yeh 4 skills market mein sabse zyada demanded hain Data Analyst roles ke liye!"
#"Market mein Snowflake (25), PostgreSQL (22), Hadoop (21) bhi maange ja rahe hain — jo mostly freshers jaante hi nahi!"


# ============================================
# ANALYSIS 6 - FRESHER SKILLS

# ============================================

print("="*50)
print("ANALYSIS 6 - FRESHER SKILLS")
print("="*50)

fresher_skills_list=[]
for skill_row in survey['Skills']:
   individual_skills=str(skill_row).split(',')
   for skill in individual_skills:
      clean_skill=skill.strip().lower()
      if clean_skill !='' and clean_skill!= 'nan' and clean_skill!='unknown':
         fresher_skills_list.append(clean_skill)

#chnge list to series
fresher_skills_series=pd.Series(fresher_skills_list)

fresher_skills_count=fresher_skills_series.value_counts()
print(fresher_skills_count)

#Insight 🎯
#"Freshers ke paas Excel (48) aur SQL (46) sabse zyada hain — but R sirf 5 freshers ke paas hai!"
#"16 freshers ML seekh rahe hain — but Data Analyst roles mein ML ki demand bahut kam hai — wrong skill pe focus ho raha hai!"


# ============================================
# ANALYSIS 7 - SKILLS GAP
# Market demand vs Fresher skills compare
# ============================================

print("="*50)
print("ANALYSIS 7 - SKILLS GAP")
print("="*50)

#COMMON SKILLS LIST
common_skills=['sql','python','power bi', 'tableau','excel','r','ml']

#MARKET DEMAND DICTIONARY
market_demand={}
for skill in common_skills:
    count=skills_series[skills_series==skill].count()
    market_demand[skill]=count

#FRESHER SKILLS DICTIONARY
fresher_demand={}
for skill in common_skills:
    count=fresher_skills_series[fresher_skills_series==skill].count()
    fresher_demand[skill]=count

#CREATE DATAFRAME FOR COMPARISON
gap_df=pd.DataFrame({
    'Skill':common_skills,
    'Market_Demand':[market_demand[s] for s in common_skills],
    'Fresher_Has':[fresher_demand[s] for s in common_skills]
})

#CALCULATE GAP
gap_df['Gap']=gap_df['Market_Demand']-gap_df['Fresher_Has']

#SHORT BY GAP
gap_df=gap_df.sort_values('Gap',ascending=False)
print(gap_df)

# Save the results
gap_df.to_csv(
    r'D:\Data Analyst\Fresher Skills Gap Analysis\skills_gap.csv',
    index=False
)

print("\nFinal Skills Gap Table:")
print(gap_df)
print("\n✅ Skills gap saved as skills_gap.csv!")
#Insight 🎯
#"Tableau market mein 54 jobs mein maanga ja raha hai — but sirf 28 freshers ke paas hai — 26 ka gap!"
#"R language 30 jobs mein required hai — but sirf 5 freshers ke paas hai — almost nobody has it!"
#"48 freshers ke paas Excel hai — but market mein sirf 14 jobs mein maanga — freshers wrong skill pe focus kar rahe hain!"
#"16 freshers ML seekh rahe hain — but Data Analyst market mein ML ki demand nahi — time waste ho raha hai!"
