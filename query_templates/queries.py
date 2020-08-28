from datetime import datetime


def query_2(stop):
    return "http://localhost:8080/rdf4j-workbench/repositories/1/query?action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0APREFIX%20rdf%3A%20%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0A%0ASELECT%20DISTINCT%20%3Fenum%0AWHERE%20%7B%0A%20%20%20%20%3Fp%20a%20ontology%3AStop%20.%0A%20%20%20%20%3Fp%20ontology%3AStopName%20%3Fvalue%20.%0A%20%20%20%20FILTER%20regex(str(%3Fvalue)%2C%20%22{}%22)%20.%0A%20%20%20%20%3FstopTime%20ontology%3AhasStop%20%3Fp%20.%0A%20%20%20%20%3Ftrip%20ontology%3AhasStopTimes%20%3FstopTime%20.%0A%20%20%20%20%3Ftrip%20ontology%3AhasRoutes%20%3Froute%20.%0A%20%20%20%20%3Froute%20ontology%3AhasTransportEnum%20%3Fenum%20.%0A%7D%0A&limit_query=0&infer=true&".format(stop)


def query_3(comune, checkin):
    date_time_obj = datetime.strptime(checkin, '%Y-%m-%dT%H:%M:%S+02:00')  # 2020-08-21T14:30:00+02:00
    # print(date_time_obj)
    # print(date_time_obj.hour)
    # print(date_time_obj.minute)
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Fstarthour%20%3Fendhour%20%3Fstars%20%3Fstreet%20%3Fprovince%20%3Fnumber%20%3Flat%20%3Flon%20%3Faccommodationenum%0AWHERE%20%7B%0A%20%20%20%20%3FAccomodation%20a%20ontology%3AAccomodation%20.%0A%20%20%20%20%3FAccomodation%20ontology%3APoiName%20%3Fname%20.%0A%20%20%20%20%3FAccomodation%20ontology%3AhasAddress%20%3Faddr%20.%0A%20%20%09%3FAccomodation%20ontology%3ALatitude%20%3Flat%20.%0A%20%20%09%3FAccomodation%20ontology%3ALongitude%20%3Flon%20.%0A%20%20%09%3FAccomodation%20ontology%3AhasAccommodationEnum%20%3Faccommodationenum%20.%0A%20%20%20%20%3Faddr%20ontology%3ACity%20%27{}%27%20.%0A%20%20%20%20%3Faddr%20ontology%3AStreet%20%3Fstreet%20.%0A%20%20%09%3Faddr%20ontology%3AhasProvinceEnum%20%3Fprovince%20.%0A%20%20%20%20%3FAccomodation%20ontology%3AhasTimetable%20%3Ftt%20.%0A%20%20%20%20%3Ftt%20ontology%3AhasSchedules%20%3Fsch%20.%0A%20%20%20%20%3Fsch%20ontology%3AScheduleName%20%22checkin%22%20.%0A%20%20%20%20%3Fsch%20ontology%3AStartHour%20%3Fstarthour%20.%0A%20%20%20%20%3Fsch%20ontology%3AEndHour%20%3Fendhour%20.%0A%20%20%20%20FILTER%20(%3Fstarthour%20%3C%3D%20%27{}%3A{}%27)%0A%20%20%20%20%20%20OPTIONAL%7B%3FAccomodation%20ontology%3AStars%20%3Fstars%7D%0A%20%20OPTIONAL%7B%3Faddr%20ontology%3ANumber%20%3Fnumber%7D%0A%7D&limit_query=0&infer=true&".format(comune.lower(), date_time_obj.hour, date_time_obj.minute)


