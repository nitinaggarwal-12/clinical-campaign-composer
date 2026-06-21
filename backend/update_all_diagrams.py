import os
import json
import html

def build_baseline_xml():
    # Construct the raw XML for the updated Baseline Architecture diagram
    xml = """<mxfile host="embed.diagrams.net">
  <diagram id="baseline_architecture" name="Baseline Architecture">
    <mxGraphModel dx="1193" dy="853" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1000" pageHeight="920" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- Row 1: Adobe Workfront Origin / Intake UI -->
        <mxCell id="intake" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="Adobe Workfront / UI Ingestion&lt;br&gt;&lt;i&gt;Origin Brief &amp;amp; Strategy Ingest&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="220" x="390" y="30" as="geometry" />
        </mxCell>
        
        <!-- Row 2: Master Orchestrator Agent -->
        <mxCell id="orchestrator" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="Master Orchestrator Agent&lt;br&gt;&lt;i&gt;AWS AgentCore + Gemini 1.5 Pro&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="220" x="390" y="115" as="geometry" />
        </mxCell>
        
        <!-- Row 3: Amazon RDS DB, BigQuery CDP, Context Layer -->
        <mxCell id="claims_db" parent="1" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#D5E8D4;strokeColor=#82B366;fontFamily=Helvetica;fontSize=11" value="Amazon RDS / PostgreSQL DB&lt;br&gt;&lt;b&gt;Veeva MCP Claims Registry&lt;/b&gt;" vertex="1">
          <mxGeometry height="80" width="230" x="110" y="202.5" as="geometry" />
        </mxCell>
        
        <mxCell id="cdp" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="BigQuery CDP&lt;br&gt;&lt;i&gt;Audience &amp;amp; Consent Verification&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="220" x="390" y="215" as="geometry" />
        </mxCell>
        
        <mxCell id="rules" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontFamily=Helvetica;fontSize=12" value="Dynamic Context Layer&lt;br&gt;&lt;b&gt;Brand Guidelines &amp;amp; FDA Rules&lt;/b&gt;" vertex="1">
          <mxGeometry height="55" width="200" x="650" y="215" as="geometry" />
        </mxCell>
        
        <!-- Row 4: 1:N Tactic Fan-Out Engine -->
        <mxCell id="fanout" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="1:N Tactic Fan-Out Engine&lt;br&gt;&lt;i&gt;Translates global strategy to tactics&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="220" x="390" y="310" as="geometry" />
        </mxCell>
        
        <!-- Row 5: Sub-agents -->
        <mxCell id="email_agent" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="Email Tactic Agent&lt;br&gt;&lt;i&gt;Gemini 2.0 Flash&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="160" x="140" y="395" as="geometry" />
        </mxCell>
        
        <mxCell id="web_agent" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="Web Landing Page Agent&lt;br&gt;&lt;i&gt;Gemini 2.0 Flash&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="160" x="420" y="395" as="geometry" />
        </mxCell>
        
        <mxCell id="sms_agent" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="SMS / Alert Agent&lt;br&gt;&lt;i&gt;Gemini 2.0 Flash&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="160" x="700" y="395" as="geometry" />
        </mxCell>
        
        <!-- Row 6: Imagen 3 & Ledger -->
        <mxCell id="imagen3" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontFamily=Helvetica;fontSize=11;fontStyle=1" value="Imagen 3 (Visual Gen)&lt;br&gt;&lt;i&gt;SynthID Provenance Watermark&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="180" x="130" y="480" as="geometry" />
        </mxCell>
        
        <mxCell id="fallback_imagen" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;fontFamily=Helvetica;fontSize=11;fontStyle=2" value="Resilient Fallback&lt;br&gt;&lt;i&gt;(imagen-3.0-generate-002)&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="180" x="130" y="565" as="geometry" />
        </mxCell>
        
        <mxCell id="ledger_agent" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontFamily=Helvetica;fontSize=11;fontStyle=1" value="Compliance Ledger Agent&lt;br&gt;&lt;b&gt;SHA-256 Digital Wax Seal&lt;/b&gt;" vertex="1">
          <mxGeometry height="60" width="180" x="410" y="480" as="geometry" />
        </mxCell>
        
        <!-- Row 7: Integrations & Connector Manager -->
        <mxCell id="connector_mgr" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="Integrations &amp;amp; Connector Manager&lt;br&gt;&lt;i&gt;Applies Cryptographic SHA-256 Lock&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="240" x="380" y="660" as="geometry" />
        </mxCell>
        
        <!-- Row 8: Target Connectors -->
        <mxCell id="veeva_conn" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="Veeva Vault Connector&lt;br&gt;&lt;i&gt;(PromoMats Portal)&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="150" x="120" y="750" as="geometry" />
        </mxCell>
        
        <mxCell id="sf_conn" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="Salesforce Connector&lt;br&gt;&lt;i&gt;(Marketing Cloud)&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="150" x="300" y="750" as="geometry" />
        </mxCell>
        
        <mxCell id="fda_gateway" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontFamily=Helvetica;fontSize=11" value="FDA ESG Portal&lt;br&gt;&lt;b&gt;Form FDA 2253 (eCTD)&lt;/b&gt;" vertex="1">
          <mxGeometry height="50" width="150" x="480" y="750" as="geometry" />
        </mxCell>
        
        <mxCell id="outlook_conn" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="Outlook / Email Channels" vertex="1">
          <mxGeometry height="50" width="150" x="660" y="750" as="geometry" />
        </mxCell>
        
        <!-- Core Connectors -->
        <mxCell id="e1" edge="1" parent="1" source="intake" target="orchestrator" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e2" edge="1" parent="1" source="orchestrator" target="claims_db" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e3" edge="1" parent="1" source="orchestrator" target="rules" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e4" edge="1" parent="1" source="orchestrator" target="cdp" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e5" edge="1" parent="1" source="claims_db" target="cdp" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e6" edge="1" parent="1" source="cdp" target="fanout" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e7" edge="1" parent="1" source="fanout" target="email_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e8" edge="1" parent="1" source="fanout" target="web_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e9" edge="1" parent="1" source="fanout" target="sms_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e10" edge="1" parent="1" source="email_agent" target="imagen3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e11" edge="1" parent="1" source="imagen3" target="fallback_imagen" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#DC2626;fontColor=#DC2626;fontSize=10;fontStyle=1" value="If 404 NOT_FOUND">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e12" edge="1" parent="1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="300" y="420" as="sourcePoint" />
            <mxPoint x="500" y="480" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e13" edge="1" parent="1" source="web_agent" target="ledger_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e14" edge="1" parent="1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="700" y="420" as="sourcePoint" />
            <mxPoint x="500" y="480" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="e15" edge="1" parent="1" source="ledger_agent" target="connector_mgr" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e16" edge="1" parent="1" source="fallback_imagen" target="connector_mgr" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e17" edge="1" parent="1" source="connector_mgr" target="veeva_conn" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e18" edge="1" parent="1" source="connector_mgr" target="sf_conn" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e19" edge="1" parent="1" source="connector_mgr" target="fda_gateway" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e20" edge="1" parent="1" source="connector_mgr" target="outlook_conn" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
    return xml

def build_gateway_xml():
    # Construct the raw XML for the updated Enterprise Gateway & Self-Healing Architecture
    xml = """<mxfile host="embed.diagrams.net">
  <diagram id="gateway_compliance_flow" name="Gateway &amp; Self-Healing Flow">
    <mxGraphModel dx="1193" dy="853" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1000" pageHeight="960" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- Row 1: Adobe Workfront Origin -->
        <mxCell id="intake" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="Adobe Workfront / UI Ingestion&lt;br&gt;&lt;i&gt;Origin Brief &amp;amp; Strategy Ingest&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="220" x="390" y="30" as="geometry" />
        </mxCell>
        
        <!-- Row 2: Kong AI Gateway & Ping -->
        <mxCell id="gateway" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#DC2626;strokeWidth=3;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="Kong AI Gateway &amp; Ping&lt;br&gt;&lt;i&gt;JWT Scope Enforcement &amp;amp; PII Filter&lt;/i&gt;" vertex="1">
          <mxGeometry height="60" width="240" x="380" y="110" as="geometry" />
        </mxCell>
        
        <!-- Row 3: Amazon RDS, BigQuery CDP, Master Orchestrator -->
        <mxCell id="claims_db" parent="1" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#D5E8D4;strokeColor=#82B366;fontFamily=Helvetica;fontSize=11" value="Amazon RDS / PostgreSQL DB&lt;br&gt;&lt;b&gt;Veeva MCP Claims Registry&lt;/b&gt;" vertex="1">
          <mxGeometry height="80" width="230" x="110" y="195" as="geometry" />
        </mxCell>
        
        <mxCell id="cdp" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="BigQuery CDP&lt;br&gt;&lt;i&gt;Audience &amp;amp; Consent Verification&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="220" x="390" y="210" as="geometry" />
        </mxCell>
        
        <mxCell id="orchestrator" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="Master Orchestrator Agent&lt;br&gt;&lt;i&gt;AWS AgentCore + Gemini 1.5 Pro&lt;/i&gt;" vertex="1">
          <mxGeometry height="60" width="240" x="650" y="207.5" as="geometry" />
        </mxCell>
        
        <mxCell id="context" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontFamily=Helvetica;fontSize=12" value="Dynamic Context Layer&lt;br&gt;&lt;b&gt;Brand Guidelines &amp;amp; FDA Rules&lt;/b&gt;" vertex="1">
          <mxGeometry height="55" width="240" x="650" y="300" as="geometry" />
        </mxCell>
        
        <!-- Row 4: 1:N Tactic Fan-Out Engine -->
        <mxCell id="fanout" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="1:N Tactic Fan-Out Engine&lt;br&gt;&lt;i&gt;Translates global strategy to tactics&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="220" x="390" y="300" as="geometry" />
        </mxCell>
        
        <!-- Row 5: Sub-agents -->
        <mxCell id="email_agent" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="Email Tactic Agent&lt;br&gt;&lt;i&gt;Gemini 2.0 Flash&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="160" x="140" y="390" as="geometry" />
        </mxCell>
        
        <mxCell id="web_agent" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="Web Landing Page Agent&lt;br&gt;&lt;i&gt;Gemini 2.0 Flash&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="160" x="420" y="390" as="geometry" />
        </mxCell>
        
        <mxCell id="sms_agent" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="SMS / Alert Agent&lt;br&gt;&lt;i&gt;Gemini 2.0 Flash&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="160" x="700" y="390" as="geometry" />
        </mxCell>
        
        <!-- Row 6: Imagen 3 & Risk & Compliance QC Agent -->
        <mxCell id="imagen3" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontFamily=Helvetica;fontSize=11;fontStyle=1" value="Imagen 3 (Visual Gen)&lt;br&gt;&lt;i&gt;SynthID Provenance Watermark&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="180" x="130" y="480" as="geometry" />
        </mxCell>
        
        <mxCell id="fallback_imagen" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;fontFamily=Helvetica;fontSize=11;fontStyle=2" value="Resilient Fallback&lt;br&gt;&lt;i&gt;(imagen-3.0-generate-002)&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="180" x="130" y="565" as="geometry" />
        </mxCell>
        
        <mxCell id="qc_agent" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#DC2626;strokeWidth=3;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="Risk &amp; Compliance QC Agent&lt;br&gt;&lt;i&gt;Gemini 1.5 Pro (Multimodal Audit). Triggers Dotted-Line Self-Healing.&lt;/i&gt;" vertex="1">
          <mxGeometry height="65" width="380" x="350" y="480" as="geometry" />
        </mxCell>
        
        <!-- Row 7: Integrations & Connector Manager -->
        <mxCell id="connector_mgr" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="Integrations &amp;amp; Connector Manager&lt;br&gt;&lt;i&gt;Applies Cryptographic SHA-256 Lock&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="240" x="380" y="660" as="geometry" />
        </mxCell>
        
        <!-- Row 8: Target Connectors -->
        <mxCell id="veeva_conn" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="Veeva Vault Connector&lt;br&gt;&lt;i&gt;(PromoMats Portal)&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="150" x="120" y="760" as="geometry" />
        </mxCell>
        
        <mxCell id="sf_conn" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="Salesforce Connector&lt;br&gt;&lt;i&gt;(Marketing Cloud)&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="150" x="300" y="760" as="geometry" />
        </mxCell>
        
        <mxCell id="fda_gateway" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontFamily=Helvetica;fontSize=11" value="FDA ESG Portal&lt;br&gt;&lt;b&gt;Form FDA 2253 (eCTD)&lt;/b&gt;" vertex="1">
          <mxGeometry height="50" width="150" x="480" y="760" as="geometry" />
        </mxCell>
        
        <mxCell id="outlook_conn" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="Outlook / Email Channels" vertex="1">
          <mxGeometry height="50" width="150" x="660" y="760" as="geometry" />
        </mxCell>
        
        <!-- Connections -->
        <mxCell id="e1" edge="1" parent="1" source="intake" target="gateway" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e2" edge="1" parent="1" source="gateway" target="orchestrator" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e3" edge="1" parent="1" source="gateway" target="claims_db" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e4" edge="1" parent="1" source="orchestrator" target="claims_db" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e5" edge="1" parent="1" source="orchestrator" target="cdp" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e6" edge="1" parent="1" source="claims_db" target="cdp" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e7" edge="1" parent="1" source="cdp" target="fanout" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e8" edge="1" parent="1" source="orchestrator" target="context" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e9" edge="1" parent="1" source="fanout" target="email_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e10" edge="1" parent="1" source="fanout" target="web_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e11" edge="1" parent="1" source="fanout" target="sms_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e12" edge="1" parent="1" source="email_agent" target="imagen3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e13" edge="1" parent="1" source="imagen3" target="fallback_imagen" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#DC2626;fontColor=#DC2626;fontSize=10;fontStyle=1" value="If 404">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e14" edge="1" parent="1" source="email_agent" target="qc_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e15" edge="1" parent="1" source="web_agent" target="qc_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e16" edge="1" parent="1" source="sms_agent" target="qc_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e17" edge="1" parent="1" source="qc_agent" target="connector_mgr" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e18" edge="1" parent="1" source="fallback_imagen" target="connector_mgr" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e19" edge="1" parent="1" source="connector_mgr" target="veeva_conn" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e20" edge="1" parent="1" source="connector_mgr" target="sf_conn" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e21" edge="1" parent="1" source="connector_mgr" target="fda_gateway" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e22" edge="1" parent="1" source="connector_mgr" target="outlook_conn" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        
        <!-- RED DOTTED SELF-HEALING LOOP -->
        <mxCell id="self_healing_loop" edge="1" parent="1" source="qc_agent" target="fanout" style="edgeStyle=orthogonalEdgeStyle;curved=1;rounded=1;html=1;strokeWidth=2.5;strokeColor=#DC2626;dashed=1;fontColor=#DC2626;fontSize=10;fontStyle=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0" value="Dotted-Line Self-Healing Trigger">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="350" y="512.5" as="sourcePoint" />
            <mxPoint x="390" y="327.5" as="targetPoint" />
            <Array as="points">
              <mxPoint x="80" y="513" />
              <mxPoint x="80" y="328" />
            </Array>
          </mxGeometry>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
    return xml

