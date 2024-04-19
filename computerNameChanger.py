import ctypes, sys 
import os 
import socket 
import subprocess 

def is_admin(): 
    try: 
        return ctypes.windll.shell32.IsUserAnAdmin() 
    except: 
        return False 

if is_admin(): 
    curComName=socket.gethostname() 

    print("") 
    print("  ===============================================") 
    print("") 
    print("  컴퓨터 이름을 변경하는 간단한 프로그램 ") 
    print("           - 원주교육지원청 정보담당 2023. 3. 22.") 
    print("") 
    print("  ===============================================") 
    print("") 
    print("  현재 컴퓨터 이름은 [ "+curComName+" ] 입니다.") 
    print("") 
    newComName=input("  변경할 이름을 입력하세요(예시: 행정과-행복한) : ") 

    print("") 
    print("  ===============================================") 
    print("") 
    print("  컴퓨터 이름을 [ "+newComName+" ] 으로 변경 설정하였습니다.") 
    print("") 
    print("  재부팅하면 새로운 이름으로 적용됩니다. ") 
    print("") 
    print("  ===============================================") 
    print("") 
    trash1=input("  설정된 내용을 확인하기 위해, 엔터키를 입력하세요. ") 

    print("") 
    print("  ===============================================") 
    print("") 

    command1="wmic computersystem where caption=\""+curComName+"\" call rename name=\""+newComName+"\" >nul 2>&1" 

    #print(command1) 
    os.system(command1) 

    command2="start /wait control sysdm.cpl" 
    os.system(command2) 

else: 
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1) 


    