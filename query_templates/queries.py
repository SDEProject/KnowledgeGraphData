from datetime import datetime


def query_3(comune, checkin):
    try:
        date_time_obj = datetime.strptime(checkin, '%Y-%m-%dT%H:%M:%S+02:00')  # 2020-08-21T14:30:00+02:00
    except:
        print('Error in datetime parsing')
        return None
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


def query_12():
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Ftime%20%3Fpoi_from%20%3Fpoi_to%20%3Fpoi_from_lat%20%3Fpoi_from_lon%20%3Fpoi_to_lat%20%3Fpoi_to_lon%20%3Flength%0AWHERE%20%7B%0A%20%20%20%20%3Fpath%20a%20ontology%3AActivityPath%20.%0A%20%20%20%20%3Fpath%20ontology%3APathName%20%3Fname%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasActivityEnum%20ontology%3AA_Walk%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasDifficultyEnum%20ontology%3ALow%20.%0A%20%20%20%20%3Fpath%20ontology%3AAvgTravelTime_seconds%20%3Ftime%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3ALength%20%3Flength%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AfromPosition%20%3Fpoi_f%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AtoPosition%20%3Fpoi_t%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3APoiName%20%3Fpoi_from%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3APoiName%20%3Fpoi_to%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALatitude%20%3Fpoi_from_lat%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALongitude%20%3Fpoi_from_lon%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALatitude%20%3Fpoi_to_lat%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALongitude%20%3Fpoi_to_lon%20.%0A%20%20%20%20FILTER(%3Flength%3C%3D5000)%0A%7D%0A&limit_query=0&infer=true&"


def query_14(difficulty):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Fsport%20%3Ftime%20%3Fpoi_from%20%3Fpoi_to%20%3Fpoi_from_lat%20%3Fpoi_from_lon%20%3Fpoi_to_lat%20%3Fpoi_to_lon%20%3Flength%0AWHERE%20%7B%0A%20%20%20%20%3Fpath%20a%20ontology%3AActivityPath%20.%0A%20%20%20%20%3Fpath%20ontology%3APathName%20%3Fname%20.%0A%20%20%20%20%3Fpath%20ontology%3AAvgTravelTime_seconds%20%3Ftime%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3ALength%20%3Flength%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AfromPosition%20%3Fpoi_f%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AtoPosition%20%3Fpoi_t%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3APoiName%20%3Fpoi_from%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3APoiName%20%3Fpoi_to%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALatitude%20%3Fpoi_from_lat%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALongitude%20%3Fpoi_from_lon%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALatitude%20%3Fpoi_to_lat%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALongitude%20%3Fpoi_to_lon%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasActivityEnum%20%3Fsport%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasDifficultyEnum%20ontology%3A{}%20.%0A%20%20%20%20FILTER(%3Fsport%3Dontology%3AA_Walk%7C%7C%3Fsport%3Dontology%3AA_Bike%7C%7C%3Fsport%3Dontology%3AA_Other)%0A%7D&limit_query=0&infer=true&".format(difficulty)


def query_17(poi_from):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Ftime%20%3Fpoi_from%20%3Fpoi_to%20%3Fpoi_from_lat%20%3Fpoi_from_lon%20%3Fpoi_to_lat%20%3Fpoi_to_lon%20%3Flength%20%3Fdifficulty%0AWHERE%20%7B%0A%20%20%20%20%3Fpath%20a%20ontology%3AActivityPath%20.%0A%20%20%20%20%3Fpath%20ontology%3APathName%20%3Fname%20.%0A%20%20%20%20%3Fpath%20ontology%3AAvgTravelTime_seconds%20%3Ftime%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3ALength%20%3Flength%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AfromPosition%20%3Fpoi_f%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AtoPosition%20%3Fpoi_t%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3APoiName%20%3Fpoi_from%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3APoiName%20%3Fpoi_to%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALatitude%20%3Fpoi_from_lat%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALongitude%20%3Fpoi_from_lon%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALatitude%20%3Fpoi_to_lat%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALongitude%20%3Fpoi_to_lon%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AhasDifficultyEnum%20%3Fdifficulty%20.%0A%20%20%20%20FILTER%20(regex(str(%3Fpoi_from)%2C%20%27{}%27)).%0A%7D&limit_query=0&infer=true&".format(poi_from)


