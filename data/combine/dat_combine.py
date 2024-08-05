##############################################
## utilizing data to create project tab csv ##
##
## required: credits and project info csvs  ##
## output: project tab csv and pivoted csv  ##
##         for streamlit                    ##
##                                          ##
##############################################

# libraries
import pandas as pd

def naming(interest):
    if interest=="project":
        proj_names = ['Project ID', 'Project Name', 'Voluntary Registry', 'ARB/WA Project', 
                'Voluntary Status', 'Scope', 'Type', 'Type Rule', 'Type ML',
                'Confidence Level', 'Reduction/Removal', 'Methodology/Protocol', 'Methodology Version', 
                'Region', 'Country', 'State', 'Project Site Location',
                'Project Developer', 'Project Owner', 'Offset Project Operator', 
                'Authorized Project Designee', 'Verifier',
                'Estimated Annual Emission Reductions', 'ARB ID', 'ARB Project Type',
                'ARB Project Status', 'WA ID', 'WA Project Type', 'POA ID', 
                'Project Listed', 'Project Registered', 'Sustainability Certification',
                'Project Type From the Registry', 'Registry Documents',
                'Project Website', 'Notes From Registry', 'Notes from the Berkeley Carbon Trading Project', 
                'Project Description', 'Added to Database Version - With Data Through']
        return proj_names
    
    elif interest=="issuances":
        cred_group_iss_names = ['Project ID', 'Total Buffer Pool Deposits', 'Total Buffer Subtractions by Issuance Year',
                      'Total Credits Issued', 'Total Credits Retired', 'PERs']
        return cred_group_iss_names
    
    elif interest=="vintages":
        cred_group_vin_names = ['Project ID', 'First Year of Project']
        return cred_group_vin_names

    elif interest=="buffers":
        cred_group_buffer_names = ['Project ID', 'Reversals Covered by Buffer Pool', 'Reversals Not Covered by Buffer Pool']
        return cred_group_buffer_names

    elif interest=="pivoted issuances":
        piv_iss_names = ['Project ID', 'Year', 'Buffer Contributions by Issuance Year','Buffer Subtractions by Issuance Year','Credits Issued by Issuance Year','Issuance Per','Credits Retired by Issuance Year']
        return piv_iss_names

    elif interest=="pivoted vintages":
        piv_vin_names = ['Project ID', 'Vintage Year', 'Buffer Contributions by Vintage Year','Buffer Subtractions by Vintage Year','Credits Issued by Vintage Year','Issuance Per','Credits Retired by Vintage Year']
        return piv_vin_names

