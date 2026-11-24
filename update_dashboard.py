import json

with open(r"C:\Users\olfor\.gemini\antigravity\scratch\transicion_verde_calama\dashboard_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Criteria scores for the 4 projects
project_criteria = {
    "Ecoesmart": {"problema": 4.00, "originalidad": 3.33, "comunicacion": 3.33, "digital": 3.00, "tecnicas": 3.67, "total": 17.33},
    "Recompost": {"problema": 4.00, "originalidad": 3.33, "comunicacion": 3.67, "digital": 3.00, "tecnicas": 3.33, "total": 17.33},
    "TecnMin": {"problema": 3.33, "originalidad": 2.67, "comunicacion": 2.67, "digital": 3.00, "tecnicas": 2.33, "total": 14.00},
    "Calama se reconstruye": {"problema": 2.67, "originalidad": 2.67, "comunicacion": 3.00, "digital": 2.67, "tecnicas": 2.67, "total": 13.67}
}

# Update project data with criteria
for p in data["projects"]:
    p["criteria"] = project_criteria.get(p["name"], {})

# Update participants: remove "Sólo diploma" terminology
for p in data["participants"]:
    if "Diploma" in p["type"] or "Sólo" in p["type"]:
        p["type"] = "Asistente al Demoday (Recepción de Diploma)"
    else:
        p["type"] = "Equipo Expositor Demoday (Pitch)"

json_str = json.dumps(data, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dashboard Demoday & Transferencia - Negocios Digitales y Circulares El Loa 2026</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Chart.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <!-- Lucide Icons CDN -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
    }}
    .brand-fuchsia {{ color: #C81057; }}
    .bg-brand-fuchsia {{ background-color: #C81057; }}
    .border-brand-fuchsia {{ border-color: #C81057; }}
    .brand-navy {{ color: #1B365D; }}
    .bg-brand-navy {{ background-color: #1B365D; }}
    .badge-promoter {{ background-color: #d1fae5; color: #065f46; border: 1px solid #a7f3d0; }}
    .badge-passive {{ background-color: #fef3c7; color: #92400e; border: 1px solid #fde68a; }}
    .badge-detractor {{ background-color: #fee2e2; color: #991b1b; border: 1px solid #fecaca; }}
  </style>
</head>
<body class="bg-[#F8FAFC] text-slate-800 min-h-screen flex flex-col">

  <!-- TOP BRAND HEADER -->
  <header class="bg-gradient-to-r from-[#1B365D] via-[#991B1B] to-[#C81057] text-white shadow-lg sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex flex-wrap justify-between items-center gap-4">
      <div class="flex items-center space-x-3.5">
        <div class="w-11 h-11 rounded-xl bg-white/10 backdrop-blur-sm border border-white/20 flex items-center justify-center font-black text-2xl shadow-inner">
          🌱
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h1 class="font-black text-lg sm:text-xl tracking-tight uppercase">Programa Negocios Circulares y Digitales</h1>
            <span class="text-[11px] bg-white/20 text-white font-extrabold px-2 py-0.5 rounded-full backdrop-blur-sm">El Loa 2026</span>
          </div>
          <p class="text-xs text-rose-100 font-light">Panel Oficial de Transferencia Cognitiva, NPS y Evaluación Demoday | Viraliza Corfo 25VIRTL-307464</p>
        </div>
      </div>

      <div class="flex items-center gap-2 sm:gap-3 text-xs">
        <a href="{data['project']['sheet_url']}" target="_blank" class="px-3.5 py-1.5 rounded-lg bg-white/10 hover:bg-white/20 transition flex items-center gap-1.5 text-white border border-white/20 font-semibold shadow-sm">
          <i data-lucide="file-spreadsheet" class="w-4 h-4 text-emerald-300"></i>
          <span>Hoja Google Drive</span>
        </a>
        <button onclick="window.print()" class="px-3.5 py-1.5 rounded-lg bg-white text-slate-900 hover:bg-slate-100 transition flex items-center gap-1.5 font-bold shadow-sm">
          <i data-lucide="printer" class="w-4 h-4 text-[#C81057]"></i>
          <span>Imprimir / PDF</span>
        </button>
      </div>
    </div>
  </header>

  <!-- NAVEGACIÓN POR PESTAÑAS Y BANNER INSTITUCIONAL -->
  <section class="bg-white border-b border-slate-200 shadow-sm sticky top-[62px] z-40">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-wrap items-center justify-between gap-4 py-2.5">
      
      <!-- TABS -->
      <nav class="flex space-x-2 sm:space-x-4">
        <button id="tabBtn1" onclick="switchTab('tab1')" class="px-4 py-2 rounded-xl text-xs sm:text-sm font-bold flex items-center gap-2 transition bg-[#C81057] text-white shadow-sm">
          <i data-lucide="layout-dashboard" class="w-4 h-4"></i>
          <span>Panel General & Proyectos</span>
        </button>

        <button id="tabBtn2" onclick="switchTab('tab2')" class="px-4 py-2 rounded-xl text-xs sm:text-sm font-bold flex items-center gap-2 transition bg-slate-100 text-slate-600 hover:bg-slate-200">
          <i data-lucide="lightbulb" class="w-4 h-4 text-amber-500"></i>
          <span>Ideas Fuerza & Testimonios</span>
        </button>

        <button id="tabBtn3" onclick="switchTab('tab3')" class="px-4 py-2 rounded-xl text-xs sm:text-sm font-bold flex items-center gap-2 transition bg-slate-100 text-slate-600 hover:bg-slate-200">
          <i data-lucide="lock" class="w-4 h-4 text-slate-400"></i>
          <span>Fichas Individuales (N=20)</span>
        </button>
      </nav>

      <!-- INSTITUCIONAL ENTIDADES -->
      <div class="hidden md:flex items-center gap-3 text-xs text-slate-500 font-medium">
        <span class="flex items-center gap-1.5">
          <span class="w-2.5 h-2.5 rounded-full bg-rose-600"></span> INACAP Sede Calama
        </span>
        <span class="text-slate-300">|</span>
        <span class="flex items-center gap-1.5">
          <span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span> AIEP Calama
        </span>
        <span class="text-slate-300">|</span>
        <span class="text-emerald-700 font-semibold flex items-center gap-1">
          <i data-lucide="check-circle" class="w-3.5 h-3.5 text-emerald-600"></i> Ejecuta Verdical
        </span>
      </div>

    </div>
  </section>

  <!-- CONTENIDO PRINCIPAL -->
  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex-1 w-full space-y-6">

    <!-- ======================================================== -->
    <!-- PESTAÑA 1: PANEL GENERAL & PROYECTOS -->
    <!-- ======================================================== -->
    <div id="tab1Content" class="space-y-6">

      <!-- BANNER CORPORATIVO PROGRAMA -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden flex flex-col lg:flex-row items-center justify-between">
        <div class="p-6 lg:p-8 space-y-3 max-w-2xl">
          <div class="flex items-center gap-2">
            <span class="bg-rose-100 text-[#C81057] font-black text-xs px-2.5 py-1 rounded-full uppercase tracking-wider">
              Viraliza Formación Corfo
            </span>
            <span class="text-xs text-slate-400 font-medium">• Provincia de El Loa</span>
          </div>
          <h2 class="text-xl sm:text-2xl font-black text-slate-900 tracking-tight leading-snug">
            Fortalecimiento del Ecosistema Emprendedor e Innovación en El Loa
          </h2>
          <p class="text-xs sm:text-sm text-slate-600 leading-relaxed font-normal">
            Programa formativo dirigido a estudiantes de educación superior con foco en la <strong>transición verde</strong> y la <strong>transformación digital</strong>, en coherencia con la Estrategia Regional de Innovación. A través de siete módulos secuenciales, capacitó y articuló a jóvenes talentos de <strong>INACAP</strong> y <strong>AIEP</strong> en torno a soluciones territoriales de economía circular.
          </p>
          <div class="pt-2 flex flex-wrap gap-2 text-[11px] font-bold">
            <span class="px-2.5 py-1 rounded-md bg-amber-100 text-amber-900 border border-amber-200">Innovación Sostenible</span>
            <span class="px-2.5 py-1 rounded-md bg-slate-100 text-slate-800 border border-slate-200">Diseño de Negocio Sostenible</span>
            <span class="px-2.5 py-1 rounded-md bg-emerald-100 text-emerald-900 border border-emerald-200">Herramientas Digitales</span>
            <span class="px-2.5 py-1 rounded-md bg-orange-100 text-orange-900 border border-orange-200">Modelos Circulares</span>
            <span class="px-2.5 py-1 rounded-md bg-slate-100 text-slate-800 border border-slate-200">Liderazgo Verde</span>
            <span class="px-2.5 py-1 rounded-md bg-amber-100 text-amber-900 border border-amber-200">Tendencias Tecnológicas</span>
          </div>
        </div>
        <div class="p-6 lg:p-8 flex justify-center items-center bg-gradient-to-br from-rose-50/50 to-amber-50/30 w-full lg:w-auto">
          <img src="assets/banner_programa.jpg" alt="Programa Negocios Circulares y Digitales El Loa 2026" class="max-h-56 sm:max-h-64 object-contain rounded-xl shadow-md border border-slate-200">
        </div>
      </div>

      <!-- HERO CARDS (KPIS) -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
        
        <!-- NPS SCORE -->
        <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm relative overflow-hidden group hover:shadow-md transition">
          <div class="absolute top-0 right-0 w-24 h-24 bg-emerald-50 rounded-bl-full -mr-6 -mt-6 transition group-hover:scale-105"></div>
          <div class="relative z-10">
            <span class="text-xs font-bold uppercase tracking-wider text-slate-500">NPS Score Global</span>
            <div class="mt-2 flex items-baseline gap-2">
              <span class="text-3xl sm:text-4xl font-black text-emerald-700">+{data['kpis']['nps_score']}</span>
              <span class="text-xs font-semibold text-emerald-600">puntos</span>
            </div>
            <div class="mt-2 flex items-center gap-1.5 text-xs text-emerald-700 font-semibold">
              <i data-lucide="award" class="w-4 h-4"></i>
              <span>Nivel de Excelencia (+45 pts)</span>
            </div>
          </div>
        </div>

        <!-- DELTA DE APRENDIZAJE -->
        <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm relative overflow-hidden group hover:shadow-md transition">
          <div class="absolute top-0 right-0 w-24 h-24 bg-rose-50 rounded-bl-full -mr-6 -mt-6 transition group-hover:scale-105"></div>
          <div class="relative z-10">
            <span class="text-xs font-bold uppercase tracking-wider text-slate-500">Salto Cognitivo (Δ)</span>
            <div class="mt-2 flex items-baseline gap-2">
              <span class="text-3xl sm:text-4xl font-black text-[#C81057]">+{data['kpis']['delta_gain']}</span>
              <span class="text-xs font-semibold text-rose-600">pts (+{data['kpis']['delta_pct']}%)</span>
            </div>
            <div class="mt-2 flex items-center gap-1.5 text-xs text-slate-500">
              <i data-lucide="trending-up" class="w-4 h-4 text-[#C81057]"></i>
              <span>Línea base 3.16 ➔ Ex-post 4.41</span>
            </div>
          </div>
        </div>

        <!-- PARTICIPANTES DEMODAY -->
        <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm relative overflow-hidden group hover:shadow-md transition">
          <div class="absolute top-0 right-0 w-24 h-24 bg-blue-50 rounded-bl-full -mr-6 -mt-6 transition group-hover:scale-105"></div>
          <div class="relative z-10">
            <span class="text-xs font-bold uppercase tracking-wider text-slate-500">Participantes Demoday</span>
            <div class="mt-2 flex items-baseline gap-2">
              <span class="text-3xl sm:text-4xl font-black text-[#1B365D]">{data['kpis']['certified_students']}</span>
              <span class="text-xs font-semibold text-slate-500">estudiantes</span>
            </div>
            <div class="mt-2 flex items-center gap-1.5 text-xs text-slate-500 font-medium">
              <i data-lucide="users" class="w-4 h-4 text-blue-600"></i>
              <span>11 Expositores + 9 Asistentes</span>
            </div>
          </div>
        </div>

        <!-- PROYECTOS PREMIADOS -->
        <div class="bg-white rounded-2xl p-5 border border-slate-200 shadow-sm relative overflow-hidden group hover:shadow-md transition">
          <div class="absolute top-0 right-0 w-24 h-24 bg-purple-50 rounded-bl-full -mr-6 -mt-6 transition group-hover:scale-105"></div>
          <div class="relative z-10">
            <span class="text-xs font-bold uppercase tracking-wider text-slate-500">Iniciativas Premiadas</span>
            <div class="mt-2 flex items-baseline gap-2">
              <span class="text-3xl sm:text-4xl font-black text-purple-700">{data['kpis']['featured_projects_count']}</span>
              <span class="text-xs font-semibold text-purple-600">equipos</span>
            </div>
            <div class="mt-2 flex items-center gap-1.5 text-xs text-purple-700 font-semibold">
              <i data-lucide="sparkles" class="w-4 h-4"></i>
              <span>Con Incentivos de Impulso</span>
            </div>
          </div>
        </div>

      </div>

      <!-- SECCIÓN GRÁFICOS (3 GRÁFICOS ESTRATÉGICOS) -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        <!-- GRÁFICO 1: RADAR DE TRANSFERENCIA COGNITIVA -->
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-between">
          <div class="flex items-center justify-between mb-2">
            <div>
              <h3 class="font-extrabold text-sm sm:text-base text-slate-900">Curva de Transferencia Cognitiva</h3>
              <p class="text-[11px] text-slate-500">Diagnóstico Ex-ante (Línea Base) vs. Ex-post (Salida)</p>
            </div>
            <span class="text-[10px] bg-emerald-100 text-emerald-800 font-extrabold px-2 py-0.5 rounded-full">Δ +1.25 pts</span>
          </div>
          <div class="relative h-64 sm:h-72 w-full my-auto">
            <canvas id="radarChart"></canvas>
          </div>
          <div class="text-[11px] text-slate-500 bg-slate-50 p-2.5 rounded-xl border border-slate-100 flex items-center justify-between mt-2">
            <span>Mayor salto: <strong>Diseño Sostenible (+1.66)</strong></span>
            <span>Digital: <strong>+1.55 pts</strong></span>
          </div>
        </div>

        <!-- GRÁFICO 2: RÚBRICA DE JURADOS EN EL DEMODAY (NUEVO REEMPLAZO) -->
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-between">
          <div class="flex items-center justify-between mb-2">
            <div>
              <h3 class="font-extrabold text-sm sm:text-base text-slate-900">Desempeño Demoday por Criterio</h3>
              <p class="text-[11px] text-slate-500">Evaluación media de los 4 proyectos (Escala 1 a 5)</p>
            </div>
            <span class="text-[10px] bg-purple-100 text-purple-800 font-extrabold px-2 py-0.5 rounded-full">3 Jurados</span>
          </div>
          <div class="relative h-64 sm:h-72 w-full my-auto">
            <canvas id="projectCriteriaChart"></canvas>
          </div>
          <div class="text-[11px] text-slate-500 bg-slate-50 p-2.5 rounded-xl border border-slate-100 flex items-center justify-between mt-2">
            <span>Foco más alto: <strong>Problema u Oportunidad (3.50/5)</strong></span>
            <span>Pitch: <strong>3.17/5</strong></span>
          </div>
        </div>

        <!-- GRÁFICO 3: COMPARATIVA INSTITUCIONAL LIMPIA (GLOBAL VS INACAP VS AIEP) -->
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-between">
          <div class="flex items-center justify-between mb-2">
            <div>
              <h3 class="font-extrabold text-sm sm:text-base text-slate-900">Comparativa Institucional</h3>
              <p class="text-[11px] text-slate-500">Rendimiento Ex-post y NPS Score por Casa de Estudios</p>
            </div>
            <span class="text-[10px] bg-blue-100 text-blue-800 font-extrabold px-2 py-0.5 rounded-full">INACAP vs AIEP</span>
          </div>
          <div class="relative h-64 sm:h-72 w-full my-auto">
            <canvas id="instCleanChart"></canvas>
          </div>
          <div class="text-[11px] text-slate-500 bg-slate-50 p-2.5 rounded-xl border border-slate-100 flex items-center justify-between mt-2">
            <span>INACAP: <strong>NPS +37.5 | 4.38/5</strong></span>
            <span>AIEP: <strong>NPS +50.0 | 4.44/5</strong></span>
          </div>
        </div>

      </div>

      <!-- SECCIÓN: LOS 4 PROYECTOS DESTACADOS DEL DEMODAY (CON INCENTIVOS) -->
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 space-y-4">
        <div class="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3">
          <div>
            <div class="flex items-center gap-2">
              <span class="text-2xl">🏆</span>
              <h2 class="text-lg font-black text-slate-900">Los 4 Proyectos Destacados del Demoday (Con Incentivos Asignados)</h2>
            </div>
            <p class="text-xs text-slate-500 mt-0.5">Estudiantes organizados en 4 equipos que expusieron sus ideas de proyecto ante la comisión de jurados</p>
          </div>
          <span class="text-xs bg-purple-50 text-purple-700 font-bold px-3 py-1 rounded-full border border-purple-200 flex items-center gap-1.5">
            <i data-lucide="award" class="w-3.5 h-3.5"></i>
            <span>Comisión Evaluadora: Valentina Muñoz, Rodrigo Mérida y Cecilia Martínez</span>
          </span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
"""

for p in data["projects"]:
    html_content += f"""
          <div class="bg-gradient-to-br from-slate-50 to-purple-50/20 rounded-xl p-5 border border-slate-200 hover:border-purple-300 transition shadow-sm space-y-3">
            <div class="flex items-start justify-between gap-2">
              <div>
                <span class="text-[10px] font-extrabold uppercase tracking-wider text-purple-700 bg-purple-100 px-2.5 py-0.5 rounded-md">{p['tag']}</span>
                <h3 class="text-lg font-black text-slate-900 mt-1">{p['name']}</h3>
                <p class="text-xs text-slate-500 font-medium">{p['team']}</p>
              </div>
              <div class="text-right">
                <span class="text-2xl font-black text-purple-800">{p['avg_score']}</span>
                <span class="text-xs text-slate-500 font-medium">/ 25 pts</span>
                <div class="text-[11px] text-emerald-600 font-bold">{p['pct_score']}% Rendimiento</div>
              </div>
            </div>

            <div class="text-xs text-slate-700 bg-white p-3 rounded-lg border border-slate-200/80">
              <span class="font-bold text-slate-900">Solución Territorial:</span> {p['pitch']}
            </div>

            <div class="text-xs space-y-1.5">
              <div class="flex items-center gap-1.5 text-emerald-700 font-bold">
                <i data-lucide="sparkles" class="w-4 h-4 text-emerald-600"></i>
                <span>{p['incentive']}</span>
              </div>
              <p class="text-[11px] text-slate-500 italic"><strong class="text-slate-700 not-italic">Fortalezas:</strong> {p['strengths']}</p>
            </div>

            <div class="pt-2 border-t border-slate-200/60">
              <details class="text-xs text-slate-600 group">
                <summary class="cursor-pointer font-bold text-rose-700 hover:text-rose-900 flex items-center justify-between">
                  <span>Ver evaluación detallada de los 3 jurados</span>
                  <i data-lucide="chevron-down" class="w-3.5 h-3.5 transition group-open:rotate-180"></i>
                </summary>
                <div class="mt-2 space-y-2 bg-white p-3 rounded-lg border border-slate-200">
"""
    for ev in p["evaluations"]:
        html_content += f"""
                  <div class="border-b border-slate-100 last:border-0 pb-1.5 last:pb-0">
                    <div class="flex justify-between font-bold text-[11px] text-slate-800">
                      <span>{ev['juror']}</span>
                      <span class="text-purple-700">{ev['score']} / 25 pts</span>
                    </div>
                    <p class="text-[11px] text-slate-600 mt-0.5 leading-relaxed">{ev['comment']}</p>
                  </div>
"""
    html_content += """
                </div>
              </details>
            </div>
          </div>
"""

html_content += f"""
        </div>
      </div>

    </div>

    <!-- ======================================================== -->
    <!-- PESTAÑA 2: IDEAS FUERZA & TESTIMONIOS CUALITATIVOS -->
    <!-- ======================================================== -->
    <div id="tab2Content" class="space-y-6 hidden">
      
      <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 space-y-4">
        <div class="border-b border-slate-100 pb-3 flex flex-wrap items-center justify-between gap-2">
          <div>
            <div class="flex items-center gap-2">
              <span class="text-2xl">💡</span>
              <h2 class="text-lg font-black text-slate-900">Ideas Fuerza Detectadas en las Evaluaciones Ex-post</h2>
            </div>
            <p class="text-xs text-slate-500 mt-0.5">Patrones cualitativos emergentes de las respuestas abiertas de los participantes sobre el territorio de El Loa</p>
          </div>
          <span class="text-xs bg-amber-50 text-amber-800 font-bold px-3 py-1 rounded-full border border-amber-200">
            5 Ejes Cualitativos
          </span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
          
          <!-- EJE 1: INTELIGENCIA ARTIFICIAL -->
          <div class="bg-gradient-to-br from-slate-50 to-rose-50/20 p-5 rounded-xl border border-slate-200 space-y-3">
            <div class="flex items-center gap-2 text-rose-700 font-black text-sm">
              <i data-lucide="cpu" class="w-4 h-4 text-[#C81057]"></i>
              <span>1. Inteligencia Artificial como Acelerador de Soluciones</span>
            </div>
            <p class="text-xs text-slate-600 leading-relaxed">
              Los estudiantes destacan la apropiación de herramientas digitales e IA generativa no como teoría, sino como copilotos prácticos para diseñar contenedores inteligentes, calcular métricas de contaminación y estructurar presentaciones de impacto.
            </p>
            <div class="space-y-1.5 text-[11px] bg-white p-3 rounded-lg border border-slate-200 italic text-slate-700">
              <p>• <strong>Carlos Olave (INACAP):</strong> "La enseñanza sobre Inteligencia Artificial influyó directamente en mi propuesta para el diseño del contenedor inteligente."</p>
              <p>• <strong>Felipe Vergara (INACAP):</strong> "Las herramientas más destacadas fueron IA y Marketing... todos los libros entregados y asistidos por el agente de IA para el pitch."</p>
            </div>
          </div>

          <!-- EJE 2: CIRCULARIDAD DE PLÁSTICOS Y ORGÁNICOS -->
          <div class="bg-gradient-to-br from-slate-50 to-emerald-50/20 p-5 rounded-xl border border-slate-200 space-y-3">
            <div class="flex items-center gap-2 text-emerald-800 font-black text-sm">
              <i data-lucide="recycle" class="w-4 h-4 text-emerald-600"></i>
              <span>2. Valorización de Residuos Críticos: Plásticos PET y Orgánicos</span>
            </div>
            <p class="text-xs text-slate-600 leading-relaxed">
              Foco prioritario en los residuos que hoy colapsan vertederos o generan microbasurales en Calama, planteando modelos de negocio circulares de reciclaje incentivado (Redimir/Reciclaz) y compostaje comunitario.
            </p>
            <div class="space-y-1.5 text-[11px] bg-white p-3 rounded-lg border border-slate-200 italic text-slate-700">
              <p>• <strong>Yoset Manacá (AIEP):</strong> "El desafío de reciclar las botellas plásticas para lograr darles nueva vida, monitoreando la huella de carbono y trazabilidad."</p>
              <p>• <strong>Mariana Zambrana (INACAP):</strong> "Detectamos la contaminación comunal basándonos en toneladas y porcentajes de la Municipalidad de Calama."</p>
            </div>
          </div>

          <!-- EJE 3: SIMBIOSIS MINERO-TERRITORIAL -->
          <div class="bg-gradient-to-br from-slate-50 to-blue-50/20 p-5 rounded-xl border border-slate-200 space-y-3">
            <div class="flex items-center gap-2 text-blue-900 font-black text-sm">
              <i data-lucide="factory" class="w-4 h-4 text-blue-600"></i>
              <span>3. Descarbonización y Encadenamiento con Minería y Agricultura</span>
            </div>
            <p class="text-xs text-slate-600 leading-relaxed">
              Comprensión del ecosistema productivo de El Loa: conectar la gran minería con agricultores y recicladores para resolver la escasez hídrica y valorizar residuos industriales.
            </p>
            <div class="space-y-1.5 text-[11px] bg-white p-3 rounded-lg border border-slate-200 italic text-slate-700">
              <p>• <strong>Mary Morales (INACAP):</strong> "En El Loa existe escasez de agua; la circularidad se relaciona con mineras, agricultores y pequeños empresarios para ahorrar recursos."</p>
              <p>• <strong>Joaquin Yufla (INACAP):</strong> "Identificamos brechas entre la formación técnica y el mundo industrial, usando la tecnología para conectar a los actores del territorio."</p>
            </div>
          </div>

          <!-- EJE 4: SUPERACIÓN DE BARRERAS CULTURALES -->
          <div class="bg-gradient-to-br from-slate-50 to-amber-50/20 p-5 rounded-xl border border-slate-200 space-y-3">
            <div class="flex items-center gap-2 text-amber-900 font-black text-sm">
              <i data-lucide="heart-handshake" class="w-4 h-4 text-amber-600"></i>
              <span>4. Liderazgo Verde y Cambio Cultural Ciudadano</span>
            </div>
            <p class="text-xs text-slate-600 leading-relaxed">
              Diagnóstico unánime sobre la necesidad de concientización: la tecnología es viable, pero se requiere liderazgo adaptativo y alianzas público-privadas para educar a los vecinos.
            </p>
            <div class="space-y-1.5 text-[11px] bg-white p-3 rounded-lg border border-slate-200 italic text-slate-700">
              <p>• <strong>Ingri Gahona (AIEP):</strong> "Si se dispusieran más recursos y educación comunitaria se derrumbaría la barrera cultural."</p>
              <p>• <strong>Lorens Barboza (INACAP):</strong> "Las personas tienden a generar mucha basura y no reciclan; la estrategia debe partir por educación temprana."</p>
            </div>
          </div>

        </div>

        <!-- EJE 5: DEMODAY Y COMPETENCIAS -->
        <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 text-xs text-slate-700 space-y-2">
          <span class="font-extrabold text-slate-900 flex items-center gap-1.5">
            <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600"></i>
            <span>5. El Valor Transformador de la Experiencia Demoday</span>
          </span>
          <p class="leading-relaxed">
            La instancia de presentarse ante un panel externo de evaluadores permitió a los estudiantes contrastar sus propuestas contra estándares de viabilidad económica, costos operativos y tracción comunitaria. Todos los expositores declararon que estructurar el pitch territorial aumentó drásticamente su seguridad técnica y capacidad de comunicación oral.
          </p>
        </div>

      </div>

    </div>

    <!-- ======================================================== -->
    <!-- PESTAÑA 3: FICHAS INDIVIDUALES (PROTEGIDO CON PASSWORD) -->
    <!-- ======================================================== -->
    <div id="tab3Content" class="space-y-6 hidden">

      <!-- PANTALLA DE BLOQUEO POR CONTRASEÑA -->
      <div id="passwordGate" class="bg-white rounded-2xl border border-slate-200 shadow-sm p-8 max-w-lg mx-auto text-center space-y-4 my-8">
        <div class="w-14 h-14 rounded-2xl bg-rose-50 border border-rose-200 flex items-center justify-center mx-auto text-rose-600 shadow-sm">
          <i data-lucide="lock" class="w-7 h-7"></i>
        </div>
        <div>
          <h3 class="text-lg font-black text-slate-900">Registro Individual de Estudiantes</h3>
          <p class="text-xs text-slate-500 mt-1">Esta sección contiene datos nominativos y calificaciones individuales de la cohorte final (N=20). Ingrese la clave de autorización para acceder.</p>
        </div>

        <form id="pwdForm" onsubmit="unlockTable(event)" class="space-y-3 pt-2">
          <div class="relative">
            <input type="password" id="pwdInput" placeholder="Ingrese clave de acceso..." class="w-full text-center text-sm bg-slate-50 border border-slate-300 rounded-xl px-4 py-2.5 focus:outline-none focus:ring-2 focus:ring-[#C81057] font-bold tracking-widest text-slate-800">
          </div>
          <p id="pwdError" class="text-xs text-rose-600 font-bold hidden">Contraseña incorrecta. Por favor intente nuevamente.</p>
          <button type="submit" class="w-full py-2.5 rounded-xl bg-[#C81057] hover:bg-rose-700 text-white font-bold text-xs uppercase tracking-wider transition shadow-sm">
            Desbloquear Información
          </button>
        </form>
      </div>

      <!-- TABLA DESBLOQUEADA (OCULTA INICIALMENTE) -->
      <div id="protectedData" class="space-y-4 hidden">
        
        <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 space-y-4">
          <div class="flex flex-wrap items-center justify-between gap-4 border-b border-slate-100 pb-3">
            <div>
              <div class="flex items-center gap-2">
                <i data-lucide="unlock" class="w-5 h-5 text-emerald-600"></i>
                <h2 class="text-lg font-black text-slate-900">Registro Individual de Estudiantes Evaluados (N=20)</h2>
              </div>
              <p class="text-xs text-slate-500 mt-0.5">Consulta de calificaciones por módulo, promedio ex-post, categoría NPS y evidencia de transferencia</p>
            </div>
            
            <div class="flex items-center gap-3">
              <div class="w-full sm:w-64">
                <input type="text" id="searchInput" onkeyup="applyFilters()" placeholder="Buscar participante..." class="w-full text-xs bg-slate-50 border border-slate-300 rounded-lg px-3 py-1.5 focus:outline-none focus:ring-2 focus:ring-[#C81057]">
              </div>
              <button onclick="lockTable()" class="px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-semibold flex items-center gap-1 transition">
                <i data-lucide="lock" class="w-3.5 h-3.5"></i>
                <span>Bloquear</span>
              </button>
            </div>
          </div>

          <div class="overflow-x-auto">
            <table class="w-full text-left border-collapse text-xs">
              <thead>
                <tr class="bg-slate-100/80 text-slate-700 border-b border-slate-200 font-bold">
                  <th class="py-2.5 px-3">Estudiante</th>
                  <th class="py-2.5 px-2 text-center">Institución</th>
                  <th class="py-2.5 px-2">Participación Demoday</th>
                  <th class="py-2.5 px-1.5 text-center" title="Innovación Sostenible">M1</th>
                  <th class="py-2.5 px-1.5 text-center" title="Diseño Negocio">M2</th>
                  <th class="py-2.5 px-1.5 text-center" title="Herramientas Digitales">M3</th>
                  <th class="py-2.5 px-1.5 text-center" title="Modelos Circulares">M4</th>
                  <th class="py-2.5 px-1.5 text-center" title="Liderazgo Verde">M5</th>
                  <th class="py-2.5 px-1.5 text-center" title="Tendencias Tech">M6</th>
                  <th class="py-2.5 px-1.5 text-center" title="Pitch Day">M7</th>
                  <th class="py-2.5 px-2 text-center">Promedio</th>
                  <th class="py-2.5 px-2 text-center">NPS</th>
                  <th class="py-2.5 px-3">Evidencia Cualitativa / Observación</th>
                </tr>
              </thead>
              <tbody id="participantsTableBody" class="divide-y divide-slate-100">
                <!-- Injected via JavaScript -->
              </tbody>
            </table>
          </div>
        </div>

      </div>

    </div>

  </main>

  <!-- FOOTER INSTITUCIONAL -->
  <footer class="bg-slate-900 text-slate-400 text-xs py-6 mt-12 border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-wrap justify-between items-center gap-4">
      <div>
        <p class="font-extrabold text-slate-200">Programa Negocios Circulares y Digitales para El Loa 2026</p>
        <p class="text-slate-400 text-[11px]">Proyecto apoyado por Comité Corfo Antofagasta (Instrumento Viraliza Formación 25VIRTL-307464) • Ejecuta Verdical</p>
      </div>
      <div class="flex items-center gap-4 text-[11px]">
        <span>INACAP Sede Calama</span>
        <span>•</span>
        <span>AIEP Calama</span>
        <span>•</span>
        <span>Noviembre 2026</span>
      </div>
    </div>
  </footer>

  <!-- LÓGICA DE JAVASCRIPT Y CHART.JS -->
  <script>
    const data = {json_str};

    let isUnlocked = sessionStorage.getItem('students_unlocked') === 'true';

    function switchTab(tabId) {{
      // Update Tab buttons
      ['tabBtn1', 'tabBtn2', 'tabBtn3'].forEach(id => {{
        const btn = document.getElementById(id);
        btn.className = "px-4 py-2 rounded-xl text-xs sm:text-sm font-bold flex items-center gap-2 transition bg-slate-100 text-slate-600 hover:bg-slate-200";
      }});

      // Hide all tab contents
      ['tab1Content', 'tab2Content', 'tab3Content'].forEach(id => {{
        document.getElementById(id).classList.add('hidden');
      }});

      if (tabId === 'tab1') {{
        document.getElementById('tabBtn1').className = "px-4 py-2 rounded-xl text-xs sm:text-sm font-bold flex items-center gap-2 transition bg-[#C81057] text-white shadow-sm";
        document.getElementById('tab1Content').classList.remove('hidden');
      }} else if (tabId === 'tab2') {{
        document.getElementById('tabBtn2').className = "px-4 py-2 rounded-xl text-xs sm:text-sm font-bold flex items-center gap-2 transition bg-[#C81057] text-white shadow-sm";
        document.getElementById('tab2Content').classList.remove('hidden');
      }} else if (tabId === 'tab3') {{
        document.getElementById('tabBtn3').className = "px-4 py-2 rounded-xl text-xs sm:text-sm font-bold flex items-center gap-2 transition bg-[#C81057] text-white shadow-sm";
        document.getElementById('tab3Content').classList.remove('hidden');
        checkLockState();
      }}

      lucide.createIcons();
    }}

    function checkLockState() {{
      const gate = document.getElementById('passwordGate');
      const prot = document.getElementById('protectedData');
      if (isUnlocked) {{
        gate.classList.add('hidden');
        prot.classList.remove('hidden');
        renderTable(data.participants);
      }} else {{
        gate.classList.remove('hidden');
        prot.classList.add('hidden');
      }}
    }}

    function unlockTable(e) {{
      e.preventDefault();
      const val = document.getElementById('pwdInput').value.trim();
      if (val === '2016') {{
        isUnlocked = true;
        sessionStorage.setItem('students_unlocked', 'true');
        document.getElementById('pwdError').classList.add('hidden');
        document.getElementById('pwdInput').value = '';
        checkLockState();
        lucide.createIcons();
      }} else {{
        document.getElementById('pwdError').classList.remove('hidden');
      }}
    }}

    function lockTable() {{
      isUnlocked = false;
      sessionStorage.removeItem('students_unlocked');
      checkLockState();
      lucide.createIcons();
    }}

    function initCharts() {{
      // 1. Radar Chart (Curva de Transferencia)
      const ctxRadar = document.getElementById('radarChart').getContext('2d');
      new Chart(ctxRadar, {{
        type: 'radar',
        data: {{
          labels: ['Innovación', 'Diseño Negocio', 'Digital', 'Circular', 'Liderazgo', 'Tendencias', 'Pitch Day'],
          datasets: [
            {{
              label: 'Ex-ante (Línea Base)',
              data: data.modules_delta.map(m => m.ex_ante),
              borderColor: '#94a3b8',
              backgroundColor: 'rgba(148, 163, 184, 0.2)',
              borderWidth: 2,
              pointBackgroundColor: '#64748b'
            }},
            {{
              label: 'Ex-post (Salida)',
              data: data.modules_delta.map(m => m.ex_post),
              borderColor: '#C81057',
              backgroundColor: 'rgba(200, 16, 87, 0.25)',
              borderWidth: 2.5,
              pointBackgroundColor: '#C81057'
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          scales: {{
            r: {{
              min: 1,
              max: 5,
              ticks: {{ stepSize: 1, backdropColor: 'transparent', font: {{ size: 9 }} }},
              pointLabels: {{ font: {{ size: 9, weight: 'bold' }} }}
            }}
          }},
          plugins: {{
            legend: {{ position: 'top', labels: {{ font: {{ size: 10 }} }} }}
          }}
        }}
      }});

      // 2. Desempeño Demoday por Criterio de Jurados (Horizontal / Grouped Bar)
      const ctxCrit = document.getElementById('projectCriteriaChart').getContext('2d');
      new Chart(ctxCrit, {{
        type: 'bar',
        data: {{
          labels: ['Problema', 'Originalidad', 'Pitch', 'Digital', 'Técnica'],
          datasets: [
            {{
              label: 'Ecoesmart',
              data: [4.00, 3.33, 3.33, 3.00, 3.67],
              backgroundColor: '#10b981',
              borderRadius: 4
            }},
            {{
              label: 'Recompost',
              data: [4.00, 3.33, 3.67, 3.00, 3.33],
              backgroundColor: '#C81057',
              borderRadius: 4
            }},
            {{
              label: 'TecnMin',
              data: [3.33, 2.67, 2.67, 3.00, 2.33],
              backgroundColor: '#F59E0B',
              borderRadius: 4
            }},
            {{
              label: 'Calama Reconstruye',
              data: [2.67, 2.67, 3.00, 2.67, 2.67],
              backgroundColor: '#06B6D4',
              borderRadius: 4
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          scales: {{
            y: {{
              min: 0,
              max: 5,
              ticks: {{ stepSize: 1 }},
              title: {{ display: true, text: 'Escala 1 a 5', font: {{ size: 10 }} }}
            }},
            x: {{
              ticks: {{ font: {{ size: 9, weight: 'bold' }} }}
            }}
          }},
          plugins: {{
            legend: {{ position: 'top', labels: {{ font: {{ size: 9 }} }} }}
          }}
        }}
      }});

      // 3. Comparativa Institucional Limpia (Global vs INACAP vs AIEP)
      const ctxInst = document.getElementById('instCleanChart').getContext('2d');
      new Chart(ctxInst, {{
        type: 'bar',
        data: {{
          labels: ['Global', 'INACAP Sede Calama', 'AIEP Calama'],
          datasets: [
            {{
              label: 'NPS Score',
              data: [data.nps.global.nps_score, data.nps.inacap.nps_score, data.nps.aiep.nps_score],
              backgroundColor: '#C81057',
              borderRadius: 6
            }},
            {{
              label: 'Promedio Ex-post (x20 pts)',
              data: [
                data.nps.global.avg_score * 20,
                data.nps.inacap.avg_score * 20,
                data.nps.aiep.avg_score * 20
              ],
              backgroundColor: '#1B365D',
              borderRadius: 6
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          scales: {{
            y: {{
              beginAtZero: true,
              max: 100,
              ticks: {{ stepSize: 20 }}
            }}
          }},
          plugins: {{
            legend: {{ position: 'top', labels: {{ font: {{ size: 10 }} }} }}
          }}
        }}
      }});
    }}

    function renderTable(list) {{
      const tbody = document.getElementById('participantsTableBody');
      if (!tbody) return;
      tbody.innerHTML = '';

      if (list.length === 0) {{
        tbody.innerHTML = '<tr><td colspan="13" class="py-8 text-center text-slate-400">No se encontraron participantes con el criterio de búsqueda</td></tr>';
        return;
      }}

      list.forEach((p, idx) => {{
        const tr = document.createElement('tr');
        tr.className = idx % 2 === 0 ? 'bg-white hover:bg-slate-50/80 transition' : 'bg-slate-50/50 hover:bg-slate-50/80 transition';

        let badgeClass = 'badge-passive';
        if (p.nps_category === 'Promotor') badgeClass = 'badge-promoter';
        if (p.nps_category === 'Detractor') badgeClass = 'badge-detractor';

        let instBadge = p.institution === 'INACAP' 
          ? '<span class="bg-rose-100 text-rose-800 font-bold px-1.5 py-0.5 rounded text-[10px]">INACAP</span>'
          : '<span class="bg-blue-100 text-blue-800 font-bold px-1.5 py-0.5 rounded text-[10px]">AIEP</span>';

        let typeBadge = p.type.includes('Expositor')
          ? '<span class="text-emerald-700 font-bold bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">Expositor Demoday</span>'
          : '<span class="text-slate-600 bg-slate-100 px-2 py-0.5 rounded">Asistente (Diploma)</span>';

        let openDetailsHtml = '';
        if (p.open_responses && p.open_responses.length > 0) {{
          openDetailsHtml = `
            <details class="text-[11px] text-slate-600 group mt-1">
              <summary class="cursor-pointer text-rose-600 hover:text-rose-800 font-semibold flex items-center gap-1">
                <span>Ver ${{p.open_responses.length}} respuestas abiertas</span>
                <i data-lucide="chevron-down" class="w-3 h-3 transition group-open:rotate-180"></i>
              </summary>
              <div class="mt-1 space-y-1 bg-slate-50 p-2 rounded border border-slate-200">
                ${{p.open_responses.map(or => `
                  <div>
                    <span class="font-bold text-slate-800">${{or.module}}:</span>
                    <span class="italic text-slate-600">"${{or.text}}"</span>
                  </div>
                `).join('')}}
              </div>
            </details>
          `;
        }}

        tr.innerHTML = `
          <td class="py-2.5 px-3 font-bold text-slate-900">${{p.name}}</td>
          <td class="py-2.5 px-2 text-center">${{instBadge}}</td>
          <td class="py-2.5 px-2">${{typeBadge}}</td>
          <td class="py-2.5 px-1.5 text-center font-medium">${{p.m1}}</td>
          <td class="py-2.5 px-1.5 text-center font-medium">${{p.m2}}</td>
          <td class="py-2.5 px-1.5 text-center font-medium">${{p.m3}}</td>
          <td class="py-2.5 px-1.5 text-center font-medium">${{p.m4}}</td>
          <td class="py-2.5 px-1.5 text-center font-medium">${{p.m5}}</td>
          <td class="py-2.5 px-1.5 text-center font-medium">${{p.m6}}</td>
          <td class="py-2.5 px-1.5 text-center font-medium">${{p.m7}}</td>
          <td class="py-2.5 px-2 text-center font-black text-slate-900">${{p.avg_score.toFixed(2)}}</td>
          <td class="py-2.5 px-2 text-center">
            <span class="px-2 py-0.5 rounded-full font-bold text-[10px] ${{badgeClass}}">${{p.nps_category}}</span>
          </td>
          <td class="py-2.5 px-3 text-[11px] text-slate-600 max-w-xs">
            ${{p.obs ? `<div class="text-amber-800 font-medium mb-1">${{p.obs}}</div>` : ''}}
            ${{openDetailsHtml}}
          </td>
        `;
        tbody.appendChild(tr);
      }});

      lucide.createIcons();
    }}

    function applyFilters() {{
      const query = document.getElementById('searchInput').value.toLowerCase().trim();
      let filtered = data.participants.filter(p => {{
        if (query && !p.name.toLowerCase().includes(query)) return false;
        return true;
      }});
      renderTable(filtered);
    }}

    window.onload = function() {{
      initCharts();
      lucide.createIcons();
    }};
  </script>
</body>
</html>
"""

out_html = r"C:\Users\olfor\.gemini\antigravity\scratch\transicion_verde_calama\negocioscirculares\index.html"
with open(out_html, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Updated index.html created.")