def query_18(poi_from, poi_to):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Ftime%20%3Fpoi_from%20%3Fpoi_to%20%3Fpoi_from_lat%20%3Fpoi_from_lon%20%3Fpoi_to_lat%20%3Fpoi_to_lon%20%3Flength%20%3Fdifficulty%0AWHERE%20%7B%0A%20%20%20%20%3Fpath%20a%20ontology%3AActivityPath%20.%0A%20%20%20%20%3Fpath%20ontology%3APathName%20%3Fname%20.%0A%20%20%20%20%3Fpath%20ontology%3AAvgTravelTime_seconds%20%3Ftime%20.%0A%20%20%09%3Fpath%20ontology%3AhasDifficultyEnum%20%3Fdifficulty%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3ALength%20%3Flength%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AfromPosition%20%3Fpoi_f%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AtoPosition%20%3Fpoi_t%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3APoiName%20%3Fpoi_from%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3APoiName%20%3Fpoi_to%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALatitude%20%3Fpoi_from_lat%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALongitude%20%3Fpoi_from_lon%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALatitude%20%3Fpoi_to_lat%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALongitude%20%3Fpoi_to_lon%20.%0A%20%20%20%20FILTER%20(regex(str(%3Fpoi_from)%2C%20%27{}%27)%20%26%26%20regex(str(%3Fpoi_to)%2C%20%27{}%27)).%0A%7D%0A&limit_query=0&infer=true&".format(poi_from, poi_to)


def query_19(path_number):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Ftime%20%3Fdifficulty%20%3Fpoi_from%20%3Fpoi_to%20%3Fpoi_from_lat%20%3Fpoi_from_lon%20%3Fpoi_to_lat%20%3Fpoi_to_lon%20%3Flength%0AWHERE%20%7B%0A%20%20%20%20%3Fpath%20a%20ontology%3AActivityPath%20.%0A%20%20%20%20%3Fpath%20ontology%3APathName%20%3Fname%20.%0A%20%20%20%20FILTER%20regex(str(%3Fname)%2C%20%22{}%22)%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasActivityEnum%20%3Ftype%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasDifficultyEnum%20%3Fdifficulty%20.%0A%20%20%20%20%3Fpath%20ontology%3AAvgTravelTime_seconds%20%3Ftime%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3ALength%20%3Flength%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AfromPosition%20%3Fpoi_f%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AtoPosition%20%3Fpoi_t%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3APoiName%20%3Fpoi_from%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3APoiName%20%3Fpoi_to%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALatitude%20%3Fpoi_from_lat%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALongitude%20%3Fpoi_from_lon%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALatitude%20%3Fpoi_to_lat%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALongitude%20%3Fpoi_to_lon%20.%0A%7D&limit_query=0&infer=true&".format(path_number)


def query_25(comune):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Fstarthour%20%3Fendhour%20%3Fstars%20%3Fstreet%20%3Fnumber%20%3Fprovince%20%3Flat%20%3Flon%20%3Faccommodationenum%0AWHERE%20%7B%0A%20%20%20%20%3FAccomodation%20a%20ontology%3AAccomodation%20.%0A%20%20%20%20%3FAccomodation%20ontology%3APoiName%20%3Fname%20.%0A%20%20%20%20%3FAccomodation%20ontology%3AhasAddress%20%3Faddr%20.%0A%20%20%20%20%3FAccomodation%20ontology%3ALatitude%20%3Flat%20.%0A%20%20%20%20%3FAccomodation%20ontology%3ALongitude%20%3Flon%20.%0A%20%20%20%20%20%20%3FAccomodation%20ontology%3AhasAccommodationEnum%20%3Faccommodationenum%20.%0A%20%20%20%20%3Faddr%20ontology%3ACity%20%27{}%27%20.%0A%20%20%20%20%3Faddr%20ontology%3AStreet%20%3Fstreet%20.%0A%20%20%20%20%3Faddr%20ontology%3ANumber%20%3Fnumber%20.%0A%20%20%20%20%3Faddr%20ontology%3AhasProvinceEnum%20%3Fprovince%20.%0A%20%20%20%20%3FAccomodation%20ontology%3AhasTimetable%20%3Ftt%20.%0A%20%20%20%20%3Ftt%20ontology%3AhasSchedules%20%3Fsch%20.%0A%20%20%20%20%3Fsch%20ontology%3AScheduleName%20%22checkin%22%20.%0A%20%20%20%20%3Fsch%20ontology%3AStartHour%20%3Fstarthour%20.%0A%20%20%20%20%3Fsch%20ontology%3AEndHour%20%3Fendhour%20.%0A%20%20%20%20%20%20OPTIONAL%7B%3FAccomodation%20ontology%3AStars%20%3Fstars%7D%0A%7D%0A&limit_query=0&infer=true&".format(comune.lower())


