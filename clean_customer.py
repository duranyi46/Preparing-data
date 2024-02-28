import pandas as pd

customers_data = pd.read_csv('customer_train.csv')

# Beginning memory usage 2.0+ MB
ds_jobs_clean = customers_data.copy()
# nominal category --> category //// ordinal category --> ordered category
# nominals/ gender, enroled_uni, major,company type,city
# ordinals ,educ level, exp, companysize, last_new_job
cat_orders = {
'education_level' : ['Primary School','High School','Graduate','Masters','Phd'],
'company_size' : ['<10','10-49','50-99','100-499','500-999','1000-4999','5000-9999','10000+'],
'last_new_job' : ['never','1','2','3','4','>4'],
'experience' : ['<1'] + list(map(str, range(1,21))) + ['>20'],
'enrolled_university' : ['no_enrollment','Part time course','Full time course'],
'relevant_experience' : ['No relevant experience','Has relevant experience']
}
for column in ds_jobs_clean:
    if ds_jobs_clean[column].dtype == 'float':
        ds_jobs_clean[column] = ds_jobs_clean[column].astype('float16')
    elif ds_jobs_clean[column].dtype == 'int64':
        ds_jobs_clean[column] = ds_jobs_clean[column].astype('int32')
    elif column in cat_orders.keys():
        category = pd.CategoricalDtype(cat_orders[column], ordered = True)
        ds_jobs_clean[column] = ds_jobs_clean[column].astype(category)
    else :
        ds_jobs_clean[column] = ds_jobs_clean[column].astype('category')

ds_jobs_clean = ds_jobs_clean[(ds_jobs_clean['company_size'] >= '1000-4999') & (ds_jobs_clean['experience'] >= '10')]
# Final memory usage 76.1 KB
