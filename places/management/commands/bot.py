#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Телеграм бот"

    def handle(self, *args, **options):
        pass
