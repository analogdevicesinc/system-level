"use strict"

const referenceDesigns = "By using the evaluation board discussed herein (together with any tools, components documentation or support materials, the \"Evaluation Board\"), you are agreeing to be bound by the terms and conditions set forth below (\"Agreement\") unless you have purchased the Evaluation Board, in which case the Analog Devices Standard Terms and Conditions of Sale shall govern. Do not use the Evaluation Board until you have read and agreed to the Agreement. Your use of the Evaluation Board shall signify your acceptance of the Agreement. This Agreement is made by and between you (\"Customer\") and Analog Devices, Inc. (\"ADI\"), with its principal place of business at One Technology Way, Norwood, MA 02062, USA. Subject to the terms and conditions of the Agreement, ADI hereby grants to Customer a free, limited, personal, temporary, non-exclusive, non-sublicensable, non-transferable license to use the Evaluation Board FOR EVALUATION PURPOSES ONLY. Customer understands and agrees that the Evaluation Board is provided for the sole and exclusive purpose referenced above, and agrees not to use the Evaluation Board for any other purpose. Furthermore, the license granted is expressly made subject to the following additional limitations: Customer shall not (i) rent, lease, display, sell, transfer, assign, sublicense, or distribute the Evaluation Board; and (ii) permit any Third Party to access the Evaluation Board. As used herein, the term \"Third Party\" includes any entity other than ADI, Customer, their employees, affiliates and in-house consultants. The Evaluation Board is NOT sold to Customer; all rights not expressly granted herein, including ownership of the Evaluation Board, are reserved by ADI. CONFIDENTIALITY. This Agreement and the Evaluation Board shall all be considered the confidential and proprietary information of ADI. Customer may not disclose or transfer any portion of the Evaluation Board to any other party for any reason. Upon discontinuation of use of the Evaluation Board or termination of this Agreement, Customer agrees to promptly return the Evaluation Board to ADI. ADDITIONAL RESTRICTIONS. Customer may not disassemble, decompile or reverse engineer chips on the Evaluation Board. Customer shall inform ADI of any occurred damages or any modifications or alterations it makes to the Evaluation Board, including but not limited to soldering or any other activity that affects the material content of the Evaluation Board. Modifications to the Evaluation Board must comply with applicable law, including but not limited to the RoHS Directive. TERMINATION. ADI may terminate this Agreement at any time upon giving written notice to Customer. Customer agrees to return to ADI the Evaluation Board at that time. LIMITATION OF LIABILITY. THE EVALUATION BOARD PROVIDED HEREUNDER IS PROVIDED \"AS IS\" AND ADI MAKES NO WARRANTIES OR REPRESENTATIONS OF ANY KIND WITH RESPECT TO IT. ADI SPECIFICALLY DISCLAIMS ANY REPRESENTATIONS, ENDORSEMENTS, GUARANTEES, OR WARRANTIES, EXPRESS OR IMPLIED, RELATED TO THE EVALUATION BOARD INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTY OF MERCHANTABILITY, TITLE, FITNESS FOR A PARTICULAR PURPOSE OR NONINFRINGEMENT OF INTELLECTUAL PROPERTY RIGHTS. IN NO EVENT WILL ADI AND ITS LICENSORS BE LIABLE FOR ANY INCIDENTAL, SPECIAL, INDIRECT, OR CONSEQUENTIAL DAMAGES RESULTING FROM CUSTOMER'S POSSESSION OR USE OF THE EVALUATION BOARD, INCLUDING BUT NOT LIMITED TO LOST PROFITS, DELAY COSTS, LABOR COSTS OR LOSS OF GOODWILL. ADI'S TOTAL LIABILITY FROM ANY AND ALL CAUSES SHALL BE LIMITED TO THE AMOUNT OF ONE HUNDRED US DOLLARS ($100.00). EXPORT. Customer agrees that it will not directly or indirectly export the Evaluation Board to another country, and that it will comply with all applicable United States federal laws and regulations relating to exports. GOVERNING LAW. This Agreement shall be governed by and construed in accordance with the substantive laws of the Commonwealth of Massachusetts (excluding conflict of law rules). Any legal action regarding this Agreement will be heard in the state or federal courts having jurisdiction in Suffolk County, Massachusetts, and Customer hereby submits to the personal jurisdiction and venue of such courts. The United Nations Convention on Contracts for the International Sale of Goods shall not apply to this Agreement and is expressly disclaimed."
const circuitsFromTheLab = "Circuits from the Lab® reference designs from Analog Devices have been designed and built by Analog Devices engineers. Standard engineering practices have been employed in the design and construction of each circuit, and their function and performance have been tested and verified in a lab environment at room temperature. However, you are solely responsible for testing the circuit and determining its suitability and applicability for your use and application. Accordingly, in no event shall Analog Devices be liable for direct, indirect, special, incidental, consequential or punitive damages due to any cause whatsoever connected to the use of any Circuits from the Lab circuits. Circuits from the Lab reference designs are intended only for use with Analog Devices products and are the intellectual property of Analog Devices or its licensors. While you may use the Circuits from the Lab reference designs in the design of your product, no other license is granted by implication or otherwise under any patents or other intellectual property by application or use of the Circuits from the Lab reference designs. Information furnished by Analog Devices is believed to be accurate and reliable. However, Circuits from the Lab reference designs are supplied \"as is\" and without warranties of any kind, express, implied, or statutory including, but not limited to, any implied warranty of merchantability, noninfringement or fitness for a particular purpose and no responsibility is assumed by Analog Devices for their use, nor for any infringements of patents or other rights of third parties that may result from their use. Analog Devices reserves the right to change any Circuits from the Lab reference designs at any time without notice but is under no obligation to do so."

