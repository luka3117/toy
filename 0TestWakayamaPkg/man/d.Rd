\name{d}
\alias{d}
\docType{data}
\title{
和歌山データ
}
\description{
和歌山データ
}
\usage{data("d")}
\format{
  A data frame with 94 observations on the following 168 variables.
  \describe{
    \item{\code{key}}{a numeric vector}
    \item{\code{pref.id}}{a numeric vector}
    \item{\code{sex}}{a character vector}
    \item{\code{pref.E}}{a character vector}
    \item{\code{pref.A}}{a character vector}
    \item{\code{pref.J}}{a character vector}
    \item{\code{pop}}{a character vector}
    \item{\code{Treatment_rate_Hospitalization_Malignant_neoplasm_2017}}{a numeric vector}
    \item{\code{Medical_treatment_rate_hospitalization_heart_dz_2017}}{a numeric vector}
    \item{\code{Treatment_rate_Hospitalization_Cerebrovascular_dz_2017}}{a numeric vector}
    \item{\code{Treatment_rate_Outpatient_Malignant_neoplasm_2017}}{a numeric vector}
    \item{\code{Treatment_rate_outpatient_heart_dz_2017}}{a numeric vector}
    \item{\code{Treatment_rate_Outpatient_Cerebrovascular_dz_2017}}{a numeric vector}
    \item{\code{Num_of_hospitals_2019}}{a numeric vector}
    \item{\code{Num_of_clinics_2019}}{a numeric vector}
    \item{\code{Num_of_certified_cancer_doctors_2020}}{a numeric vector}
    \item{\code{Num_of_cardiologists_2020}}{a numeric vector}
    \item{\code{Num_of_endoscopists_2020}}{a numeric vector}
    \item{\code{Mortality_Malignant_Neoplasm_2018_Under_75}}{a numeric vector}
    \item{\code{Book_purchase_price_2019}}{a numeric vector}
    \item{\code{LE_2015}}{a numeric vector}
    \item{\code{HLE_2016}}{a numeric vector}
    \item{\code{Under_75_Adjusted_Mortality_Evil_Neoplasms_2019}}{a numeric vector}
    \item{\code{mortality_heart_dz_2015}}{a numeric vector}
    \item{\code{mortality_cerebrovascular_dz_2015}}{a numeric vector}
    \item{\code{pop_over_60_2015}}{a numeric vector}
    \item{\code{Learn_rate_2016}}{a numeric vector}
    \item{\code{Read_rate_2016}}{a numeric vector}
    \item{\code{pop_Young_pop_Ratio_2020}}{a numeric vector}
    \item{\code{pop_oldElderly_pop_Ratio_2020}}{a numeric vector}
    \item{\code{pop_Working_Age_pop_Ratio_2020}}{a numeric vector}
    \item{\code{pop_Rough_Mortality_2020}}{a numeric vector}
    \item{\code{pop_Double_income_household_ratio_2020}}{a numeric vector}
    \item{\code{Natural_environment_annual_avg_temperature}}{a numeric vector}
    \item{\code{Natural_environment_annual_avg_relative_humidity}}{a numeric vector}
    \item{\code{Natural_environment_annual_rain}}{a numeric vector}
    \item{\code{Natural_environment_annual_Num_of_snow_days}}{a numeric vector}
    \item{\code{Economic_pref_income}}{a numeric vector}
    \item{\code{Admin_base_Financial_strength_index}}{a numeric vector}
    \item{\code{Admin_base_balance_ratio}}{a numeric vector}
    \item{\samp{Admin_infrastructure_living_protection_cost_ratio_(prefectural_finance)}}{a numeric vector}
    \item{\samp{Admin_infrastructure_Edu_cost_ratio_(prefectural_finance)}}{a numeric vector}
    \item{\code{Edu_Ptc_of_university_graduate_students_with_a_final_academic_background}}{a numeric vector}
    \item{\code{Labor_primary_industry_emp_ratio}}{a numeric vector}
    \item{\code{Labor_secondary_industry_emp_ratio}}{a numeric vector}
    \item{\code{Labor_tertiary_industry_emp_ratio}}{a numeric vector}
    \item{\code{Labor_Unemp_rate}}{a numeric vector}
    \item{\code{Num_of_libraries}}{a numeric vector}
    \item{\code{Num_of_general_clinics}}{a numeric vector}
    \item{\code{Sports_Participant_Rate}}{a numeric vector}
    \item{\code{Travel_Rate}}{a numeric vector}
    \item{\code{Residence_owner_ratio}}{a numeric vector}
    \item{\code{Residence_house_ratio}}{a numeric vector}
    \item{\code{Residence_water_supply_pop_ratio}}{a numeric vector}
    \item{\code{Residence_sewerage_ratio}}{a numeric vector}
    \item{\code{Volunteer_Activity_Participant_Rate}}{a numeric vector}
    \item{\samp{Residential_city_park_area_(per_pop)}}{a numeric vector}
    \item{\code{Residence_Num_of_city_parks}}{a numeric vector}
    \item{\code{HM_Num_of_general_hospitals}}{a numeric vector}
    \item{\code{Residence_road_pavement_rate}}{a numeric vector}
    \item{\code{Residence_simachi_pavement_rate}}{a numeric vector}
    \item{\code{HM_Num_of_general_dental_clinics_per_100k_pop}}{a numeric vector}
    \item{\code{HM_Num_of_doctors_engaged_in_medical_facilities_per_100k_pop}}{a numeric vector}
    \item{\code{HM_Num_of_public_health_nurses_per_100k_pop}}{a numeric vector}
    \item{\code{Safety_Num_of_traffic_accidents_per_100k_pop}}{a numeric vector}
    \item{\code{Household_actual_income}}{a numeric vector}
    \item{\code{Household_consumption_expenditure}}{a numeric vector}
    \item{\code{Household_Edu_cost_ratio}}{a numeric vector}
    \item{\code{Household_Liberal_Arts_and_Entertainment_Expenditure_Ratio}}{a numeric vector}
    \item{\code{Household_Savings}}{a numeric vector}
    \item{\code{Household_Smartphone_ownership_quantity}}{a numeric vector}
    \item{\code{Household_PC_ownership_quantity}}{a numeric vector}
    \item{\code{Household_Car_ownership_quantity}}{a numeric vector}
    \item{\code{Household_Tablet_terminal_Ownership_quantity}}{a numeric vector}
    \item{\code{pop_Household_Ratio_of_elderly_single_person_households}}{a numeric vector}
    \item{\code{Sports_Activity_rate}}{a numeric vector}
    \item{\code{Sports_Activity_Rate_Training_with_Equipment}}{a numeric vector}
    \item{\code{Sports_Activity_rate_walking}}{a numeric vector}
    \item{\code{Travel_Traveling_Tourism_Activity_Rate}}{a numeric vector}
    \item{\code{Travel_Rate}}{a numeric vector}
    \item{\code{Traveling_rate}}{a numeric vector}
    \item{\code{Tourism_Rate}}{a numeric vector}
    \item{\code{Volunteer_Activity_Rate_total}}{a numeric vector}
    \item{\code{Volunteer_town_development}}{a numeric vector}
    \item{\code{Volunteer_International_Cooperation}}{a numeric vector}
    \item{\code{Volunteer_health_and_medical}}{a numeric vector}
    \item{\code{Volunteer_for_the_Elderly}}{a numeric vector}
    \item{\code{Volunteer_for_Persons_with_Disabilities}}{a numeric vector}
    \item{\code{Volunteer_for_Children}}{a numeric vector}
    \item{\code{Hobbies_Total}}{a numeric vector}
    \item{\code{Hobbies_Gardening}}{a numeric vector}
    \item{\code{Hobbies_Sports_View}}{a numeric vector}
    \item{\code{Hobbies_Read}}{a numeric vector}
    \item{\code{Self_development_rate}}{a numeric vector}
    \item{\code{Self_development_art_culture}}{a numeric vector}
    \item{\code{Self_development_Eng}}{a numeric vector}
    \item{\samp{Self_development_languages_​​other_than_English}}{a numeric vector}
    \item{\code{Self_development_PC_etc}}{a numeric vector}
    \item{\code{Volunteer_for_Life_Safe}}{a numeric vector}
    \item{\code{Volunteer_environmental_activities}}{a numeric vector}
    \item{\code{Volunteer_disaster_activities}}{a numeric vector}
    \item{\code{Hypertension_Hospitalization_2014}}{a numeric vector}
    \item{\code{Hypertension_Outpatient_2014}}{a numeric vector}
    \item{\code{Diabetes_hospitalization_2014}}{a numeric vector}
    \item{\code{Diabetes_Outpatient_2014}}{a numeric vector}
    \item{\code{Cerebrovascular_mortality_2015}}{a numeric vector}
    \item{\samp{Malignant_neoplasm_(stomach)_mortality_rate_2015}}{a numeric vector}
    \item{\samp{Malignant_neoplasm_(intestine)_mortality_rate_2015}}{a numeric vector}
    \item{\samp{Malignant_neoplasm_(liver)_mortality_rate_2015}}{a numeric vector}
    \item{\samp{Malignant_neoplasm_(lungs)_mortality_2015}}{a numeric vector}
    \item{\samp{Malignant_neoplasm_(breast)_mortality_rate_2015}}{a numeric vector}
    \item{\samp{Malignant_neoplasm_(uterus)_mortality_rate_2015}}{a numeric vector}
    \item{\code{Heart_dz_mortality_2015}}{a numeric vector}
    \item{\code{Pneumonia_mortality_2015}}{a numeric vector}
    \item{\code{Acute_myocardial_infarction_mortality_2015}}{a numeric vector}
    \item{\code{Use_blood_pressure_binary_2014}}{a numeric vector}
    \item{\code{Use_Insulin_binary_2014}}{a numeric vector}
    \item{\code{Use_Cholesterol_binary_2014}}{a numeric vector}
    \item{\code{Eat_within_2_hours_before_sleep_binary_2014}}{a numeric vector}
    \item{\code{Physical_activity_walking_binary_2014}}{a numeric vector}
    \item{\code{Sweat_exercise_twice_a_week_binary_2014}}{a numeric vector}
    \item{\code{Smoking_over_100_binary_2014}}{a numeric vector}
    \item{\code{Gain_10kg_Wt_compared_to_20yr_binary_2014}}{a numeric vector}
    \item{\code{Fast_Walking_compared_to_the_same_age_binary_2014}}{a numeric vector}
    \item{\code{Drinking_2_or_more_per_day_binary_2014}}{a numeric vector}
    \item{\code{Drinking_everyday_binary_2014}}{a numeric vector}
    \item{\code{Enough_sleep_binary_2014}}{a numeric vector}
    \item{\code{Skip_breakfast_three_times_a_week_binary_2014}}{a numeric vector}
    \item{\code{Snacks_three_times_a_week_after_dinner_binary_2014}}{a numeric vector}
    \item{\code{Meat_2014}}{a numeric vector}
    \item{\code{Seafood_2014}}{a numeric vector}
    \item{\code{Milk_2014}}{a numeric vector}
    \item{\code{Dairy_2014}}{a numeric vector}
    \item{\code{Egg_2014}}{a numeric vector}
    \item{\code{Soybean_2014}}{a numeric vector}
    \item{\code{Usual_barrier_free_handrails_2013}}{a numeric vector}
    \item{\code{Usual_barrier_free_no_steps_2013}}{a numeric vector}
    \item{\code{High_barrier_free_handrails_2013}}{a numeric vector}
    \item{\code{High_barrier_free_no_steps_2013}}{a numeric vector}
    \item{\code{High_barrier_free_wheelchairs_pass_Width}}{a numeric vector}
    \item{\code{Total_working_hours_2016}}{a numeric vector}
    \item{\code{Total_salary_2016}}{a numeric vector}
    \item{\code{Fish_meat_consumption_2014}}{a numeric vector}
    \item{\code{Fish_meat_consumption_2015}}{a numeric vector}
    \item{\code{Fish_meat_consumption_2016}}{a numeric vector}
    \item{\code{Fish_meat_consumption_avg_2014_2016}}{a numeric vector}
    \item{\code{Confectionery_consumption_2014}}{a numeric vector}
    \item{\code{Confectionery_consumption_2015}}{a numeric vector}
    \item{\code{Confectionery_consumption_2016}}{a numeric vector}
    \item{\code{Confectionery_consumption_avg_2014_2016}}{a numeric vector}
    \item{\code{Fruits_consumption_2014}}{a numeric vector}
    \item{\code{Fruits_consumption_2015}}{a numeric vector}
    \item{\code{Fruits_consumption_2016}}{a numeric vector}
    \item{\code{Fruit_consumption_avg_2014_2016}}{a numeric vector}
    \item{\code{Academic_ability_middle_school_2015}}{a numeric vector}
    \item{\code{Academic_ability_elementary_school_2015}}{a numeric vector}
    \item{\code{Total_Num_of_caries_2014}}{a numeric vector}
    \item{\code{Total_Num_of_periodontal_2014}}{a numeric vector}
    \item{\code{Bone_density_disorder_2014}}{a numeric vector}
    \item{\code{Fracture_2014}}{a numeric vector}
    \item{\code{Tooth_supplement_2014}}{a numeric vector}
    \item{\code{Alzheimer_dz_2014}}{a numeric vector}
    \item{\code{Gini_coeff_2014}}{a numeric vector}
    \item{\code{Income_Gini_Coeff_Working_Household_2014}}{a numeric vector}
    \item{\code{Vegetable_intake_2012}}{a numeric vector}
    \item{\code{Salt_intake_2012}}{a numeric vector}
    \item{\code{BMI_2012}}{a character vector}
    \item{\code{Num_Steps_2012_per_day}}{a numeric vector}
  }
}
\details{
%%  ~~ If necessary, more details than the __description__ above ~~
}
\source{
%%  ~~ reference to a publication or URL from which the data were obtained ~~
}
\references{
%%  ~~ possibly secondary sources and usages ~~
}
\examples{
data(d)
## maybe str(d) ; plot(d) ...
}
\keyword{datasets}
