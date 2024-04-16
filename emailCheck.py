import re

def is_valid_email(email):
  """
  이메일 주소가 유효한지 검사하는 함수입니다.

  Args:
    email: 검사할 이메일 주소 문자열입니다.

  Returns:
    이메일 주소가 유효하면 True, 그렇지 않으면 False를 반환합니다.
  """
  regex = r"""^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[-a-z0-9]*[a-z0-9])?\.)+[a-z]{2,}$"""
  return bool(re.search(regex, email))

def main():
  """
  사용자에게 이메일 주소를 입력받아 유효성을 검사하고 결과를 출력하는 함수입니다.
  """
  email = input("이메일 주소를 입력하세요: ")

  if is_valid_email(email):
    print(f"{email}은 유효한 이메일 주소입니다.")
  else:
    print(f"{email}은 유효하지 않은 이메일 주소입니다.")

if __name__ == "__main__":
  main()