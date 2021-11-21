import logging
import sys

format = logging.Formatter("%(levelname)-10s %(asctime)s %(message)s %(filename)s %(funcName)s")

crit_hand = logging.StreamHandler(sys.stderr)
crit_hand.setLevel(logging.CRITICAL)
crit_hand.setFormatter(format)

app_warning = logging.FileHandler("log_warning.log")
app_warning.setLevel(logging.WARNING)
app_warning.setFormatter(format)

app_error = logging.FileHandler("log_error.log")
app_error.setLevel(logging.ERROR)
app_error.setFormatter(format)

applog_hand = logging.FileHandler('log.log')
applog_hand.setFormatter(format)

app_log = logging.getLogger('log')
app_log.setLevel(logging.INFO)
app_log.addHandler(applog_hand)
app_log.addHandler(crit_hand)
app_log.addHandler(app_warning)
app_log.addHandler(app_error)