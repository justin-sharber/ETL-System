-- T-Mobile Bronze Layer - Merged-Insert
MERGE `netspark-database.raw_input.tmobile_upfront_raw` T
USING `netspark-database.load.tmobile_upfront_load` S
ON T.CheckNumber = S.CheckNumber
    AND T.ActivityType = S.ActivityType
    AND T.ServiceUniversalID = S.ServiceUniversalID

WHEN NOT MATCHED THEN
INSERT (Month, CheckNumber, CustomerName, BAN, ActDate, DeactDate, ReactDate, ProductType, ActivityType, ServiceUniversalID, DealerCode, DealerName, Coop, Spiff, Commission, Deposit, MonthlyAccess, PlanCode, MarketCode, KeyID, LineOfServiceID, ServiceNumber, SIM, IMEI, ContractTerm, CreditClass, CreditType, PretoPostMigration, HandSetOfferTypeIndicator, SubdealerID, ProdCatDescription, ContractID, OrderID, ContractHolderCode, isEligible, NonCommissionableReason, Source, AccountTypeID, AccountSubTypeID, LastUpgradedate, OrigLineActDate, OriginalLineMRC, OriginalTotalMRC, ActivatingStoreID, DensityClass, LeadTransferDate, LeadCreationDate, PortInCarrier, BTS, InStorePickup, SameMonth, LastSuspendDate, InsiderDiscountFlag, TransactionSource, UploadDate)

VALUES (S.Month, S.CheckNumber, S.CustomerName, S.BAN, S.ActDate, S.DeactDate, S.ReactDate, S.ProductType, S.ActivityType, S.ServiceUniversalID, S.DealerCode, S.DealerName, S.Coop, S.Spiff, S.Commission, S.Deposit, S.MonthlyAccess, S.PlanCode, S.MarketCode, S.KeyID, S.LineOfServiceID, S.ServiceNumber, S.SIM, S.IMEI, S.ContractTerm, S.CreditClass, S.CreditType, S.PretoPostMigration, S.HandSetOfferTypeIndicator, S.SubdealerID, S.ProdCatDescription, S.ContractID, S.OrderID, S.ContractHolderCode, S.isEligible, S.NonCommissionableReason, S.Source, S.AccountTypeID, S.AccountSubTypeID, S.LastUpgradedate, S.OrigLineActDate, S.OriginalLineMRC, S.OriginalTotalMRC, S.ActivatingStoreID, S.DensityClass, S.LeadTransferDate, S.LeadCreationDate, S.PortInCarrier, S.BTS, S.InStorePickup, S.SameMonth, S.LastSuspendDate, S.InsiderDiscountFlag, S.TransactionSource, S.UploadDate);