def reorder(merged_df):
    column_order = ['Project ID', 'Project Name', 'Voluntary Registry', 'ARB/WA Project',
       'Voluntary Status', 'Scope', 'Type', 'Reduction/Removal', 'Methodology/Protocol', 
       'Region', 'Country', 'State', 'Project Site Location','Project Developer', 
       'Total Credits Issued', 'Total Credits Retired', 'Total Credits Remaining',
       'Total Buffer Pool Deposits', 'Reversals Covered by Buffer Pool','Reversals Not Covered by Buffer Pool',
       'First Year of Project',
       '2002 Credits Issued by Vintage Year', '2004 Credits Issued by Vintage Year','2005 Credits Issued by Vintage Year', 
       '2006 Credits Issued by Vintage Year','2007 Credits Issued by Vintage Year', '2008 Credits Issued by Vintage Year',
       '2009 Credits Issued by Vintage Year', '2010 Credits Issued by Vintage Year','2011 Credits Issued by Vintage Year', 
       '2012 Credits Issued by Vintage Year','2013 Credits Issued by Vintage Year','2014 Credits Issued by Vintage Year', 
       '2015 Credits Issued by Vintage Year','2016 Credits Issued by Vintage Year', '2017 Credits Issued by Vintage Year',
       '2018 Credits Issued by Vintage Year', '2019 Credits Issued by Vintage Year', '2020 Credits Issued by Vintage Year', 
       '2021 Credits Issued by Vintage Year', '2022 Credits Issued by Vintage Year', '2023 Credits Issued by Vintage Year',
       '2024 Credits Issued by Vintage Year','1996 Credits Issued by Vintage Year','1997 Credits Issued by Vintage Year',
       '1998 Credits Issued by Vintage Year','1999 Credits Issued by Vintage Year','2000 Credits Issued by Vintage Year',
       '2001 Credits Issued by Vintage Year','2002 Credits Issued by Vintage Year','2003 Credits Issued by Vintage Year',
       '2004 Credits Issued by Vintage Year','2005 Credits Issued by Vintage Year','2006 Credits Issued by Vintage Year',
       '2007 Credits Issued by Vintage Year','2008 Credits Issued by Vintage Year','2009 Credits Issued by Vintage Year',
       '2010 Credits Issued by Vintage Year','2011 Credits Issued by Vintage Year','2012 Credits Issued by Vintage Year',
       '2013 Credits Issued by Vintage Year','2014 Credits Issued by Vintage Year','2015 Credits Issued by Vintage Year',
       '2016 Credits Issued by Vintage Year','2017 Credits Issued by Vintage Year','2018 Credits Issued by Vintage Year',
       '2019 Credits Issued by Vintage Year','2020 Credits Issued by Vintage Year','2021 Credits Issued by Vintage Year',
       '2022 Credits Issued by Vintage Year','2023 Credits Issued by Vintage Year','2024 Credits Issued by Vintage Year',
       'Credits Retired or Cancelled in 2002','Credits Retired or Cancelled in 2004',
       'Credits Retired or Cancelled in 2005','Credits Retired or Cancelled in 2006','Credits Retired or Cancelled in 2007',
       'Credits Retired or Cancelled in 2008','Credits Retired or Cancelled in 2009','Credits Retired or Cancelled in 2010',
       'Credits Retired or Cancelled in 2011','Credits Retired or Cancelled in 2012','Credits Retired or Cancelled in 2013',
       'Credits Retired or Cancelled in 2014','Credits Retired or Cancelled in 2015','Credits Retired or Cancelled in 2016',
       'Credits Retired or Cancelled in 2017','Credits Retired or Cancelled in 2018','Credits Retired or Cancelled in 2019',
       'Credits Retired or Cancelled in 2020','Credits Retired or Cancelled in 2021','Credits Retired or Cancelled in 2022',
       'Credits Retired or Cancelled in 2023','Credits Retired or Cancelled in 2024',
       '2002 Credits Remaining by Vintage','2004 Credits Remaining by Vintage','2005 Credits Remaining by Vintage',
       '2006 Credits Remaining by Vintage','2007 Credits Remaining by Vintage','2008 Credits Remaining by Vintage',
       '2009 Credits Remaining by Vintage','2010 Credits Remaining by Vintage','2011 Credits Remaining by Vintage',
       '2012 Credits Remaining by Vintage','2013 Credits Remaining by Vintage','2014 Credits Remaining by Vintage',
       '2015 Credits Remaining by Vintage','2016 Credits Remaining by Vintage','2017 Credits Remaining by Vintage',
       '2018 Credits Remaining by Vintage','2019 Credits Remaining by Vintage','2020 Credits Remaining by Vintage',
       '2021 Credits Remaining by Vintage','2022 Credits Remaining by Vintage','2023 Credits Remaining by Vintage',
       '2024 Credits Remaining by Vintage',
       'Project Owner', 'Offset Project Operator','Authorized Project Designee', 'Verifier',
       'Estimated Annual Emission Reductions', 
       'PERs',
       'Registry/ARB/WA','Project Listed', 'Project Registered', 'Sustainability Certification',
       'Project Type From the Registry', 'Registry Documents','Project Website', 'Notes From Registry',
       '2002 Credits Issued by Issuance Year','2004 Credits Issued by Issuance Year','2005 Credits Issued by Issuance Year',
       '2006 Credits Issued by Issuance Year','2007 Credits Issued by Issuance Year','2008 Credits Issued by Issuance Year',
       '2009 Credits Issued by Issuance Year','2010 Credits Issued by Issuance Year','2011 Credits Issued by Issuance Year',
       '2012 Credits Issued by Issuance Year','2013 Credits Issued by Issuance Year','2014 Credits Issued by Issuance Year',
       '2015 Credits Issued by Issuance Year','2016 Credits Issued by Issuance Year','2017 Credits Issued by Issuance Year',
       '2018 Credits Issued by Issuance Year','2019 Credits Issued by Issuance Year','2020 Credits Issued by Issuance Year',
       '2021 Credits Issued by Issuance Year',
       'Notes from the Berkeley Carbon Trading Project', 'Added to Database Version - With Data Through']
    merged_df = merged_df[column_order]
    return merged_df

