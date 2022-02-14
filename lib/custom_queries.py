#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django_booking.places.models import District, Location, LocationService


def get_districts_list() -> list:
    return [{'name': district.name,
             'id': district.id, }
            for district in District.objects.all()
            ]


def get_locations():
    return Location.objects.get_all()


def get_all_district_locations(district_id):
    return Location.objects.filter(district__id=district_id)
