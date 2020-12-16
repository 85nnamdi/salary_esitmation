import scrapper as s
import pandas as pd

path = "C:/Users/ekwea\Desktop/salary_estimation/chromedriver"

df = s.get_jobs('Software engineer', 15, False, path,15)