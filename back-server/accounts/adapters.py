from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        # super()를 사용하여 부모의 데이터(기본 데이터)를 저장
        user = super().save_user(request, user, form, False)

        # 저장하고자 하는 추가 필드를 아래와 같이 여러 개 정의한 다음 user의 속성 값에 할당
        # user의 속성 값은 우리가 지정한 데이터 필드 이름
        # 추가 저장 필드: sex (예시)
        nickname = data.get("nickname")
        
        if nickname:
            user.nickname = nickname

        user.save() # 저장
        return user