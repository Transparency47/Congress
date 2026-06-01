# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6834?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6834
- Title: STORE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6834
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-05-22T08:08:12Z
- Update date including text: 2026-05-22T08:08:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6834",
    "number": "6834",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "STORE Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:12Z",
    "updateDateIncludingText": "2026-05-22T08:08:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:05:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-20T14:38:16Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
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
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "WA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "OR"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6834ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6834\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Ms. Bonamici (for herself, Ms. Schrier , Ms. Salinas , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo address infrastructure needs for food banks serving rural communities and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Transportation Organization and Refrigeration Expansion Act of 2025 or STORE Act of 2025 .\n#### 2. Improving the EFAP infrastructure grants program\nSection 209 of the Emergency Food Assistance Act of 1983 ( 7 U.S.C. 7511a ) is amended\u2014\n**(1)**\nin subsection (a) by striking an emergency feeding organization and inserting the State agency designated by a State in the State plan required by section 202A ( 7 U.S.C. 7503 ) ,\n**(2)**\nin subsection (b)(2)\u2014\n**(A)**\nby striking the heading and inserting Preference ,\n**(B)**\nby inserting Tribal, low income, and remote before communities , and\n**(C)**\nin subparagraph (A) by striking and inserting rural with these ,\n**(3)**\nin subsection (c)\u2014\n**(A)**\nby striking carry out activities of the eligible entity and inserting distribute grant amounts to support activities ,\n**(B)**\nin paragraph (1) by striking for the tracking of time-sensitive food products and inserting needed to safely and efficiently distribute food to people in need ,\n**(C)**\nin paragraph (2) by striking time-sensitive and perishable food products and inserting commodities provided by the Secretary under this Act and commodities secured from other sources ,\n**(D)**\nin paragraph (3)\u2014\n**(i)**\nby striking through the support of small or mid-size farms and ranches, fisheries, and aquaculture, and donations from local food producers and manufacturers to persons in need , and\n**(ii)**\nby inserting , including expanding mobile and home delivery options and assessments or professional studies of outreach activities after United States ,\n**(E)**\nin paragraph (4) by inserting , governmental, and Tribal after nonprofit ,\n**(F)**\nin paragraph (5)\u2014\n**(i)**\nin subparagraph (B) by inserting , governmental, and Tribal after nonprofit , and\n**(ii)**\nin subparagraph (C)\u2014\n**(I)**\nby striking rural areas and inserting underserved areas identified in subsection (b)(2) , and\n**(II)**\nby striking and at the end,\n**(G)**\nin paragraph (6)\u2014\n**(i)**\nby striking constructing and inserting renovating , and\n**(ii)**\nby striking the period at the end and inserting ; and , and\n**(H)**\nby adding at the end the following:\n(7) not more than 10 percent of such grant for administrative costs to carry this section. , and\n**(4)**\nin subsection (d) by striking $15,000,000 and all that follows through 2023 , and inserting $25,000,000 for each of the fiscal years 2026 through 2030 .\n#### 3. Report on cold storage needs nationally\n##### (a) Report\nNot later than 2 years after the date of the enactment of this Act, the Secretary of Agriculture shall carry out a study and produce a report\u2014\n**(1)**\non the shortages to meet the total emergency food needs for refrigerated and frozen storage space, as well as refrigerated trucks and other delivery vehicles, for use by emergency food organizations to meet the needs of their communities, and\n**(2)**\nan estimate of the cost to meet the needs of all emergency food organizations, including food banks and food pantries, nationally for new coolers, freezers, refrigerated and dry trucks, and trailers.\n##### (b) Definitions\nIn this section\u2014\n**(1) Emergency food organization**\nThe term emergency food organization has the meaning given it in section 2 of the Emergency Food Assistance Act of 1983 ( 7 U.S.C. 7501 ) and is not otherwise limited to relevant organizations participating in the emergency food assistance program under such Act.\n**(2) Shortages**\nThe term shortages means meeting the total emergency food needs of the community, group, school, network, region, town, city, state, or otherwise relevant area an emergency feeding organization serves.\n##### (c) Appropriations\nThere is appropriated, out of any funds in the Treasury not otherwise appropriated, $1,000,000, to remain available until expended, to carry out this section.",
      "versionDate": "2025-12-18",
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
        "updateDate": "2026-01-16T19:01:12Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6834ih.xml"
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
      "title": "STORE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STORE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T05:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Transportation Organization and Refrigeration Expansion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T05:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To address infrastructure needs for food banks serving rural communities and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T05:33:30Z"
    }
  ]
}
```
