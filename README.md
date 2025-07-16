# 🧠 AiAgentManual

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
![Last commit](https://img.shields.io/github/last-commit/id0s/AiAgentManual)  
![Language](https://img.shields.io/github/languages/top/id0s/AiAgentManual)

**AiAgentManual** adalah panduan dan kumpulan template agent AI berbasis LLM (Large Language Model), dirancang untuk membantu pengembang membangun agen otomatisasi cerdas, reasoning multi-step, dan integrasi tool.

---

## ✨ Fitur Utama

- Template agent siap pakai: `SimpleAgent`, `PlannerAgent`, `ToolAgent`
- Dukungan multi-tool: Web Search, File System, Calculator, dan lainnya
- Loop reasoning dan kontrol context dengan memory/session
- Modul NLP berbasis OpenAI atau model lain
- Dokumentasi arsitektur & debugging agent

---

## 📁 Struktur Proyek

```text
AiAgentManual/
├── src/
│   ├── agents/         # agent AI siap pakai
│   ├── tools/          # tools API seperti search & math
│   ├── utils/          # logging, memory, validation
│   ├── main.js         # entry point agent
│   └── config.js
├── docs/               # teori dan panduan agent
├── examples/           # skrip siap pakai
├── tests/
├── .env.example
├── package.json
└── LICENSE
```

---

## ⚙️ Instalasi & Setup

1. Clone repo:
   ```bash
   git clone https://github.com/id0s/AiAgentManual.git
   cd AiAgentManual
   ```

2. Install dependensi:
   ```bash
   npm install
   ```

3. Buat file `.env`:
   ```bash
   cp .env.example .env
   ```

4. Isi variabel:
   ```
   OPENAI_API_KEY=your_openai_key
   ```

5. Jalankan:
   ```bash
   node src/main.js
   ```

---

## 📌 Contoh Penggunaan

```js
import { SimpleAgent } from './src/agents/SimpleAgent';
import { WebSearchTool } from './src/tools/search';

const agent = new SimpleAgent({
  tools: [new WebSearchTool()],
  openaiKey: process.env.OPENAI_API_KEY
});

agent.run("Siapa presiden Indonesia saat ini?");
```

---

## 🧪 Testing

Jalankan seluruh tes:
```bash
npm test
```

---

## 📈 Rencana Pengembangan

- [ ] Tambah agent Reflexion dan ReAct
- [ ] Integrasi tools seperti Google Sheets, Email API
- [ ] Evaluasi agent secara otomatis
- [ ] Dokumentasi interaktif berbasis Jupyter/Colab

---

## 🤝 Kontribusi

1. Fork repo ini  
2. Buat branch baru: `git checkout -b fitur-xyz`  
3. Commit & push: `git commit -m "Tambah fitur xyz"`  
4. Ajukan PR, akan kami review secepatnya 🚀

---

## 📄 Lisensi

Berlisensi [MIT License](LICENSE) — silakan digunakan bebas untuk riset, eksperimen, dan proyek komersial.

---

## 👨‍💻 Pembuat

- Dibuat oleh: [id0s](https://github.com/id0s)  
- Email: contact@id0s.dev  
- Repo: https://github.com/id0s/AiAgentManual

---

> Jelajahi masa depan AI dengan agen yang fleksibel, modular, dan powerful.
