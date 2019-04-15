#!/usr/bin/env python
#!/usr/bin/env python

import os, imp, math, ROOT
import numpy as np

tdrstyle = imp.load_source('tdrstyle', 'tdrstyle.py')
CMS_lumi = imp.load_source('CMS_lumi', 'CMS_lumi.py') 

def signaleff():

  masses = np.array([
    750 ,
    800 ,
    900 ,
    1000,
    1200,
    1400,
    1600,
    1800,
    2000,
    2500,
    3000,
    4000,
    4500,
    ], 'd'
    )
  
  effs_BulkGrav_LL = np.array([
    0.027 - 0.015 , 
    0.057 - 0.032 , 
    0.092 - 0.051 , 
    0.111 - 0.062 , 
    0.129 - 0.068 , 
    0.129 - 0.064 , 
    0.128 - 0.061 , 
    0.130 - 0.059 , 
    0.123 - 0.054 , 
    0.113 - 0.044 , 
    0.102 - 0.034 , # * 0.69 , ### Due to signal truncation at Mjjred = 3 TeV
    0.078 - 0.021 , 
    0.065 - 0.016 , 
    ], 'd'  
    ) 
  
  effs_BulkGrav_TT = np.array([
    0.015 ,
    0.032 ,
    0.051 ,
    0.062 ,
    0.068 ,
    0.064 ,
    0.061 ,
    0.059 ,
    0.054 ,
    0.044 ,
    0.034 , # * 0.62 , ### Due to signal truncation at Mjjred = 3 TeV
    0.021 ,
    0.016 ,
    ], 'd'
    )
  
  effs_Radion_LL = np.array([
    0.016 - 0.009 , 
    0.036 - 0.021 , 
    0.061 - 0.033 , 
    0.075 - 0.041 , 
    0.084 - 0.044 , 
    0.087 - 0.044 , 
    0.086 - 0.041 , 
    0.082 - 0.036 , 
    0.081 - 0.036 , 
    0.076 - 0.030 , 
    0.068 - 0.022 , # * 0.69 , ### Due to signal truncation at Mjjred = 3 TeV
    0.059 - 0.018 , 
    0.044 - 0.010 , 
    ], 'd'
    )
  
  effs_Radion_TT = np.array([
    0.009 ,
    0.021 ,
    0.033 ,
    0.041 ,
    0.044 ,
    0.044 ,
    0.041 ,
    0.036 ,
    0.036 ,
    0.030 ,
    0.022 , # * 0.62 , ### Due to signal truncation at Mjjred = 3 TeV
    0.018 ,
    0.010 ,
    ], 'd'
    )
  
  geffs_BulkGrav_LL = ROOT.TGraph(len(masses), masses, effs_BulkGrav_LL)
  geffs_BulkGrav_TT = ROOT.TGraph(len(masses), masses, effs_BulkGrav_TT)
  geffs_Radion_LL   = ROOT.TGraph(len(masses), masses, effs_Radion_LL)
  geffs_Radion_TT   = ROOT.TGraph(len(masses), masses, effs_Radion_TT)

  geffs_BulkGrav_LL .SetName('geffs_BulkGrav_LL') 
  geffs_BulkGrav_TT .SetName('geffs_BulkGrav_TT') 
  geffs_Radion_LL   .SetName('geffs_Radion_LL') 
  geffs_Radion_TT   .SetName('geffs_Radion_TT') 

  return geffs_BulkGrav_LL, geffs_BulkGrav_TT, geffs_Radion_LL, geffs_Radion_TT
  
