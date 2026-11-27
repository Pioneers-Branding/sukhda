import re

# 1. medicine-and-critical-care.html
with open('medicine-and-critical-care.html', 'r', encoding='utf-8') as f:
    med = f.read()

old_med = '''                <article class="hd-card">
                    <a href="opd-schedule.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp"
                            alt="Dr. Manaswi Gupta - Consultant Physician — Medicine &amp; Critical Care"
                            loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="opd-schedule.html">Dr. Manaswi Gupta</a></h3>
                        <div class="hd-desig">Consultant Physician — Medicine &amp; Critical Care</div>
                        <div class="hd-qual">MBBS, DNB (General Medicine)</div>
                        <div class="hd-actions">
                            <a href="opd-schedule.html" class="hd-btn-profile">View OPD</a>
                            <a href="contact.html" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

new_med = '''                <article class="hd-card">
                    <a href="dr-manaswi-gupta.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp"
                            alt="Dr. Manaswi Gupta - Consultant Physician — Medicine &amp; Critical Care"
                            loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="dr-manaswi-gupta.html">Dr. Manaswi Gupta</a></h3>
                        <div class="hd-desig">Consultant Physician — Medicine &amp; Critical Care</div>
                        <div class="hd-qual">MBBS, MD (General Medicine), FICE</div>
                        <div class="hd-actions">
                            <a href="dr-manaswi-gupta.html" class="hd-btn-profile">View Profile</a>
                            <a href="contact.html?doctor=dr-manaswi-gupta" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

assert old_med in med, "old_med not found in medicine-and-critical-care.html"
med = med.replace(old_med, new_med)
with open('medicine-and-critical-care.html', 'w', encoding='utf-8') as f:
    f.write(med)
print("Updated medicine-and-critical-care.html")


# 2. sukhda-multispecialty-hospital.html
with open('sukhda-multispecialty-hospital.html', 'r', encoding='utf-8') as f:
    multi = f.read()

old_multi = '''                <article class="hd-card">
                    <a href="opd-schedule.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp"
                            alt="Dr. Manaswi Gupta - Associate Consultant — Internal Medicine" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="opd-schedule.html">Dr. Manaswi Gupta</a></h3>
                        <div class="hd-desig">Associate Consultant — Internal Medicine</div>
                        <div class="hd-qual">MBBS, DNB (General Medicine)</div>
                        <div class="hd-actions">
                            <a href="opd-schedule.html" class="hd-btn-profile">View OPD</a>
                            <a href="contact.html" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

new_multi = '''                <article class="hd-card">
                    <a href="dr-manaswi-gupta.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp"
                            alt="Dr. Manaswi Gupta - Consultant Physician — Medicine &amp; Critical Care" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="dr-manaswi-gupta.html">Dr. Manaswi Gupta</a></h3>
                        <div class="hd-desig">Consultant Physician — Medicine &amp; Critical Care</div>
                        <div class="hd-qual">MBBS, MD (General Medicine), FICE</div>
                        <div class="hd-actions">
                            <a href="dr-manaswi-gupta.html" class="hd-btn-profile">View Profile</a>
                            <a href="contact.html?doctor=dr-manaswi-gupta" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

assert old_multi in multi, "old_multi not found in sukhda-multispecialty-hospital.html"
multi = multi.replace(old_multi, new_multi)
with open('sukhda-multispecialty-hospital.html', 'w', encoding='utf-8') as f:
    f.write(multi)
print("Updated sukhda-multispecialty-hospital.html")


# 3. sukhda-medpark-hospital.html
with open('sukhda-medpark-hospital.html', 'r', encoding='utf-8') as f:
    medpark = f.read()

old_medpark = '''                <article class="hd-card">
                    <a href="opd-schedule.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp"
                            alt="Dr. Manaswi Gupta - Associate Consultant — Internal Medicine" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="opd-schedule.html">Dr. Manaswi Gupta</a></h3>
                        <div class="hd-desig">Associate Consultant — Internal Medicine</div>
                        <div class="hd-qual">MBBS, DNB (General Medicine)</div>
                        <div class="hd-actions">
                            <a href="opd-schedule.html" class="hd-btn-profile">View OPD</a>
                            <a href="contact.html" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

new_medpark = '''                <article class="hd-card">
                    <a href="dr-manaswi-gupta.html" class="hd-photo">
                        <img src="assets/images/doctors/latest/dr-manaswi-gupta.webp"
                            alt="Dr. Manaswi Gupta - Consultant Physician — Medicine &amp; Critical Care" loading="lazy">
                    </a>
                    <div class="hd-body">
                        <h3><a href="dr-manaswi-gupta.html">Dr. Manaswi Gupta</a></h3>
                        <div class="hd-desig">Consultant Physician — Medicine &amp; Critical Care</div>
                        <div class="hd-qual">MBBS, MD (General Medicine), FICE</div>
                        <div class="hd-actions">
                            <a href="dr-manaswi-gupta.html" class="hd-btn-profile">View Profile</a>
                            <a href="contact.html?doctor=dr-manaswi-gupta" class="hd-btn-book">Book OPD</a>
                        </div>
                    </div>
                </article>'''

assert old_medpark in medpark, "old_medpark not found in sukhda-medpark-hospital.html"
medpark = medpark.replace(old_medpark, new_medpark)
with open('sukhda-medpark-hospital.html', 'w', encoding='utf-8') as f:
    f.write(medpark)
print("Updated sukhda-medpark-hospital.html")
