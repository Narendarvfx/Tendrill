import requests
import xlsxwriter

workbook = xlsxwriter.Workbook('essl.xlsx')
worksheet = workbook.add_worksheet()

url = "http://127.0.0.1:8000/api/essl/attendance/"
headers = {
    'Authorization': "token 90cca45e7d7cc3f2ae98832d77ab6bc1978bbf12" ,
    'Accept': 'application/json'
}
response = requests.request("GET", url, headers=headers)
print(response.json())
for i, data in enumerate(response.json()):
    worksheet.write('A'+str(i), data['employee_id'])
    worksheet.write('B'+str(i), data['punch_type'])
    worksheet.write('C'+str(i), data['punch_date'])

workbook.close()
