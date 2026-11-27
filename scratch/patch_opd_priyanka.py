with open('opd-schedule.html', 'r', encoding='utf-8') as f:
    opd = f.read()

old_block = '''                        <tr class="opd-row" data-doctor="dr-priyanka-chhabra" data-category="others"
                            data-days="Monday,Tuesday,Wednesday,Thursday,Friday,Saturday"
                            data-search="dr. priyanka chhabra mbbs, dmrd (radiology) · consultant – radiology radiodiagnosis &amp; imaging sukhda medpark monday tuesday wednesday thursday friday saturday">
                            <td style="color:var(--muted);font-weight:700;">17</td>
                            <td>
                                <div class="doc-cell">
                                    <span class="opd-doc-name">Dr. Priyanka Chhabra</span>
                                    <span class="opd-doc-qual">DMRD (Radiology) · Consultant – Radiology</span>
                                </div>
                            </td>
                            <td>
                                <div class="dept-cell">
                                    <a href="radiodiagnosis-and-imaging.html" class="opd-dept-link">Radiodiagnosis &amp; Imaging</a>
                                    <a href="sukhda-medpark-hospital.html" class="hospital-tag"><i
                                            data-lucide="building" style="width:11px;height:11px"></i> Sukhda
                                        MedPark</a>
                                </div>
                            </td>
                            <td>
                                <span class="days-badge">Mon – Sat</span>
                            </td>
                            <td>
                                <div class="time-slots">
                                    <span class="time-pill morning"><i data-lucide="phone-call"
                                            style="width:12px;height:12px"></i> Timings: please call the OPD desk</span>
                                </div>
                            </td>
                            <td>
                                <span class="status-badge available" data-status-badge><i data-lucide="check-circle"
                                        style="width:11px;height:11px"></i> Doctor Available</span>
                            </td>
                            <td style="text-align: right;">
                                <div class="action-btns" style="justify-content: flex-end;">
                                    <a href="contact.html" class="btn-book-opd"><i data-lucide="calendar"></i> Book</a>
                                </div>
                            </td>
                        </tr>'''

new_block = '''                        <tr class="opd-row" data-doctor="dr-priyanka-chhabra" data-category="others"
                            data-days="Monday,Tuesday,Wednesday,Thursday,Friday,Saturday"
                            data-search="dr. priyanka chhabra mbbs, dmrd, edir, dicri · senior consultant radiologist &amp; director radiodiagnosis &amp; imaging sukhda medpark monday tuesday wednesday thursday friday saturday">
                            <td style="color:var(--muted);font-weight:700;">17</td>
                            <td>
                                <div class="doc-cell">
                                    <a href="dr-priyanka-chhabra.html" class="opd-doc-name" style="color:var(--blue);text-decoration:none;font-weight:700;">Dr. Priyanka Chhabra</a>
                                    <span class="opd-doc-qual">MBBS, DMRD, EDiR, DICRI · Senior Consultant Radiologist &amp; Director</span>
                                </div>
                            </td>
                            <td>
                                <div class="dept-cell">
                                    <a href="radiodiagnosis-and-imaging.html" class="opd-dept-link">Radiodiagnosis &amp; Imaging</a>
                                    <a href="sukhda-medpark-hospital.html" class="hospital-tag"><i
                                            data-lucide="building" style="width:11px;height:11px"></i> Sukhda
                                        MedPark</a>
                                </div>
                            </td>
                            <td>
                                <span class="days-badge">Mon – Sat</span>
                            </td>
                            <td>
                                <div class="time-slots">
                                    <span class="time-pill morning"><i data-lucide="phone-call"
                                            style="width:12px;height:12px"></i> Timings: please call the OPD desk</span>
                                </div>
                            </td>
                            <td>
                                <span class="status-badge available" data-status-badge><i data-lucide="check-circle"
                                        style="width:11px;height:11px"></i> Doctor Available</span>
                            </td>
                            <td style="text-align: right;">
                                <div class="action-btns" style="justify-content: flex-end;">
                                    <a href="dr-priyanka-chhabra.html" class="btn-book-opd" style="background:#eaf1f8;color:var(--blue);margin-right:6px;"><i data-lucide="user"></i> Profile</a>
                                    <a href="contact.html?doctor=dr-priyanka-chhabra" class="btn-book-opd"><i data-lucide="calendar"></i> Book</a>
                                </div>
                            </td>
                        </tr>'''

assert old_block in opd, "old_block not found in opd-schedule.html"
opd = opd.replace(old_block, new_block)
with open('opd-schedule.html', 'w', encoding='utf-8') as f:
    f.write(opd)

print("SUCCESS: Updated opd-schedule.html")
