<div id="top" align="center">
  <img src="/Polytechnic_University_of_the_Philippines_Quezon_City_Logo.svg.png" alt="PUP IMS Logo" width="150"/>

<div align="center">
  <h1>Academic Analytics Lite</h1>
  <p class="lead">
    A lightweight Python pipeline for processing student performance data — array-first, modular, and easy to configure.
  </p>
  <div class="badges" style="margin-top:8px" align="center">
    <img src="https://img.shields.io/badge/Python%203.8%2B-white?style=for-the-badge&logo=python" alt="Badge">
    <img src="https://img.shields.io/badge/License-Academic-white?style=for-the-badge&labelColor=blue" alt="license">
    <img src="https://img.shields.io/badge/Status%3A%20v1.0-blue?style=for-the-badge" alt="Badge">
  </div>
</div>

<h2 align="center">Overview</h2>
<p align="center"> 
  This project ingests CSV data exported from an LMS, applies array-based transformations and analytics, and produces instructor-facing reports: grade distributions, per-section exports, and at-risk lists. It favors plain Python data structures (lists, dicts) and JSON configuration, with an optional NumPy-accelerated mode.
</p>

<section class="card" align="center">
<h2>Key Features</h2>
<ul align="right" style="list-style-position: inside; padding-left: 0; margin-left: 0; text-align: left; display: inline-block;"> 
  <li>CSV ingestion & validation (handles missing/invalid fields)</li>
  <li>Array operations: select, project, sort, insert, delete</li>
  <li>Analytics: weighted grades, letter mapping, percentiles, outliers</li>
  <li>Export reports per-section and at-risk students as CSV</li>
  <li>Configurable via <code>config.json</code></li>
  <li>Unit tests and timing for performance checks</li>
  <li>Stretch: CLI menu and NumPy version</li>
</ul>
</section>

<section class="card" align="center">
<h2>Prerequisites & Setup</h2>
<div align="center">
  <table style="width: 600px; border-collapse: collapse; margin-top: 10px; font-size: 15px;">
    <tr>
      <td align="center" style="width: 48px;">1️⃣</td>
      <td>
        <strong>Python 3.8+</strong><br>
        Required to run all scripts.
      </td>
    </tr>
    <tr>
      <td align="center">2️⃣</td>
      <td>
        <strong>NumPy (optional)</strong><br>
        <code>pip install numpy</code> for NumPy-accelerated mode.
      </td>
    </tr>
    <tr>
      <td align="center">3️⃣</td>
      <td>
        <strong>Project ZIP file</strong><br>
        <em>DSA-CASE STUDY-GROUP7-BSIT 2-2.zip</em> — contains all source files, config, and data.
      </td>
    </tr>
    <tr>
      <td align="center">4️⃣</td>
      <td>
        <strong>Unzip & Configure</strong><br>
        Unzip the project into your workspace and edit <code>config.json</code> for weights, thresholds, and paths.
      </td>
    </tr>
  </table>
</div>
</section>

<section class="card" align="center">
<h2>Usage Instructions</h2>
<div align="center">
  <table style="width: 600px; border-collapse: collapse; margin-top: 24px; justify-content: center; font-size: 15px;">
    <tr>
      <td align="center" style="width: 48px;">1️⃣</td>
      <td>
        <strong>Run the main script</strong><br>
        <pre><code>python src/main.py</code></pre>
        Outputs include per-section CSVs and <code>at_risk.csv</code> in the <code>output/</code> folder.
      </td>
    </tr>
  </table>
</div>
</section>

