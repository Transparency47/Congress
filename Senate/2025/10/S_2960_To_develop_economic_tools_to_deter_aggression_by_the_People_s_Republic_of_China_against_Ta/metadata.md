# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2960?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2960
- Title: Deter PRC Aggression Against Taiwan Act
- Congress: 119
- Bill type: S
- Bill number: 2960
- Origin chamber: Senate
- Introduced date: 2025-10-01
- Update date: 2026-05-14T15:31:18Z
- Update date including text: 2026-05-14T15:31:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-01: Introduced in Senate
- 2025-10-01 - IntroReferral: Introduced in Senate
- 2025-10-01 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 245.
- Latest action: 2025-10-01: Introduced in Senate

## Actions

- 2025-10-01 - IntroReferral: Introduced in Senate
- 2025-10-01 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 245.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-01",
    "latestAction": {
      "actionDate": "2025-10-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2960",
    "number": "2960",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "Deter PRC Aggression Against Taiwan Act",
    "type": "S",
    "updateDate": "2026-05-14T15:31:18Z",
    "updateDateIncludingText": "2026-05-14T15:31:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 245.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-22",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-01",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": [
          {
            "date": "2025-10-30T15:43:18Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-22T14:03:57Z",
            "name": "Markup By"
          },
          {
            "date": "2025-10-01T15:41:31Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "NH"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-16",
      "state": "DE"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-10-16",
      "state": "NE"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-11-03",
      "state": "CO"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-11-03",
      "state": "TX"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-03",
      "state": "NJ"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-11-03",
      "state": "NC"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-11-03",
      "state": "TN"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-11-03",
      "state": "FL"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-11-03",
      "state": "AR"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "OR"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "MS"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "PA"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2960is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2960\nIN THE SENATE OF THE UNITED STATES\nOctober 1, 2025 Mr. Risch introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo develop economic tools to deter aggression by the People's Republic of China against Taiwan.\n#### 1. Short title\nThis Act may be cited as the Deter PRC Aggression Against Taiwan Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that the United States must be prepared to take immediate action to impose sanctions with respect to any military or non-military entities owned, controlled, or acting at the direction of the Government of the PRC or the Chinese Communist Party that are supporting actions by the Government of the PRC or by the Chinese Communist Party\u2014\n**(1)**\nto overthrow or dismantle the governing institutions in Taiwan;\n**(2)**\nto occupy any territory controlled or administered by Taiwan;\n**(3)**\nto violate the territorial integrity of Taiwan; or\n**(4)**\nto take significant action against Taiwan, including\u2014\n**(A)**\nconducting a naval blockade of Taiwan;\n**(B)**\nseizing any outlying island of Taiwan; or\n**(C)**\nperpetrating a significant physical or cyber attack on Taiwan that erodes the ability of the governing institutions in Taiwan to operate or provide essential services to the citizens of Taiwan.\n#### 3. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate ;\n**(C)**\nthe Committee on Commerce, Science, and Transportation of the Senate ;\n**(D)**\nthe Committee on Finance of the Senate ;\n**(E)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(F)**\nthe Committee on Financial Services of the House of Representatives ;\n**(G)**\nthe Committee on Energy and Commerce of the House of Representatives ; and\n**(H)**\nthe Committee on Ways and Means of the House of Representatives .\n**(2) PRC**\nThe term PRC means the People's Republic of China.\n**(3) PRC sanctions task force; task force**\nThe terms PRC Sanctions Task Force and Task Force mean the task force established pursuant to section 4.\n#### 4. PRC Sanctions Task Force\n##### (a) Establishment\nNot later than 180 days after the date of the enactment of this Act, the Coordinator for Sanctions of the Department of State and the Director of the Office of Foreign Assets Control of the Department of the Treasury, in coordination with the Director of National Intelligence and the heads of other Federal agencies, as appropriate, shall establish an interagency task force to identify military and non-military entities that could be subject to sanctions or other economic actions imposed by the United States immediately following any action taken by the PRC that demonstrates an attempt to achieve, or has the significant effect of achieving, the physical or political control of Taiwan, including by taking any of the actions described in paragraphs (1) through (4) of section 2.\n##### (b) Strategy\nNot later than 180 days after the establishment of the PRC Sanctions Task Force, the Task Force shall provide a briefing to the appropriate congressional committees for identifying proposed targets for sanctions or other economic actions referred to in subsection (a), which shall\u2014\n**(1)**\nassess how existing sanctions programs could be used to impose sanctions with respect to entities identified by the Task Force;\n**(2)**\ndevelop or propose, as appropriate, new sanctions authorities that might be required to impose sanctions with respect to such entities;\n**(3)**\nanalyze the potential economic consequences to the United States, and to allies and partners of the United States, of imposing various types of such sanctions with respect to such entities;\n**(4)**\nassess measures that could be taken to mitigate the consequences referred to in paragraph (3), including through the use of licenses, exemptions, carve-outs, and other approaches;\n**(5)**\ninclude coordination with allies and partners of the United States\u2014\n**(A)**\nto leverage sanctions and other economic tools including actions targeting the PRC\u2019s financial and industrial sectors to deter or respond to aggression against Taiwan;\n**(B)**\nto identify and resolve potential impediments to coordinating sanctions-related efforts or other economic actions with respect to responding to or deterring aggression against Taiwan;\n**(C)**\nto identify industries, sectors, or goods and services where the United States and allies and partners of the United States can take coordinated action through sanctions or other economic tools that will have a significant negative impact on the economy of the PRC; and\n**(D)**\nto coordinate actions with partners and allies to provide economic support to Taiwan and other countries being threatened by the PRC, including measures to counter economic coercion by the PRC;\n**(6)**\nassess the resource gaps and needs at the Department of State, the Department of the Treasury, the Department of Commerce, the United States Trade Representative, and other Federal agencies, as appropriate, to most effectively use sanctions and other economic tools to respond to the threats posed by the PRC;\n**(7)**\nrecommend how best to target sanctions and other economic tools against individuals, entities, and economic sectors in the PRC, which shall take into account\u2014\n**(A)**\nthe role of such targets in supporting policies and activities of the Government of the PRC, or of the Chinese Communist Party, that pose a threat to the national security or foreign policy interests of the United States;\n**(B)**\nthe negative economic implications of such sanctions and tools for the Government of the PRC, including its ability to achieve its objectives with respect to Taiwan; and\n**(C)**\nthe potential impact of such sanctions and tools on the stability of the global financial system, including with respect to\u2014\n**(i)**\nstate-owned enterprises;\n**(ii)**\nofficials of the Government of the PRC and of the Chinese Communist Party;\n**(iii)**\nfinancial institutions associated with the Government of the PRC; and\n**(iv)**\ncompanies in the PRC that are not formally designated by the Government of the PRC as state-owned enterprises; and\n**(8)**\nidentify any foreign military or non-military entities that would likely be used to achieve the outcomes specified in section 2, including entities in the shipping, logistics, energy (including oil and gas), maritime, aviation, ground transportation, and technology sectors.\n#### 5. Annual report\nNot later than 180 days after the briefing required under section 4(b), and annually thereafter, the PRC Sanctions Task Force shall submit a classified report to the appropriate congressional committees that includes information regarding\u2014\n**(1)**\nany entities identified pursuant to section 4(b)(8);\n**(2)**\nany new authorities required to impose sanctions with respect to such entities;\n**(3)**\npotential economic impacts on the PRC, the United States, and allies and partners of the United States resulting from the imposition of sanctions with respect to such entities;\n**(4)**\nmitigation measures that could be employed to limit any deleterious economic impacts on the United States and allies and partners of the United States of such sanctions;\n**(5)**\nthe status of coordination with allies and partners of the United States regarding sanctions and other economic tools identified under this Act;\n**(6)**\nresource gaps and recommendations to enable the Department of State and the Department of the Treasury to use sanctions to more effectively respond to the malign activities of the Government of the PRC; and\n**(7)**\nany additional resources that may be necessary to carry out the strategies and recommendations included in the report submitted pursuant to section 4(b).",
      "versionDate": "2025-10-01",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2960rs.xml",
      "text": "II\nCalendar No. 245\n119th CONGRESS\n1st Session\nS. 2960\nIN THE SENATE OF THE UNITED STATES\nOctober 1, 2025 Mr. Risch (for himself, Mrs. Shaheen , Mr. Coons , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nOctober 30, 2025 Reported by Mr. Risch with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo develop economic tools to deter aggression by the People's Republic of China against Taiwan.\n#### 1. Short title\nThis Act may be cited as the Deter PRC Aggression Against Taiwan Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that the United States must be prepared to take immediate action to impose sanctions with respect to any military or non-military entities owned, controlled, or acting at the direction of the Government of the PRC or the Chinese Communist Party that are supporting actions by the Government of the PRC or by the Chinese Communist Party\u2014\n**(1)**\nto overthrow or dismantle the governing institutions in Taiwan;\n**(2)**\nto occupy any territory controlled or administered by Taiwan;\n**(3)**\nto violate the territorial integrity of Taiwan; or\n**(4)**\nto take significant action against Taiwan, including\u2014\n**(A)**\nconducting a naval blockade of Taiwan;\n**(B)**\nseizing any outlying island of Taiwan; or\n**(C)**\nperpetrating a significant physical or cyber attack on Taiwan that erodes the ability of the governing institutions in Taiwan to operate or provide essential services to the citizens of Taiwan.\n#### 3. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate ;\n**(C)**\nthe Committee on Commerce, Science, and Transportation of the Senate ;\n**(D)**\nthe Committee on Finance of the Senate ;\n**(E)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(F)**\nthe Committee on Financial Services of the House of Representatives ;\n**(G)**\nthe Committee on Energy and Commerce of the House of Representatives ; and\n**(H)**\nthe Committee on Ways and Means of the House of Representatives .\n**(2) PRC**\nThe term PRC means the People's Republic of China.\n**(3) PRC sanctions task force; task force**\nThe terms PRC Sanctions Task Force and Task Force mean the task force established pursuant to section 4.\n#### 4. PRC Sanctions Task Force\n##### (a) Establishment\nNot later than 180 days after the date of the enactment of this Act, the Coordinator for Sanctions of the Department of State and the Director of the Office of Foreign Assets Control of the Department of the Treasury, in coordination with the Director of National Intelligence and the heads of other Federal agencies, as appropriate, shall establish an interagency task force to identify military and non-military entities that could be subject to sanctions or other economic actions imposed by the United States immediately following any action taken by the PRC that demonstrates an attempt to achieve, or has the significant effect of achieving, the physical or political control of Taiwan, including by taking any of the actions described in paragraphs (1) through (4) of section 2.\n##### (b) Strategy\nNot later than 180 days after the establishment of the PRC Sanctions Task Force, the Task Force shall provide a briefing to the appropriate congressional committees for identifying proposed targets for sanctions or other economic actions referred to in subsection (a), which shall\u2014\n**(1)**\nassess how existing sanctions programs could be used to impose sanctions with respect to entities identified by the Task Force;\n**(2)**\ndevelop or propose, as appropriate, new sanctions authorities that might be required to impose sanctions with respect to such entities;\n**(3)**\nanalyze the potential economic consequences to the United States, and to allies and partners of the United States, of imposing various types of such sanctions with respect to such entities;\n**(4)**\nassess measures that could be taken to mitigate the consequences referred to in paragraph (3), including through the use of licenses, exemptions, carve-outs, and other approaches;\n**(5)**\ninclude coordination with allies and partners of the United States\u2014\n**(A)**\nto leverage sanctions and other economic tools including actions targeting the PRC\u2019s financial and industrial sectors to deter or respond to aggression against Taiwan;\n**(B)**\nto identify and resolve potential impediments to coordinating sanctions-related efforts or other economic actions with respect to responding to or deterring aggression against Taiwan;\n**(C)**\nto identify industries, sectors, or goods and services where the United States and allies and partners of the United States can take coordinated action through sanctions or other economic tools that will have a significant negative impact on the economy of the PRC; and\n**(D)**\nto coordinate actions with partners and allies to provide economic support to Taiwan and other countries being threatened by the PRC, including measures to counter economic coercion by the PRC;\n**(6)**\nassess the resource gaps and needs at the Department of State, the Department of the Treasury, the Department of Commerce, the United States Trade Representative, and other Federal agencies, as appropriate, to most effectively use sanctions and other economic tools to respond to the threats posed by the PRC;\n**(7)**\nrecommend how best to target sanctions and other economic tools against individuals, entities, and economic sectors in the PRC, which shall take into account\u2014\n**(A)**\nthe role of such targets in supporting policies and activities of the Government of the PRC, or of the Chinese Communist Party, that pose a threat to the national security or foreign policy interests of the United States;\n**(B)**\nthe negative economic implications of such sanctions and tools for the Government of the PRC, including its ability to achieve its objectives with respect to Taiwan; and\n**(C)**\nthe potential impact of such sanctions and tools on the stability of the global financial system, including with respect to\u2014\n**(i)**\nstate-owned enterprises;\n**(ii)**\nofficials of the Government of the PRC and of the Chinese Communist Party;\n**(iii)**\nfinancial institutions associated with the Government of the PRC; and\n**(iv)**\ncompanies in the PRC that are not formally designated by the Government of the PRC as state-owned enterprises; and\n**(8)**\nidentify any foreign military or non-military entities that would likely be used to achieve the outcomes specified in section 2, including entities in the shipping, logistics, energy (including oil and gas), maritime, aviation, ground transportation, and technology sectors.\n#### 5. Annual report\nNot later than 180 days after the briefing required under section 4(b), and annually thereafter, the PRC Sanctions Task Force shall submit a classified report to the appropriate congressional committees that includes information regarding\u2014\n**(1)**\nany entities identified pursuant to section 4(b)(8);\n**(2)**\nany new authorities required to impose sanctions with respect to such entities;\n**(3)**\npotential economic impacts on the PRC, the United States, and allies and partners of the United States resulting from the imposition of sanctions with respect to such entities;\n**(4)**\nmitigation measures that could be employed to limit any deleterious economic impacts on the United States and allies and partners of the United States of such sanctions;\n**(5)**\nthe status of coordination with allies and partners of the United States regarding sanctions and other economic tools identified under this Act;\n**(6)**\nresource gaps and recommendations to enable the Department of State and the Department of the Treasury to use sanctions to more effectively respond to the malign activities of the Government of the PRC; and\n**(7)**\nany additional resources that may be necessary to carry out the strategies and recommendations included in the report submitted pursuant to section 4(b).",
      "versionDate": "2025-10-30",
      "versionType": "Reported in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-05-07",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "8693",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Deter PRC Aggression Against Taiwan Act",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2026-04-01T20:26:46Z"
          },
          {
            "name": "Asia",
            "updateDate": "2026-04-01T20:26:26Z"
          },
          {
            "name": "China",
            "updateDate": "2026-04-01T20:26:19Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-01T20:26:53Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2026-04-01T20:26:40Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2026-04-01T20:26:32Z"
          },
          {
            "name": "Taiwan",
            "updateDate": "2026-04-01T20:26:12Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-11-19T21:18:01Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2960is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2960rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Deter PRC Aggression Against Taiwan Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T12:03:23Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Deter PRC Aggression Against Taiwan Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-01T03:38:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Deter PRC Aggression Against Taiwan Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T06:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to develop economic tools to deter aggression by the People's Republic of China against Taiwan.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T06:18:16Z"
    }
  ]
}
```
