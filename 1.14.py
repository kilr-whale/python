import matplotlib.pyplot as plt

# 주어진 강우강도 데이터
data = [
    39.91, 40.78, 41.31, 42.96, 43.11, 43.3, 43.93, 44.67, 45.05, 45.98,
    46.77, 47.38, 48.21, 48.26, 49.57, 50.37, 50.51, 51.28, 53.02, 53.29,
    54.49, 54.91, 55.77, 58.71, 58.83, 59.12, 63.52, 67.59, 67.72
]

# 히스토그램 그리기
plt.hist(data, bins=10, edgecolor='black', alpha=0.7)

# 도수분포다각형을 만들기 위해 중심값과 도수 계산
hist, bins = np.histogram(data, bins=10)
center = (bins[:-1] + bins[1:]) / 2

# 도수분포다각형 그리기
plt.plot(center, hist, 'r-', linewidth=2)

# 그래프 제목과 레이블 설정
plt.title('Frequency Polygon of Rainfall Intensity')
plt.xlabel('Rainfall Intensity (in)')
plt.ylabel('Frequency')

# 그래프 보여주기
plt.show()
