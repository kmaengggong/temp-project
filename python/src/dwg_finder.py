import os
import glob

def check_dwg_files(root_folder):
    for root, dirs, files in os.walk(root_folder):
        dwg_files = glob.glob(os.path.join(root, '*.dwg'))
        
        if not dwg_files:
            print(f"폴더 '{root}' - 사유: .dwg 파일이 없음")
        else:
            valid_dwg_files = [file for file in dwg_files if os.path.getsize(file) >= 1024]
            if not valid_dwg_files:
                print(f"폴더 '{root}' - 사유: 1KB 미만의 .dwg 파일만 존재함")

def choose_directory():
    current_folder = os.path.dirname(__file__)  # 현재 파이썬 파일의 경로로 설정
    
    while True:
        print(f"\n현재 경로: {current_folder}")
        choice = input("현재 경로로 하시겠습니까? (Y/N): ").strip().upper()
        
        if choice == 'Y':
            return current_folder
        elif choice == 'N':
            subfolders = [f for f in os.listdir(current_folder) if os.path.isdir(os.path.join(current_folder, f))]
            
            if not subfolders:
                print("하위 폴더가 없습니다. 다른 경로를 선택해주세요.")
                continue
            
            print("\n하위 폴더 목록:")
            for i, folder in enumerate(subfolders, start=1):
                print(f"{i}. {folder}")
            
            choice = input("사용할 폴더 이름이나 번호를 입력하세요: ").strip()
            
            if choice.isdigit() and 1 <= int(choice) <= len(subfolders):
                selected_folder = subfolders[int(choice) - 1]
            else:
                selected_folder = choice
            
            new_path = os.path.join(current_folder, selected_folder)
            if os.path.isdir(new_path):
                current_folder = new_path
            else:
                print("유효한 폴더가 아닙니다. 다시 선택해주세요.")
        else:
            print("Y 또는 N을 입력해주세요.")

# 프로그램 실행
if __name__ == "__main__":
    target_folder = choose_directory()
    print(f"\n선택된 폴더: {target_folder}")
    check_dwg_files(target_folder)
    
    # 프로그램 종료되지 않도록 대기
    input("\nPress Enter to exit...")
