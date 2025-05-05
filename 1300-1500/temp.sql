truncate table [API_Normalized].[btr].[ShipsJSON]

truncate table [API_json].[btr].[ShipsJSON]




USE [APIBackup]
GO

/****** Object:  Table [btr].[Macs3.ApiName]    Script Date: 02/12/2023 03:20 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [btr].[Macs3.ApiName](
	[GUID] [uniqueidentifier] NOT NULL,
	[imo] [int] NULL,
	[vesselImo] [int] NULL,
	[port] [nvarchar](100) NULL,
	[arrivalTimeUtc] [nvarchar](100) NULL,
	[departureTimeUtc] [nvarchar](100) NULL,
	[voyage] [nvarchar](100) NULL,
	[containersLoaded_fortyFeet] [float] NULL,
	[containersLoaded_twentyFeet] [float] NULL,
	[containersLoaded_fortyFiveFeet] [float] NULL,
	[containersLoaded_daGo] [float] NULL,
	[containersLoaded_reefer] [float] NULL,
	[containersLoaded_empty] [float] NULL,
	[containersLoaded_generalCargoWeight] [float] NULL,
	[containersLoaded_totalTeu] [float] NULL,
	[containersLoaded_totalWeight] [float] NULL,
	[containersDischarged_fortyFeet] [float] NULL,
	[containersDischarged_twentyFeet] [float] NULL,
	[containersDischarged_fortyFiveFeet] [float] NULL,
	[containersDischarged_daGo] [float] NULL,
	[containersDischarged_reefer] [float] NULL,
	[containersDischarged_empty] [float] NULL,
	[containersDischarged_generalCargoWeight] [float] NULL,
	[containersDischarged_totalTeu] [float] NULL,
	[containersDischarged_totalWeight] [float] NULL,
	[containersSailed_fortyFeet] [float] NULL,
	[containersSailed_twentyFeet] [float] NULL,
	[containersSailed_fortyFiveFeet] [float] NULL,
	[containersSailed_daGo] [float] NULL,
	[containersSailed_reefer] [float] NULL,
	[containersSailed_empty] [float] NULL,
	[containersSailed_generalCargoWeight] [float] NULL,
	[containersSailed_totalTeu] [float] NULL,
	[containersSailed_totalWeight] [float] NULL,
	[load_id] [int] NULL
) ON [PRIMARY]
GO

insert into [btr].[Macs3.ApiName](
		[GUID],
		[imo]
      ,[vesselImo]
      ,[port]
      ,[arrivalTimeUtc]
      ,[departureTimeUtc]
      ,[voyage]
      ,[containersLoaded_fortyFeet]
      ,[containersLoaded_twentyFeet]
      ,[containersLoaded_fortyFiveFeet]
      ,[containersLoaded_daGo]
      ,[containersLoaded_reefer]
      ,[containersLoaded_empty]
      ,[containersLoaded_generalCargoWeight]
      ,[containersLoaded_totalTeu]
      ,[containersLoaded_totalWeight]
      ,[containersDischarged_fortyFeet]
      ,[containersDischarged_twentyFeet]
      ,[containersDischarged_fortyFiveFeet]
      ,[containersDischarged_daGo]
      ,[containersDischarged_reefer]
      ,[containersDischarged_empty]
      ,[containersDischarged_generalCargoWeight]
      ,[containersDischarged_totalTeu]
      ,[containersDischarged_totalWeight]
      ,[containersSailed_fortyFeet]
      ,[containersSailed_twentyFeet]
      ,[containersSailed_fortyFiveFeet]
      ,[containersSailed_daGo]
      ,[containersSailed_reefer]
      ,[containersSailed_empty]
      ,[containersSailed_generalCargoWeight]
      ,[containersSailed_totalTeu]
      ,[containersSailed_totalWeight]
      ,[load_id])



SELECT NEWID()
      ,[imo]
      ,[vesselImo]
      ,[port]
      ,[arrivalTimeUtc]
      ,[departureTimeUtc]
      ,[voyage]
      ,[containersLoaded_fortyFeet]
      ,[containersLoaded_twentyFeet]
      ,[containersLoaded_fortyFiveFeet]
      ,[containersLoaded_daGo]
      ,[containersLoaded_reefer]
      ,[containersLoaded_empty]
      ,[containersLoaded_generalCargoWeight]
      ,[containersLoaded_totalTeu]
      ,[containersLoaded_totalWeight]
      ,[containersDischarged_fortyFeet]
      ,[containersDischarged_twentyFeet]
      ,[containersDischarged_fortyFiveFeet]
      ,[containersDischarged_daGo]
      ,[containersDischarged_reefer]
      ,[containersDischarged_empty]
      ,[containersDischarged_generalCargoWeight]
      ,[containersDischarged_totalTeu]
      ,[containersDischarged_totalWeight]
      ,[containersSailed_fortyFeet]
      ,[containersSailed_twentyFeet]
      ,[containersSailed_fortyFiveFeet]
      ,[containersSailed_daGo]
      ,[containersSailed_reefer]
      ,[containersSailed_empty]
      ,[containersSailed_generalCargoWeight]
      ,[containersSailed_totalTeu]
      ,[containersSailed_totalWeight]
      ,[load_id]
  FROM [API_Normalized].[btr].[Macs3.ApiName]























