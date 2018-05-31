import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt
import numpy as np
import pandas as pd


## Create engine using the `belly_button_biodiversity.sqlite` database file
#engine = create_engine("sqlite:///belly_button_biodiversity.sqlite")
## Declare a Base using `automap_base()`
#Base = automap_base()
## Use the Base class to reflect the database tables
#Base.prepare(engine, reflect=True)
## Assign the samples class to a variable called `Samples`
#Samples = Base.classes
## Create a session
#session = Session(engine)
## Create connection
#conn = engine.connect()


# def get_sample_names():
#     '''List of sample names'''
#     sample_names = []
#     first_row = session.query(Samples).first()
#     abc = first_row.__dict__
#     for key in abc:
#         sample_names.append(key)
#     sample_names.sort()
#     sample_names = sample_names[0:-2]
#     # return render_template('index.html', samplenames = sample_names) 
#     print(sample_names)

# get_sample_names()

#def get_otu_descriptions():
#    '''List of OTU descriptions'''
#    otu_list = []
#    # first_row = session.query(Samples.otu).first()
#    # abc = first_row.__dict__
#    for row in session.query(Samples.otu.lowest_taxonomic_unit_found).all():
#        otu_list.append(row[0])
#    print(otu_list)

#get_otu_descriptions()

#def get_default_values():
#    '''OTU IDs and Sample Values for a given sample.'''
#    data_samples = pd.read_sql("SELECT * FROM samples", conn)
#    default_dict={}
#    default_data = []
#    for c in data_samples.columns[1:]:
#        sample_values = []
#        otu_id = []
#
#        for x in range(len(data_samples[c])):
#            if data_samples[c][x] != 0:     
#                sample_values.append(data_samples[c][x])
#                otu_id.append(data_samples['otu_id'][x])
#        temp_df = pd.DataFrame({'sample_values': sample_values, 'otu_id': otu_id}, 
#                               columns=['sample_values', 'otu_id'])
#        temp_df = temp_df.sort_values('sample_values', ascending=False).reset_index(drop=True)
#        s_list = list(temp_df.sample_values)
#        o_list = list(temp_df.otu_id)
#        
#        default_dict['otu_ids'] = o_list[0:11]
#        default_dict['sample_values'] = s_list[0:11]
#        
#    default_data = [{
#    "labels": o_list[0:11],
#    "values": s_list[0:11],
#    "type": "pie"}]
#    print (default_data)
#    
#get_default_values()

#def get_default_values2():
#    '''OTU IDs and Sample Values for a given sample.'''
#    data_samples = pd.read_sql("SELECT * FROM samples", conn)
#    final_list=[]
#    count = 1
#    for c in data_samples.columns[1:]:
#    #     print(c)
#        all_sample_info = {}
#        sample_values = []
#        otu_id = []
#    #     print(len(data_samples[c]))
#        for x in range(len(data_samples[c])):
#    #         print(len(data_samples[c]))
#    #         print(data_samples[c][x])
#    #         print(data_samples['otu_id'][x])
#            if data_samples[c][x] != 0:     
#                sample_values.append(data_samples[c][x])
#                otu_id.append(data_samples['otu_id'][x])
#        temp_df = pd.DataFrame({'sample_values': sample_values, 'otu_id': otu_id}, 
#                               columns=['sample_values', 'otu_id'])
#        temp_df = temp_df.sort_values('sample_values', ascending=False).reset_index(drop=True)
#        s_values = []
#        o_values = []
#        for x in range(len(temp_df['sample_values'])):
#            s_values.append(temp_df.sample_values[x])
#            o_values.append(temp_df.otu_id[x])
#
#        all_sample_info['otu_ids'] = o_values[0:11]
#        all_sample_info['sample_values'] = s_values[0:11]
#        all_sample_info_dict = {}
#        all_sample_info_dict[data_samples.columns[count]]=all_sample_info
#        final_list.append(all_sample_info_dict)
#        count += 1
#    print(final_list)
#    
#get_default_values2()



#def get_default_values3():
#    data_samples = pd.read_sql("SELECT * FROM samples", conn)
#
#    final_list=[]
#    count = 1
#    for c in data_samples.columns[1:]:
#    #     print(c)
#        all_sample_info = {}
#        sample_values = []
#        otu_id = []
#    #     print(len(data_samples[c]))
#        for x in range(len(data_samples[c])):
#    #         print(len(data_samples[c]))
#    #         print(data_samples[c][x])
#    #         print(data_samples['otu_id'][x])
#            if data_samples[c][x] != 0:     
#                sample_values.append(data_samples[c][x])
#                otu_id.append(data_samples['otu_id'][x])
#        temp_df = pd.DataFrame({'sample_values': sample_values, 'otu_id': otu_id}, 
#                               columns=['sample_values', 'otu_id'])
#        temp_df = temp_df.sort_values('sample_values', ascending=False).reset_index(drop=True)
#        temp_df['sample_values'] = temp_df['sample_values'].astype(float)
#        temp_df['otu_id'] = temp_df['otu_id'].astype(str)
#        s_values = []
#        o_values = []
#        for x in range(len(temp_df['sample_values'])):
#            s_values.append(temp_df.sample_values[x])
#            o_values.append(temp_df.otu_id[x])
#
#        all_sample_info['otu_ids'] = o_values[0:11]
#        all_sample_info['sample_values'] = s_values[0:11]
#        all_sample_info_dict = {}
#        all_sample_info_dict[data_samples.columns[count]]=all_sample_info
#        final_list.append(all_sample_info_dict)
#        count += 1
#    print(final_list)
#get_default_values3()


