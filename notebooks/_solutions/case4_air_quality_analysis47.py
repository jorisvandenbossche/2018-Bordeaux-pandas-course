exceedances = data.rolling(8).mean().resample('D').max() > 100