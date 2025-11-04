import pandas as pd

# cap 파일 불러오기 (예: 탭으로 구분되어 있다면)
df = pd.read_csv("20250715Align_grid.cap", sep="\t", header=None)

# 예시: 컬럼명 지정
df.columns = ["Time", "X", "Y", "Intensity1", "Intensity2"]

# CSV로 저장
df.to_csv("converted_file.csv", index=False)
#안녕하세요
print("하이")