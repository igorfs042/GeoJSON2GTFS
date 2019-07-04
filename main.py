import json
from datetime import timedelta

ID = 0
ROUTE_NAME = ''
ROUTE_ID = ID
SERVICE_ID = ID
TRIP_ID = ID

INICIO = 8
FIM = 17

with open('input.json') as f:
    data = json.load(f)
f.close()

with open('./output/agency.txt', 'w') as f:
    f.writelines('agency_name,agency_url,agency_timezone')
    f.write('\n')
    f.writelines('UFERSA,https://ufersa.edu.br,America/Fortaleza')
    f.write('\n')
f.close()


with open('./output/calendar.txt', 'w') as f:
    f.writelines('service_id,monday,tuesday,wednesday,thursday,friday,saturday,sunday,start_date,end_date')
    f.write('\n')
f.close()


with open('./output/routes.txt', 'w') as f:
    f.writelines('route_id,route_short_name,route_long_name,route_type')
    f.write('\n')
f.close()


with open('./output/trips.txt', 'w') as f:
    f.writelines('route_id,service_id,trip_id')
    f.write('\n')
f.close()


with open('./output/stops.txt', 'w') as f:
    f.writelines('stop_id,stop_name,stop_lat,stop_lon')
    f.write('\n')
f.close()


with open('./output/stop_times.txt', 'w') as f:
    f.writelines('trip_id,arrival_time,departure_time,stop_id,stop_sequence')
    f.write('\n')
f.close()

for i in range(len(data)):

    ID = i
    ROUTE_NAME = data[i]['name'].upper()
    ROUTE_ID = ID
    SERVICE_ID = ID
    TRIP_ID = ID

    with open('./output/calendar.txt', 'a') as f:
        f.writelines(str(SERVICE_ID)+',1,1,1,1,1,1,1,20190101,20191231')
        f.write('\n')
    f.close()


    with open('./output/routes.txt', 'a') as f:
        f.writelines(str(ROUTE_ID)+','+str(ROUTE_NAME)+','+str(ROUTE_NAME)+',3')
        f.write('\n')
    f.close()


    with open('./output/trips.txt', 'a') as f:
        f.writelines(str(ROUTE_ID)+','+str(SERVICE_ID)+','+str(TRIP_ID))
        f.write('\n')
    f.close()


    stops = ''
    stop_times = ''
    j = 0

    hora_inicio = timedelta(hours=INICIO)
    hora_fim = timedelta(hours=FIM)
    tempo_medio = (FIM*60 - INICIO*60)/len(data[i]['stops'])

    hora = hora_inicio

    for item in data[i]['stops']:
        stops += str(item['id']) + "," + "P"+str(item['id']) + "," + str(item['location']['lat']) + "," + str(item['location']['lng']) + "\n"
        j += 1
        hora += timedelta(minutes=int(tempo_medio))
        stop_times += str(TRIP_ID)+"," + str(hora) +","+ str(hora) + "," + str(item['id']) +","+ str(j) + "\n"


    with open('./output/stops.txt', 'a') as f:
        f.write(stops)
    f.close()


    with open('./output/stop_times.txt', 'a') as f:
        f.write(stop_times)
    f.close()
