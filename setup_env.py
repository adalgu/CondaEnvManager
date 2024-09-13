#!/usr/bin/env python3
"""
setup_env.py

이 스크립트는 현재 디렉토리 이름을 기반으로 Conda 가상환경을 자동으로 생성하고 활성화합니다.
또한, 현재 디렉토리에 `requirements.txt` 파일이 있으면 해당 패키지를 설치합니다.

사용법:
    ./setup_env.py

주의사항:
    - Conda가 설치되어 있고 `conda` 명령어가 시스템 PATH에 있어야 합니다.
    - 이 스크립트는 Windows와 Unix 계열 시스템 모두에서 작동하도록 설계되었습니다.
"""

import os
import subprocess
import sys


def get_conda_envs():
    """
    시스템에 설치된 모든 Conda 가상환경의 목록을 가져옵니다.

    Returns:
        envs (list): 환경 이름의 리스트.
    """
    # Conda 환경 목록을 가져오는 명령 실행
    result = subprocess.run(["conda", "env", "list"], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.strip().split("\n")
    envs = []
    # 환경 이름 추출
    for line in lines[2:]:
        parts = line.split()
        if len(parts) >= 1:
            envs.append(parts[0])
    return envs


def create_env(env_name):
    """
    주어진 이름과 Python 3.8로 새로운 Conda 가상환경을 생성합니다.

    Args:
        env_name (str): 생성할 환경의 이름.
    """
    print(f"Conda 가상환경 생성: {env_name}")
    # Conda 환경 생성 명령 실행
    subprocess.run(["conda", "create", "--name", env_name, "python=3.8", "-y"])
    install_requirements(env_name)


def activate_env(env_name):
    """
    Conda 가상환경을 활성화합니다.

    Note:
        Python 스크립트 내에서 환경을 활성화해도 스크립트 종료 후에는 비활성화됩니다.
        따라서 직접 환경을 활성화해야 합니다.

    Args:
        env_name (str): 활성화할 환경의 이름.
    """
    print(
        f"Conda 가상환경을 활성화하려면 다음 명령을 실행하세요:\nconda activate {env_name}"
    )


def install_requirements(env_name):
    """
    `requirements.txt` 파일에서 패키지를 설치합니다.

    Args:
        env_name (str): 패키지를 설치할 환경의 이름.
    """
    if os.path.isfile("requirements.txt"):
        print("requirements.txt에서 패키지 설치")
        # 지정된 환경에서 pip로 패키지 설치
        subprocess.run(
            ["conda", "run", "-n", env_name, "pip", "install", "-r", "requirements.txt"]
        )
    else:
        print("현재 디렉토리에 requirements.txt가 없습니다.")


def main():
    """
    환경 설정을 관리하는 메인 함수.
    """
    # 현재 디렉토리 이름을 환경 이름으로 사용
    env_name = os.path.basename(os.getcwd())
    envs = get_conda_envs()

    if env_name in envs:
        print(f"가상환경 '{env_name}'이 이미 존재합니다.")
        print("사용 가능한 Conda 환경:")
        for idx, env in enumerate(envs):
            print(f"{idx + 1}. {env}")
        choice = input("활성화할 환경의 번호를 선택하세요: ")
        try:
            selected_env = envs[int(choice) - 1]
            activate_env(selected_env)
        except (IndexError, ValueError):
            print("올바른 번호를 선택하지 않았습니다.")
    else:
        create_env(env_name)
        activate_env(env_name)

    print("\n설정이 완료되었습니다.")
    print(f"가상환경을 활성화하려면 다음 명령을 실행하세요:\nconda activate {env_name}")
    print("이제 이 환경에서 Python 스크립트를 실행할 수 있습니다.")


if __name__ == "__main__":
    main()
