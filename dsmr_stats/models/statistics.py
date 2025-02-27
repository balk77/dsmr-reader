from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel

from dsmr_backend.mixins import ModelUpdateMixin


class DayStatistics(ModelUpdateMixin, models.Model):
    """ Daily consumption usage summary. """
    day = models.DateField(unique=True, db_index=True, verbose_name=_('Date'))

    """ Diffs calculated (field names may be renamed in the future to clarify) """
    electricity1 = models.DecimalField(
        max_digits=9, decimal_places=3, verbose_name=_('Electricity tariff 1 diff'),
        help_text=_('The difference between the first and last reading of the day')
    )
    electricity2 = models.DecimalField(
        max_digits=9, decimal_places=3, verbose_name=_('Electricity tariff 2 diff'),
        help_text=_('The difference between the first and last reading of the day')
    )
    electricity1_returned = models.DecimalField(
        max_digits=9, decimal_places=3, verbose_name=_('Electricity tariff 1 returned diff'),
        help_text=_('The difference between the first and last reading of the day')
    )
    electricity2_returned = models.DecimalField(
        max_digits=9, decimal_places=3, verbose_name=_('Electricity tariff 2 returned diff'),
        help_text=_('The difference between the first and last reading of the day')
    )
    electricity1_cost = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name=_('Electricity tariff 1 cost')
    )
    electricity2_cost = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name=_('Electricity tariff 2 cost')
    )
    # Gas readings are optional/not guaranteed.
    gas = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, default=None, verbose_name=_('Gas diff'),
        help_text=_('The difference between the first and last reading of the day')
    )
    gas_cost = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, default=None, verbose_name=_('Gas cost')
    )
    # Temperature readings depend on user settings.
    lowest_temperature = models.DecimalField(
        max_digits=4, decimal_places=1, null=True, default=None, verbose_name=_('Lowest temperature')
    )
    highest_temperature = models.DecimalField(
        max_digits=4, decimal_places=1, null=True, default=None, verbose_name=_('Highest temperature')
    )
    average_temperature = models.DecimalField(
        max_digits=4, decimal_places=1, null=True, default=None, verbose_name=_('Average temperature')
    )
    fixed_cost = models.DecimalField(
        max_digits=8, decimal_places=2, default=0, verbose_name=_('Fixed cost')
    )
    total_cost = models.DecimalField(
        db_index=True, max_digits=8, decimal_places=2, verbose_name=_('Total cost')
    )

    """ Historic meter positions """
    electricity1_reading = models.DecimalField(
        max_digits=9, decimal_places=3, blank=True, null=True, default=None,
        verbose_name=_('Electricity tariff 1 reading'),
        help_text=_('The first absolute value read at the start of the day')
    )
    electricity2_reading = models.DecimalField(
        max_digits=9, decimal_places=3, blank=True, null=True, default=None,
        verbose_name=_('Electricity tariff 2 reading'),
        help_text=_('The first absolute value read at the start of the day')
    )
    electricity1_returned_reading = models.DecimalField(
        max_digits=9, decimal_places=3, blank=True, null=True, default=None,
        verbose_name=_('Electricity tariff 1 reading'),
        help_text=_('The first absolute value read at the start of the day')
    )
    electricity2_returned_reading = models.DecimalField(
        max_digits=9, decimal_places=3, blank=True, null=True, default=None,
        verbose_name=_('Electricity tariff 2 reading'),
        help_text=_('The first absolute value read at the start of the day')
    )
    gas_reading = models.DecimalField(
        max_digits=9, decimal_places=3, blank=True, null=True, default=None,
        verbose_name=_('Gas reading'),
        help_text=_('The first absolute value read at the start of the day')
    )

    @property
    def electricity_merged(self):
        return self.electricity1 + self.electricity2

    @property
    def electricity_returned_merged(self):
        return self.electricity1_returned + self.electricity2_returned

    class Meta:
        default_permissions = tuple()
        verbose_name = _('Day statistics (automatically generated data)')
        verbose_name_plural = verbose_name
        ordering = ['day']

    def __str__(self):
        return '{}: {}'.format(
            self.__class__.__name__, self.day
        )


