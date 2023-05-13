import re
from collections import Counter, defaultdict
from pprint import pp

jobs_file = r"C:\Users\Amma\Documents\jobs.txt"

months = Counter()
weeks = Counter()
dates = {}
vendor = Counter()
times = Counter()
month_vendor = defaultdict(Counter)

with open(jobs_file, "rb") as fh:
    content = fh.read().split(b"--END--")[0].decode("utf-8")

for each_line in content.splitlines():
    data = re.search(
        r"(?P<date>\d+ \w+ \d+)\s+(?P<week>[a-zA-Z()]+)\s+(?P<startTime>\d{2}:\d{2} \w{2} \w{3})\s+"
        "(?P<endTime>\d{2}:\d{2} \w{2} \w{3})\s+-(?P<vendor>.*)",
        each_line,
    ).groupdict()

    dates.setdefault(data["date"], 0)
    dates[data["date"]] += 1
    # dates.update([data["date"]])
    weeks.update([data["week"]])

    curr_month = data["date"].split(maxsplit=1)[1]
    months.update([curr_month])

    each_vendor = data["vendor"].split("-")[0].strip()
    vendor.update([each_vendor])
    month_vendor[curr_month].update([each_vendor])
    # times.update([each_line.split(")")[1].split("-")[0].strip()])
else:
    # pp(months)
    print("Monthly Average:", round(sum(list(months.values())) / len(months), 2))
    print("~" * 30)
    # pp(weeks)
    # pp(dates)
    pp(vendor)
    # pp(times)
    print("~" * 30)
    pp(month_vendor[curr_month])
    print("~" * 30)
    pp(months)

# from matplotlib import pyplot as plt
# # plt.plot([0, 1, 2, 3, 4, 5], [0, 1, 4, 9, 16, 25])
# print("dates.keys()", dates.keys())
# print("dates.values()", dates.values())
# plt.plot(dates.keys(), dates.values())
# plt.show()
