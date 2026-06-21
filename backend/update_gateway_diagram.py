import os
import json
import html
import re

def build_xml():
    # Construct the raw XML for the Gateway & Self-Healing Flow (Diagram #2)
    xml = """<mxfile host="embed.diagrams.net">
  <diagram id="gateway_compliance_flow" name="Gateway &amp; Self-Healing Flow">
    <mxGraphModel dx="1193" dy="853" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1000" pageHeight="950" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- Row 1: Intake UI -->
        <mxCell id="ui" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="Single Pane of Glass UI&lt;br&gt;&lt;i&gt;Conversational Intake / Upload&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="220" x="390" y="30" as="geometry" />
        </mxCell>
        
        <!-- Row 2: Kong AI Gateway & Ping -->
        <mxCell id="gateway" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#DC2626;strokeWidth=3;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="Kong AI Gateway &amp;amp; Ping&lt;br&gt;&lt;i&gt;JWT Scope Enforcement &amp;amp; PII Filter&lt;/i&gt;" vertex="1">
          <mxGeometry height="60" width="240" x="380" y="115" as="geometry" />
        </mxCell>
        
        <!-- Row 3: Claims DB, Context Layer, Orchestrator -->
        <mxCell id="claims_db" parent="1" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#D5E8D4;strokeColor=#82B366;fontFamily=Helvetica;fontSize=12" value="Scalable Claims DB&lt;br&gt;&lt;b&gt;320+ Approved HCP Claims&lt;/b&gt;" vertex="1">
          <mxGeometry height="80" width="200" x="120" y="215" as="geometry" />
        </mxCell>
        
        <mxCell id="context" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontFamily=Helvetica;fontSize=12" value="Dynamic Context Layer&lt;br&gt;&lt;b&gt;Brand Guidelines &amp;amp; FDA Rules&lt;/b&gt;" vertex="1">
          <mxGeometry height="55" width="180" x="410" y="227.5" as="geometry" />
        </mxCell>
        
        <mxCell id="orchestrator" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="Master Orchestrator Agent&lt;br&gt;&lt;i&gt;AWS AgentCore + Gemini 1.5 Pro (2M Context)&lt;/i&gt;" vertex="1">
          <mxGeometry height="60" width="250" x="650" y="225" as="geometry" />
        </mxCell>
        
        <!-- Row 4: 1:N Tactic Fan-Out Engine -->
        <mxCell id="fanout" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="1:N Tactic Fan-Out Engine&lt;br&gt;&lt;i&gt;Translates global strategy to tactics&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="220" x="390" y="325" as="geometry" />
        </mxCell>
        
        <!-- Row 5: Sub-agents -->
        <mxCell id="email_agent" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="Email Tactic Agent&lt;br&gt;&lt;i&gt;Gemini 2.0 Flash&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="160" x="140" y="420" as="geometry" />
        </mxCell>
        
        <mxCell id="web_agent" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="Web Landing Page Agent&lt;br&gt;&lt;i&gt;Gemini 2.0 Flash&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="160" x="420" y="420" as="geometry" />
        </mxCell>
        
        <mxCell id="sms_agent" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="SMS / Alert Agent&lt;br&gt;&lt;i&gt;Gemini 2.0 Flash&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="160" x="700" y="420" as="geometry" />
        </mxCell>
        
        <!-- Row 6: Risk & Compliance QC Agent -->
        <mxCell id="qc_agent" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#DC2626;strokeWidth=3;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="Risk &amp;amp; Compliance QC Agent&lt;br&gt;&lt;i&gt;Gemini 1.5 Pro (Multimodal Audit). Triggers Dotted-Line Self-Healing.&lt;/i&gt;" vertex="1">
          <mxGeometry height="65" width="380" x="310" y="510" as="geometry" />
        </mxCell>
        
        <!-- Row 7: Integrations & Connector Manager -->
        <mxCell id="connector_mgr" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="Integrations &amp;amp; Connector Manager&lt;br&gt;&lt;i&gt;Applies Cryptographic SHA-256 Lock&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="240" x="380" y="615" as="geometry" />
        </mxCell>
        
        <!-- Row 8: Target Connectors -->
        <mxCell id="veeva_conn" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="Veeva Vault Connector&lt;br&gt;&lt;i&gt;(PromoMats Portal)&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="150" x="120" y="710" as="geometry" />
        </mxCell>
        
        <mxCell id="sf_conn" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="Salesforce Connector&lt;br&gt;&lt;i&gt;(Marketing Cloud)&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="150" x="300" y="710" as="geometry" />
        </mxCell>
        
        <mxCell id="fda_gateway" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontFamily=Helvetica;fontSize=11" value="FDA ESG Portal&lt;br&gt;&lt;b&gt;Form FDA 2253 (eCTD)&lt;/b&gt;" vertex="1">
          <mxGeometry height="50" width="150" x="480" y="710" as="geometry" />
        </mxCell>
        
        <mxCell id="outlook_conn" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="Outlook / Email Channels" vertex="1">
          <mxGeometry height="50" width="150" x="660" y="710" as="geometry" />
        </mxCell>
        
        <!-- Core Connectors -->
        <mxCell id="e1" edge="1" parent="1" source="ui" target="gateway" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
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
        <mxCell id="e5" edge="1" parent="1" source="orchestrator" target="context" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e6" edge="1" parent="1" source="orchestrator" target="fanout" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e7" edge="1" parent="1" source="claims_db" target="fanout" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e8" edge="1" parent="1" source="fanout" target="email_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e9" edge="1" parent="1" source="fanout" target="web_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e10" edge="1" parent="1" source="fanout" target="sms_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e11" edge="1" parent="1" source="email_agent" target="qc_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e12" edge="1" parent="1" source="web_agent" target="qc_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e13" edge="1" parent="1" source="sms_agent" target="qc_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e14" edge="1" parent="1" source="qc_agent" target="connector_mgr" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e15" edge="1" parent="1" source="connector_mgr" target="veeva_conn" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e16" edge="1" parent="1" source="connector_mgr" target="sf_conn" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e17" edge="1" parent="1" source="connector_mgr" target="fda_gateway" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e18" edge="1" parent="1" source="connector_mgr" target="outlook_conn" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        
        <!-- RED DOTTED SELF-HEALING LOOP (qc_agent -> fanout) -->
        <mxCell id="self_healing_loop" edge="1" parent="1" source="qc_agent" target="fanout" style="edgeStyle=orthogonalEdgeStyle;curved=1;rounded=1;html=1;strokeWidth=2.5;strokeColor=#DC2626;dashed=1;fontColor=#DC2626;fontSize=10;fontStyle=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0" value="Dotted-Line Self-Healing Trigger">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="310" y="542.5" as="sourcePoint" />
            <mxPoint x="390" y="352.5" as="targetPoint" />
            <Array as="points">
              <mxPoint x="80" y="543" />
              <mxPoint x="80" y="353" />
            </Array>
          </mxGeometry>
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
    return xml

def build_target_state_xml():
    # Construct the raw XML for the Google-Native Target-State Flow (Diagram #3)
    # Includes [2a] AWS MCP, [8a] A2A Bridge, and [8b] Vertex AI Imagen 3 (Image Generation)
    xml = """<mxfile host="embed.diagrams.net">
  <diagram id="target_agentic_flow" name="Google-Native Target-State Flow">
    <mxGraphModel dx="1193" dy="853" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1100" pageHeight="950" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        
        <!-- Row 1: Adobe Ingestion & Kong Gateway -->
        <mxCell id="adobe_intake" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="&lt;b&gt;[1]&lt;/b&gt; Adobe Workfront Ingestion&lt;br&gt;&lt;i&gt;Campaign Strategy &amp;amp; Brief Ingest&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="220" x="390" y="30" as="geometry" />
        </mxCell>
        
        <mxCell id="kong_gateway" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="&lt;b&gt;[2]&lt;/b&gt; Kong AI Gateway &amp;amp; Ping Identity&lt;br&gt;&lt;i&gt;OAuth JWT Scope &amp;amp; PHI/PII Filters&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="240" x="380" y="115" as="geometry" />
        </mxCell>
        
        <!-- AWS MCP Agents (Exposed legacy/specialized agents running on AWS) -->
        <mxCell id="aws_mcp_agents" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FF9900;strokeColor=#CC6600;strokeWidth=2;fontColor=#FFFFFF;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="&lt;b&gt;[2a]&lt;/b&gt; AWS-Hosted MCP Servers&lt;br&gt;&lt;i&gt;AccessIQ Pricing &amp;amp; Legacy Agents&lt;/i&gt;" vertex="1">
          <mxGeometry height="60" width="210" x="80" y="112.5" as="geometry" />
        </mxCell>
        
        <!-- Row 2: Grounding & Governance Layer (AWS as Data Host, Google as AI Brain) -->
        <mxCell id="aws_data" parent="1" style="shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#FF9900;strokeColor=#CC6600;fontColor=#FFFFFF;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="&lt;b&gt;[3]&lt;/b&gt; AWS Enterprise Data Host&lt;br&gt;&lt;b&gt;Amazon RDS / Redshift (Claims)&lt;/b&gt;" vertex="1">
          <mxGeometry height="80" width="210" x="90" y="205" as="geometry" />
        </mxCell>
        
        <mxCell id="google_vector" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontFamily=Helvetica;fontSize=12" value="&lt;b&gt;[4]&lt;/b&gt; Google Vertex AI Vector Search&lt;br&gt;&lt;b&gt;Real-time Grounding (Brand/FDA)&lt;/b&gt;" vertex="1">
          <mxGeometry height="55" width="230" x="385" y="217.5" as="geometry" />
        </mxCell>
        
        <mxCell id="agent_designer" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="&lt;b&gt;[5]&lt;/b&gt; Vertex AI Agent Designer&lt;br&gt;&lt;i&gt;System Instructions &amp;amp; Persona Hub&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="220" x="690" y="217.5" as="geometry" />
        </mxCell>
        
        <!-- Row 3: Google Agentic Execution Core -->
        <mxCell id="agent_registry" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontFamily=Helvetica;fontSize=12" value="&lt;b&gt;[6]&lt;/b&gt; Google Agent Registry&lt;br&gt;&lt;i&gt;Governance &amp;amp; Security Hub&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="210" x="90" y="325" as="geometry" />
        </mxCell>
        
        <mxCell id="master_orchestrator" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=3;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="&lt;b&gt;[7]&lt;/b&gt; Master Orchestrator Agent&lt;br&gt;&lt;b&gt;Gemini 1.5 Pro (2M Context)&lt;/b&gt;" vertex="1">
          <mxGeometry height="60" width="250" x="375" y="322.5" as="geometry" />
        </mxCell>
        
        <mxCell id="google_adk" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontFamily=Helvetica;fontSize=12" value="&lt;b&gt;[8]&lt;/b&gt; Google ADK (Agent Dev Kit)&lt;br&gt;&lt;i&gt;Runtime Tool Calling &amp;amp; Grounding&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="220" x="690" y="325" as="geometry" />
        </mxCell>
        
        <!-- [8b] Vertex AI Imagen 3 (Image & Asset Generation) -->
        <mxCell id="imagen_3" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;strokeWidth=2;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="&lt;b&gt;[8b]&lt;/b&gt; Vertex AI Imagen 3&lt;br&gt;&lt;i&gt;Compliant Multimodal Image Gen &amp;amp; SynthID Watermark&lt;/i&gt;" vertex="1">
          <mxGeometry height="60" width="180" x="920" y="322.5" as="geometry" />
        </mxCell>
        
        <!-- Google-AWS A2A Bridge (Cross-cloud Pub/Sub tunnel placed in empty left-hand column space) -->
        <mxCell id="a2a_bridge" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;strokeWidth=1.5;dashed=1;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="&lt;b&gt;[8a]&lt;/b&gt; Google-AWS A2A Bridge&lt;br&gt;&lt;i&gt;EventBridge / PubSub Tunnel&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="210" x="90" y="515" as="geometry" />
        </mxCell>
        
        <!-- Row 4: Specialized Tactic Sub-Agents (Google-Native) -->
        <mxCell id="email_agent" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="&lt;b&gt;[9a]&lt;/b&gt; Email Tactic Agent&lt;br&gt;&lt;i&gt;Gemini 2.0 Flash via ADK&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="160" x="140" y="420" as="geometry" />
        </mxCell>
        
        <mxCell id="web_agent" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="&lt;b&gt;[9b]&lt;/b&gt; Web Landing Page Agent&lt;br&gt;&lt;i&gt;Gemini 2.0 Flash via ADK&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="160" x="420" y="420" as="geometry" />
        </mxCell>
        
        <mxCell id="sms_agent" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="&lt;b&gt;[9c]&lt;/b&gt; SMS / Alert Agent&lt;br&gt;&lt;i&gt;Gemini 2.0 Flash via ADK&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="160" x="700" y="420" as="geometry" />
        </mxCell>
        
        <!-- Row 5: Multimodal Quality Control & Real-time Audit -->
        <mxCell id="vertex_monitor" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E6FFFA;strokeColor=#0D9488;strokeWidth=3;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="&lt;b&gt;[10]&lt;/b&gt; Vertex AI Model Monitoring &amp;amp; Auditor&lt;br&gt;&lt;i&gt;Gemini 1.5 Pro (Multimodal QC: Audits Copy, Layout, &amp;amp; Imagen 3 SynthID Watermarks)&lt;/i&gt;" vertex="1">
          <mxGeometry height="65" width="400" x="300" y="510" as="geometry" />
        </mxCell>
        
        <!-- Row 6: Secure Connector & Enterprise Integrations -->
        <mxCell id="connector_mgr" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontFamily=Helvetica;fontSize=12;fontStyle=1" value="&lt;b&gt;[11]&lt;/b&gt; Secure Connector Manager&lt;br&gt;&lt;i&gt;Applies Cryptographic SHA-256 Lock&lt;/i&gt;" vertex="1">
          <mxGeometry height="55" width="240" x="380" y="615" as="geometry" />
        </mxCell>
        
        <!-- Row 7: Target Connectors -->
        <mxCell id="veeva_conn" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="&lt;b&gt;[12a]&lt;/b&gt; Veeva Vault Connector&lt;br&gt;&lt;i&gt;(PromoMats Portal)&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="150" x="120" y="710" as="geometry" />
        </mxCell>
        
        <mxCell id="sf_conn" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="&lt;b&gt;[12b]&lt;/b&gt; Salesforce Connector&lt;br&gt;&lt;i&gt;(Marketing Cloud)&lt;/i&gt;" vertex="1">
          <mxGeometry height="50" width="150" x="300" y="710" as="geometry" />
        </mxCell>
        
        <mxCell id="fda_gateway" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontFamily=Helvetica;fontSize=11" value="&lt;b&gt;[12c]&lt;/b&gt; FDA ESG Portal&lt;br&gt;&lt;b&gt;Form FDA 2253 (eCTD)&lt;/b&gt;" vertex="1">
          <mxGeometry height="50" width="150" x="480" y="710" as="geometry" />
        </mxCell>
        
        <mxCell id="outlook_conn" parent="1" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;fontFamily=Helvetica;fontSize=11" value="&lt;b&gt;[12d]&lt;/b&gt; Outlook / Email Channels" vertex="1">
          <mxGeometry height="50" width="150" x="660" y="710" as="geometry" />
        </mxCell>
        
        <!-- Edges -->
        <mxCell id="e1" edge="1" parent="1" source="adobe_intake" target="kong_gateway" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e2" edge="1" parent="1" source="kong_gateway" target="master_orchestrator" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e3" edge="1" parent="1" source="kong_gateway" target="aws_data" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e4" edge="1" parent="1" source="aws_data" target="master_orchestrator" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e5" edge="1" parent="1" source="google_vector" target="master_orchestrator" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e6" edge="1" parent="1" source="agent_designer" target="master_orchestrator" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e7" edge="1" parent="1" source="agent_registry" target="master_orchestrator" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e8" edge="1" parent="1" source="master_orchestrator" target="google_adk" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e9" edge="1" parent="1" source="google_adk" target="email_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e10" edge="1" parent="1" source="google_adk" target="web_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e11" edge="1" parent="1" source="google_adk" target="sms_agent" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e12" edge="1" parent="1" source="email_agent" target="vertex_monitor" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e13" edge="1" parent="1" source="web_agent" target="vertex_monitor" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e14" edge="1" parent="1" source="sms_agent" target="vertex_monitor" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e15" edge="1" parent="1" source="vertex_monitor" target="connector_mgr" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e16" edge="1" parent="1" source="connector_mgr" target="veeva_conn" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e17" edge="1" parent="1" source="connector_mgr" target="sf_conn" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e18" edge="1" parent="1" source="connector_mgr" target="fda_gateway" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="e19" edge="1" parent="1" source="connector_mgr" target="outlook_conn" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#666666">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        
        <!-- DOTTED SELF-HEALING LOOP (vertex_monitor -> agent_designer) - Routed on the far right at x=940 -->
        <mxCell id="self_healing_loop" edge="1" parent="1" source="vertex_monitor" target="agent_designer" style="edgeStyle=orthogonalEdgeStyle;curved=1;rounded=1;html=1;strokeWidth=2.5;strokeColor=#DC2626;dashed=1;fontColor=#DC2626;fontSize=10;fontStyle=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0" value="[10a] Google-Native Self-Healing Loop">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="700" y="542.5" as="sourcePoint" />
            <mxPoint x="910" y="245" as="targetPoint" />
            <Array as="points">
              <mxPoint x="940" y="543" />
              <mxPoint x="940" y="245" />
            </Array>
          </mxGeometry>
        </mxCell>
        
        <!-- NEW CROSS-CLOUD CONNECTIONS -->
        <!-- AWS MCP Agents -> Kong Gateway (Secure Ingress) -->
        <mxCell id="e_mcp1" edge="1" parent="1" source="aws_mcp_agents" target="kong_gateway" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#FF9900">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        
        <!-- Dotted bi-directional MCP Link (Dynamic Tool-Calling) - Routed through the clear gap channel at x=330 -->
        <mxCell id="e_mcp2" edge="1" parent="1" source="master_orchestrator" target="aws_mcp_agents" style="edgeStyle=orthogonalEdgeStyle;rounded=1;curved=1;html=1;strokeWidth=2;strokeColor=#1A73E8;dashed=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0" value="MCP Protocol Link (Tool Calling)">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="375" y="352.5" as="sourcePoint" />
            <mxPoint x="300" y="142.5" as="targetPoint" />
            <Array as="points">
              <mxPoint x="330" y="353" />
              <mxPoint x="330" y="143" />
            </Array>
          </mxGeometry>
        </mxCell>
        
        <!-- Google ADK -> A2A Bridge (Asynchronous handoff) -->
        <mxCell id="e_a2a1" edge="1" parent="1" source="google_adk" target="a2a_bridge" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#6C8EBF;dashed=1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        
        <!-- A2A Bridge -> AWS MCP Agents (Cross-Cloud Event Tunnel) - Routed safely on the far left margin at x=50 -->
        <mxCell id="e_a2a2" edge="1" parent="1" source="a2a_bridge" target="aws_mcp_agents" style="edgeStyle=orthogonalEdgeStyle;rounded=1;curved=1;html=1;strokeWidth=1.5;strokeColor=#FF9900;dashed=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="90" y="542.5" as="sourcePoint" />
            <mxPoint x="80" y="142.5" as="targetPoint" />
            <Array as="points">
              <mxPoint x="50" y="543" />
              <mxPoint x="50" y="143" />
            </Array>
          </mxGeometry>
        </mxCell>
        
        <!-- Google ADK -> Imagen 3 (Shared Image Gen tool) -->
        <mxCell id="e_imagen" edge="1" parent="1" source="google_adk" target="imagen_3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=1.5;strokeColor=#9673A6">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
    return xml

