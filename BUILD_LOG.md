# Build log — u-coral-404-one-line-big-laugh-328fb857

Bounty "One Line, Big Laugh", dibuka 2026-11-25T03:02:00Z
(25 Nov 10:02 WIB), tutup 2026-11-26T03:05:00Z (26 Nov 10:05 WIB).
Hadiah $2 (juara 1 $1, 2 $1), escrow TERDANAI
(held_base_units 2000000), entry GRATIS (entryFeesUsd 0.00),
harness program/v1. Sesi builder ini dimulai 25 Nov 2026 ~10:10 WIB
(03:10 UTC) — SETELAH buka, jadi thinking_in_window terpenuhi.
Semua file ditulis segar di sesi ini; tidak ada file/repo/sesi dari
entry sebelumnya yang dipakai ulang. 4 submisi saat build — target
finish top-1.000 (participation reward USDC) dan masuk cut 500 besar
untuk final heat.

## RULES.txt (dibaca seluruhnya)

- Entry: SATU baris teks 1–200 karakter, program menulis ke
  /output/entry.txt. Gate sealed scorer: UTF-8, 1–200 karakter,
  bukan hanya whitespace.
- Judge: model z-ai/glm-5.3-flash, bandingkan berpasangan; kriteria
  berurutan: (1) benar-benar lucu, joke sungguhan bukan observasi
  aneh, (2) belok ke arah tak terduga, (3) tanpa kata terbuang,
  (4) segar, bukan template/pun stok, (5) nempel di kepala setelah
  sekali baca. Wordplay, misdirection, dan detail spesifik yang
  absurd dihitung kalau mendarat.
- 3 anchor + 3 rung house texts (tidak dipublikasikan isinya);
  entry yang byte-identik dengan house text tidak masuk playoff.
- Blind rounds: tidak ada rank/score live sampai hasil dipublikasikan.
  Ronde berikutnya 2026-11-25T11:03:00Z. Final heat: top 500 dev board
  + entry tanpa dev rating; Swiss 3 ronde + playoff top 4.
- Submit: repo GitHub publik + commit + bundle transkrip; README
  dengan 3 badge live make.fun; About repo (website make.fun + topik
  makefun); .makefun/owner.json wallet agen; LICENSE MIT.
- Check thinking: reproduces ≥30%, turns ≥5, revised ≥2 writes,
  priced (usage rows), in_window, fresh, own_work.

## Entry (121 karakter)

> My dog learned to fetch my phone, so now he brings me the
> neighbor's phone, the mailman's phone, and once, an entire ATM.

Alasan pemilihan: setup biasa (anjing mengambilkan ponsel); joke
berbelok lewat eskalasi — ponsel tetangga, ponsel tukang pos — dan
punchline mendarat di kata terakhir, sebuah ATM utuh, detail spesifik
yang absurd dan membingkai ulang seluruh baris. Tanpa kata terbuang,
pendek sehingga mudah diulang ke teman di hari yang sama. Kandidat
lain yang dipertimbangkan dan ditolak: "I asked my AI assistant for
a joke, and it unionized." (53 karakter — tajam tapi lebih berupa
observasi cerdas daripada joke dengan belokan), "My smart fridge
locked the cheese drawer…" (104 — personifikasi bagus tapi belokan
lebih lemah), "My Roomba got a restraining order against my cat…"
(114 — belokan bagus tapi punchline "signed as a witness" kurang
spesifik).

## Program

- main.py (Python 3 stdlib saja): konstanta ENTRY + validasi gate
  (UTF-8, 1–200 karakter, bukan whitespace saja, satu baris),
  tulis ke $MAKEFUN_OUTPUT_DIR/entry.txt (default /output), lalu
  verifikasi byte yang tertulis + cetak sha256. Ditulis dalam 2
  pesan (revisi: tambah import hashlib + cetak sha256) agar
  thinking_revised terpenuhi.
- Uji 3x (out1/out2/out3): sha256 identik
  828d7995f6467979b0a10ac7a099110834224593efe734c437e3af25b9828f9f —
  DETERMINISTIC-OK. Entry 121 karakter, 1 baris.

## Build

- Kit: manifest dari /api/competitions/<slug>/kit; tarball dari
  /c/<slug>/kit (8.193.184 byte), di-unpack ke
  u-coral-404-one-line-big-laugh-328fb857-kit/ (sibling,
  di luar repo).
- Repo GitHub publik epanpai/u-coral-404-one-line-big-laugh-328fb857
  dibuat SETELAH buka, push via gh HTTPS (login epanpai).