#
#
#def get_metadata(sample1):
#    '''Get Metadata of given sample id'''
#    # Create engine using the `belly_button_biodiversity.sqlite` database file
#    engine = create_engine("sqlite:///belly_button_biodiversity.sqlite")
#    # Declare a Base using `automap_base()`
#    Base = automap_base()
#    # Use the Base class to reflect the database tables
#    Base.prepare(engine, reflect=True)
#    # Assign the samples class to a variable called `Samples`
##    Samples2 = Base.classes
#    # Create a session
##    session = Session(engine)
#    conn = engine.connect()
#    
#    metadata_info = {}
#
#    data = pd.read_sql("SELECT * FROM samples_metadata", conn)
#    data['SAMPLEID2'] = ''
#    for x in range(len(data.SAMPLEID)):
#        data.SAMPLEID2[x] = "BB_" + str(data.SAMPLEID[x]) 
#
#    sample_metadata = data[['SAMPLEID2', 'AGE', 'BBTYPE', 'ETHNICITY', 'GENDER', 'LOCATION', 'SAMPLEID']]
#    sample_metadata.set_index("SAMPLEID2", inplace=True)
#    sample_metadata = sample_metadata.transpose()
#    sample_metadata.to_json('resources/sample_metadata.json')
#    sample_metadata_json = pd.read_json('resources/sample_metadata.json')
#    
#    metadata_info['AGE'] =        sample_metadata_json[sample1]['AGE']
#    metadata_info['BBTYPE'] =     sample_metadata_json[sample1]['BBTYPE']
#    metadata_info['ETHNICITY'] =  sample_metadata_json[sample1]['ETHNICITY']
#    metadata_info['GENDER'] =     sample_metadata_json[sample1]['GENDER']
#    metadata_info['LOCATION'] =   sample_metadata_json[sample1]['LOCATION']
#    metadata_info['SAMPLEID'] =   sample_metadata_json[sample1]['SAMPLEID']
#    print(metadata_info)
#    
#get_metadata('BB_940')




def get_metadata():
    '''Get Metadata of given sample id'''
    # Create engine using the `belly_button_biodiversity.sqlite` database file
    engine = create_engine("sqlite:///belly_button_biodiversity.sqlite")
    # Declare a Base using `automap_base()`
    Base = automap_base()
    # Use the Base class to reflect the database tables
    Base.prepare(engine, reflect=True)
    # Assign the samples class to a variable called `Samples`
#    Samples2 = Base.classes
    # Create a session
#    session = Session(engine)
    conn = engine.connect()

    data = pd.read_sql("SELECT * FROM samples_metadata", conn)
#    data['SAMPLEID2'] = ''
#    for x in range(len(data.SAMPLEID)):
#        data.SAMPLEID2[x] = "BB_" + str(data.SAMPLEID[x]) 

    sample_metadata = data[['AGE', 'BBTYPE', 'ETHNICITY', 'GENDER', 'LOCATION', 'SAMPLEID']]
    xyz = []
    for x in range(len(sample_metadata.SAMPLEID)):
        xyz.append("BB_" + str(sample_metadata.SAMPLEID[x]))
    sample_metadata = sample_metadata.assign(SAMPLEID2=xyz)
    sample_metadata1=pd.DataFrame(sample_metadata['AGE'].astype(int))
    sample_metadata1['BBTYPE']=sample_metadata['BBTYPE'].astype(str)
    sample_metadata1['ETHNICITY']=sample_metadata['ETHNICITY'].astype(str)
    sample_metadata1['GENDER']=sample_metadata['GENDER'].astype(str)
    sample_metadata1['LOCATION']=sample_metadata['LOCATION'].astype(str)
    sample_metadata1['SAMPLEID']=sample_metadata['SAMPLEID'].astype(int)
    sample_metadata1['SAMPLEID2']=sample_metadata['SAMPLEID2'].astype(str)
    
    sample_metadata1.set_index("SAMPLEID2", inplace=True)
    
    sample_metadata1 = sample_metadata1.transpose()
    
    metadata_list = []
    for x in range(len(sample_metadata1.columns)):
        metadata_info = {}
        col = sample_metadata1.columns[x]
        metadata_info['AGE']  = sample_metadata1[col]['AGE']
        metadata_info['BBTYPE'] =     sample_metadata1[col]['BBTYPE']
        metadata_info['ETHNICITY'] =  sample_metadata1[col]['ETHNICITY']
        metadata_info['GENDER'] =     sample_metadata1[col]['GENDER']
        metadata_info['LOCATION'] =   sample_metadata1[col]['LOCATION']
        metadata_info['SAMPLEID'] =   sample_metadata1[col]['SAMPLEID']
        metadata_sample = {}
        metadata_sample[col]=metadata_info
        metadata_list.append(metadata_sample)
    print(metadata_list)

get_metadata()