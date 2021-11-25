import datetime
from db.models.user import User
from ..action import Action


class MonthlyUsers(Action):
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
        users = {}
        for month in months:
            users[month.strftime('%B')] = len([user for user in User.objects.all() if user.created_at.strftime('%Y%m') == month.strftime('%Y%m')])

        return users
