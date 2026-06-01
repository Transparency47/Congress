# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/289?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/289
- Title: SAP Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 289
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-04-16T12:53:33Z
- Update date including text: 2026-04-16T12:53:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on Forestry and Horticulture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/289",
    "number": "289",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "L000600",
        "district": "23",
        "firstName": "Nicholas",
        "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
        "lastName": "Langworthy",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "SAP Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-16T12:53:33Z",
    "updateDateIncludingText": "2026-04-16T12:53:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-14",
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
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:30:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-14T18:01:03Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "VT"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "ME"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr289ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 289\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Langworthy (for himself and Ms. Balint ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Act of 2014 with respect to the Acer access and development program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting All Producers Act of 2025 or the SAP Act of 2025 .\n#### 2. Acer access and development program\nSection 12306 of the Agricultural Act of 2014 ( 7 U.S.C. 1632c ) is amended\u2014\n**(1)**\nby redesignating subsections (e) and (f) as subsections (f) and (g), respectively;\n**(2)**\nby inserting after subsection (d) the following:\n(e) Consultations (1) In general Beginning with the first request for applications under this section that occurs at least 1 year after the date of the enactment of the SAP Act of 2025, not later than 6 months before such a request for applications, the Secretary shall solicit input from maple industry stakeholders with respect to the research and education priorities of the maple industry. (2) Consideration The Secretary shall consider the information provided through the consultation required under paragraph (1) when making grants under this section. ; and\n**(3)**\nin subsection (g), as so redesignated, by striking 2023 and inserting 2030 .",
      "versionDate": "2025-01-09",
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
        "actionDate": "2026-03-05",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 17."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-09",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "56",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SAP Act",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-02-20T15:02:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr289",
          "measure-number": "289",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr289v00",
            "update-date": "2025-02-21"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Supporting All Producers Act of 2025 or the SAP Act</strong> <strong>of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to solicit input from maple industry stakeholders with respect to the research and education priorities of the maple industry for the Acer Access and Development Program (Acer). Specifically, the bill amends Acer to require USDA to consider the information provided through consultation with the maple industry when making program grants.</p><p>The bill also extends the program's authorization through FY2030.</p><p>As background, Acer provides competitive grants to states, tribal governments, and research institutions to support their efforts to promote the domestic maple syrup industry through activities\u00a0associated with, among other things,\u00a0the promotion of (1) research and education related to maple syrup production, and (2) natural resource sustainability in the maple syrup industry.</p>"
        },
        "title": "SAP Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr289.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting All Producers Act of 2025 or the SAP Act</strong> <strong>of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to solicit input from maple industry stakeholders with respect to the research and education priorities of the maple industry for the Acer Access and Development Program (Acer). Specifically, the bill amends Acer to require USDA to consider the information provided through consultation with the maple industry when making program grants.</p><p>The bill also extends the program's authorization through FY2030.</p><p>As background, Acer provides competitive grants to states, tribal governments, and research institutions to support their efforts to promote the domestic maple syrup industry through activities\u00a0associated with, among other things,\u00a0the promotion of (1) research and education related to maple syrup production, and (2) natural resource sustainability in the maple syrup industry.</p>",
      "updateDate": "2025-02-21",
      "versionCode": "id119hr289"
    },
    "title": "SAP Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting All Producers Act of 2025 or the SAP Act</strong> <strong>of 2025</strong></p><p>This bill directs the Department of Agriculture (USDA) to solicit input from maple industry stakeholders with respect to the research and education priorities of the maple industry for the Acer Access and Development Program (Acer). Specifically, the bill amends Acer to require USDA to consider the information provided through consultation with the maple industry when making program grants.</p><p>The bill also extends the program's authorization through FY2030.</p><p>As background, Acer provides competitive grants to states, tribal governments, and research institutions to support their efforts to promote the domestic maple syrup industry through activities\u00a0associated with, among other things,\u00a0the promotion of (1) research and education related to maple syrup production, and (2) natural resource sustainability in the maple syrup industry.</p>",
      "updateDate": "2025-02-21",
      "versionCode": "id119hr289"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr289ih.xml"
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
      "title": "SAP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting All Producers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Act of 2014 with respect to the Acer access and development program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T03:03:29Z"
    }
  ]
}
```
