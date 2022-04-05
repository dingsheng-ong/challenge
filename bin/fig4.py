#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("survey.csv")
nice_data = data[
    data["Interviewer's comments"].str.contains('nice')
    | data["Interviewer's comments"].str.contains('Nice')
]

province_counts = data.groupby('Province').count()['crop id']
nice_province_counts = nice_data.groupby('Province').count()['crop id']
(nice_province_counts / province_counts * 100).plot(kind='bar')

plt.ylabel('% of respondents described as "nice"')
plt.tight_layout()
plt.show()