def query_4(region, shop_enum):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Fstreet%20%3Fcity%20%3Fnumber%20%3Flat%20%3Flon%0AWHERE%20%7B%0A%20%20%20%20%3Fshop%20a%20ontology%3AShop%20.%0A%20%20%20%20%3Fshop%20ontology%3APoiName%20%3Fname%20.%0A%20%20%20%20%3Fshop%20ontology%3AhasAddress%20%3Faddr%20.%0A%20%20%20%20%3Faddr%20ontology%3AhasProvinceEnum%20ontology%3A{}%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3AStreet%20%3Fstreet%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3ACity%20%3Fcity%20.%0A%20%20%09%3Faddr%20ontology%3ANumber%20%3Fnumber%20.%0A%20%20%09%3Fshop%20ontology%3ALatitude%20%3Flat%20.%0A%20%20%09%3Fshop%20ontology%3ALongitude%20%3Flon%20.%0A%20%20%20%20%3Fshop%20ontology%3AhasShopEnum%20ontology%3A{}%20.%0A%7D&limit_query=0&infer=true&".format(region, shop_enum)


def query_5(shop_enum):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Fstreet%20%3Fcity%20%3Fprovince%20%3Fnumber%20%3Flat%20%3Flon%0AWHERE%20%7B%0A%20%20%20%20%3Fshop%20a%20ontology%3AShop%20.%0A%20%20%20%20%3Fshop%20ontology%3APoiName%20%3Fname%20.%0A%20%20%20%20%3Fshop%20ontology%3AhasAddress%20%3Faddr%20.%0A%20%20%20%20%3Faddr%20ontology%3AhasProvinceEnum%20%3Fprovince%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3AStreet%20%3Fstreet%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3ACity%20%3Fcity%20.%0A%20%20%09%3Faddr%20ontology%3ANumber%20%3Fnumber%20.%0A%20%20%09%3Fshop%20ontology%3ALatitude%20%3Flat%20.%0A%20%20%09%3Fshop%20ontology%3ALongitude%20%3Flon%20.%0A%20%20%20%20%3Fshop%20ontology%3AhasShopEnum%20ontology%3A{}%20.%0A%7D%0A&limit_query=0&infer=true&".format(shop_enum)


def query_6(checkin):
    date_time_obj = datetime.strptime(checkin, '%Y-%m-%dT%H:%M:%S+02:00')
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Fstarthour%20%3Fendhour%20%3Fstars%20%3Fstreet%20%3Fcity%20%3Fnumber%20%3Fprovince%20%3Flat%20%3Flon%20%3Faccommodationenum%0AWHERE%20%7B%0A%20%20%20%20%3FAccomodation%20a%20ontology%3AAccomodation%20.%0A%20%20%20%20%3FAccomodation%20ontology%3APoiName%20%3Fname%20.%0A%20%20%20%20%3FAccomodation%20ontology%3AhasAddress%20%3Faddr%20.%0A%20%20%20%20%3FAccomodation%20ontology%3ALatitude%20%3Flat%20.%0A%20%20%20%20%3FAccomodation%20ontology%3ALongitude%20%3Flon%20.%0A%20%20%09%3FAccomodation%20ontology%3AhasAccommodationEnum%20%3Faccommodationenum%20.%0A%20%20%20%20%3Faddr%20ontology%3ACity%20%3Fcity%20.%0A%20%20%20%20%3Faddr%20ontology%3AStreet%20%3Fstreet%20.%0A%20%20%20%20%3Faddr%20ontology%3ANumber%20%3Fnumber%20.%0A%20%20%20%20%3Faddr%20ontology%3AhasProvinceEnum%20%3Fprovince%20.%0A%20%20%20%20%3FAccomodation%20ontology%3AhasTimetable%20%3Ftt%20.%0A%20%20%20%20%3Ftt%20ontology%3AhasSchedules%20%3Fsch%20.%0A%20%20%20%20%3Fsch%20ontology%3AScheduleName%20%22checkin%22%20.%0A%20%20%20%20%3Fsch%20ontology%3AStartHour%20%3Fstarthour%20.%0A%20%20%20%20%3Fsch%20ontology%3AEndHour%20%3Fendhour%20.%0A%20%20%20%20FILTER%20(%3Fstarthour%20%3C%3D%20%27{}%3A{}%27)%0A%20%20%20%20%20%20OPTIONAL%7B%3FAccomodation%20ontology%3AStars%20%3Fstars%7D%0A%7D&limit_query=0&infer=true&".format(date_time_obj.hour, date_time_obj.minute)


