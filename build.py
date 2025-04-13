#!/usr/bin/env python3

import subprocess
from pathlib import Path

# Config
TARGET = "x86_64-unknown-linux-gnu"
DOCKER_IMAGE = "rust:latest"


def build_with_docker():
    print(f"🔧 Starting Docker build for {TARGET}...")

    docker_cmd = (
        f'docker run --rm '
        f'--platform linux/amd64 '
        f'-v "{Path.cwd()}:/usr/src/myapp" '
        f'-w /usr/src/myapp '
        f'{DOCKER_IMAGE} '
        f'bash -c "apt update && '
        f'apt install -y gcc libc6-dev pkg-config libssl-dev && '
        f'rustup target add {TARGET} && '
        f'export PKG_CONFIG_ALLOW_CROSS=1 && '
        f'cargo build --release --target={TARGET}"'
    )

    result = subprocess.run(docker_cmd, shell=True)
    if result.returncode != 0:
        raise RuntimeError("❌ Build failed.")

    print(f"✅ Done! Check ./target/{TARGET}/release/")


if __name__ == "__main__":
    build_with_docker()
