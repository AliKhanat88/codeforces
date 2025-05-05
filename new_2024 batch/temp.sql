{
  "page": 0,
  "pageCount": 0,
  "pageSize": 0,
  "totalCount": 0,
  "items": [
    {
      "vesselImo": 0,
      "port": "string",
      "arrivalTimeUtc": "2024-03-05T14:26:06.992Z",
      "departureTimeUtc": "2024-03-05T14:26:06.992Z",
      "voyage": "string",
      "summary": {
        "containersLoaded": {
          "fortyFeet": 0,
          "twentyFeet": 0,
          "fortyFiveFeet": 0,
          "daGo": 0,
          "reefer": 0,
          "empty": 0,
          "generalCargoWeight": 0,
          "totalTeu": 0,
          "totalWeight": 0
        },
        "containersDischarged": {
          "fortyFeet": 0,
          "twentyFeet": 0,
          "fortyFiveFeet": 0,
          "daGo": 0,
          "reefer": 0,
          "empty": 0,
          "generalCargoWeight": 0,
          "totalTeu": 0,
          "totalWeight": 0
        },
        "containersSailed": {
          "fortyFeet": 0,
          "twentyFeet": 0,
          "fortyFiveFeet": 0,
          "daGo": 0,
          "reefer": 0,
          "empty": 0,
          "generalCargoWeight": 0,
          "totalTeu": 0,
          "totalWeight": 0
        }
      }
    }
  ]
}

insert into [API_Normalized].[macs3].[CargoAnalysisResults]
select 
    main.imo,
    CAST(JSON_VALUE(sec.value, '$.vesselImo') as int) as vesselImo,
    CAST(JSON_VALUE(sec.value, '$.port') as nvarchar(50)) as port,
    CAST(JSON_VALUE(sec.value, '$.arrivalTimeUtc') as nvarchar(50)) as arrivalTimeUtc,
    CAST(JSON_VALUE(sec.value, '$.departureTimeUtc') as nvarchar(50)) as departureTimeUtc,
    CAST(JSON_VALUE(sec.value, '$.voyage') as nvarchar(50)) as voyage,
    CAST(JSON_VALUE(sec.value, '$.summary.containersLoaded.fortyFeet') as int) as summary_containersLoaded_fortyFeet,
    CAST(JSON_VALUE(sec.value, '$.summary.containersLoaded.twentyFeet') as int) as summary_containersLoaded_twentyFeet,
    CAST(JSON_VALUE(sec.value, '$.summary.containersLoaded.fortyFiveFeet') as int) as summary_containersLoaded_fortyFiveFeet,
    CAST(JSON_VALUE(sec.value, '$.summary.containersLoaded.daGo') as int) as summary_containersLoaded_daGo,
    CAST(JSON_VALUE(sec.value, '$.summary.containersLoaded.reefer') as int) as summary_containersLoaded_reefer,
    CAST(JSON_VALUE(sec.value, '$.summary.containersLoaded.empty') as int) as summary_containersLoaded_empty,
    CAST(JSON_VALUE(sec.value, '$.summary.containersLoaded.generalCargoWeight') as int) as summary_containersLoaded_generalCargoWeight,
    CAST(JSON_VALUE(sec.value, '$.summary.containersLoaded.totalTeu') as int) as summary_containersLoaded_totalTeu,
    CAST(JSON_VALUE(sec.value, '$.summary.containersLoaded.totalWeight') as int) as summary_containersLoaded_totalWeight
    CAST(JSON_VALUE(sec.value, '$.summary.containersDischarged.fortyFeet') as int) as summary_containersDischarged_fortyFeet,
    CAST(JSON_VALUE(sec.value, '$.summary.containersDischarged.twentyFeet') as int) as summary_containersDischarged_twentyFeet,
    CAST(JSON_VALUE(sec.value, '$.summary.containersDischarged.fortyFiveFeet') as int) as summary_containersDischarged_fortyFiveFeet,
    CAST(JSON_VALUE(sec.value, '$.summary.containersDischarged.daGo') as int) as summary_containersDischarged_daGo,
    CAST(JSON_VALUE(sec.value, '$.summary.containersDischarged.reefer') as int) as summary_containersDischarged_reefer,
    CAST(JSON_VALUE(sec.value, '$.summary.containersDischarged.empty') as int) as summary_containersDischarged_empty,
    CAST(JSON_VALUE(sec.value, '$.summary.containersDischarged.generalCargoWeight') as int) as summary_containersDischarged_generalCargoWeight,
    CAST(JSON_VALUE(sec.value, '$.summary.containersDischarged.totalTeu') as int) as summary_containersDischarged_totalTeu,
    CAST(JSON_VALUE(sec.value, '$.summary.containersDischarged.totalWeight') as int) as summary_containersDischarged_totalWeight,
    CAST(JSON_VALUE(sec.value, '$.summary.containersSailed.fortyFeet') as int) as summary_containersSailed_fortyFeet,
    CAST(JSON_VALUE(sec.value, '$.summary.containersSailed.twentyFeet') as int) as summary_containersSailed_twentyFeet,
    CAST(JSON_VALUE(sec.value, '$.summary.containersSailed.fortyFiveFeet') as int) as summary_containersSailed_fortyFiveFeet,
    CAST(JSON_VALUE(sec.value, '$.summary.containersSailed.daGo') as int) as summary_containersSailed_daGo,
    CAST(JSON_VALUE(sec.value, '$.summary.containersSailed.reefer') as int) as summary_containersSailed_reefer,
    CAST(JSON_VALUE(sec.value, '$.summary.containersSailed.empty') as int) as summary_containersSailed_empty,
    CAST(JSON_VALUE(sec.value, '$.summary.containersSailed.generalCargoWeight') as int) as summary_containersSailed_generalCargoWeight,
    CAST(JSON_VALUE(sec.value, '$.summary.containersSailed.totalTeu') as int) as summary_containersSailed_totalTeu,
    CAST(JSON_VALUE(sec.value, '$.summary.containersSailed.totalWeight') as int) as summary_containersSailed_totalWeight
from mainTableJson as main
cross apply openjson(main.rawdata, "$.items") as sec