def query_7(shop_enum):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Flat%20%3Flon%20%3Fcity%20%3Fstreet%20%3Fnumber%20%3Fprovince%0AWHERE%20%7B%0A%20%20%20%20%3Fshop%20a%20ontology%3AShop%20.%0A%20%20%20%20%3Fshop%20ontology%3APoiName%20%3Fname%20.%0A%20%20%20%20%20%20%3Fshop%20ontology%3AhasAddress%20%3Faddr%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3ACity%20%3Fcity%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3AStreet%20%3Fstreet%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3ANumber%20%3Fnumber%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3AhasProvinceEnum%20%3Fprovince%20.%0A%20%20%20%20%3Fshop%20ontology%3ALatitude%20%3Flat%20.%0A%20%20%20%20%3Fshop%20ontology%3ALongitude%20%3Flon%20.%0A%20%20%20%20%3Fshop%20ontology%3AhasShopEnum%20ontology%3A{}%20.%0A%7D%0A&limit_query=0&infer=true&".format(shop_enum)


def query_8(difficulty, min_time, max_time):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Ftime%20%3Fpoi_from%20%3Fpoi_to%20%3Fpoi_from_lat%20%3Fpoi_from_lon%20%3Fpoi_to_lat%20%3Fpoi_to_lon%20%3Flength%0AWHERE%20%7B%0A%20%20%20%20%3Fpath%20a%20ontology%3AActivityPath%20.%0A%20%20%20%20%3Fpath%20ontology%3APathName%20%3Fname%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasDifficultyEnum%20ontology%3A{}%20.%0A%20%20%20%20%3Fpath%20ontology%3AAvgTravelTime_seconds%20%3Ftime%20.%0A%20%20%09%3Fpath%20ontology%3ALength%20%3Flength%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AfromPosition%20%3Fpoi_f%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AtoPosition%20%3Fpoi_t%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3APoiName%20%3Fpoi_from%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3APoiName%20%3Fpoi_to%20.%0A%20%20%09%3Fpoi_f%20ontology%3ALatitude%20%3Fpoi_from_lat%20.%0A%20%20%09%3Fpoi_f%20ontology%3ALongitude%20%3Fpoi_from_lon%20.%0A%20%20%09%3Fpoi_t%20ontology%3ALatitude%20%3Fpoi_to_lat%20.%0A%20%20%09%3Fpoi_t%20ontology%3ALongitude%20%3Fpoi_to_lon%20.%0A%20%20%20%20FILTER(%3Ftime%3E%3D{}%26%26%3Ftime%3C%3D{})%0A%7D&limit_query=0&infer=true&".format(difficulty, int(min_time), int(max_time))


def query_9(difficulty, equipment_required):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Ftime%20%3Fpoi_from%20%3Fpoi_to%20%3Fpoi_from_lat%20%3Fpoi_from_lon%20%3Fpoi_to_lat%20%3Fpoi_to_lon%20%3Flength%0AWHERE%20%7B%0A%20%20%20%20%3Fpath%20a%20ontology%3AActivityPath%20.%0A%20%20%20%20%3Fpath%20ontology%3APathName%20%3Fname%20.%0A%20%20%20%20%3Fpath%20ontology%3AAvgTravelTime_seconds%20%3Ftime%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3ALength%20%3Flength%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AfromPosition%20%3Fpoi_f%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AtoPosition%20%3Fpoi_t%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3APoiName%20%3Fpoi_from%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3APoiName%20%3Fpoi_to%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALatitude%20%3Fpoi_from_lat%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALongitude%20%3Fpoi_from_lon%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALatitude%20%3Fpoi_to_lat%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALongitude%20%3Fpoi_to_lon%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasDifficultyEnum%20ontology%3A{}%20.%0A%20%20%20%20%3Fpath%20ontology%3AEquipmentRequired%20{}%20.%0A%7D%0A&limit_query=0&infer=true&".format(difficulty, equipment_required)


