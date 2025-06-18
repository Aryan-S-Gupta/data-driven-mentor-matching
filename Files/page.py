import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/spreadsheets'," https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('gs_credential.json',scope)
client = gspread.authorize(credentials)
sheet = client.create("First Sheet")
sheet.share('guptaaryansomesh@gmail.com', perm_type='user', role='writer')