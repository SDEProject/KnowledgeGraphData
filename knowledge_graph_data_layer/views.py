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
    # print(json_response)
    results = json_response['sparql']['results']['result']
    # print(results)
    all_res = []
    for item in results:
        print(item)
        res_obj = {}
        for key, value in item.items():
            # print(key, value)
            for orderdict in value:
                p = []
                for k, v in orderdict.items():
                    # print(k, v)
                    p.append(v)
                res_obj[p[0]] = p[1]
        # print(res_obj)
        all_res.append(res_obj)
    # print(all_res)
    return all_res


# Create your views here.
class QueriesView(View):
    def get(self, request):
        # response = {'name': 'ciao'}
        parameters = request.GET
        print(parameters)

        query = parameters.get('query', None)
        print(query)
        all_res = []

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
            print(difficulty)
            equipment_required = 'true' if parameters.get('info_equipment', None) == 'with equipment' else 'false'
            r = requests.get(KNOWLEDGE_GRAPH_POSITION + queries.query_9(difficulty, equipment_required))
            all_res = get_query_results(r)

        print(all_res)
        response = {"results": all_res}

        # retrieve get parameter request.GET.get('intentName', None)
        # response['fulfillmentMessages'][0]['text']['text'].append('I\'ll execute query ' + query)
        return JsonResponse(response)