def plotEffs():
  
  geffs_BulkGrav_LL, geffs_BulkGrav_TT, geffs_Radion_LL, geffs_Radion_TT = signaleff()

  geffs_BulkGrav_LL.SetLineColor(616+3) 
  geffs_BulkGrav_TT.SetLineColor(616+3) 
  
  geffs_Radion_LL.SetLineColor(416+4) 
  geffs_Radion_TT.SetLineColor(416+4) 
  
  geffs_BulkGrav_LL.SetLineWidth(2) 
  geffs_BulkGrav_TT.SetLineWidth(2) 
  
  geffs_Radion_LL.SetLineWidth(2) 
  geffs_Radion_TT.SetLineWidth(2) 
  
  geffs_BulkGrav_LL.SetLineStyle(1) 
  geffs_BulkGrav_TT.SetLineStyle(2) 
  
  geffs_Radion_LL.SetLineStyle(1) 
  geffs_Radion_TT.SetLineStyle(4) 
  
  geffs_BulkGrav_LL .SetMarkerSize(1.4) 
  geffs_BulkGrav_TT .SetMarkerSize(1.4) 
  geffs_Radion_LL   .SetMarkerSize(1.3) 
  geffs_Radion_TT   .SetMarkerSize(1.6) 
  
  geffs_BulkGrav_LL .SetMarkerStyle(20) 
  geffs_BulkGrav_TT .SetMarkerStyle(21) 
  geffs_Radion_LL   .SetMarkerStyle(22) 
  geffs_Radion_TT   .SetMarkerStyle(23) 
  
  geffs_BulkGrav_LL .SetMarkerColor(geffs_BulkGrav_LL.GetLineColor()) 
  geffs_BulkGrav_TT .SetMarkerColor(geffs_BulkGrav_TT.GetLineColor()) 
  geffs_Radion_LL   .SetMarkerColor(geffs_Radion_LL  .GetLineColor()) 
  geffs_Radion_TT   .SetMarkerColor(geffs_Radion_TT  .GetLineColor()) 
  
  pol3 = ROOT.TF1('pol3', '[0] + [1]*x + [2]*x*x + [3]*x*x*x', 750., 3000)
  
  #geffs_BulkGrav_LL.Fit("pol3")
  
  c0 = ROOT.TCanvas('csigEff','',800,600)
  c0.cd()
  c0.SetTopMargin(0.10)
  c0.SetBottomMargin(0.15)
  c0.SetLeftMargin(0.15)
  c0.SetRightMargin(0.05)
  h = c0.DrawFrame(750,0.0,3000,0.15)
  geffs_Radion_LL.Draw("LP")
  geffs_BulkGrav_LL.Draw("LP")
  geffs_Radion_TT.Draw("LP")
  geffs_BulkGrav_TT.Draw("LP")
  c0.RedrawAxis()
  c0.Update()
  h.GetXaxis().SetTitle("m_{X} [GeV]")
  h.GetXaxis().SetTitleFont(42)
  h.GetXaxis().SetLabelFont(42)
  h.GetXaxis().SetTitleSize(0.05)
  h.GetXaxis().SetLabelSize(0.05)
  h.GetXaxis().SetTitleOffset(1.08)
  h.GetYaxis().SetTitle("Selection efficiency")
  h.GetYaxis().SetTitleFont(42)
  h.GetYaxis().SetLabelFont(42)
  h.GetYaxis().SetTitleSize(0.05)
  h.GetYaxis().SetLabelSize(0.05)
  h.GetYaxis().SetTitleOffset(1.30)
  leg0 = ROOT.TLegend(0.40,0.58,0.88,0.88)
  leg0.SetBorderSize(0)
  leg0.SetFillColor(0)
  leg0.SetTextSize(0.045)
  leg0.SetTextFont(42)
  leg0.SetMargin(0.20)  
  leg0.SetNColumns(1)
  leg0.SetColumnSeparation(0.1)
  leg0.SetEntrySeparation(0.15)
  leg0.AddEntry(geffs_Radion_LL  , "Radions: LL category", "LP")
  leg0.AddEntry(geffs_BulkGrav_LL  , "Bulk gravitons: LL category", "LP")
  leg0.AddEntry(geffs_Radion_TT  , "Radions: TT category", "LP")
  leg0.AddEntry(geffs_BulkGrav_TT  , "Bulk gravitons: TT category", "LP")
  leg0.Draw()
  
  c0.RedrawAxis()
  
  iPos = 11
  CMS_lumi.relPosX = 0.04
  CMS_lumi.writeExtraText = 1
  CMS_lumi.extraText = "Simulation"
  CMS_lumi.lumi_13TeV = " "
  CMS_lumi.lumiTextOffset = 0.18
  
  CMS_lumi.CMS_lumi(c0, 4, iPos)
  c0.Update() 
  
  c0.SaveAs("../B2G-16-026-figures/ForPaper/"+"%s.pdf" % c0.GetName())
  c0.SaveAs("../B2G-16-026-figures/ForPaper/"+"%s.png" % c0.GetName())

plotEffs()