def main():
    # 1. Build XML structures
    baseline_xml = build_baseline_xml()
    gateway_xml = build_gateway_xml()
    
    # 2. Package Baseline Config
    baseline_config = {
        "highlight": "#0D9488",
        "nav": True,
        "resize": True,
        "toolbar": "zoom layers tags edit",
        "edit": "_blank",
        "xml": baseline_xml
    }
    baseline_json = html.escape(json.dumps(baseline_config))
    
    # 3. Package Gateway Config
    gateway_config = {
        "highlight": "#0D9488",
        "nav": True,
        "resize": True,
        "toolbar": "zoom layers tags edit",
        "edit": "_blank",
        "xml": gateway_xml
    }
    gateway_json = html.escape(json.dumps(gateway_config))
    
    # 4. Read and update user_guide.html
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    user_guide_path = os.path.join(base_dir, "frontend", "user_guide.html")
    
    with open(user_guide_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Inject both placeholders
    html_content = html_content.replace("__BASELINE_DIAGRAM_JSON__", baseline_json)
    html_content = html_content.replace("__GATEWAY_DIAGRAM_JSON__", gateway_json)
    
    with open(user_guide_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("✅ Successfully updated both architecture diagrams in user_guide.html with production-grade changes!")

if __name__ == "__main__":
    main()
