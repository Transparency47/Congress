# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1579?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1579
- Title: PARTNER with ASEAN, CERN, and PIF Act
- Congress: 119
- Bill type: S
- Bill number: 1579
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2026-03-10T18:31:57Z
- Update date including text: 2026-03-10T18:31:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-06-05 - Committee: Committee on Foreign Relations. Ordered to be reported without amendment favorably.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-06-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 95.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-06-05 - Committee: Committee on Foreign Relations. Ordered to be reported without amendment favorably.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-06-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 95.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1579",
    "number": "1579",
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
    "title": "PARTNER with ASEAN, CERN, and PIF Act",
    "type": "S",
    "updateDate": "2026-03-10T18:31:57Z",
    "updateDateIncludingText": "2026-03-10T18:31:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 95.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-06-18",
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
      "text": "Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-01",
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
      "actionDate": "2025-05-01",
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
            "date": "2025-06-18T18:16:00Z",
            "name": "Reported By"
          },
          {
            "date": "2025-06-05T14:30:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-01T17:55:18Z",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "IL"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "NV"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1579is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1579\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mr. Risch (for himself, Ms. Duckworth , Mr. Ricketts , Ms. Cortez Masto , and Ms. Ernst ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo provide for the treatment of the Association of Southeast Asian Nations (ASEAN), the European Organization for Nuclear Research (CERN), and the Pacific Islands Forum (PIF) as international organizations for purposes of the International Organizations Immunities Act, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Providing Appropriate Recognition and Treatment Needed to Enhance Relations with ASEAN, CERN, and PIF Act or the PARTNER with ASEAN, CERN, and PIF Act .\n#### 2. Authorization to extend the provisions of the International Organizations Immunities Act to additional international organizations\n##### (a) Association of Southeast Asian Nations\nThe International Organizations Immunities Act ( 22 U.S.C. 288 et seq. ) is amended by adding at the end the following:\n18. Under such terms and conditions as the President shall determine, the President is authorized to extend the provisions of this title to the Association of Southeast Asian Nations (ASEAN) in the same manner, to the same extent, and subject to the same conditions, as it may be extended to a public international organization in which the United States participates pursuant to any treaty or under the authority of any Act of Congress authorizing such participation or making an appropriation for such participation. .\n##### (b) European Organization for Nuclear Research\nThe International Organizations Immunities Act, as amended by subsection (a), is further amended by adding at the end the following:\n19. Under such terms and conditions as the President shall determine, the President is authorized to extend the provisions of this title to the European Organization for Nuclear Research (CERN) in the same manner, to the same extent, and subject to the same conditions, as it may be extended to a public international organization in which the United States participates pursuant to any treaty or under the authority of any Act of Congress authorizing such participation or making an appropriation for such participation. .\n##### (c) Pacific Islands Forum\nThe International Organizations Immunities Act, as amended by subsections (a) and (b), is further amended by adding at the end the following:\n20. Under such terms and conditions as the President shall determine, the President is authorized to extend the provisions of this title to the Pacific Islands Forum (PIF) in the same manner, to the same extent, and subject to the same conditions, as it may be extended to a public international organization in which the United States participates pursuant to any treaty or under the authority of any Act of Congress authorizing such participation or making an appropriation for such participation. .",
      "versionDate": "2025-05-01",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1579rs.xml",
      "text": "II\nCalendar No. 95\n119th CONGRESS\n1st Session\nS. 1579\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mr. Risch (for himself, Ms. Duckworth , Mr. Ricketts , Ms. Cortez Masto , and Ms. Ernst ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nJune 18, 2025 Reported by Mr. Risch , without amendment\nA BILL\nTo provide for the treatment of the Association of Southeast Asian Nations (ASEAN), the European Organization for Nuclear Research (CERN), and the Pacific Islands Forum (PIF) as international organizations for purposes of the International Organizations Immunities Act, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Providing Appropriate Recognition and Treatment Needed to Enhance Relations with ASEAN, CERN, and PIF Act or the PARTNER with ASEAN, CERN, and PIF Act .\n#### 2. Authorization to extend the provisions of the International Organizations Immunities Act to additional international organizations\n##### (a) Association of Southeast Asian Nations\nThe International Organizations Immunities Act ( 22 U.S.C. 288 et seq. ) is amended by adding at the end the following:\n18. Under such terms and conditions as the President shall determine, the President is authorized to extend the provisions of this title to the Association of Southeast Asian Nations (ASEAN) in the same manner, to the same extent, and subject to the same conditions, as it may be extended to a public international organization in which the United States participates pursuant to any treaty or under the authority of any Act of Congress authorizing such participation or making an appropriation for such participation. .\n##### (b) European Organization for Nuclear Research\nThe International Organizations Immunities Act, as amended by subsection (a), is further amended by adding at the end the following:\n19. Under such terms and conditions as the President shall determine, the President is authorized to extend the provisions of this title to the European Organization for Nuclear Research (CERN) in the same manner, to the same extent, and subject to the same conditions, as it may be extended to a public international organization in which the United States participates pursuant to any treaty or under the authority of any Act of Congress authorizing such participation or making an appropriation for such participation. .\n##### (c) Pacific Islands Forum\nThe International Organizations Immunities Act, as amended by subsections (a) and (b), is further amended by adding at the end the following:\n20. Under such terms and conditions as the President shall determine, the President is authorized to extend the provisions of this title to the Pacific Islands Forum (PIF) in the same manner, to the same extent, and subject to the same conditions, as it may be extended to a public international organization in which the United States participates pursuant to any treaty or under the authority of any Act of Congress authorizing such participation or making an appropriation for such participation. .",
      "versionDate": "2025-05-01",
      "versionType": "Reported in Senate"
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
            "name": "ASEAN countries",
            "updateDate": "2025-06-12T18:27:25Z"
          },
          {
            "name": "Asia",
            "updateDate": "2025-06-12T18:27:32Z"
          },
          {
            "name": "Australia",
            "updateDate": "2025-06-12T18:30:32Z"
          },
          {
            "name": "Brunei",
            "updateDate": "2025-06-12T18:27:41Z"
          },
          {
            "name": "Burma",
            "updateDate": "2025-06-12T18:27:50Z"
          },
          {
            "name": "Cambodia",
            "updateDate": "2025-06-12T18:27:57Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-06-12T18:42:41Z"
          },
          {
            "name": "European Union",
            "updateDate": "2025-06-12T18:42:47Z"
          },
          {
            "name": "Fiji",
            "updateDate": "2025-06-12T18:40:53Z"
          },
          {
            "name": "France",
            "updateDate": "2025-06-12T18:41:05Z"
          },
          {
            "name": "Indonesia",
            "updateDate": "2025-06-12T18:28:04Z"
          },
          {
            "name": "International law and treaties",
            "updateDate": "2025-06-12T18:28:12Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2025-06-12T18:28:24Z"
          },
          {
            "name": "Japan",
            "updateDate": "2025-06-12T18:42:29Z"
          },
          {
            "name": "Kiribati",
            "updateDate": "2025-06-12T18:41:12Z"
          },
          {
            "name": "Laos",
            "updateDate": "2025-06-12T18:28:32Z"
          },
          {
            "name": "Malaysia",
            "updateDate": "2025-06-12T18:28:39Z"
          },
          {
            "name": "Marshall Islands",
            "updateDate": "2025-06-12T18:41:44Z"
          },
          {
            "name": "Micronesia",
            "updateDate": "2025-06-12T18:40:46Z"
          },
          {
            "name": "Nauru",
            "updateDate": "2025-06-12T18:41:18Z"
          },
          {
            "name": "New Zealand",
            "updateDate": "2025-06-12T18:41:24Z"
          },
          {
            "name": "Oceania",
            "updateDate": "2025-06-12T18:40:38Z"
          },
          {
            "name": "Palau",
            "updateDate": "2025-06-12T18:41:30Z"
          },
          {
            "name": "Papua New Guinea",
            "updateDate": "2025-06-12T18:41:38Z"
          },
          {
            "name": "Philippines",
            "updateDate": "2025-06-12T18:28:48Z"
          },
          {
            "name": "Russia",
            "updateDate": "2025-06-12T18:42:35Z"
          },
          {
            "name": "Samoa",
            "updateDate": "2025-06-12T18:41:51Z"
          },
          {
            "name": "Singapore",
            "updateDate": "2025-06-12T18:30:06Z"
          },
          {
            "name": "Solomon Islands",
            "updateDate": "2025-06-12T18:41:58Z"
          },
          {
            "name": "Thailand",
            "updateDate": "2025-06-12T18:30:14Z"
          },
          {
            "name": "Tonga",
            "updateDate": "2025-06-12T18:42:10Z"
          },
          {
            "name": "Tuvalu",
            "updateDate": "2025-06-12T18:42:15Z"
          },
          {
            "name": "Vanuatu",
            "updateDate": "2025-06-12T18:42:22Z"
          },
          {
            "name": "Vietnam",
            "updateDate": "2025-06-12T18:30:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-06-04T15:09:51Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1579is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1579rs.xml"
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
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "PARTNER with ASEAN, CERN, and PIF Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-06-21T02:53:16Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Providing Appropriate Recognition and Treatment Needed to Enhance Relations with ASEAN, CERN, and PIF Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-06-21T02:53:16Z"
    },
    {
      "title": "PARTNER with ASEAN, CERN, and PIF Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PARTNER with ASEAN, CERN, and PIF Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Providing Appropriate Recognition and Treatment Needed to Enhance Relations with ASEAN, CERN, and PIF Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the treatment of the Association of Southeast Asian Nations (ASEAN), the European Organization for Nuclear Research (CERN), and the Pacific Islands Forum (PIF) as international organizations for purposes of the International Organizations Immunities Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:27Z"
    }
  ]
}
```
