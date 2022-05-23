import xlsxwriter

import api


def get_employees_teamLead():
    data = api.getAllArtists()
    # Create an new Excel file and add a worksheet.
    try:
        workbook = xlsxwriter.Workbook('demo.xlsx')
        worksheet = workbook.add_worksheet()

        # Widen the first column to make the text clearer.
        worksheet.set_column('A:A', 20)

        # Add a bold format to use to highlight cells.
        bold = workbook.add_format({'bold': True})

        # Write some simple text.
        worksheet.write('A1', 'Employee Code', bold)
        worksheet.write('B1', 'Employee Name', bold)

        # Text with formatting.
        worksheet.write('C1', 'Department', bold)

        # Text with formatting.
        worksheet.write('D1', 'Team', bold)
        team_data = api.get_team_list()
        for i, data in enumerate(data):
            if data['employement_status'] == "Active":
                for team_id in team_data:

                    if data['team'] == team_id['id']:
                        team_lead_id = team_id['lead']
                if data['team'] is not None:
                    team = api.get_employee_data(str(team_lead_id))
                    team_lead = team['fullName']
                else:
                    team_lead = ""
                worksheet.write('A{}'.format(i + 2),data['employee_id'])
                worksheet.write('B{}'.format(i + 2), data['fullName'])
                worksheet.write('C{}'.format(i + 2), data['department'])
                worksheet.write('D{}'.format(i + 2), team_lead)

        workbook.close()
    except Exception as e:
        print(e)

get_employees_teamLead()