def query_12(difficulty, length):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Ftime%20%3Fpoi_from%20%3Fpoi_to%20%3Fpoi_from_lat%20%3Fpoi_from_lon%20%3Fpoi_to_lat%20%3Fpoi_to_lon%20%3Flength%0AWHERE%20%7B%0A%20%20%20%20%3Fpath%20a%20ontology%3AActivityPath%20.%0A%20%20%20%20%3Fpath%20ontology%3APathName%20%3Fname%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasActivityEnum%20ontology%3AA_Walk%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasDifficultyEnum%20ontology%3A{}%20.%0A%20%20%20%20%3Fpath%20ontology%3AAvgTravelTime_seconds%20%3Ftime%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3ALength%20%3Flength%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AfromPosition%20%3Fpoi_f%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AtoPosition%20%3Fpoi_t%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3APoiName%20%3Fpoi_from%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3APoiName%20%3Fpoi_to%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALatitude%20%3Fpoi_from_lat%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALongitude%20%3Fpoi_from_lon%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALatitude%20%3Fpoi_to_lat%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALongitude%20%3Fpoi_to_lon%20.%0A%20%20%20%20FILTER(%3Flength%3C%3D{})%0A%7D%0A&limit_query=0&infer=true&".format(difficulty, length)


def query_13(min_difficulty, max_difficulty):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Ftime%20%3Fpoi_from%20%3Fpoi_to%20%3Fpoi_from_lat%20%3Fpoi_from_lon%20%3Fpoi_to_lat%20%3Fpoi_to_lon%20%3Flength%0AWHERE%20%7B%0A%20%20%20%20%3Fpath%20a%20ontology%3AActivityPath%20.%0A%20%20%20%20%3Fpath%20ontology%3APathName%20%3Fname%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasActivityEnum%20ontology%3AA_Walk%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasDifficultyEnum%20%3Fdiff%20.%0A%20%20%20%20%3Fpath%20ontology%3AAvgTravelTime_seconds%20%3Ftime%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3ALength%20%3Flength%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AfromPosition%20%3Fpoi_f%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AtoPosition%20%3Fpoi_t%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3APoiName%20%3Fpoi_from%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3APoiName%20%3Fpoi_to%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALatitude%20%3Fpoi_from_lat%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALongitude%20%3Fpoi_from_lon%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALatitude%20%3Fpoi_to_lat%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALongitude%20%3Fpoi_to_lon%20.%0A%20%20%20%20FILTER(%3Fdiff%3Dontology%3A{}%7C%7C%3Fdiff%3Dontology%3A{})%0A%7D&limit_query=0&infer=true&".format(min_difficulty, max_difficulty)


def query_14(difficulty):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Fsport%20%3Ftime%20%3Fpoi_from%20%3Fpoi_to%20%3Fpoi_from_lat%20%3Fpoi_from_lon%20%3Fpoi_to_lat%20%3Fpoi_to_lon%20%3Flength%0AWHERE%20%7B%0A%20%20%20%20%3Fpath%20a%20ontology%3AActivityPath%20.%0A%20%20%20%20%3Fpath%20ontology%3APathName%20%3Fname%20.%0A%20%20%20%20%3Fpath%20ontology%3AAvgTravelTime_seconds%20%3Ftime%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3ALength%20%3Flength%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AfromPosition%20%3Fpoi_f%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AtoPosition%20%3Fpoi_t%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3APoiName%20%3Fpoi_from%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3APoiName%20%3Fpoi_to%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALatitude%20%3Fpoi_from_lat%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALongitude%20%3Fpoi_from_lon%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALatitude%20%3Fpoi_to_lat%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALongitude%20%3Fpoi_to_lon%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasActivityEnum%20%3Fsport%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasDifficultyEnum%20ontology%3A{}%20.%0A%20%20%20%20FILTER(%3Fsport%3Dontology%3AA_Walk%7C%7C%3Fsport%3Dontology%3AA_Bike%7C%7C%3Fsport%3Dontology%3AA_Other)%0A%7D&limit_query=0&infer=true&".format(difficulty)


def query_16():
    return


