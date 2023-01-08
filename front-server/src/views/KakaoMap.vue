<template>
  <div class="article-box">
    <div class="header-box">
      <h2 class="header-box_text">영화관 찾기</h2>
    </div>
    <hr class="hr">
    <!-- <div class="s-btn">
      <button class="s-btn_c" @click="search">여기를 눌러서 영화관 가져와라</button>
    </div> -->
    <div class="map">
      <div class="map_box">
        <div id="map"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'KakaoMap',
  data() {
    return {
      map: null,
      markerPositions: [],
      markers: [],
      positionObj: {},
    }
  },
  methods: {
    initMap() {
      const position = this.$store.state.positionObj
      console.log(position)
      const container = document.querySelector("#map")
      const options = {
        center: new kakao.maps.LatLng(position.latitude, position.longitude),
        level: 7,
      }
      this.map = new kakao.maps.Map(container, options)
      // 더미 마커
      // this.markerPositions = [
      //   {title: "카카오", latlng: new kakao.maps.LatLng(33.450705, 126.570677)},
      //   {title: "집", latlng: new kakao.maps.LatLng(36.3675852, 127.3381844)},
      // ]

      // 영화관 서치 함수 실행 위치
      this.searchPlaces('영화관')

      // dragend 이벤트가 일어났을 때, 새로 검색하기
      kakao.maps.event.addListener(this.map, 'dragend', () => {
        this.searchPlaces('영화관')
      })
    },
    displayMarkers(positions) {
      // 1. 현재 표시되어있는 marker들이 있다면 marker에 등록된 map을 없애준다.
      // console.log(this.markers)
      if (this.markers.length > 0) {
        this.markers.forEach((item) => {
          item.setMap(null) // CustomOverlay-setMap: setMap(map) 맵에 올린다, setMap(null) 맵에서 제거, setMap(roadview) 로드뷰에 올린다
        })
      }

      // 2. 마커 이미지 커스터마이징 하기
      // javascript 영역에서 assets의 정보 가져오기
      const imgSrc = require("@/assets/free-location-icon.png")
      const imgSize = new kakao.maps.Size(35, 35)
      const markerImage = new kakao.maps.MarkerImage(imgSrc, imgSize)

      // 3. 마커 표시하기
      positions.forEach((position) => {
        // information window 생성
        const infowindow = new kakao.maps.InfoWindow({
          removable: true,
          content: `<div style="padding:5px;">${position.title}</div>`,
        })

        const marker = new kakao.maps.Marker({
          map: this.map,                 // 마커가 올라갈 맵(이걸 적어뒀기 때문에 setMap을 안해도 됨)
          position: position.latlng,     // 마커의 위치
          title: position.title,         // 마우스 오버 시 표시할 제목 
          image: markerImage,            // 마커의 이미지 
        })

        // 이벤트 등록
        // kakao.maps.event.addListener(marker, "click", () => {infowindow.open(this.map, marker)})
        kakao.maps.event.addListener(marker, "mouseover", () => {infowindow.open(this.map, marker)})
        kakao.maps.event.addListener(marker, "mouseout", () => {infowindow.close(this.map, marker)})

        this.markers.push(marker)
      })

      // 4. 지도를 이동시켜주기
      // 배열.reduce( (누적값, 현재값, 인덱스, 요소)=>{ return 결과값}, 초기값)
      // 검색된 장소 위치를 기준으로 지도범위를 재설정하기위해 LatLngBounds 객체에 좌표를 추가
      // const bounds = positions.reduce(
      //   (bounds, position) => bounds.extend(position.latlng),
      //   new kakao.maps.LatLngBounds()
      // )

      // this.map.setBounds(bounds)
    },
    searchPlaces(keyword) {
      // 검색할 키워드
      // const keyword = '영화관'

      // 중심 좌표 확인
      // console.log(this.map.getCenter())

      // 장소 검색 객체 생성
      const ps = new kakao.maps.services.Places(this.map)

      // option 설정
      const searchOptions = {
        useMapCenter: true
      }
      // 키워드 검색 후 호출할 콜백 함수
      const placesSearchCB = (data, status) => {
        if (status === kakao.maps.services.Status.OK) {
          // console.log(data)
          // console.log(pagination)

          const places = []

          // 검색 결과를 돌면서 장소를 객체를 생성해서 담는다.
          data.forEach((site) => {
            const place = {title: site.place_name, latlng: new kakao.maps.LatLng(site.y, site.x)}
            // console.log('place',place)
            places.push(place)
          })

          // 검색 결과로 마커 변경
          this.markerPositions = places

          // 마커를 찍어라
          this.displayMarkers(this.markerPositions)
        }
      }

      // 키워드로 장소 검색
      ps.keywordSearch(keyword, placesSearchCB, searchOptions)
    },
    search() {
      this.searchPlaces('영화관')
    },
    // 위치 찾는 api 함수
    getCurrentPosition () {
      if (!navigator.geolocation) {
        this.setAlert('위치 정보를 찾을 수 없습니다.1')
      } else {
        navigator.geolocation.getCurrentPosition(this.getPositionValue, this.geolocationError)
      }
    },
    // getPositionValue (val) {
    //   console.log(val)
    //   this.positionObj.latitude = val.coords.latitude
    //   this.positionObj.longitude = val.coords.longitude
    //   this.isPositionReady = true
    //   this.$store.commit('GETCURRENTSITE', this.positionObj)
    //   this.setAlert('주소 확인 완료')
    //   this.initMap()
    // },
    // geolocationError () {
    //   this.setAlert('위치 정보를 찾을 수 없습니다.2')
    // },
    // setAlert (text) {
    //   alert(text)
    // }
  },
  created() {
    // this.getCurrentPosition()
    // 사용자 위치정보 요청
    navigator.geolocation.getCurrentPosition((position) => {
      this.positionObj.latitude = position.coords.latitude
      this.positionObj.longitude = position.coords.longitude
      this.$store.commit('GETCURRENTSITE', this.positionObj)
    })
  },
  mounted() {
    if (!window.kakao || !window.kakao.maps) {
      // script 태그 객체 생성
      const script = document.createElement("script")
      // src 속성을 추가하여 .env.local에 등록한 api 키 활용
      // script.src = "//dapi.kakao.com/v2/maps/sdk.js?appkey="+process.env.VUE_APP_KAKAOMAP_API_KEY
      // 동적 로딩을 위해서 autoload=false 추가
      // script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${process.env.VUE_APP_KAKAOMAP_API_KEY}`
      // 카카오맵 services 라이브러리 추가
      script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${process.env.VUE_APP_KAKAOMAP_API_KEY}&libraries=services`

      // 로딩 시점 파악을 위한 load
      // kakao 객체는 global에 전역으로 등록됨, 아래 주석은 eslint에게 kakao가 global 변수임을 알려준다.
      // eslint => 코딩 스타일 규칙으로 정해진 것, 여기에서 벗어나면 오류로 잡히게 됨.
      /* global kakao */
      script.addEventListener("load", () => {
        // console.log("loaded", kakao); - 전역객체지만 window를 통해서 접근해야한다.(not defined), 그래서 화살표 함수를 써야함.
        // console.log('loaded : ', window.kakao)
        kakao.maps.load(this.initMap)
      })

      // document의 head에 script 추가
      document.head.appendChild(script)

    } else {
      // console.log('이미 로딩 됨: ', window.kakao)
      this.initMap()
    }
  },
}
</script>

<style>

</style>