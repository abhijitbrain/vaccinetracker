# Updated By Abhijit

from cowin_api import CoWinAPI

#state_id = '26'

cowin = CoWinAPI()

district_id = '446'
date = '14-05-2021'     # Optional. Takes today's date by default
#min_age_limit = 20      # Optional. By default returns centers without filtering by min_age_limit
counter = 0

#available_centers = cowin.get_availability_by_district(district_id, date, min_age_limit)

#center              =   available_centers["centers"]
#c_details           =   center[0]       # 50
#sessions            =   c_details['sessions']
#s_details           =   sessions[0]     #7
#available_capacity  =   s_details['available_capacity']

# For 18+ age
available_centers = cowin.get_availability_by_district(district_id, date, 19)
center              =   available_centers["centers"]
for i in range(0,len(center)) :
    for j in range(0,len(center[i]['sessions'])):
        available = available_centers['centers'][i]['sessions'][j]['available_capacity'];
        #print(available)
        if available > 0 :
            print("18+")
            print("Name : ", center[i]['name'])
            print("Available slots : ", available)
            print("Date : ", available_centers['centers'][i]['sessions'][j]['date'])
            counter+=1
            #print('\n')
        
if counter == 0 :
    print("18+ Sorry No Slots Available")

# for 45+ age
available_centers = cowin.get_availability_by_district(district_id, date, 46)
center              =   available_centers["centers"]
for i in range(0,len(center)) :
    for j in range(0,len(center[i]['sessions'])):
        available = available_centers['centers'][i]['sessions'][j]['available_capacity'];
        #print(available)
        if available > 0 :
            print("45+")
            print("Name : ", center[i]['name'])
            print("Available slots : ", available)
            print("Date : ", available_centers['centers'][i]['sessions'][j]['date'])
            counter+=1
            #print('\n')
        
if counter == 0 :
    print("45+ Sorry No Slots Available")
