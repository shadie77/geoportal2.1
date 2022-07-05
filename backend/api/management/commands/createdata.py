from datetime import datetime
from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
import random
from api.models import Accident, Ridership, Boat, Drivers,Jetty_Supervisors, Jetty

accident_causes = [
    "Head on Collision",
    "Collide with submerged object",
    "Head on collision between two boats",
    "Wave and deckhand fell overboard",
    "Passenger boat collide with iron boat",
    "Passenger boat collide with police security boat",
    "Night travel, no jacket, overoading and water turbulance",
    "Caused by tug wave"
]

boats = [
    "Wooden",
    "Fiber",
    "Aluminiun",
    "Steel",
    "Others"
]

arrivalordeparture = [
    "Arrival",
    "Departure"
]

class Provider(faker.providers.BaseProvider):
    def causation(self):
        return self.random_element(accident_causes)

    def boatchoice(self):
        return self.random_element(boats)

    def arrive(self):
        return self.random_element(arrivalordeparture)

class Command(BaseCommand):
    help = "This command help to populate the models with fake data"

    def handle(self, *args,**kwargs):
        fake = Faker()
        fake.add_provider(Provider)
        print(fake.date_time())
        #print(fake.date_between_dates(date_start= datetime(2018,1,1), date_end = datetime(2022,5,8)))
        #print(fake.name())
        #print(fake.time())
        #print(fake.street_name())
        #print(fake.pyint(min_value=1, max_value=10))
        #print(fake.causation())
        """
        for _ in range(150):
            boat_name = fake.name()
            accident_dates = fake.date_between_dates(date_start= datetime(2018,1,1), date_end = datetime(2022,5,8))
            accident_times = fake.time()
            accident_location = fake.street_name()
            casualties = fake.pyint(min_value=10, max_value=20)
            injuries = fake.pyint(min_value=1, max_value=4)
            rescues = fake.pyint(min_value=4, max_value=6)
            death = casualties - (injuries + rescues)
            causes = fake.causation()
            Accident.objects.create(
                Boat_type_or_name = boat_name,
                accident_date = accident_dates,
                accident_time = accident_times,
                location = accident_location,
                number_of_casuality = casualties,
                number_of_injuries = injuries,
                number_of_death = death,
                number_of_rescues = rescues,
                cause = causes
            )
        check_accident = Accident.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of accident: {check_accident}"))

        for _ in range(40):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email_field = f"{first_name}_{last_name}@{fake.domain_name()}"
            jetty = Jetty.objects.get(pk=random.randint(1,29))
            Jetty_Supervisors.objects.create(
                jetty_id = jetty,
                firstname = first_name,
                surname = last_name,
                email = email_field
            )
        check_supervisor = Jetty_Supervisors.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of supervisors: {check_supervisor}"))

        for _ in range(50):
            firstname = fake.first_name()
            lastname = fake.last_name()
            emails = f"{firstname}_{lastname}@{fake.domain_name()}"
            dob = fake.date_of_birth()

            Drivers.objects.create(
                first_name = firstname,
                last_name = lastname,
                email = emails,
                date_of_birth = dob
            )
        check_driver = Drivers.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of drivers: {check_driver}"))

        for _ in range(60):
            boatname = fake.name()
            boattype = fake.boatchoice()
            driver = Drivers.objects.get(pk=random.randint(1,50))
            boatcapacity = fake.pyint(min_value= 20, max_value = 21)
            Boat.objects.create(
                boat_name = boatname,
                boat_type = boattype,
                boat_driver = driver,
                boat_capacity = boatcapacity
            )
        check_boat = Boat.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of Boat: {check_boat}"))

        """

        for _ in range(3000):
            jettyid = Jetty.objects.get(pk=random.randint(1,29))
            arrivalDepart = fake.arrive()
            time = fake.date_time()
            location = Jetty.objects.get(pk=random.randint(1,29))
            if location == jettyid:
                location= Jetty.objects.get(pk=random.randint(1, 29))
            passengers = fake.pyint(min_value= 15, max_value = 20)
            fare = fake.pyint(min_value= 3000, max_value = 5500)
            boatid = Boat.objects.get(pk=random.randint(1,60))
            water_guard = fake.name()
            Ridership.objects.create(
                jetty_id = jettyid,
                arrival_departure = arrivalDepart,
                arrival_departure_time = time,
                arrival_departure_location = location,
                number_of_passengers = passengers,
                transport_fare = fare,
                boat_id = boatid,
                waterguard = water_guard
            )
        check_ridership = Ridership.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of ridership: {check_ridership}"))