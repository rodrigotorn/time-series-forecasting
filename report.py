# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown] tags=[]
# # Time Series Forecasting
#
# This report is a case study for a time series analysis and forecasting.
#
# The data was provided by a power utility. It contains a time series about the power in one feeder. A preprocessing stage was needed because there was outlier data points, such as zero values and writing errors on the raw file provided.
#
# Both raw and preprocessed files are available in `/data`. The proprocessing script in available in `/src`.

# %%
