from places.models import *


def _get_districts() -> list:
    """ Возвращает список со всеми объектами районов District"""
    return District.objects.all()


def _get_locations():
    """ Возвращает список со всеми объектами локаций Location"""
    return Location.objects.all()


def _get_all_district_locations(name):
    """ Возвращает список со всеми объектами локаций Location в определенном районе"""
    return Location.objects.filter(district__name=name)


def _get_all_resting_places_in_location(location_name):
    """ Возвращает список объектов(QueryList) мест отдыха(LocationRestingPlace) в определенной локации(Location)"""
    return LocationRestingPlace.objects.filter(location__name=location_name)


# Функции форматеры для бота.

def reply_districts_list():
    """ Возвращает словарь с отформатированым списком районом для бота"""
    districts = _get_districts()
    return [district.name for district in districts]


def reply_locations_list():
    locations = _get_locations()
    return [
        {'name': location.name,
         'id': location.id,
         } for location in locations
    ]


def reply_locations_in_district(district_name):
    locations = _get_all_district_locations(district_name)
    return [
        {'name': location.name,
         'id': location.id,
         } for location in locations
    ]
