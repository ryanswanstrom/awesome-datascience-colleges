import pandas as pd

in_file = 'https://raw.githubusercontent.com/ryanswanstrom/awesome-datascience-colleges/master/data_science_colleges.csv'

## Read in the file
df = pd.read_csv(in_file)

# get a full degree name
df['DEGREE_FULL'] = df[['DEGREE']].apply(lambda x:
  ('Bachelors' if x[0]=='B' else 'Masters' if x[0]=='M' else 'Certificate' if x[0]=='C' else 'Doctorate' if x[0]=='D' else 'UNK'), axis=1)

df['html'] = df[['SCHOOL','PROGRAM','DEGREE_FULL','ONLINE','ONCAMPUS','URL']].apply(lambda x: 
  '<tr><td><b>{0}</b>[<a title="{0}-{1}" href="{5}" target="_blank">{1}</a>] </td><td>{2} </td><td>{3}/{4} </td></tr>'.format(x[0],x[1],x[2],x[3],x[4],x[5]), axis=1)

# write out the output
f = open('html.dat','w') 
for row in df['html']:
  f.write(row)
f.close()
