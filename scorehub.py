# Necessary packages
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import requests
from bs4 import BeautifulSoup # webscrapping
import json # Extract the json
import webbrowser

# Create the urls for the season and league
base_url = 'https://understat.com/league'
leagues = ['La_liga', 'EPL', 'Bundesliga', 'Serie_A', 'Ligue_1', 'RFPL']
seasons = ['2018','2019','2020', '2021', '2022']

# Getting the latest data for EPL 2022
url = base_url+'/'+leagues[1]+'/'+seasons[4]
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser') # changed this from 'lxml' to 'html.parser' 

# Based on the structure of the webpage, I found that data is in the JSON variable, under <script> tags
scripts = soup.find_all('script')

# Extract the json
string_with_json_obj = ''

# Find data for teams
for el in scripts:
    if 'teamsData' in str(el):
      string_with_json_obj = str(el).strip()
      
# print(string_with_json_obj)

# strip unnecessary symbols and get only JSON data
ind_start = string_with_json_obj.index("('")+2
ind_end = string_with_json_obj.index("')")
json_data = string_with_json_obj[ind_start:ind_end]

json_data = json_data.encode('utf8').decode('unicode_escape')

# Everyone loves Arsenal so lets start by getting their info
# convert JSON data into Python dictionary
data = json.loads(json_data)
print(data.keys())
print('='*50)
print(data['83'].keys()) # Change from 138
print('='*50)
print(data['83']['id'])
print('='*50)
print(data['83']['title'])
print('='*50)
print(data['83']['history'][0])

# Get teams and their relevant ids and put them into separate dictionary
teams = {}
for id in data.keys():
  teams[id] = data[id]['title']

print(teams)

# EDA to get a feeling of how the JSON is structured
# Column names are all the same, so we just use first element
columns = []
# Check the sample of values per each column
values = []
for id in data.keys():
  columns = list(data[id]['history'][0].keys())
  values = list(data[id]['history'][0].values())
  break

print(columns)
print(values)

# Getting data for all teams
dataframes = {}
for id, team in teams.items():
  teams_data = []
  for row in data[id]['history']:
    teams_data.append(list(row.values()))
    
  df = pd.DataFrame(teams_data, columns=columns)
  dataframes[team] = df
  print('Added data for {}.'.format(team))

# Sample check of our newly created DataFrame
dataframes['Arsenal'].head(5)

for team, df in dataframes.items():
  dataframes[team]['ppda_coef'] = dataframes[team]['ppda'].apply(lambda x: x['att']/x['def'] if x['def'] != 0 else 0)
  dataframes[team]['oppda_coef'] = dataframes[team]['ppda_allowed'].apply(lambda x: x['att']/x['def'] if x['def'] != 0 else 0)
  
# And check how our new dataframes look based on Arsenal dataframe
dataframes['Arsenal'].head(2)

cols_to_sum = ['xG', 'xGA', 'npxG', 'npxGA', 'deep', 'deep_allowed', 'scored', 'missed', 'xpts', 'wins', 'draws', 'loses', 'pts', 'npxGD']
cols_to_mean = ['ppda_coef', 'oppda_coef']

frames = []
for team, df in dataframes.items():
  sum_data = pd.DataFrame(df[cols_to_sum].sum()).transpose()
  mean_data = pd.DataFrame(df[cols_to_mean].mean()).transpose()
  final_df = sum_data.join(mean_data)
  final_df['team'] = team
  final_df['matches'] = len(df)
  frames.append(final_df)
  
full_stat = pd.concat(frames)

# Next we reorder columns for better readability, sort rows based on points, reset index and add column 'position'.
full_stat = full_stat[['team', 'matches', 'wins', 'draws', 'loses', 'scored', 'missed', 'pts', 'xG', 'npxG', 'xGA', 'npxGA', 'npxGD', 'ppda_coef', 'oppda_coef', 'deep', 'deep_allowed', 'xpts']]
full_stat.sort_values('pts', ascending=False, inplace=True)
full_stat.reset_index(inplace=True, drop=True)
full_stat['position'] = range(1,len(full_stat)+1)

# Also in the original table we have values of differences between expected metrics and real. Let's add those too.
full_stat['xG_diff'] = full_stat['xG'] - full_stat['scored']
full_stat['xGA_diff'] = full_stat['xGA'] - full_stat['missed']
full_stat['xpts_diff'] = full_stat['xpts'] - full_stat['pts']

# Converting floats to integers where apropriate
cols_to_int = ['wins', 'draws', 'loses', 'scored', 'missed', 'pts', 'deep', 'deep_allowed']
full_stat[cols_to_int] = full_stat[cols_to_int].astype(int)

# Prettifying output and final view of a DataFrame
col_order = ['position','team', 'matches', 'wins', 'draws', 'loses', 'scored', 'missed', 'pts', 'xG', 'xG_diff', 'npxG', 'xGA', 'xGA_diff', 'npxGA', 'npxGD', 'ppda_coef', 'oppda_coef', 'deep', 'deep_allowed', 'xpts', 'xpts_diff']
full_stat = full_stat[col_order]
pd.options.display.float_format = '{:,.2f}'.format
full_stat.head(10)

print(full_stat)

# Converting the data frame to an HTML Table
html_table = full_stat.to_html()
# print(html_table)

# write html to file
text_file = open("index.html", "w")
text_file.write(html_table)
text_file.close()

url = 'index.html'
webbrowser.open(url, new=2)  # open in new tab