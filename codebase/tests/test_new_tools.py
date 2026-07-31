import sys
from pathlib import Path

# Thêm codebase vào sys.path để test có thể import
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools import TOOL_FUNCTIONS

def test_compare_periods():
    compare_periods = TOOL_FUNCTIONS["compare_periods"]
    
    # 1. compare_periods with valid topic_id
    res1 = compare_periods(
        period_a={"from": "2026-07-20", "to": "2026-07-23"},
        period_b={"from": "2026-07-24", "to": "2026-07-25"},
        metric="count",
        topic_id="DAY_01_CH_01"  # Thay bằng một topic_id hợp lệ có trong data
    )
    print("Test 1 (valid topic_id):", res1)
    
    # 2. compare_periods with no topic_id (aggregate)
    res2 = compare_periods(
        period_a={"from": "2026-07-20", "to": "2026-07-23"},
        period_b={"from": "2026-07-24", "to": "2026-07-25"},
        metric="count"
    )
    print("Test 2 (aggregate):", res2)
    
    # 3. compare_periods where one period has zero data
    res3 = compare_periods(
        period_a={"from": "1999-01-01", "to": "1999-01-02"},
        period_b={"from": "2026-07-24", "to": "2026-07-25"},
        metric="count"
    )
    print("Test 3 (zero data period):", res3)

def test_search_by_keyword():
    search_by_keyword = TOOL_FUNCTIONS["search_by_keyword"]
    
    # 1. keyword with matches (giả sử từ khóa "slide" hoặc "giải thích" rất phổ biến)
    res1 = search_by_keyword(keyword="slide")
    print("Test 4 (keyword matches):", res1)
    
    # 2. keyword with zero matches
    res2 = search_by_keyword(keyword="môtừkhóakhôngbaogiờtồntại")
    print("Test 5 (zero matches):", res2)
    
    # 3. time_range filter applied
    res3 = search_by_keyword(
        keyword="slide",
        time_range={"from": "2026-07-24", "to": "2026-07-25"}
    )
    print("Test 6 (time_range applied):", res3)

if __name__ == "__main__":
    print("Running tests...")
    test_compare_periods()
    test_search_by_keyword()
    print("Done.")
