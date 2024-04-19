import ctypes
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def change_computer_name(new_computer_name):
    try:
        # Run sysdm.cpl command to open System Properties window
        subprocess.run(["control", "sysdm.cpl"])

        # Prompt user to change computer name manually through System Properties window
        print("시스템 속성 창이 열렸습니다. 거기에서 컴퓨터 이름을 변경하고 저장해주세요.")

        # Wait for the user to manually change and save the computer name
        input("컴퓨터 이름이 변경되었다면 엔터 키를 눌러주세요.")

        print("컴퓨터 이름 변경이 완료되었습니다.")
        return True
    except Exception as e:
        print("컴퓨터 이름 변경 중 오류가 발생했습니다:", e)
        return False

if __name__ == "__main__":
    if is_admin():
        new_computer_name = input("변경할 컴퓨터 이름을 입력하세요: ")
        change_computer_name(new_computer_name)
    else:
        # Re-run the script with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "python", __file__, None, 1)
