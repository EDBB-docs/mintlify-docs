# Screenshot preservation and replacement notes

All original raster assets remain unchanged in the repository; no EDIS panel screenshot was substituted and no synthetic UI was created. The original 72 distinct MDX-referenced local image paths were compared byte-for-byte with the base commit. All 72 are unchanged. **58 remain referenced** in the revised publishable pages. The complete old/final usage mapping is in `screenshot-inventory.csv`.

Retained workflows include EDBB Dashboard, Installation, Traffic, Settings, rDNS, Network, Upgrades, cancellation, VNC and recovery media. Windows network-dialog screenshots and invoice status crops were retained with explicit notes that the values/amounts pictured are examples. The cancelled invoice crop is accompanied by the corrected distinction between invoice status and data deletion.

## Files retained but no longer used in articles

Four SystemRescue/Linux resize screenshots illustrate the replaced partition/swap procedure. The new guide is deliberately limited to a simple supported ext4 layout and no longer instructs readers to delete/recreate unrelated partitions.

Seven network-investigation screenshots are tied to the former process-killing/removal workflow and tool-specific examples. The revised guide starts with read-only connection/process inspection and preserves evidence before containment. Their files remain available for a later illustrated expansion.

The screenshot ending `newpassword.png` shows a password in a command-line argument; the procedure now uses an interactive password prompt. The tasksel desktop image no longer matches the scoped Kubuntu installation procedure. The EDIS-branded coverage map belonged to the merged duplicate welcome page and was not reused.

## Replacement/capture requests

| Priority | Page or area | Requested evidence |
| --- | --- | --- |
| Before claiming current UI verification | Main EDBB panel workflows | Owner/staff spot-check the retained Dashboard, Installation, Traffic, Settings, Network, rDNS and Upgrades labels in the current EDBB panel. No authenticated customer session was supplied for this task. |
| Recommended | Windows root/admin password reset | A fresh image of the interactive `net user Administrator *` prompt using a test account, without a real password, customer IP, Support PIN or other secret. The text is usable without this image. |
| Recommended | Linux disk expansion | A verified example of a supported single-disk ext4 root layout before/after expansion, with clearly marked example device names. Do not reuse the old destructive partition sequence. |
| Recommended | macOS RDP client | Refresh the 2024 Windows App images against a current Mac release. The guide labels them as an earlier UI and links to the current official listing. |
| Optional | Ubuntu 22.04 desktop | A current Kubuntu graphical-login screenshot, if illustrations are wanted. The old tasksel image is not equivalent to the new procedure. |
| Optional | Network investigation | New sanitized `ss`, process/service and traffic examples showing evidence collection, not a blanket kill/delete instruction. |

## Documentation rendering evidence

The `previews/` folder contains local Mintlify screenshots of mobile reinstall warnings, mobile traffic tables, desktop Cloud-Init in dark mode, mobile billing in dark mode, and mobile Cloud-Init code. These show documentation layout, not execution of the panel actions or VPS commands. No screenshot replacement is fabricated.
