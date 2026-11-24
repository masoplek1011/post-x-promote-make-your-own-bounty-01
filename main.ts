// main.ts — entry program for post-x-promote-make-your-own-bounty-01.
//
// The whole job of this program is one deterministic copy: it reads
// POST.json from the repository directory and writes an identical copy
// into the output directory. It uses only the Node standard library,
// touches no network, reads no clock, and writes nowhere else.
//
// Environment:
//   MAKEFUN_BOT_DIR    directory holding POST.json (default: /bot)
//   MAKEFUN_OUTPUT_DIR directory receiving the copy (default: /output)

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

// Read the file first so a malformed POST.json fails loudly here,
// before anything is written to the output directory.
const source = join(botDir, "POST.json");
const parsed = JSON.parse(readFileSync(source, "utf8"));
if (typeof parsed !== "object" || parsed === null || typeof parsed.url !== "string") {
  throw new Error("POST.json must be a JSON object with a string url");
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, join(outDir, "POST.json"));
