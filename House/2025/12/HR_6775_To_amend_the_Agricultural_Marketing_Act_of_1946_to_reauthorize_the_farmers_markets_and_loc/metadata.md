# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6775?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6775
- Title: New Markets for Farmers and Families Act
- Congress: 119
- Bill type: HR
- Bill number: 6775
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-05-22T08:08:50Z
- Update date including text: 2026-05-22T08:08:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-05-20 - Committee: Referred to the Subcommittee on Forestry and Horticulture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6775",
    "number": "6775",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "U000040",
        "district": "14",
        "firstName": "Lauren",
        "fullName": "Rep. Underwood, Lauren [D-IL-14]",
        "lastName": "Underwood",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "New Markets for Farmers and Families Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:50Z",
    "updateDateIncludingText": "2026-05-22T08:08:50Z"
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
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Forestry and Horticulture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:08:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-20T14:27:17Z",
              "name": "Referred to"
            }
          },
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6775ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6775\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Ms. Underwood introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Marketing Act of 1946 to reauthorize the farmers\u2019 markets and local food promotion program.\n#### 1. Short title\nThis Act may be cited as the New Markets for Farmers and Families Act .\n#### 2. Farmers\u2019 markets and local food promotion program reauthorization\n##### (a) Matching funds\nSection 210A(d)(6)(E) of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1627c(d)(6)(E) ) is amended to read as follows:\n(E) Matching funds (i) In general An eligible entity that receives a grant under this paragraph shall provide matching funds in the form of cash or an in-kind contribution in an amount that is equal to 25 percent of the total amount of the Federal portion of the grant. (ii) Exception Clause (i) shall not apply to an eligible entity that is carrying out a priority grant described in clause (i) or (ii) of subparagraph (C). .\n##### (b) Funding\nSection 210A(i) of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1627c(i) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking $50,000,000 and inserting $100,000,000 ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby striking for fiscal year 2019 and each fiscal year thereafter and inserting for each of fiscal years 2019 through 2026 ; and\n**(B)**\nby striking the period at the end and inserting the following: , and $50,000,000 for fiscal year 2027 and each fiscal year thereafter, to remain available until expended. ; and\n**(3)**\nin paragraph (3)(B), by adding at the end the following: Of the amount made available pursuant to the preceding sentence for a fiscal year, 30 percent shall be reserved for priority grants described in clause (i) or (ii) of subparagraph (C) of subsection (d)(6) for entities that have not received a grant under such subsection in the preceding 3 years and will use the funds to establish a new farmers\u2019 market. If applications for such priority grants are insufficient in number or merit in a fiscal year, the Secretary may use such reserved funds for grants described in the first sentence of this subparagraph. .\n##### (c) Reports\n**(1) Secretary of Agriculture report**\nNot later than 3 years after the date of the enactment of this section, the Secretary of Agriculture shall make publicly available on the website of the Department of Agriculture a report describing\u2014\n**(A)**\nthe number of applications for a grant under section 210A(d)(6) of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1627c(d)(6) ) in the preceding 2 years;\n**(B)**\nthe number of such applications that were submitted by eligible entities that had not previously applied for such a grant;\n**(C)**\nthe number of such applications that met the requirements for a priority grant described in clause (i) or (ii) of subparagraph (C) of such section; and\n**(D)**\nthe number of grants awarded relating to the applications described in paragraph (2) and (3), respectively.\n**(2) Inspector General report**\nNot later than 3 years after the date of the enactment of this section, the Inspector General of the Department of Agriculture shall make publicly available on the website of the Department of Agriculture a report describing\u2014\n**(A)**\nany fraud or abuse related to the grant program under section 210A(d)(6) of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1627c(d)(6) ) in the preceding 2 years; and\n**(B)**\nthe effects of the amendment made by subsection (a) on participation in such grant program.",
      "versionDate": "2025-12-17",
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
        "updateDate": "2026-01-16T18:59:53Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6775ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "New Markets for Farmers and Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T05:53:21Z"
    },
    {
      "title": "New Markets for Farmers and Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Marketing Act of 1946 to reauthorize the farmers' markets and local food promotion program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T05:48:44Z"
    }
  ]
}
```