def cred_group_and_piv(cred):
    #first groups
    cred_group_issuanceDate = cred.groupby(['project_id', 'transaction_type', 'issuance_date']).amount.sum().reset_index()
    cred_group_vintageDate = cred.groupby(['project_id', 'transaction_type', 'vintage_year']).amount.sum().reset_index()
    cred_buffer = cred.loc[
        (cred['sub_transaction_type'] == 'cancelled_for_intentional_reversal') |
        ((cred['transaction_type'] == 'buffer_subtraction') & (cred['sub_transaction_type'] == 'unintentional_reversal'))]
    cred_buffer = cred_buffer.groupby(['project_id', 'sub_transaction_type']).amount.sum().reset_index()

    #first pivot
    cred_piv_iss = cred_group_issuanceDate.pivot(index=['project_id', 'issuance_date'], 
                      columns='transaction_type', values='amount').reset_index()
    cred_piv_vin = cred_group_vintageDate.pivot(index=['project_id', 'vintage_year'], 
                      columns='transaction_type', values='amount').reset_index()
    
    #second group
    cred_group_iss = cred_piv_iss.groupby(['project_id']).agg({'buffer_contribution':'sum', 
                                               'buffer_subtraction':'sum', 
                                               'issuance':'sum',
                                               'retirement_cancellation':'sum',
                                                          'per':'sum'}).reset_index()
    cred_group_vin = cred_piv_vin.groupby(['project_id']).agg({'vintage_year':'min'}).reset_index()
    cred_group_buffer = cred_buffer.pivot(index=['project_id'], 
                        columns='sub_transaction_type', values='amount').reset_index()
    
    #second pivot
    #issuances by issuance date
    cred_piv_iss['issuance_date'] = cred_piv_iss['issuance_date'].astype(int)
    pivot_iss_iss = cred_piv_iss[cred_piv_iss['issuance_date']<=2024].pivot(index='project_id', columns='issuance_date', values='issuance').reset_index()
    pivot_iss_iss = pivot_iss_iss.drop(columns=[0])
    pivot_iss_iss.columns = [pivot_iss_iss.columns[0]] + [f"{col} Credits Issued by Issuance Year" for col in pivot_iss_iss.columns[1:]]
    pivot_iss_iss.columns.values[0] = "Project ID"
    pivot_iss_iss.fillna(0, inplace=True)
    #issuances by vintage date
    cred_piv_vin['vintage_year'] = cred_piv_vin['vintage_year'].astype(int)
    pivot_vin_iss = cred_piv_vin[cred_piv_vin['vintage_year']<=2024].pivot(index='project_id', columns='vintage_year', values='issuance').reset_index()
    pivot_vin_iss = pivot_vin_iss.drop(columns=[0])
    pivot_vin_iss.columns = [pivot_vin_iss.columns[0]] + [f"{col} Credits Issued by Vintage Year" for col in pivot_vin_iss.columns[1:]]
    pivot_vin_iss.columns.values[0] = "Project ID"
    pivot_vin_iss.fillna(0, inplace=True)
    #retirements by issuance date
    pivot_iss_rc= cred_piv_iss.pivot(index='project_id', columns='issuance_date', values='retirement_cancellation').reset_index()
    pivot_iss_rc = pivot_iss_rc.drop(columns=[0])
    pivot_iss_rc.columns = [pivot_iss_rc.columns[0]] + [f"Credits Retired or Cancelled in {col}" for col in pivot_iss_rc.columns[1:]]
    pivot_iss_rc.columns.values[0] = "Project ID"
    pivot_iss_rc.fillna(0, inplace=True)

    return cred_group_iss, cred_group_vin, cred_group_buffer, pivot_iss_iss, pivot_vin_iss, pivot_iss_rc, cred_piv_iss, cred_piv_vin

