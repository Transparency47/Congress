# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5551?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5551
- Title: Balanced Agricultural Support and Efficiency Act
- Congress: 119
- Bill type: HR
- Bill number: 5551
- Origin chamber: House
- Introduced date: 2025-09-23
- Update date: 2025-11-25T16:14:21Z
- Update date including text: 2025-11-25T16:14:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-23: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-09-23: Introduced in House

## Actions

- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-23",
    "latestAction": {
      "actionDate": "2025-09-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5551",
    "number": "5551",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "J000301",
        "district": "",
        "firstName": "Dusty",
        "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
        "lastName": "Johnson",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Balanced Agricultural Support and Efficiency Act",
    "type": "HR",
    "updateDate": "2025-11-25T16:14:21Z",
    "updateDateIncludingText": "2025-11-25T16:14:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-23",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-23",
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
          "date": "2025-09-23T13:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5551ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5551\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 23, 2025 Mr. Johnson of South Dakota (for himself and Ms. Budzinski ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Act of 2014 to require a one-time update of base acres for covered commodities to ensure base acres reflect recent planting history, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Balanced Agricultural Support and Efficiency Act .\n#### 2. Mandatory base acres\n##### (a) Definitions\nSection 1111 of the Agricultural Act of 2014 ( 7 U.S.C. 9011 ) is amended\u2014\n**(1)**\nby striking paragraph (4) and inserting the following:\n(4) Base acres The term base acres , with respect to a covered commodity on a farm, means the number of acres determined for a farm under section 1112. ;\n**(2)**\nby striking paragraph (10); and\n**(3)**\nby redesignating paragraphs (11) through (26) as paragraphs (10) through (25), respectively.\n##### (b) Base acres\nSection 1112 of the Agricultural Act of 2014 ( 7 U.S.C. 9012 ) is amended\u2014\n**(1)**\nby striking subsection (a) and inserting the following:\n(a) Mandatory one-Time update of base acres (1) In general As soon as practicable after the date of enactment of the Balanced Agricultural Support and Efficiency Act, the Secretary shall update the base acres on a farm, as in effect under this title on the day before the date of enactment of that Act, for the 2025 crop year in accordance with this section. (2) Mandatory update For the purpose of applying this title to covered commodities, the Secretary shall determine the base acres on a farm by updating all of the base acres for covered commodities on the farm among those covered commodities planted on the farm at any time during the 2020 through 2024 crop years. (3) Update formula The updated base acres among covered commodities on a farm shall be the proportion that\u2014 (A) the 5-year average of\u2014 (i) the acreage planted on the farm to each covered commodity for harvest, grazing, haying, silage, or other similar purposes for the 2020 through 2024 crop years; and (ii) any acreage on the farm that the producers were prevented from planting during the 2020 through 2024 crop years to that covered commodity because of drought, flood, or other natural disaster, or other condition beyond the control of the producers, as determined by the Secretary; bears to (B) the 5-year average of\u2014 (i) the acreage planted on the farm to all covered commodities for harvest, grazing, haying, silage, or other similar purposes for the 2020 through 2024 crop years; and (ii) any acreage on the farm that the producers were prevented from planting during the 2020 through 2024 crop years to covered commodities because of drought, flood, or other natural disaster, or other condition beyond the control of the producers, as determined by the Secretary. (4) Inclusion of all 5 years in average For the purpose of determining a 5-year acreage average under paragraph (3) for a farm, the Secretary shall not exclude any crop year in which a covered commodity was not planted. (5) Treatment of multiple planting or prevented planting For the purpose of determining under paragraph (3) the acreage on a farm that producers planted or were prevented from planting during the 2020 through 2024 crop years to covered commodities, if the acreage that was planted or prevented from being planted was devoted to another covered commodity in the same crop year (other than a covered commodity produced under an established practice of double cropping), the owner\u2014 (A) may elect the commodity to be used for that crop year in determining the 5-year average; but (B) may not include both the initial commodity and the subsequent commodity. ;\n**(2)**\nin subsection (b)(1), in the matter preceding subparagraph (A), by striking Notwithstanding the election and all that follows through circumstances occur: and inserting the following: Notwithstanding subsection (a), the Secretary shall provide for an adjustment, as appropriate, in the base acres for covered commodities for a farm whenever any of the following circumstances occur: ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking the election made under ;\n**(ii)**\nby striking , including generic base acres each place it appears; and\n**(iii)**\nby striking or generic base acres ; and\n**(B)**\nin paragraph (3), by striking or generic base acres ; and\n**(4)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1)(A), by striking or generic base acres ; and\n**(B)**\nin paragraph (2)(A), in the matter preceding clause (i), by striking , including any generic base acres, .\n##### (c) Conforming amendments\n**(1) Payment yields**\nSection 1113(c)(1) of the Agricultural Act of 2014 (7 U.S.C. 9013(c)(l)) is amended by striking established or that is planted on generic base acres, and inserting established, .\n**(2) Payment acres**\nSection 1114 of the Agricultural Act of 2014 ( 7 U.S.C. 9014 ) is amended\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (1), by striking subsection (e) and inserting subsection (d) ; and\n**(ii)**\nin paragraph (2), by striking subsection (e) and inserting subsection (d) ;\n**(B)**\nby striking subsections (b) and (f); and\n**(C)**\nby redesignating subsections (c), (d), and (e) as subsections (b), (c), and (d), respectively.\n**(3) Price loss coverage**\nSection 1116(g) of the Agricultural Act of 2014 ( 7 U.S.C. 9016(g) ) is amended, in the matter preceding paragraph (1), by striking (19) and inserting (18) .",
      "versionDate": "2025-09-23",
      "versionType": "Introduced in House"
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
        "name": "Agriculture and Food",
        "updateDate": "2025-11-25T16:14:21Z"
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
      "date": "2025-09-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5551ih.xml"
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
      "title": "Balanced Agricultural Support and Efficiency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T06:08:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Balanced Agricultural Support and Efficiency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T06:08:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Act of 2014 to require a one-time update of base acres for covered commodities to ensure base acres reflect recent planting history, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T06:03:26Z"
    }
  ]
}
```
