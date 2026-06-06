import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from src.load_data import load_data
from src.eda import run_eda
from src.visualise import run_visualise
from src.insights import run_insights

df = load_data()
run_eda(df)
run_visualise(df)
run_insights(df)