from __future__ import annotations

from pathlib import Path

TARGET_LINE = (
    "custom_proxy_group=🌏 东南亚节点`url-test`(越南|Vietnam|VN|印尼|Indonesia|ID|尼泊尔|Nepal|NP|"
    "柬埔寨|Cambodia|KH|缅甸|Myanmar|MM|马来西亚|Malaysia|MY)`"
    "http://www.gstatic.com/generate_204`300,,50"
)
KOREA_PREFIX = "custom_proxy_group=🇰🇷 韩国节点"
KOREA_REF_TOKEN = "[]🇰🇷 韩国节点`"
SEA_REF_TOKEN = "[]🌏 东南亚节点`"


def ensure_trailing_newline(text: str) -> str:
    if text.endswith("\n"):
        return text
    return text + ("\n" if text else "")


def inject_sea_reference(lines: list[str]) -> bool:
    changed = False
    for idx, line in enumerate(lines):
        if not line.startswith("custom_proxy_group="):
            continue
        if SEA_REF_TOKEN in line:
            continue
        token_idx = line.find(KOREA_REF_TOKEN)
        if token_idx == -1:
            continue
        insertion_point = token_idx + len(KOREA_REF_TOKEN)
        lines[idx] = line[:insertion_point] + SEA_REF_TOKEN + line[insertion_point:]
        changed = True
    return changed


def insert_sea_group(content: str) -> tuple[str, bool]:
    lines = content.splitlines()

    has_target = any(line.strip() == TARGET_LINE for line in lines)
    changed = False

    if not has_target:
        insert_idx: int | None = None
        for idx, line in enumerate(lines):
            if line.lstrip().startswith(KOREA_PREFIX):
                insert_idx = idx + 1
                break

        if insert_idx is None:
            lines.append(TARGET_LINE)
        else:
            lines.insert(insert_idx, TARGET_LINE)
        changed = True

    if inject_sea_reference(lines):
        changed = True

    new_content = "\n".join(lines)
    new_content = ensure_trailing_newline(new_content)
    return new_content, changed


def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    new_text, changed = insert_sea_group(text)
    if changed:
        path.write_text(new_text, encoding="utf-8")
        print(f"Inserted SEA group into {path}")
    else:
        print(f"No change needed for {path}")
    return changed


def main() -> None:
    config_dir = Path("config")
    if not config_dir.exists():
        raise SystemExit("config directory not found; run after pulling ACL4SSR configs.")

    ini_files = sorted(config_dir.glob("ACL4SSR_Online_Full*"))
    if not ini_files:
        print("No ACL4SSR_Online_*.ini files detected.")
        return

    changed_any = False
    for ini_path in ini_files:
        if process_file(ini_path):
            changed_any = True

    if not changed_any:
        print("SEA group already present in all files.")


if __name__ == "__main__":
    main()
