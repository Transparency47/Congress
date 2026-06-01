# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5841?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5841
- Title: Boosting Benefits and COLAs for Seniors Act
- Congress: 119
- Bill type: HR
- Bill number: 5841
- Origin chamber: House
- Introduced date: 2025-10-28
- Update date: 2025-12-05T21:50:32Z
- Update date including text: 2026-05-28T16:27:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-28: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-28 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-10-28: Introduced in House

## Actions

- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-28 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5841",
    "number": "5841",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "B001315",
        "district": "13",
        "firstName": "Nikki",
        "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
        "lastName": "Budzinski",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Boosting Benefits and COLAs for Seniors Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:50:32Z",
    "updateDateIncludingText": "2026-05-28T16:27:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
        "item": {
          "date": "2025-10-28T17:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-10-28T17:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "FL"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "RI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5841ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5841\nIN THE HOUSE OF REPRESENTATIVES\nOctober 28, 2025 Ms. Budzinski (for herself, Ms. Lois Frankel of Florida , and Mr. Magaziner ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title II of the Social Security Act to require the Commissioner of Social Security to use the Consumer Price Index for Elderly Consumers for purposes of determining cost-of-living adjustments under titles II, VIII, and XVI of the Social Security Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Boosting Benefits and COLAs for Seniors Act .\n#### 2. More accurate cost-of-living adjustment\n##### (a) In general\n**(1) In general**\nSection 215(i)(1)(D) of the Social Security Act ( 42 U.S.C. 415(i)(1)(D) ) is amended by striking Consumer Price Index and all that follows through such index and inserting Consumer Price Index for Urban Wage Earners and Clerical Workers (CPI\u2013W, as published by the Bureau of Labor Statistics of the Department of Labor) or Consumer Price Index for Elderly Consumers (CPI\u2013E, as published by such Bureau) (whichever such index results in the higher percentage under this subparagraph) exceeds the same such index .\n**(2) Conforming amendment**\nSection 215(i)(1)(G) of the Social Security Act ( 42 U.S.C. 415(i)(1)(G) ) is amended by inserting applicable for purposes of subparagraph (D) after Consumer Price Index .\n##### (b) Application to pre-1979 law\n**(1) In general**\nSection 215(i) of the Social Security Act as in effect in December 1978, and as applied in certain cases under the provisions of such Act as in effect after December 1978, is amended\u2014\n**(A)**\nin paragraph (1)(B), by striking Consumer Price Index and all that follows through such Index and inserting Consumer Price Index for Urban Wage Earners and Clerical Workers (CPI\u2013W, as published by the Bureau of Labor Statistics of the Department of Labor) or Consumer Price Index for Elderly Consumers (CPI\u2013E, as published by such Bureau of such Department) (whichever such index results in the higher per centum under this subparagraph) exceeds, by not less than 3 per centum, the same such Index ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A)(ii), by striking Consumer Price Index for such cost-of-living computation quarter and inserting Consumer Price Index applicable for such year under paragraph (1)(B) ; and\n**(ii)**\nin subparagraph (C)(i), by striking Consumer Price Index as published for any month exceeds by 2.5 percent or more the level of such index and inserting Consumer Price Index for Urban Wage Earners and Clerical Workers or Consumer Price Index for Elderly Consumers as published for any month exceeds by 2.5 percent or more the level of such index .\n**(2) Conforming changes**\nSection 215(i)(4) of the Social Security Act ( 42 U.S.C. 415(i)(4) ) is amended\u2014\n**(A)**\nby striking and by section 9001 and inserting , section 9001 ; and\n**(B)**\nby inserting and section 2 of the Boosting Benefits and COLAs for Seniors Act , after 1986, .\n##### (c) No effect on adjustments under other laws\nSection 215(i) of the Social Security Act ( 42 U.S.C. 415(i) ) is amended by adding at the end the following:\n(6) With respect to any provision of law (other than in this title, title VIII, or title XVI) which provides for an adjustment of an amount under such provision of law in the same percentage as a cost-of-living adjustment applied to benefit amounts under this title, such provision of law shall be applied and administered as if the percentage of such cost-of-living adjustment applied to benefit amounts under this title were determined without regard to the amendments made by subsections (a) and (b) of section 2 of the Boosting Benefits and COLAs for Seniors Act . .\n##### (d) Publication of Consumer Price Index for Elderly Consumers\nThe Bureau of Labor Statistics of the Department of Labor shall prepare and publish an index for each calendar month to be known as the Consumer Price Index for Elderly Consumers that indicates changes over time in expenditures for consumption which are typical for individuals in the United States who have attained age 62.\n##### (e) Transition rule\nPrior to the publication of the Consumer Price Index for Elderly Consumers (CPI\u2013E) pursuant to subsection (d), the reference to such index made in each of the amendments made by subsections (a) and (b) shall be deemed to be a reference to the research price index prepared by the Bureau of Labor Statistics of the Department of Labor known as the Consumer Price Index for Americans 62 years of age and older (R\u2013CPI\u2013E).\n##### (f) Effective date\nThe amendments made by this section shall apply to determinations made with respect to cost-of-living computation quarters (as defined in section 215(i)(1)(B) of the Social Security Act ( 42 U.S.C. 415(i)(1)(B) )) ending on or after September 30, 2026.",
      "versionDate": "2025-10-28",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-10-27",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3059",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Boosting Benefits and COLAs for Seniors Act",
      "type": "S"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-11-26T15:57:58Z"
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
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5841ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Boosting Benefits and COLAs for Seniors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T09:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Boosting Benefits and COLAs for Seniors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T09:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title II of the Social Security Act to require the Commissioner of Social Security to use the Consumer Price Index for Elderly Consumers for purposes of determining cost-of-living adjustments under titles II, VIII, and XVI of the Social Security Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T09:03:16Z"
    }
  ]
}
```