<section class="card">
<h3>Project Structure</h3>
<pre><code>
Academic-Analytics-Lite/
├── 📁 pycache/ # Compiled Python bytecode files
│ ├── analyze.cpython-313.pyc
│ ├── ingest.cpython-313.pyc
│ ├── reports.cpython-313.pyc
│ └── transform.cpython-313.pyc
│
├── 📁 output_reports/ # Generated CSV reports
│ ├── at_risk_students.csv
│ ├── section_a.csv
│ ├── section_b.csv
│ └── section_c.csv
│
├── 📁 src/ # Core Python source files
│ ├── analyze.py # Handles data analysis and computations
│ ├── ingest.py # Reads and loads input data
│ ├── main.py # Main program execution
│ ├── reports.py # Generates reports and summaries
│ └── transform.py # Processes and transforms data
│
├── ⚙️ config.json # Configuration file (weights, thresholds, paths)
├── 🖼️ cs-output.png # Output visualization
├── 🖼️ csv.PNG # CSV file reference or sample screenshot
├── 📄 input.csv # Input dataset
├── 🏫 Polytechnic_University_of_the_Philippines_Quezon_City.png # School logo
└── 📘 README.md # Documentation file
</code></pre>
</section>

<section class="card">
<h3>Sample <code>config.json</code></h3>
<pre><code>
{
  "weights": {
    "quizzes": 0.2,
    "midterm": 0.3,
    "final": 0.3,
    "attendance": 0.2
  },
  "at_risk_threshold": 75
}
</code></pre>
</section>

<section class="card columns">
<div>
<h2>Complexity & Performance</h2>
<table style="width: 600px; border-collapse: collapse; margin-top: 30px; justify-content: center;">
<thead><tr><th>Stage</th><th>Time</th><th>Space</th></tr></thead>
<tbody>
<tr><td>Ingestion</td><td>O(N)</td><td>O(N)</td></tr>
<tr><td>Sorting</td><td>O(N log N)</td><td>O(N)</td></tr>
<tr><td>Analytics</td><td>O(N)</td><td>O(N)</td></tr>
<tr><td>Outlier Detection</td><td>O(N²) worst-case</td><td>O(N)</td></tr>
</tbody>
</table>
<p class="muted">NumPy mode vectorizes many computations and yields significant speedups for large datasets.</p>
</div>
<div>

<section class="card">
<h2>Input Format</h2>
<p>CSV columns expected:</p>
<pre>student_id,last_name,first_name,section,quiz1,...,quiz5,midterm,final,attendance_percent</pre>
<p class="muted">Scores should be 0–100; missing numeric values will be treated as <code>null</code> and handled by validation logic.</p>
</section>

<section class="card">
<h2>Screenshots / Demo (placeholders)</h2>
<div class="columns">
<div class="screenshot">CLI Summary Output</div>
<img src="/cs-output.png" alt="CS-Output"/>
<div class="screenshot">Per-section CSV Preview</div>
<img src="/csv.PNG" alt="CSV Preview"/>
</div>
</section>

<div align="center">
  <h3>BSIT 2-2 S.Y. 2025-2026 Group 7</h3>
  <p>Polytechnic University of the Philippines - Quezon City</p>
  <section class="card" align="center" style="padding:1rem;">
  <p>🌟 <b>Trish Anne Adoray</b></p>
  <p>🎨 <b>Chini Drew Ante</b></p>
  <p>📊 <b>Paul John Delloro</b></p>
  <p>⚙️ <b>John Andrew General</b></p>
  <p>📝 <b>Sena Alondra Gutierrez</b></p>
  <p>🧩 <b>Jems Vin Rhestie Petallo</b></p>
</section>
  
<section class="card" align="center" style="; color:#1a1a1a; padding:20px; border-radius:12px; max-width:800px; margin:auto; ">
<h2>Key Takeaways</h2>
<ul style="text-align:left; padding-left:20px;">
<li><strong style="color:#0d47a1;">Programming & Skills:</strong> Applied Python, handled modules, data ingestion, and visualization; improved problem-solving, debugging, and coding practices.</li>
<li><strong style="color:#0d47a1;">Teamwork & Collaboration:</strong> Learned to communicate, understand teammates’ logic, and integrate work effectively.</li>
<li><strong style="color:#0d47a1;">Personal Growth:</strong> Built patience, resilience, and resourcefulness; realized programming is continuous learning.</li>
<li><strong style="color:#0d47a1;">Practical Application:</strong> Gained knowledge applicable to real-life situations and future projects.</li>
</ul>
</section>

  
<footer>
<p>Academic Analytics Lite — v1.0 &middot; Author: Data Structures and Algorithms Team (BSIT2-2 - GROUP 7)</p>
</footer>
