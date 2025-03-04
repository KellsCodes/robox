import pandas as pd

from .models import Trade


def detect_stoploss_mistakes():
    """Identify trades where stoploss is too tight"""
    trades = Trade.objects.filter(outcome="Loss").values()
    df = pd.DataFrame(trades)

    df["stoploss_distance"] = abs(df["entry_price"] - df["stoploss_price"])
    avg_stoploss_distance = df["stoploss_distance"].mean()

    # Find trades where stoploss distance is much lower than the average
    risky_trades = df[df["stoploss_distance"] < avg_stoploss_distance * 0.5]

    return risky_trades.to_dict(orient="records")


def detect_low_risk_reward_trades():
    """Identify trades with poor risk-reward ratio"""
    trades = Trade.objects.values()
    df = pd.DataFrame(trades)

    # Filter trades where risk-reward ratio is below 1:1
    low_risk_reward_trades = df[df["risk_reward_ratio"] < 1.0]

    return low_risk_reward_trades.to_dict(orient="records")


def detect_bad_entry_timing():
    """Check if trades were placed at volatile market times"""
    trades = Trade.objects.values()
    df = pd.DataFrame(trades)

    # Convert execution_time to datetime
    df["execution_time"] = pd.to_datetime(df["execution_time"])

    # Identify trades executed around news times (assuming we have a news event_list)
    news_times = ["14:30", "08:30"]
    df["time_of_day"] = df["execution_time"].dt.strftime("%H:%M")

    bad_timing_trades = df[df["time_of_day"].isin(news_times)]

    return bad_timing_trades.to_dict(orient="records")


def detect_overstayed_trades():
    """Find trades held for too long before closing"""
    trades = Trade.objects.filter(outcome="Loss").values()
    df = pd.DataFrame(trades)

    avg_duration = df["trade_duration"].mean()

    # Identify trades held significantly longer than average
    oveystayed_trades = df[df["trade_duration"] > avg_duration * 1.5]

    return oveystayed_trades.to_dict(orient="records")
