import json
from datetime import timedelta

ROUTE_SHORT_NAME = ''
ROUTE_LONG_NAME = ''
ROUTE_ID = 0
SERVICE_ID = 0
TRIP_ID = 0

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
    f.writelines(
        'service_id,monday,tuesday,wednesday,thursday,friday,saturday,sunday,start_date,end_date')
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

    ROUTE_SHORT_NAME = data[i]['short_name'].upper()
    ROUTE_LONG_NAME = data[i]['long_name'].upper()
    ROUTE_ID = data[i]['id']

    with open('./output/routes.txt', 'a') as f:
        f.writelines(str(ROUTE_ID)+','+str(ROUTE_SHORT_NAME) +
                     ','+str(ROUTE_LONG_NAME)+',3')
        f.write('\n')
    f.close()

    for j in range(len(data[i]['calendar'])):
        with open('./output/calendar.txt', 'a') as f:
            MONDAY = "1" if data[i]['calendar'][j]['monday'] else "0"
            TUESDAY = "1" if data[i]['calendar'][j]['tuesday'] else "0"
            WEDNESDAY = "1" if data[i]['calendar'][j]['wednesday'] else "0"
            THURSDAY = "1" if data[i]['calendar'][j]['thursday'] else "0"
            FRIDAY = "1" if data[i]['calendar'][j]['friday'] else "0"
            SATURDAY = "1" if data[i]['calendar'][j]['saturday'] else "0"
            SUNDAY = "1" if data[i]['calendar'][j]['sunday'] else "0"
            f.writelines(str(SERVICE_ID)+','+str(MONDAY)+','+str(TUESDAY) +
                         ','+str(WEDNESDAY)+','+str(THURSDAY)+','+str(FRIDAY)+','+str(SATURDAY)+','+str(SUNDAY)+',20190101,20191231')
            f.write('\n')
        f.close()

        with open('./output/trips.txt', 'a') as f:
            f.writelines(str(ROUTE_ID)+',' +
                         str(SERVICE_ID)+','+str(TRIP_ID))
            f.write('\n')
        f.close()

        TRIP_ID += 1
        SERVICE_ID += 1

        for k in range(len(data[i]['stop_times'])):
            stops = ''
            stop_times = ''

            HORA_INICIO = data[i]['stop_times'][k]['departure_time']['hour']
            MINUTO_INICIO = data[i]['stop_times'][k]['departure_time']['minute']
            HORA_FIM = data[i]['stop_times'][k]['arrival time']['hour']
            MINUTO_FIM = data[i]['stop_times'][k]['arrival time']['minute']

            hora_inicio_total = timedelta(
                hours=HORA_INICIO, minutes=MINUTO_INICIO)
            hora_fim = timedelta(hours=HORA_FIM, minutes=MINUTO_FIM)
            tempo_medio = ((HORA_FIM*60 + MINUTO_FIM) -
                           (HORA_INICIO*60 + MINUTO_INICIO))/len(data[i]['stops'])

            hora = hora_inicio_total

            for item in data[i]['stops']:
                hora += timedelta(minutes=int(tempo_medio))

                stops += str(TRIP_ID)+str(item['id'])[0:2]+str(hora.seconds) + "," + "P"+str(item['id']) + "," + \
                    str(item['location']['lat']) + "," + \
                    str(item['location']['lng']) + "\n"

                stop_times += str(TRIP_ID)+"," + str(hora) + "," + \
                    str(hora) + "," + str(TRIP_ID)+str(item['id'])[0:2]+str(hora.seconds) + "," + str(TRIP_ID)+str(
                        item['id'])[0:2]+str((hora + timedelta(minutes=int(tempo_medio))).seconds) + "\n"

            with open('./output/stops.txt', 'a') as f:
                f.write(stops)
            f.close()

            with open('./output/stop_times.txt', 'a') as f:
                f.write(stop_times)
            f.close()
