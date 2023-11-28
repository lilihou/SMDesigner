# SMDesigner 0.1
SMDesinger is a tool used to design mutation for structure ncRNAs according to structure information. These mutations have potentially affected the function of ncRNAs.

## input file: .sto file
eg:   # STOCKHOLM 1.0
      CP011599.1/36880-36951     GGAGCAGCAACGAUGUUACGCAGCAGGGCAGUCGCCCUAAAACAAAGUUAGGCCGCAUG--GACACA---A-CGCAGG
      CP000650.1/38256-38185     GGAGCAGCAACGAUGUUACGCAGCAGGGCAGUCGCCCUAAAACAAGGUUAGGCCGCAUG--GACACA---A-CGCAGG
      CP018135.1/1913478-1913552 GGAGCAGCAACGAUGUUACGCAGCAGGGCAGUCGCCCUAAAACAAAGUUAGGCAUCAUGGGUGAAUU---UUUCCCUG
      CP018839.1/285461-285385   GGAGCAGCAACGAUGUUACGCAGCAGGGCAGUCGCCCUAAAACAAAGUUA-GCCGAGAGGAGAAACUAUGUCUGCAAA
      #=GC SS_cons               :::[,<-<<____>>->,,((-((,<<<<____>>>><<<_______>>>,))-)),,<-<<___>>...->,,]:::
      #=GC RF                    GGAGCAGCAACGAUGUUACgcAGCAGGGCAGUCGCCCUAAAACAAAGUUAGGCcgcAugGggAaAcc...ucugCaag
      //

## output file: .fa file 
output file includes wild type sequence and two type mutation sequences 
eg:   >w1_CP000930.2/563090-563271/1-182_189
      ACGGUUACCCUUGUUGCAGGUGCCGCUGAGCGGCUGAAAAGGGAAUGAGGUGUAAAGCCUCAGCAGCCCCCGCUACUGUAAGGGAAGACGACCCGCCACAGAUCCACUGGACUUCGGUCUGGGAAGGAGGCGGGAGCGGAUGACGCCCGAGCCAGGAGACCUGCCUGCGACAAACGAAAGAC
      >m1_1_CP000930.2/563090-563271/1-182_189
      ACGGUUACCCUUGUUGCAGGUGCCGCUGAGCGGCUGAAAAGGGAAUGAGGUGUAAAGCCUCAGCAGCCCCCGCUACUGUAAGGGAAGACGACCCGGCACAGAUGCACUGGACUUCGGUCUGGGAAGGAGGCGGGAGCGGAUGACGCCCGAGCCAGGAGACCUGCCUGCGACAAACGAAAGAC
      >m1_2_CP000930.2/563090-563271/1-182_189
      ACGGUUACCCUUGUUGCAGGUGCCGCUGAGCGGCUGAAAAGGGAAUGAGGUGUAAAGCCUCAGCAGCCCCCGCUACUGUAAGGGAAGACGACCCGGCACAGAUGCACUGGACUUCGGUCUGGGAAGCAGCCGGGAGCGGAUGACGCCCGAGCCAGGAGACCUGCCUGCGACAAACGAAAGAC
