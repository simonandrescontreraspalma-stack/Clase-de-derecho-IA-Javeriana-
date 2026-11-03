/* ==========================================================================
   CONTRATO CHECK  Core JavaScript & Legal Rule Engine
   Pontificia Universidad Javeriana · 2026-II
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {

    // DOM Elements
    const contractForm = document.getElementById('contract-form');
    const contractType = document.getElementById('contract-type');
    const contractText = document.getElementById('contract-text');
    const btnLoadSample = document.getElementById('btn-load-sample');
    const btnAnalyze = document.getElementById('btn-analyze');

    const emptyState = document.getElementById('empty-state');
    const loadingState = document.getElementById('loading-state');
    const analysisContent = document.getElementById('analysis-content');

    const riskLevelBadge = document.getElementById('risk-level-badge');
    const riskScoreValue = document.getElementById('risk-score-value');
    const riskScoreText = document.getElementById('risk-score-text');

    const statCriticalCount = document.getElementById('stat-critical-count');
    const statWarningCount = document.getElementById('stat-warning-count');
    const statMissingCount = document.getElementById('stat-missing-count');

    const findingsList = document.getElementById('findings-list');
    const recommendationsList = document.getElementById('recommendations-list');

    // --------------------------------------------------------------------------
    // Sample Contract with Real Legal Risks (Arrendamiento)
    // --------------------------------------------------------------------------
    const sampleContractText = `CONTRATO DE ARRENDAMIENTO DE VIVIENDA URBANA

Entre los suscritos a saber: MARÍA GÓMEZ, mayor de edad, identificada con C.C. 1.098.765.432, denominada el ARRENDADOR, y JUAN PÉREZ, identificado con C.C. 1.012.345.678, denominado el ARRENDATARIO, se celebra el presente contrato sujeto a las siguientes cláusulas:

PRIMERA. OBJETO: El ARRENDADOR entrega en arrendamiento al ARRENDATARIO el inmueble ubicado en la Calle 45 # 12-34 Apto 301 de la ciudad de Bogotá D.C.

SEGUNDA. CANON DE ARRENDAMIENTO Y REAJUSTE: El canon mensual será de DOS MILLONES DE PESOS ($2.000.000 COP). Al finalizar cada 12 meses, el arrendador podrá incrementar unilateralmente el canon en un VEINTE POR CIENTO (20%), independientemente de la inflación o el IPC oficial.

TERCERA. DEPÓSITO EN GARANTÍA EN DINERO: Para garantizar el cumplimiento de las obligaciones del presente contrato, el ARRENDATARIO entregará al momento de la firma la suma en efectivo de TRES MILLONES DE PESOS ($3.000.000 COP) en calidad de depósito en dinero en efectivo. Dicho depósito no devengará intereses y será devuelto si el arrendador lo considera conveniente.

CUARTA. MANTENIMIENTO Y REPARACIONES: El ARRENDATARIO asume la totalidad de las reparaciones del inmueble, incluidas las reparaciones locativas, estructurales, tuberías internas y vicios ocultos de construcción. El ARRENDADOR queda totalmente exonerado de cualquier mantenimiento.

QUINTA. TERMINACIÓN E INDEMNIZACIÓN: El ARRENDADOR podrá solicitar la restitución inmediata del inmueble en cualquier momento sin necesidad de dar preaviso alguno ni justificar causal alguna. En caso de mora de 1 solo día en el pago, el arrendatario pagará una sanción equivalente a CINCO CANONES mensuales.

SEXTA. CESIÓN: Queda totalmente prohibida la subarrienda o cesión del inmueble.

Firmado en Bogotá D.C. a los 10 días del mes de agosto de 2026.`;

    // Load sample text when clicking the action button
    btnLoadSample.addEventListener('click', () => {
        contractType.value = 'arrendamiento';
        contractText.value = sampleContractText;
        contractText.focus();
    });

    // --------------------------------------------------------------------------
    // Form Submission & Analysis Handler
    // --------------------------------------------------------------------------
    contractForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const text = contractText.value.trim();
        const type = contractType.value;

        if (!text) {
            alert('Por favor pega el texto de un contrato antes de analizar.');
            return;
        }

        // Show Loading State
        emptyState.classList.add('hidden');
        analysisContent.classList.add('hidden');
        loadingState.classList.remove('hidden');

        // Simulate analysis scan latency (1.5 seconds)
        setTimeout(() => {
            const results = analyzeContractText(text, type);
            renderAnalysisResults(results);

            loadingState.classList.add('hidden');
            analysisContent.classList.remove('hidden');
        }, 1200);
    });

    // --------------------------------------------------------------------------
    // Colombian Legal Rule Engine (Normative Scanner)
    // --------------------------------------------------------------------------
    function analyzeContractText(text, type) {
        const textLower = text.toLowerCase();
        const findings = [];
        const recommendations = [];

        let criticalCount = 0;
        let warningCount = 0;
        let missingCount = 0;

        // RULE 1: Depósito en dinero en efectivo (Prohibido por Ley 820 de 2003)
        if (type === 'arrendamiento') {
            if (textLower.includes('depósito') && (textLower.includes('dinero') || textLower.includes('efectivo') || textLower.includes('suma'))) {
                criticalCount++;
                findings.push({
                    type: 'critical',
                    title: '🚨 Depósito en dinero prohibido por ley',
                    quote: 'Exigencia de depósito en dinero o efectivo para garantizar el contrato.',
                    citation: 'Ley 820 de 2003 — Artículo 16: "En los contratos de arrendamiento de vivienda urbana no se podrán exigir depósitos en dinero o garantías reales para garantizar el cumplimiento..."',
                    explanation: 'En vivienda urbana está expresamente prohibido por ley exigir depósitos en dinero al arrendatario. Esta cláusula es ineficaz y nula de pleno derecho.'
                });
                recommendations.push('Exige la eliminación inmediata del depósito en dinero. En su lugar, el arrendador puede solicitar póliza de arrendamiento o fiador.');
            }
        }

        // RULE 2: Reajuste del canon superior al IPC
        if (type === 'arrendamiento') {
            if (textLower.includes('reajuste') || textLower.includes('incrementar') || textLower.includes('incremento') || textLower.includes('aumento')) {
                if (textLower.includes('20%') || textLower.includes('15%') || textLower.includes('30%') || textLower.includes('independientemente de la inflación') || textLower.includes('sin tener en cuenta el ipc')) {
                    criticalCount++;
                    findings.push({
                        type: 'critical',
                        title: '🚨 Incremento de canon superior al límite legal (IPC)',
                        quote: 'Aumento unilateral superior al índice de precios al consumidor (IPC).',
                        citation: 'Ley 820 de 2003 — Artículo 20: "Cada doce meses de ejecución del contrato... el arrendador podrá reajustar el canon en un porcentaje que no podrá ser superior al 100% del incremento que haya tenido el Índice de Precios al Consumidor (IPC)..."',
                        explanation: 'El arrendador NO puede fijar arbitrariamente un % fijo (ej. 20%) superior al IPC determinado por el DANE para el año anterior.'
                    });
                    recommendations.push('Solicita ajustar la cláusula de reajuste para que quede expresamente limitada al 100% del IPC acumulado del año anterior.');
                }
            }
        }

        // RULE 3: Exoneración de reparaciones estructurales y vicios ocultos
        if (textLower.includes('exonerado') || textLower.includes('estructurales') || textLower.includes('vicios ocultos') || textLower.includes('totalidad de las reparaciones')) {
            warningCount++;
            findings.push({
                type: 'warning',
                title: '⚠️ Exoneración desproporcionada de reparaciones necesarias',
                quote: 'El arrendatario/contratista asume reparaciones estructurales o locativas necesarias.',
                citation: 'Código Civil Colombiano — Artículo 1985 & Ley 820 de 2003: El arrendador está obligado a realizar las reparaciones necesarias no locativas indispensables para el uso.',
                explanation: 'Transferir la responsabilidad de mantenimientos estructurales o vicios de construcción al arrendatario rompe el equilibrio del contrato.'
            });
            recommendations.push('Aclara que las reparaciones locativas derivadas del uso normal corresponden al usuario, pero las estructurales y de tuberías internas son obligación del propietario.');
        }

        // RULE 4: Ausencia de Preaviso de Terminación
        if (textLower.includes('sin necesidad de dar preaviso') || textLower.includes('inmediata') || textLower.includes('en cualquier momento')) {
            criticalCount++;
            findings.push({
                type: 'critical',
                title: '🚨 Terminación sin preaviso legal',
                quote: 'Restitución inmediata sin previo aviso ni causal.',
                citation: 'Ley 820 de 2003 — Artículos 22 y 24: La terminación unilateral por el arrendador exige preaviso escrito no menor a tres (3) meses.',
                explanation: 'La ley exige otorgar un término mínimo de 3 meses de anticipación con las indemnizaciones legales si no hay causal de incumplimiento.'
            });
            recommendations.push('Establece que cualquier intención de terminación debe notificarse por escrito con al menos 3 meses de anticipación.');
        }

        // RULE 5: Cláusula Penal Excesiva
        if (textLower.includes('sanción equivalente a cinco') || textLower.includes('5 canones') || textLower.includes('cláusula penal')) {
            warningCount++;
            findings.push({
                type: 'warning',
                title: '⚠️ Cláusula penal desproporcionada',
                quote: 'Multa o sanción por mora o incumplimiento excesivamente elevada.',
                citation: 'Código Civil — Artículo 1601: La cláusula penal enorme puede ser reducida judicialmente si excede el duplo de la obligación principal.',
                explanation: 'Una penalidad de 5 cánones por un retraso de 1 día es abusiva y desproporcionada ante los estrados judiciales.'
            });
            recommendations.push('Negocia fijar la cláusula penal en máximo 1 o 2 cánones de arrendamiento previa constitución en mora.');
        }

        // CHECK FOR MISSING ESSENTIAL CLAUSES
        if (!textLower.includes('inventario')) {
            missingCount++;
            findings.push({
                type: 'missing',
                title: 'ℹ️ Ausencia de acta de inventario inicial',
                quote: 'No se menciona la elaboración de un inventario detallado del estado del bien.',
                citation: 'Código Civil — Artículo 1996 / Buenas prácticas contractuales',
                explanation: 'Al no incluir un inventario con fotos y estado inicial de servicios públicos, pueden cobrarte daños inexistentes al entregar.'
            });
            recommendations.push('Exige adjuntar un Anexo de Inventario firmado donde conste el estado de muros, pisos y servicios.');
        }

        if (!textLower.includes('servicios públicos')) {
            missingCount++;
            findings.push({
                type: 'missing',
                title: 'ℹ️ Claridad en pago de servicios públicos',
                quote: 'Falta especificación explícita sobre quién asume los recibos de servicios.',
                citation: 'Ley 820 de 2003 — Artículo 15',
                explanation: 'Debe especificarse el pago de acueducto, energía, gas e internet para evitar cortes o cobros extemporáneos.'
            });
        }

        // Fallback default finding if text is too generic
        if (findings.length === 0) {
            findings.push({
                type: 'warning',
                title: '✔️ No se detectaron cláusulas evidentemente ilegales',
                quote: 'Texto dentro de los parámetros contractuales generales.',
                citation: 'Autonomía de la Voluntad (Código Civil — Art. 1602)',
                explanation: 'Recuerda revisar de forma detallada nombres de las partes, valor exacto en números/letras y fechas de pago.'
            });
            recommendations.push('Verifica la identidad del propietario mediante Certificado de Libertad y Tradición reciente antes de realizar abonos.');
        }

        // Calculate Overall Risk Score
        let riskScore = (criticalCount * 35) + (warningCount * 15) + (missingCount * 8);
        if (riskScore > 100) riskScore = 98;
        if (riskScore === 0 && findings.length > 0) riskScore = 15;

        return {
            riskScore,
            criticalCount,
            warningCount,
            missingCount,
            findings,
            recommendations
        };
    }

    // --------------------------------------------------------------------------
    // Render Results in UI
    // --------------------------------------------------------------------------
    function renderAnalysisResults(results) {
        // Render Score & Stats
        riskScoreValue.textContent = `${results.riskScore}%`;
        
        statCriticalCount.textContent = results.criticalCount;
        statWarningCount.textContent = results.warningCount;
        statMissingCount.textContent = results.missingCount;

        // Set Risk Level Badge & Score Text
        if (results.riskScore >= 60) {
            riskLevelBadge.textContent = '🚨 RIESGO ALTO';
            riskLevelBadge.className = 'badge badge-danger';
            riskScoreText.textContent = 'Requiere ajustes urgentes antes de firmar';
            riskScoreValue.className = 'stat-value text-danger';
        } else if (results.riskScore >= 25) {
            riskLevelBadge.textContent = '⚠️ RIESGO MEDIO';
            riskLevelBadge.className = 'badge badge-warning';
            riskScoreText.textContent = 'Contiene cláusulas ambiguas o desfavorables';
            riskScoreValue.className = 'stat-value text-warning';
        } else {
            riskLevelBadge.textContent = '🟢 RIESGO BAJO';
            riskLevelBadge.className = 'badge badge-success';
            riskScoreText.textContent = 'Contrato equilibrado en líneas generales';
            riskScoreValue.className = 'stat-value text-success';
        }

        // Render Findings List
        findingsList.innerHTML = '';
        results.findings.forEach(item => {
            const findingEl = document.createElement('div');
            findingEl.className = `finding-item ${item.type}`;
            
            findingEl.innerHTML = `
                <div class="finding-header">
                    <span class="finding-title">${item.title}</span>
                </div>
                <p style="font-size: 0.88rem; margin-top: 4px;">${item.explanation}</p>
                <div class="finding-quote">"${item.quote}"</div>
                <div class="finding-citation">📌 <strong>Fuente Jurídica:</strong> ${item.citation}</div>
            `;
            findingsList.appendChild(findingEl);
        });

        // Render Recommendations List
        recommendationsList.innerHTML = '';
        results.recommendations.forEach(rec => {
            const li = document.createElement('li');
            li.textContent = rec;
            recommendationsList.appendChild(li);
        });
    }

});