let active = false

function addLegalese() {
  if (!active) return
  const body = document.querySelector('.documentwrapper .body')
  if (!body) return

  const page = new URL(window.location.href)
  const siteRoot = new URL(window.app.state.content_root, page)
  if (!page.pathname.startsWith(siteRoot.pathname)) return
  let docname = decodeURIComponent(page.pathname.slice(siteRoot.pathname.length))
  if (docname.endsWith('/')) docname += 'index.html'
  const prefixes = [
    ['solutions/reference-designs/', referenceDesigns],
    ['solutions/circuit-from-the-lab/', circuitsFromTheLab],
  ]
  const text = prefixes.find(([prefix]) => docname.startsWith(prefix) ||
    docname.startsWith('system-level/' + prefix))?.[1]
  if (!text || body.querySelector('#legal-terms-and-conditions')) return

  const section = document.createElement('section')
  section.id = 'legal-terms-and-conditions'
  section.className = 'legalese'
  const title = document.createElement('h2')
  title.textContent = 'Legal Terms and Conditions'
  const headerlink = document.createElement('a')
  headerlink.className = 'headerlink'
  headerlink.href = '#legal-terms-and-conditions'
  headerlink.title = 'Link to this heading'
  title.append(headerlink)
  const paragraph = document.createElement('p')
  paragraph.textContent = text
  section.append(title, paragraph)
  body.append(section)

  const toc = document.querySelector('.localtoc nav > ul')
  if (toc) {
    const item = document.createElement('li')
    const link = document.createElement('a')
    link.className = 'reference internal'
    link.href = '#legal-terms-and-conditions'
    link.textContent = 'Legal Terms and Conditions'
    link.tabIndex = document.querySelector('#input-show-localtoc')?.checked ? 0 : -1
    item.append(link)
    toc.append(item)
    window.app.navigation.init_scroll_spy()
  }
}

window.addEventListener('app:hot_reload:doc_unload', () => {
  active = false
})
window.addEventListener('app:hot_reload:doc_loaded', () => {
  if (window.app.state.repository === 'system-level')
    active = true
})
window.addEventListener('app:hot_reload:page_loaded', addLegalese)
