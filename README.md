# 파이썬으로 만들어진 Brainfuck 인터프리터
## 특징
- 파이썬으로 만들어진 만큼 매우 느리다
- pypy를 쓰면 그나마 빠르다
- PyInstaller로 빌드된 Windows용 실행파일을 제공한다. (실행파일이 있는 위치(/dist/bf-py)를 환경 변수에 추가하고 재부팅하면 bf-py 명령어 만으로 간편하게 사용할 수 있다)

## 사용법
bf-py를 실행하려면 한개의 인수를 넣어야 합니다.
```
python bf-py.py <filename>
```
\<filename>은 실행할 Brainfuck 프로그램의 파일 이름 혹은 경로입니다.

예시:
```
python bf-py.py helloworld.bf
```
이는 실행파일도 마찬가지입니다.