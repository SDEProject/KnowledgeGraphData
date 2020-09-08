import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from requests import Response
from rest_framework import viewsets, mixins
from travelando import settings
from query_templates import queries
import json
from xml.etree import cElementTree as ElementTree
import xmltodict


KNOWLEDGE_GRAPH_POSITION = "http://52.17.47.46:8080/rdf4j-workbench/repositories/1/query?"


def get_query_results(r):
    json_response = xmltodict.parse(r.content)
    results = json_response['sparql']['results']['result']
    all_res = []
    try:
        for item in results:
            res_obj = {}
            if item != 'binding':
                for key, value in item.items():
                    for orderdict in value:
                        p = []
                        for k, v in orderdict.items():
                            p.append(v)
                        res_obj[p[0]] = p[1]
                all_res.append(res_obj)
            else:
                for value in dict(results)['binding']:
                    p = []
                    for k, v in value.items():
                        p.append(v)
                    res_obj[p[0]] = p[1]
                all_res.append(res_obj)
    except:
        print('Unable to parse results')
        return []
    return all_res


# Create your views here.
class QueriesView(View):
    def get(self, request):
        parameters = request.GET
        print(parameters)

        status_code = 200

        query = parameters.get('query', None)
        print(query)
        all_res = []

        try:
            if query == '3':
                checkin = parameters.get('checkin', None)
                comune = parameters.get('comune', None)
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_3(comune, checkin))
                all_res = get_query_results(r)
            elif query == '6':
                checkin = parameters.get('checkin', None)
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_6(checkin))
                all_res = get_query_results(r)
            elif query == '4':
                region = parameters.get('region', None)
                shop_enum = parameters.get('shop_enum', None)
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_4(region, shop_enum))
                all_res = get_query_results(r)
            elif query == '5':
                shop_enum = parameters.get('shop_enum', None)
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_5(shop_enum))
                all_res = get_query_results(r)
            elif query == '7':
                shop_enum = parameters.get('shop_enum', None)
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_7(shop_enum))
                all_res = get_query_results(r)
            elif query == '9':
                difficulty = parameters.get('path_difficulty', None)
                equipment_required = 'true' if parameters.get('info_equipment', None) == 'with equipment' else 'false'
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_9(difficulty, equipment_required))
                all_res = get_query_results(r)
            elif query == '12':
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_12())
                all_res = get_query_results(r)
            elif query == '13':
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_13())
                all_res = get_query_results(r)
            elif query == '14':
                difficulty = parameters.get('path_difficulty', None)
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_14(difficulty))
                all_res = get_query_results(r)
            elif query == '17':
                poi_from = parameters.get('poi_activity_from', None)
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_17(poi_from))
                all_res = get_query_results(r)
            elif query == '18':
                poi_from = parameters.get('poi_activity_from', None)
                poi_to = parameters.get('poi_activity_to', None)
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_18(poi_from, poi_to))
                all_res = get_query_results(r)
            elif query == '19':
                try:
                    path_number = str(int(float(parameters.get('path_number', None))))
                    r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_19(path_number))
                    all_res = get_query_results(r)
                except:
                    print('Failed to parse path number in query 19.')
                    status_code = 500
            elif query == '25':
                comune = parameters.get('comune', None)
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_25(comune))
                all_res = get_query_results(r)
            elif query == '26':
                region = parameters.get('region', None)
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_26(region))
                all_res = get_query_results(r)
            elif query == '27':
                equipment = 'true' if parameters.get('info_equipment', None) == 'with equipment' else 'false'
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_27(equipment))
                all_res = get_query_results(r)
            elif query == '28':
                comune = parameters.get('comune', None)
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_28(comune))
                all_res = get_query_results(r)
            elif query == '29':
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_29())
                all_res = get_query_results(r)
            elif query == '30':
                subject = parameters.get('subject', None)
                comune = parameters.get('comune', None)
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_30(subject, comune))
                all_res = get_query_results(r)
            elif query == '31':
                subject = parameters.get('subject', None)
                region = parameters.get('region', None)
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_31(subject, region))
                all_res = get_query_results(r)
            elif query == '32':
                subject = parameters.get('subject', None)
                r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_32(subject))
                all_res = get_query_results(r)
            else:
                print('Query not found')
                status_code = 404
            print(all_res)
            if len(all_res) > 0:
                response = {"results": all_res}
            else:
                response = {'text': 'Sorry, I cannot execute your request.'}
                status_code = 404
        except:
            print('Error in call Knowledge Graph server.')
            status_code = 500
            response = {'text': 'I\'m having trouble in executing your request.'}

        return JsonResponse(response, status=status_code)