def proj_prep(proj):
    proj.columns = naming("project")
    proj1 = proj.iloc[:, :19]
    proj2 = proj.drop(proj.columns[1:19], axis=1)

    return proj1, proj2

def cred_prep(cred):
    cred[['vintage_year','issuance_date']] = cred[['vintage_year','issuance_date']].astype(str)
    cred[['vintage_year','issuance_date','amount']] = cred[['vintage_year','issuance_date','amount']].fillna(0)
    cred[['vintage_year','issuance_date']] = cred[['vintage_year','issuance_date']].replace('NaT', 0)
    cred[['vintage_year','issuance_date']] = cred[['vintage_year','issuance_date']].replace('nan', 0)
    cred[['vintage_year','issuance_date']] = cred[['vintage_year','issuance_date']].astype(str)
    cred['vintage_year'] = cred['vintage_year'].str.replace('.0', '')
    cred['temp1'] = cred['issuance_date'].str.contains('-')
    cred['temp2'] = cred['issuance_date'].str.contains('/')
    cred.loc[cred['temp1'], 'issuance_date'] = cred.loc[cred['temp1'], 'issuance_date'].str[:4]
    cred.loc[cred['temp2'], 'issuance_date'] = cred.loc[cred['temp2'], 'issuance_date'].str.split('/').str[2].str[:4]
    cred = cred.drop(columns=['temp1', 'temp2'])

    #get all necessary outputs for merging
    cred_group_iss, cred_group_vin, cred_group_buffer, pivot_iss_iss, pivot_vin_iss, pivot_iss_rc, cred_piv_iss, cred_piv_vin = cred_group_and_piv(cred)

    #rename columns 
    cred_group_iss.columns = naming("issuances")
    cred_group_vin.columns = naming("vintages")
    cred_group_buffer.columns = naming("buffers")

    return cred_group_iss, cred_group_vin, cred_group_buffer, pivot_iss_iss, pivot_vin_iss, pivot_iss_rc, cred_piv_iss, cred_piv_vin

def remaining_columns(df, start_col):
    # Create or reset 'temp2' column
    df['temp'] = df['Total Credits Issued']
    df['temp2'] = 0 
    
    # Iterate over columns starting from the specified index
    for col in df.columns[start_col:]:
        df['temp2'] = df[col]  # Copy current column to temp2
        df[col] = df[col].where(df[col] != 0, df['temp'] - df['temp2'])  # Subtract temp if not 0
        df['temp'] = df['temp'] - df['temp2']
    return df

def clean_merge(merged_df):
    #clean features
    #create Registry/ARB/WA feature
    merged_df['Registry/ARB/WA'] = merged_df['Voluntary Registry']
    merged_df.loc[merged_df['ARB/WA Project'].isin(['ARB Compliance', 'ARB Early Action']), 'Registry/ARB/WA'] = 'ARB'
    merged_df.loc[merged_df['ARB/WA Project'].isin(['WA Compliance', 'WA Early Action']), 'Registry/ARB/WA'] = 'WA'
    merged_df.loc[merged_df['WA Project Type'].isin(['ODS']), 'Registry/ARB/WA'] = 'WA'

    #Fix Buffer Pool info
    merged_df[['Total Buffer Pool Deposits','Reversals Covered by Buffer Pool','Reversals Not Covered by Buffer Pool','Total Credits Issued','Total Credits Retired']] = merged_df[['Total Buffer Pool Deposits','Reversals Covered by Buffer Pool', 'Reversals Not Covered by Buffer Pool','Total Credits Issued','Total Credits Retired']].fillna(0).astype(int)
    merged_df['Total Credits Retired'] = merged_df['Total Credits Retired'].abs()
    merged_df[merged_df.columns[76:98]] = merged_df[merged_df.columns[76:98]].abs()
    merged_df['Total Credits Remaining'] = merged_df['Total Credits Issued']-merged_df['Total Credits Retired']

    #fill nulls
    merged_df[merged_df.filter(like='Credits Issued by Vintage Year').columns] = merged_df[merged_df.filter(like='Credits Issued by Vintage Year').columns].fillna(0)
    merged_df[merged_df.filter(like='Credits Issued by Issuance Year').columns] = merged_df[merged_df.filter(like='Credits Issued by Issuance Year').columns].fillna(0)
    merged_df[merged_df.filter(like='Credits Retired or Cancelled in').columns] = merged_df[merged_df.filter(like='Credits Retired or Cancelled in').columns].fillna(0)

    #drop unnecessary columns
    merged_df = merged_df.drop(columns=['Type Rule','Type ML','Confidence Level','ARB ID', 'ARB Project Type','ARB Project Status', 'WA ID', 'WA Project Type', 'POA ID','Project Description'])

    #set up for remaining cols
    columns_to_duplicate = merged_df.columns[75:97]
    new_column_names = [col[-4:] + ' Credits Remaining by Vintage' for col in columns_to_duplicate]
    # Duplicate the columns with new names
    new_columns_df = merged_df[columns_to_duplicate].copy()
    new_columns_df.columns = new_column_names
    # Concatenate the new columns to the original df
    merged_df = pd.concat([merged_df, new_columns_df], axis=1)
    #then fill it
    merged_df = remaining_columns(merged_df, 112)

    return(merged_df)

