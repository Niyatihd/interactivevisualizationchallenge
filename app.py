#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 19:34:35 2018

@author: niyatidesai
"""

from flask import Flask, render_template, jsonify
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import pandas as pd

#from d123 import get_default_values

blah = ['chichi', 'peepee', 'pad']

app = Flask(__name__)

#################################################
# Database Setup
#################################################
from flask_sqlalchemy import SQLAlchemy
# The database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///belly_button_biodiversity.sqlite"

db = SQLAlchemy(app)

class Samples(db.Model):
    __tablename__ = 'samples'

    id = db.Column(db.Integer, primary_key=True)
    otu_id = db.Column(db.String)
    BB_1233 = db.Column(db.Integer)

    def __repr__(self):
        return '<Samples %r>' % (self.otu_id)

# Create database tables
@app.before_first_request
def setup():
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()
    
#################################################
# Database Setup read to pandas
#################################################

#################################################
# Flask Setup
#################################################
@app.route('/')
def index():
    return render_template('index.html', blah=blah)

 
@app.route('/values')
def get_values():
    results = db.session.query(Samples.otu_id, Samples.BB_1233).\
            order_by(Samples.BB_1233.desc()).\
            limit(10).all()
    df = pd.DataFrame(results, columns=['otu_id', 'BB_1233'])
     # Format the data for Plotly
    plot_trace = {
            "labels": df["otu_id"].values.tolist(),
            "values": df["BB_1233"].values.tolist(),
            "type": "pie"
    }
    return jsonify(plot_trace)



@app.route("/names")
def get_sample_names():
    '''List of sample names'''
    engine = create_engine("sqlite:///belly_button_biodiversity.sqlite")    
    # Declare a Base using `automap_base()`
    Base = automap_base()
    # Use the Base class to reflect the database tables
    Base.prepare(engine, reflect=True)
    # Assign the samples class to a variable called `Samples`
    Samples1 = Base.classes
    # Create a session
    session = Session(engine)
    #session = scoped_session(sessionmaker(bind=engine))
    # Create connection
#    conn = engine.connect()
    first_row = session.query(Samples1.samples).first()

    sample_names = []
    abc = first_row.__dict__
    for key in abc:
        sample_names.append(key)
    sample_names.sort()
    sample_names = sample_names[0:-2]
    return jsonify(sample_names)
#    return render_template('names.html', sample_names = sample_names)
    
@app.route('/samples/<sample>')
def get_otuids_samplevalues(sample):
    '''OTU IDs and Sample Values for a given sample.'''
    '''List of sample names'''
#    from sqlalchemy.ext.automap import automap_base
#    from sqlalchemy.orm import Session
#    from sqlalchemy import create_engine
    engine = create_engine("sqlite:///belly_button_biodiversity.sqlite")    
    # Declare a Base using `automap_base()`
    Base = automap_base()
    # Use the Base class to reflect the database tables
    Base.prepare(engine, reflect=True)
    # Assign the samples class to a variable called `Samples`
#    Samples2 = Base.classes
    # Create a session
#    session = Session(engine)
    #session = scoped_session(sessionmaker(bind=engine))
    # Create connection
    conn = engine.connect()
    data_samples = pd.read_sql("SELECT * FROM samples", conn)

    final_list=[]
    count = 1
    for c in data_samples.columns[1:]:
    #     print(c)
        all_sample_info = {}
        sample_values = []
        otu_id = []
    #     print(len(data_samples[c]))
        for x in range(len(data_samples[c])):
    #         print(len(data_samples[c]))
    #         print(data_samples[c][x])
    #         print(data_samples['otu_id'][x])
            if data_samples[c][x] != 0:     
                sample_values.append(data_samples[c][x])
                otu_id.append(data_samples['otu_id'][x])
        temp_df = pd.DataFrame({'sample_values': sample_values, 'otu_id': otu_id}, 
                               columns=['sample_values', 'otu_id'])
        temp_df = temp_df.sort_values('sample_values', ascending=False).reset_index(drop=True)
        temp_df['sample_values'] = temp_df['sample_values'].astype(float)
        temp_df['otu_id'] = temp_df['otu_id'].astype(str)
        s_values = []
        o_values = []
        for x in range(len(temp_df['sample_values'])):
            s_values.append(temp_df.sample_values[x])
            o_values.append(temp_df.otu_id[x])

        all_sample_info['otu_ids'] = o_values[0:10]
        all_sample_info['sample_values'] = s_values[0:10]
        all_sample_info_dict = {}
        all_sample_info_dict[data_samples.columns[count]]=all_sample_info
        final_list.append(all_sample_info_dict)
        count += 1
    return jsonify(final_list)


@app.route("/otu")
def get_otu_descriptions():
    '''List of OTU descriptions'''
    # Create engine using the `belly_button_biodiversity.sqlite` database file
    engine = create_engine("sqlite:///belly_button_biodiversity.sqlite")
    # Declare a Base using `automap_base()`
    Base = automap_base()
    # Use the Base class to reflect the database tables
    Base.prepare(engine, reflect=True)
    # Assign the samples class to a variable called `Samples`
    Samples2 = Base.classes
    # Create a session
    session = Session(engine)
    otu_list = []
    # first_row = session.query(Samples.otu).first()
    # abc = first_row.__dict__
    for row in session.query(Samples2.otu.lowest_taxonomic_unit_found).all():
        otu_list.append(row[0])
    # return otu_list
    return jsonify(otu_list)


#@app.route('/metadata/<sample>')
#def get_metadata(sample):
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
#    metadata_list = []
#    for x in range(len(sample_metadata_json.columns)):
#        metadata_info = {}
#        col = sample_metadata_json.columns[x]
#        metadata_info['AGE']  = sample_metadata_json[col]['AGE']
#        metadata_info['BBTYPE'] =     sample_metadata_json[col]['BBTYPE']
#        metadata_info['ETHNICITY'] =  sample_metadata_json[col]['ETHNICITY']
#        metadata_info['GENDER'] =     sample_metadata_json[col]['GENDER']
#        metadata_info['LOCATION'] =   sample_metadata_json[col]['LOCATION']
#        metadata_info['SAMPLEID'] =   sample_metadata_json[col]['SAMPLEID']
#        metadata_sample = {}
#        metadata_sample[col]=metadata_info
#        metadata_list.append(metadata_sample)
#    return jsonify(metadata_list)

@app.route('/metadata/<sample>')
def get_metadata(sample):
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
    
    return jsonify(metadata_list)



if __name__ == "__main__":
    app.run(debug=True)
    