def main():
    # 1. Generate XML and JSON payloads
    xml2 = build_xml()
    config2 = {
        "highlight": "#0D9488",
        "nav": True,
        "resize": True,
        "toolbar": "zoom layers tags edit",
        "edit": "_blank",
        "xml": xml2
    }
    escaped_json2 = html.escape(json.dumps(config2))

    xml3 = build_target_state_xml()
    config3 = {
        "highlight": "#0D9488",
        "nav": True,
        "resize": True,
        "toolbar": "zoom layers tags edit",
        "edit": "_blank",
        "xml": xml3
    }
    escaped_json3 = html.escape(json.dumps(config3))

    # 2. Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    user_guide_path = os.path.join(base_dir, "frontend", "user_guide.html")

    with open(user_guide_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # 3. Check and inject Section 1C if not present
    section_1c_id = 'id="google_target_architecture"'
    if section_1c_id not in html_content:
        print("💡 Injecting Section 1C (Google-Native Target State) into user_guide.html...")
        
        # We find the closing tag of section 1B (gateway_architecture)
        # To do this cleanly, we search for the closing section tag right before the UI Guide comment
        target_split = """            </section>

            <!-- NEW SECTION: UI Guide -->"""
        
        section_1c_html = """            </section>

            <!-- SECTION 1C: Google-Native Target State Agentic Architecture -->
            <section id="google_target_architecture" class="guide-section">
                <h2><span class="section-icon">💎</span> Google-Native Target State Agentic Architecture</h2>
                <p>To establish a future-proof, highly governed agentic framework, we compare the agentic capabilities of **Google Cloud (Vertex AI / Gemini)** and **AWS (Bedrock / AgentCore)**. While AWS serves as a robust enterprise data host (hosting raw claims registries in Amazon RDS or S3), **Google\'s Agentic AI framework is demonstrably superior** for orchestrating complex, regulated marketing and clinical pipelines due to its native multimodal reasoning, massive context window, and cohesive developer tooling.</p>
                
                <div class="comparison-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 1.5rem 0;">
                    <div class="card" style="background: rgba(26, 115, 232, 0.04); border: 1px solid rgba(26, 115, 232, 0.2); padding: 1.25rem; border-radius: 8px;">
                        <h4 style="color: var(--color-primary); margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">
                            <span>💙</span> Google Cloud Agentic Advantage (Winner)
                        </h4>
                        <ul style="margin: 0.5rem 0 0 1.25rem; padding: 0; font-size: 0.88rem; line-height: 1.5; color: var(--color-text-muted);">
                            <li><strong>2M Token Context Window:</strong> Gemini 1.5 Pro natively ingests the entire campaign brief, complete brand guidelines, FDA regulations, and historical assets in a single call—eliminating complex, lossy RAG chunking.</li>
                            <li><strong>Unified Developer Ecosystem:</strong> Seamless integration across **Vertex AI Agent Designer**, **Google ADK (Agent Development Kit)**, and the **Agent Registry** provides unified governance and ultra-low latency tool calling.</li>
                            <li><strong>Natively Integrated Multimodal Gen (Imagen 3 &amp; Gemini):</strong> Vertex AI Imagen 3 is called directly via the Google ADK to generate high-fidelity, on-brand marketing images, while Gemini 2.0 Flash generates copy, HTML, and email layouts in parallel.</li>
                        </ul>
                    </div>
                    <div class="card" style="background: rgba(255, 153, 0, 0.04); border: 1px solid rgba(255, 153, 0, 0.2); padding: 1.25rem; border-radius: 8px;">
                        <h4 style="color: #CC6600; margin-top: 0; display: flex; align-items: center; gap: 0.5rem;">
                            <span>🧡</span> AWS Bedrock &amp; AgentCore Limitations
                        </h4>
                        <ul style="margin: 0.5rem 0 0 1.25rem; padding: 0; font-size: 0.88rem; line-height: 1.5; color: var(--color-text-muted);">
                            <li><strong>Fragmented Tooling:</strong> Bedrock Agents, AgentCore, and AWS Step Functions are loosely coupled, resulting in higher integration overhead, increased latency, and complex state synchronization.</li>
                            <li><strong>Restrictive Context Constraints:</strong> AWS models have significantly smaller context windows, forcing heavy reliance on multi-hop chunked RAG, which frequently loses critical regulatory or brand nuance.</li>
                            <li><strong>High Multi-Model Latency:</strong> Lacks a single, powerful native multimodal model equivalent to Gemini 1.5 Pro, requiring separate models for layout vision, text checking, and code generation.</li>
                        </ul>
                    </div>
                </div>

                <p>Below is the target-state **Google-Native Enterprise Agentic Architecture**, featuring secure, authenticated ingestion, AWS clinical data hosting, Google Vector Search grounding, Vertex Agent Registry governance, and Vertex AI Model Monitoring auditing with a real-time Dotted-Line Self-Healing Loop:</p>
                
                <!-- Draw.io Interactive Embed Container for Target State Diagram (Adjusted to 840px to prevent clipping) -->
                <div style="width: 100%; height: 840px; background: var(--bg-sub); border: 1px solid var(--border-color); border-radius: 8px; overflow: hidden; margin: 1.5rem 0; position: relative; box-shadow: inset 0 2px 8px rgba(0,0,0,0.02);">
                    <div class="mxgraph" style="max-width:100%; height: 100%; border:none; box-sizing:border-box;" data-mxgraph="__TARGET_DIAGRAM_JSON__"></div>
                </div>
            </section>

            <!-- NEW SECTION: UI Guide -->"""
        
        if target_split in html_content:
            html_content = html_content.replace(target_split, section_1c_html)
        else:
            print("❌ Error: Could not locate end of Section 1B to inject Section 1C.")
            return

    # 4. Inject Diagram #2 (Gateway & Self-Healing Flow) in-place
    pattern2 = r'<div class="mxgraph"[^>]*data-mxgraph="[^"]*gateway_compliance_flow[^"]*"[^>]*></div>'
    placeholder2 = "__GATEWAY_DIAGRAM_JSON__"
    
    if placeholder2 in html_content:
        html_content = html_content.replace(placeholder2, escaped_json2)
        print("✅ Successfully injected Diagram #2 into placeholder.")
    elif re.search(pattern2, html_content):
        replacement2 = f'<div class="mxgraph" style="max-width:100%; height: 100%; border:none; box-sizing:border-box;" data-mxgraph="{escaped_json2}"></div>'
        html_content = re.sub(pattern2, lambda m: replacement2, html_content)
        print("✅ Successfully updated Diagram #2 in-place.")
    else:
        print("❌ Warning: Diagram #2 container not found.")

    # 5. Inject Diagram #3 (Google-Native Target State) in-place
    pattern3 = r'<div class="mxgraph"[^>]*data-mxgraph="[^"]*target_agentic_flow[^"]*"[^>]*></div>'
    placeholder3 = "__TARGET_DIAGRAM_JSON__"
    
    if placeholder3 in html_content:
        html_content = html_content.replace(placeholder3, escaped_json3)
        print("✅ Successfully injected Diagram #3 into placeholder.")
    elif re.search(pattern3, html_content):
        replacement3 = f'<div class="mxgraph" style="max-width:100%; height: 100%; border:none; box-sizing:border-box;" data-mxgraph="{escaped_json3}"></div>'
        html_content = re.sub(pattern3, lambda m: replacement3, html_content)
        print("✅ Successfully updated Diagram #3 in-place.")
    else:
        print("❌ Warning: Diagram #3 container not found.")

    # 6. Adjust ALL diagram container heights from 580px to 840px in the HTML to prevent clipping
    html_content = html_content.replace(
        'height: 580px; background: var(--bg-sub);',
        'height: 840px; background: var(--bg-sub);'
    )
    html_content = html_content.replace(
        'height: 580px; background:var(--bg-sub);',
        'height: 840px; background:var(--bg-sub);'
    )

    # 7. Write back to user_guide.html
    with open(user_guide_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("🎉 All diagrams and sections successfully updated in user_guide.html!")

if __name__ == "__main__":
    main()
