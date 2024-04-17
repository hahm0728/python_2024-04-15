import psutil

def get_memory_info():
  """
  컴퓨터의 메모리 정보를 가져와 사전에 담아 반환하는 함수입니다.

  Returns:
    사전 형태로 된 메모리 정보를 반환합니다. 키는 다음과 같습니다.
      * total: 총 메모리 용량 (바이트)
      * available: 사용 가능한 메모리 용량 (바이트)
      * used: 사용 중인 메모리 용량 (바이트)
      * percent_used: 사용 중인 메모리 비율 (%)
  """
  memory_info = psutil.virtual_memory()
  return {
      "total": memory_info.total,
      "available": memory_info.available,
      "used": memory_info.used,
      "percent_used": memory_info.percent_used,
  }

def print_memory_info():
  """
  메모리 정보를 가져와 출력하는 함수입니다.
  """
  memory_info = get_memory_info()

  print("메모리 정보:")
  print(f"총 메모리: {memory_info['total']:,} 바이트")
  print(f"사용 가능한 메모리: {memory_info['available']:,} 바이트")
  print(f"사용 중인 메모리: {memory_info['used']:,} 바이트")
  print(f"사용 중인 메모리 비율: {memory_info['percent_used']:.1f}%")

if __name__ == "__main__":
  print_memory_info()