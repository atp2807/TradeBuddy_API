# app/ai/analysis.py

def analyze_trade(trade):
    """
    예시 AI 분석 함수: 실제 AI 연결 전까지는 임시 결과 반환
    """
    # 예시 규칙: 매도인데 가격이 낮으면 감정적 매도라고 가정
    if trade.trade_type == "SELL" and trade.trade_price < 250:
        return {
            "is_loss_pattern": True,
            "message": "이전 손실 패턴과 유사합니다. 감정적 매도일 수 있습니다."
        }
    return {
        "is_loss_pattern": False,
        "message": "정상적인 거래로 보입니다."
    }
