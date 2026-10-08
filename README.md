# ooclear: Sovereign BUFFER PURGER

<div align="center">

```
================================================================================
                                ooclear
               Sovereign openOODA TERMINAL BUFFER PURGER
================================================================================
```

**Sovereign BUFFER PURGER**  
*High-performance screen clearing and scrollback purge with VT100/ANSI compliance.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/ooclear/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S ooclear-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/ooclear/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/ooclear/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
ooclear-uninstall
# or: curl -fsSL https://openooda-tools.github.io/ooclear/uninstall.sh | bash
```

---

## 2. CLI Usage

```
ooclear 0.2.0 (openOODA sovereign terminal & buffer)
usage: ooclear [options]

Clear the terminal screen and scrollback buffer.

Options:
  -x                  do not clear scrollback buffer
  -s, --scrollback    clear scrollback buffer only (keep visible screen)
  -r, --reset         perform terminal hardware reset (RIS)
      --soft-reset    perform soft terminal reset (DECSTR)
  -T, --term=NAME     override terminal type (default from $TERM)
      --raw           print escape sequences without executing clear
      --audit         audit terminal capabilities and active profile
      --demo          run demonstration scenarios with synthetic profiles
      --json          output formatted as JSON telemetry
  -h, --help          display this help and exit
  -V, --version       output version information and exit
      --mcp           run as Model Context Protocol stdio server
```

---

## 3. High-Precision Terminal Reset & Purge

`ooclear` evaluates host `$TERM` and `$COLORTERM` capabilities to dispatch mathematically precise control sequences:

```bash
# Standard screen clear and scrollback purge (ED2 + ED3 + CUP):
ooclear

# Retain scrollback buffer (ED2 + CUP, matching legacy clear -x):
ooclear -x

# Purge scrollback only (ED3):
ooclear -s

# Full hardware terminal reset (RIS \x1bc):
ooclear -r

# Inspect escape sequence for another terminal profile:
ooclear --raw -T vt100
```

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `ooclear` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

```bash
ooclear --mcp
```

### Registered Tools
* **`clear_screen`**: Generate escape sequence to clear visible screen and home cursor.
* **`clear_scrollback`**: Generate escape sequence to clear visible screen and purge scrollback buffer.
* **`clear_reset`**: Generate hard terminal hardware reset (RIS) escape sequence.
* **`clear_sequences`**: List ANSI control sequence catalog for specified terminal profile.
* **`clear_audit`**: Audit host terminal environment and report supported buffer capabilities.

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&EnvCap`, `&McpCap`). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