def clean_merge2(merged_df2):
    merged_df2['Registry/ARB/WA'] = merged_df2['Voluntary Registry']
    merged_df2.loc[merged_df2['ARB/WA Project'].isin(['ARB Compliance', 'ARB Early Action']), 'Registry/ARB/WA'] = 'ARB'
    merged_df2.loc[merged_df2['ARB/WA Project'].isin(['WA Compliance', 'WA Early Action']), 'Registry/ARB/WA'] = 'WA'

    merged_df2[['Total Buffer Pool Deposits','Total Credits Issued','Issuance Per','Total Credits Retired']] = merged_df2[['Total Buffer Pool Deposits','Total Credits Issued','Issuance Per','Total Credits Retired']].fillna(0).astype(int)
    merged_df2['Total Credits Retired'] = merged_df2['Total Credits Retired'].abs()

    merged_df2 = merged_df2[(merged_df2['Year'].notna()) & (merged_df2['Year'] != 0)]

    return merged_df2

def merge_dat(proj, cred):
    proj1, proj2 = proj_prep(proj)
    cred_group_iss, cred_group_vin, cred_group_buffer, pivot_iss_iss, pivot_vin_iss, pivot_iss_rc, cred_piv_iss, cred_piv_vin = cred_prep(cred)

    #merge all data
    merged_df = proj1.merge(cred_group_iss, on='Project ID', how='outer') \
                  .merge(cred_group_vin, on='Project ID', how='outer') \
                  .merge(cred_group_buffer, on='Project ID', how='outer') \
                  .merge(pivot_iss_iss, on='Project ID', how='outer') \
                  .merge(pivot_vin_iss, on='Project ID', how='outer') \
                  .merge(pivot_iss_rc, on='Project ID', how='outer') \
                  .merge(proj2, on='Project ID', how='outer')
    
    #clean the new merged df
    merged_df = clean_merge(merged_df)

    cred_piv_iss.columns = naming("pivoted issuances")
    cred_piv_vin.columns = naming("pivoted vintages")

    merged_df2 =  proj1.merge(cred_piv_iss, on='Project ID', how ='outer') \
                .merge(cred_group_iss, on='Project ID', how ='outer')
    
    #clean the pivoted merge
    merged_df2 = clean_merge2(merged_df2)

    return(merged_df, merged_df2)


if __name__ == "__main__":
    #bring in inputs
    cred = pd.read_csv("credit_activities.csv")
    proj = pd.read_csv("project_info.csv")

    #create the project tab
    merged_df, merged_df2 = merge_dat(proj, cred)
    merged_df = reorder(merged_df)

    #export the project tab
    merged_df.to_csv("TEST_Project_Tab.csv", index=False)
    merged_df.to_csv("../../streamlit_test/data/TEST_Project_Tab.csv", index=False)

    #export the output for streamlit
    merged_df2.to_csv("../../streamlit_test/data/Project_Tab_Pivoted.csv", index=False)