def query_26(regione):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Fstarthour%20%3Fendhour%20%3Fstars%20%3Fstreet%20%3Fnumber%20%3Fcity%20%3Flat%20%3Flon%20%3Faccommodationenum%0AWHERE%20%7B%0A%20%20%20%20%3FAccomodation%20a%20ontology%3AAccomodation%20.%0A%20%20%20%20%3FAccomodation%20ontology%3APoiName%20%3Fname%20.%0A%20%20%20%20%3FAccomodation%20ontology%3AhasAddress%20%3Faddr%20.%0A%20%20%20%20%3FAccomodation%20ontology%3ALatitude%20%3Flat%20.%0A%20%20%20%20%3FAccomodation%20ontology%3ALongitude%20%3Flon%20.%0A%20%20%20%20%20%20%3FAccomodation%20ontology%3AhasAccommodationEnum%20%3Faccommodationenum%20.%0A%20%20%20%20%3Faddr%20ontology%3ACity%20%3Fcity%20.%0A%20%20%20%20%3Faddr%20ontology%3AStreet%20%3Fstreet%20.%0A%20%20%20%20%3Faddr%20ontology%3ANumber%20%3Fnumber%20.%0A%20%20%20%20%3Faddr%20ontology%3AhasProvinceEnum%20ontology%3A{}%20.%0A%20%20%20%20%3FAccomodation%20ontology%3AhasTimetable%20%3Ftt%20.%0A%20%20%20%20%3Ftt%20ontology%3AhasSchedules%20%3Fsch%20.%0A%20%20%20%20%3Fsch%20ontology%3AScheduleName%20%22checkin%22%20.%0A%20%20%20%20%3Fsch%20ontology%3AStartHour%20%3Fstarthour%20.%0A%20%20%20%20%3Fsch%20ontology%3AEndHour%20%3Fendhour%20.%0A%20%20%20%20%20%20OPTIONAL%7B%3FAccomodation%20ontology%3AStars%20%3Fstars%7D%0A%7D&limit_query=0&infer=true&".format(regione)


def query_27(equipment):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Ftime%20%3Fpoi_from%20%3Fpoi_to%20%3Fpoi_from_lat%20%3Fpoi_from_lon%20%3Fpoi_to_lat%20%3Fpoi_to_lon%20%3Flength%20%3Fdifficulty%0AWHERE%20%7B%0A%20%20%20%20%3Fpath%20a%20ontology%3AActivityPath%20.%0A%20%20%20%20%3Fpath%20ontology%3APathName%20%3Fname%20.%0A%20%20%20%20%3Fpath%20ontology%3AAvgTravelTime_seconds%20%3Ftime%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3ALength%20%3Flength%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AfromPosition%20%3Fpoi_f%20.%0A%20%20%20%20%20%20%3Fpath%20ontology%3AtoPosition%20%3Fpoi_t%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3APoiName%20%3Fpoi_from%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3APoiName%20%3Fpoi_to%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALatitude%20%3Fpoi_from_lat%20.%0A%20%20%20%20%20%20%3Fpoi_f%20ontology%3ALongitude%20%3Fpoi_from_lon%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALatitude%20%3Fpoi_to_lat%20.%0A%20%20%20%20%20%20%3Fpoi_t%20ontology%3ALongitude%20%3Fpoi_to_lon%20.%0A%20%20%20%20%3Fpath%20ontology%3AhasDifficultyEnum%20%3Fdifficulty%20.%0A%20%20%20%20%3Fpath%20ontology%3AEquipmentRequired%20{}%20.%0A%7D%0A&limit_query=0&infer=true&".format(equipment)


def query_28(comune):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Fstreet%20%3Fprovince%20%3Fnumber%20%3Flat%20%3Flon%20%0AWHERE%20%7B%0A%20%20%20%20%3Fshop%20a%20ontology%3AShop%20.%0A%20%20%20%20%3Fshop%20ontology%3APoiName%20%3Fname%20.%0A%20%20%20%20%3Fshop%20ontology%3AhasAddress%20%3Faddr%20.%0A%20%20%20%20%3Faddr%20ontology%3AhasProvinceEnum%20%3Fprovince%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3AStreet%20%3Fstreet%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3ACity%20%27{}%27%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3ANumber%20%3Fnumber%20.%0A%20%20%20%20%20%20%3Fshop%20ontology%3ALatitude%20%3Flat%20.%0A%20%20%20%20%20%20%3Fshop%20ontology%3ALongitude%20%3Flon%20.%0A%20%20%20%20%3Fshop%20ontology%3AhasShopEnum%20ontology%3AS_Local_traditional_products%20.%0A%7D&limit_query=0&infer=true&".format(comune)


