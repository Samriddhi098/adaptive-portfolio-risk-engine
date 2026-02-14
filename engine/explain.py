def generate_explanation(date, regime, vol_scale, dd_scale):
    explanation = f"""
    Date: {date}
    Regime Detected: {regime}
    Volatility Scaling Applied: {round(vol_scale, 2)}
    Drawdown Scaling Applied: {round(dd_scale, 2)}
    """

    return explanation
