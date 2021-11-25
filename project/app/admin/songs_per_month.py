import datetime
from ..action import Action
from db.models.songs import Song


class MonthlySongs(Action):

    def perform(self, request):
        today = datetime.datetime.today()

        if today.month == 1:
            one_month_ago = today.replace(year=today.year - 1, month=12)
            two_months_ago = today.replace(year=today.year - 1, month=11)

        elif today.month == 2:
            one_month_ago = today.replace(month=today.month - 1, day=today.day)
            two_months_ago = today.replace(year=today.year - 1, month=12)

        else:
            extra_days = 0
            while True:
                try:
                    one_month_ago = today.replace(month=today.month - 1, day=today.day - extra_days)
                    two_months_ago = today.replace(month=today.month - 2, day=today.day - extra_days)
                    break
                except ValueError:
                    extra_days += 1

        months = [two_months_ago, one_month_ago, today]
        songs = {}
        for month in months:
            songs[month.strftime('%B')] = len([song for song in Song.objects.all() if song.created_at.strftime('%Y%m') == month.strftime('%Y%m')])

        return songs