def query_17(poi_from):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Ftime%20%3Fpoi_from%20%3Fpoi_to%20%3Fpoi_from_lat%20%3Fpoi_from_lon%20%3Fpoi_to_lat%20%3Fpoi_to_lon%20%3Flength%0AWHERE%20%7B%0A%20%20%20%20%3Fpath%20a%20ontology%3AActivityPath%20.%0A%20%20%20%20%3Fpath%20ontology%3APathName%20%3Fname%20.%0A%20%20%20%20%3Fpath%20ontology%3AAvgTravelTime_seconds%20%3Ftime%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3ALength%20%3Flength%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AfromPosition%20%3Fpoi_f%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AtoPosition%20%3Fpoi_t%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3APoiName%20%3Fpoi_from%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3APoiName%20%3Fpoi_to%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALatitude%20%3Fpoi_from_lat%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALongitude%20%3Fpoi_from_lon%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALatitude%20%3Fpoi_to_lat%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALongitude%20%3Fpoi_to_lon%20.%0A%20%20%20%20FILTER%20(regex(str(%3Fpoi_from)%2C%20%27{}%27)).%0A%7D%0A&limit_query=0&infer=true&".format(poi_from)


def query_18(poi_from, poi_to):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Ftime%20%3Fpoi_from%20%3Fpoi_to%20%3Fpoi_from_lat%20%3Fpoi_from_lon%20%3Fpoi_to_lat%20%3Fpoi_to_lon%20%3Flength%20%3Fdifficulty%0AWHERE%20%7B%0A%20%20%20%20%3Fpath%20a%20ontology%3AActivityPath%20.%0A%20%20%20%20%3Fpath%20ontology%3APathName%20%3Fname%20.%0A%20%20%20%20%3Fpath%20ontology%3AAvgTravelTime_seconds%20%3Ftime%20.%0A%20%20%09%3Fpath%20ontology%3AhasDifficultyEnum%20%3Fdifficulty%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3ALength%20%3Flength%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AfromPosition%20%3Fpoi_f%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AtoPosition%20%3Fpoi_t%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3APoiName%20%3Fpoi_from%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3APoiName%20%3Fpoi_to%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALatitude%20%3Fpoi_from_lat%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALongitude%20%3Fpoi_from_lon%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALatitude%20%3Fpoi_to_lat%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALongitude%20%3Fpoi_to_lon%20.%0A%20%20%20%20FILTER%20(regex(str(%3Fpoi_from)%2C%20%27{}%27)%20%26%26%20regex(str(%3Fpoi_to)%2C%20%27{}%27)).%0A%7D%0A&limit_query=0&infer=true&".format(poi_from, poi_to)


def query_19(path_number):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Ftime%20%3Fdifficulty%20%3Fpoi_from%20%3Fpoi_to%20%3Fpoi_from_lat%20%3Fpoi_from_lon%20%3Fpoi_to_lat%20%3Fpoi_to_lon%20%3Flength%0AWHERE%20%7B%0A%20%20%20%20%3Fpath%20a%20ontology%3AActivityPath%20.%0A%20%20%20%20%3Fpath%20ontology%3APathName%20%3Fname%20.%0A%20%20%20%20FILTER%20regex(str(%3Fname)%2C%20%22{}%22)%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasActivityEnum%20%3Ftype%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasDifficultyEnum%20%3Fdifficulty%20.%0A%20%20%20%20%3Fpath%20ontology%3AAvgTravelTime_seconds%20%3Ftime%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3ALength%20%3Flength%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AfromPosition%20%3Fpoi_f%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AtoPosition%20%3Fpoi_t%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3APoiName%20%3Fpoi_from%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3APoiName%20%3Fpoi_to%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALatitude%20%3Fpoi_from_lat%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALongitude%20%3Fpoi_from_lon%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALatitude%20%3Fpoi_to_lat%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALongitude%20%3Fpoi_to_lon%20.%0A%7D&limit_query=0&infer=true&".format(path_number)


def query_20():
    return


def query_21():
    return


def query_22():
    return


def query_23():
    return


def query_24():
    return