class HourStatistics(ModelUpdateMixin, models.Model):
    """ Hourly consumption usage summary. """
    hour_start = models.DateTimeField(unique=True, db_index=True, verbose_name=_('Hour start'))

    electricity1 = models.DecimalField(
        max_digits=9, decimal_places=3, verbose_name=_('Electricity 1 (low tariff)')
    )
    electricity2 = models.DecimalField(
        max_digits=9, decimal_places=3, verbose_name=_('Electricity 2 (high tariff)')
    )
    electricity1_returned = models.DecimalField(
        max_digits=9, decimal_places=3, verbose_name=_('Electricity 1 returned (low tariff)')
    )
    electricity2_returned = models.DecimalField(
        max_digits=9, decimal_places=3, verbose_name=_('Electricity 2 returned (high tariff)')
    )

    # Gas readings are optional/not guaranteed. But need to be zero due to averages.
    gas = models.DecimalField(max_digits=9, decimal_places=3, default=0, verbose_name=_('Gas'))

    @property
    def electricity_merged(self):
        return self.electricity1 + self.electricity2

    @property
    def electricity_returned_merged(self):
        return self.electricity1_returned + self.electricity2_returned

    class Meta:
        default_permissions = tuple()
        verbose_name = _('Hour statistics (automatically generated data)')
        verbose_name_plural = verbose_name
        ordering = ['hour_start']

    def __str__(self):
        return '{}: {}'.format(
            self.__class__.__name__, timezone.localtime(self.hour_start)
        )


class ElectricityStatistics(SingletonModel):
    """ Keeps track of the highest electricity statistics per phase. """
    highest_usage_l1_timestamp = models.DateTimeField(
        null=True, blank=True, default=None, verbose_name=_('Timestamp of highest usage on L1+')
    )
    highest_usage_l2_timestamp = models.DateTimeField(
        null=True, blank=True, default=None, verbose_name=_('Timestamp of highest usage on L2+')
    )
    highest_usage_l3_timestamp = models.DateTimeField(
        null=True, blank=True, default=None, verbose_name=_('Timestamp of highest usage on L3+')
    )
    highest_return_l1_timestamp = models.DateTimeField(
        null=True, blank=True, default=None, verbose_name=_('Timestamp of highest return on L1-')
    )
    highest_return_l2_timestamp = models.DateTimeField(
        null=True, blank=True, default=None, verbose_name=_('Timestamp of highest return on L2-')
    )
    highest_return_l3_timestamp = models.DateTimeField(
        null=True, blank=True, default=None, verbose_name=_('Timestamp of highest return on L3-')
    )
    lowest_usage_l1_timestamp = models.DateTimeField(
        null=True, blank=True, default=None, verbose_name=_('Timestamp of lowest usage on L1+')
    )
    lowest_usage_l2_timestamp = models.DateTimeField(
        null=True, blank=True, default=None, verbose_name=_('Timestamp of lowest usage on L2+')
    )
    lowest_usage_l3_timestamp = models.DateTimeField(
        null=True, blank=True, default=None, verbose_name=_('Timestamp of lowest usage on L3+')
    )

    highest_usage_l1_value = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, blank=True, default=None,
        verbose_name=_('Highest usage on L1+ (in kWh)')
    )
    highest_usage_l2_value = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, blank=True, default=None,
        verbose_name=_('Highest usage on L2+ (in kWh)')
    )
    highest_usage_l3_value = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, blank=True, default=None,
        verbose_name=_('Highest usage on L3+ (in kWh)')
    )
    highest_return_l1_value = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, blank=True, default=None,
        verbose_name=_('Highest return on L1- (in kWh)')
    )
    highest_return_l2_value = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, blank=True, default=None,
        verbose_name=_('Highest return on L2- (in kWh)')
    )
    highest_return_l3_value = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, blank=True, default=None,
        verbose_name=_('Highest return on L3- (in kWh)')
    )
    lowest_usage_l1_value = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, blank=True, default=None,
        verbose_name=_('Lowest usage on L1+ (in kWh)')
    )
    lowest_usage_l2_value = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, blank=True, default=None,
        verbose_name=_('Lowest usage on L2+ (in kWh)')
    )
    lowest_usage_l3_value = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, blank=True, default=None,
        verbose_name=_('Lowest usage on L3+ (in kWh)')
    )

    def export(self):
        """ Converts the data in to ready to use format. """
        data = self.__dict__

        for key in data.keys():
            if key.endswith('_value'):
                try:
                    data[key] = int(data[key] * 1000) or 0
                except TypeError:
                    data[key] = 0

        return data

    class Meta:
        default_permissions = tuple()
        verbose_name = _('Electricity statistics')
