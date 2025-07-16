# 공역 탐지 역지오코딩

## 소개

드론스팟의 비행/촬영 허가 여부를 판단하기 위해 좌표를 제공하면 해당 좌표에는 어떤 공역이 해당하는지 알려주는 기능이 필요했습니다.  
그래서 vworld의 api를 이용하여 shp 파일로 공역 정보를 저장하고, 저장한 데이터를 바탕으로 좌표를 이용하여 공역 정보를 가져오는 기능을 만들었습니다.

## 구현

### 데이터

- [WMS/WFS API 2.0 레퍼런스](https://www.vworld.kr/dev/v4dv_wmsguide2_s001.do) API를 활용하여 '군작전구역', '초경량비행장치공역', '위험구역' 등 여러 공역의 폴리곤 데이터를 가져와 저장하여 공역 정보 데이터를 구성했습니다.
- [main.py](https://github.com/dravel-drone/dravel-airspace-detector/blob/master/main.py) 참고