def query_29():
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Fstarthour%20%3Fendhour%20%3Fstars%20%3Fstreet%20%3Fnumber%20%3Fcity%20%3Flat%20%3Flon%20%3Faccommodationenum%20%3Fprovince%0AWHERE%20%7B%0A%20%20%20%20%3FAccomodation%20a%20ontology%3AAccomodation%20.%0A%20%20%20%20%3FAccomodation%20ontology%3APoiName%20%3Fname%20.%0A%20%20%20%20%3FAccomodation%20ontology%3AhasAddress%20%3Faddr%20.%0A%20%20%20%20%3FAccomodation%20ontology%3ALatitude%20%3Flat%20.%0A%20%20%20%20%3FAccomodation%20ontology%3ALongitude%20%3Flon%20.%0A%20%20%20%20%20%20%3FAccomodation%20ontology%3AhasAccommodationEnum%20%3Faccommodationenum%20.%0A%20%20%20%20%3Faddr%20ontology%3ACity%20%3Fcity%20.%0A%20%20%20%20%3Faddr%20ontology%3AStreet%20%3Fstreet%20.%0A%20%20%20%20%3Faddr%20ontology%3ANumber%20%3Fnumber%20.%0A%20%20%20%20%3Faddr%20ontology%3AhasProvinceEnum%20%3Fprovince%20.%0A%20%20%20%20%3FAccomodation%20ontology%3AhasTimetable%20%3Ftt%20.%0A%20%20%20%20%3Ftt%20ontology%3AhasSchedules%20%3Fsch%20.%0A%20%20%20%20%3Fsch%20ontology%3AScheduleName%20%22checkin%22%20.%0A%20%20%20%20%3Fsch%20ontology%3AStartHour%20%3Fstarthour%20.%0A%20%20%20%20%3Fsch%20ontology%3AEndHour%20%3Fendhour%20.%0A%20%20%20%20%20%20OPTIONAL%7B%3FAccomodation%20ontology%3AStars%20%3Fstars%7D%0A%7D%0A&limit_query=0&infer=true&"


def query_30(subject, comune):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Fstreet%20%3Fprovince%20%3Fnumber%20%3Flat%20%3Flon%20%0AWHERE%20%7B%0A%20%20%20%20%3Frest%20a%20ontology%3A{}%20.%0A%20%20%20%20%3Frest%20ontology%3APoiName%20%3Fname%20.%0A%20%20%20%20%3Frest%20ontology%3AhasAddress%20%3Faddr%20.%0A%20%20%20%20%3Faddr%20ontology%3AhasProvinceEnum%20%3Fprovince%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3AStreet%20%3Fstreet%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3ACity%20%27{}%27%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3ANumber%20%3Fnumber%20.%0A%20%20%20%20%20%20%3Frest%20ontology%3ALatitude%20%3Flat%20.%0A%20%20%20%20%20%20%3Frest%20ontology%3ALongitude%20%3Flon%20.%0A%7D&limit_query=0&infer=true&".format(subject, comune)


def query_31(subject, regione):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Fstreet%20%3Fcity%20%3Fnumber%20%3Flat%20%3Flon%20%0AWHERE%20%7B%0A%20%20%20%20%3Frest%20a%20ontology%3A{}%20.%0A%20%20%20%20%3Frest%20ontology%3APoiName%20%3Fname%20.%0A%20%20%20%20%3Frest%20ontology%3AhasAddress%20%3Faddr%20.%0A%20%20%20%20%3Faddr%20ontology%3AhasProvinceEnum%20ontology%3A{}%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3AStreet%20%3Fstreet%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3ACity%20%3Fcity%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3ANumber%20%3Fnumber%20.%0A%20%20%20%20%20%20%3Frest%20ontology%3ALatitude%20%3Flat%20.%0A%20%20%20%20%20%20%3Frest%20ontology%3ALongitude%20%3Flon%20.%0A%7D&limit_query=0&infer=true&".format(subject, regione)


def query_32(subject):
    return "action=exec&queryLn=SPARQL&query=PREFIX%20ontology%3A%3Chttp%3A%2F%2Fwww.semanticweb.org%2Faleca%2Fontologies%2F2019%2F10%2Funtitled-ontology-10%23%3E%0A%0ASELECT%20%3Fname%20%3Fstreet%20%3Fcity%20%3Fnumber%20%3Flat%20%3Flon%20%3Fprovince%0AWHERE%20%7B%0A%20%20%20%20%3Frest%20a%20ontology%3A{}%20.%0A%20%20%20%20%3Frest%20ontology%3APoiName%20%3Fname%20.%0A%20%20%20%20%3Frest%20ontology%3AhasAddress%20%3Faddr%20.%0A%20%20%20%20%3Faddr%20ontology%3AhasProvinceEnum%20%3Fprovince%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3AStreet%20%3Fstreet%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3ACity%20%3Fcity%20.%0A%20%20%20%20%20%20%3Faddr%20ontology%3ANumber%20%3Fnumber%20.%0A%20%20%20%20%20%20%3Frest%20ontology%3ALatitude%20%3Flat%20.%0A%20%20%20%20%20%20%3Frest%20ontology%3ALongitude%20%3Flon%20.%0A%7D&limit_query=0&infer=true&".format(subject)
