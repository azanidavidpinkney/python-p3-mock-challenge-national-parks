class NationalPark:
    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name") and len(name) >= 3:
            self._name = name
        else:
            Exception

    def trips(self, trip=None):
        if trip and isinstance(trip, Trip):
            self._trips.append(trip)
        return self._trips

    def visitors(self):
        return list(set([trip.visitor for trip in self._trips]))

    def total_visits(self):
        return len(self._trips)

    def best_visitor(self):
        _best_visitor = None
        highest_trip_count = 0
        for _visitor in self.visitors():
            trip_count = len(
                [trip for trip in self.trips() if trip.visitor == _visitor]
            )
            if trip_count > highest_trip_count:
                highest_trip_count = trip_count
                _best_visitor = _visitor
        return _best_visitor


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
        national_park.trips(
            self
        )  # connects Trip instances to the national_park variable as .trips. We will pass in an instances of the NationalPark class to the national_park variable here.
        visitor.trips(
            self
        )  # connects Trip instances to the visitor variable as .trips. We will pass in instances of the Visitor class to the visitor variable here.

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
        else:
            Exception

    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
        else:
            Exception


class Visitor:
    def __init__(self, name):
        self._name = name
        self._trips = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            Exception

    def trips(self, trip=None):
        if isinstance(trip, Trip):
            self._trips.append(trip)
        return self._trips

    def national_parks(self):
        return list(set([trip.national_park for trip in self._trips]))

    def total_visits_at_park(self, park):
        park_visits = len(
            [trip for trip in self._trips if park == self_.trips.national_park]
        )

        if park_visits >= 1:
            return park_visits
        else:
            return "0"
