# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/985?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/985
- Title: To amend the Agriculture Improvement Act of 2018 to reauthorize the dairy business innovation initiatives.
- Congress: 119
- Bill type: HR
- Bill number: 985
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-03-25T12:45:40Z
- Update date including text: 2025-03-25T12:45:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-14 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-14 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/985",
    "number": "985",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "V000135",
        "district": "3",
        "firstName": "Derrick",
        "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
        "lastName": "Van Orden",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "To amend the Agriculture Improvement Act of 2018 to reauthorize the dairy business innovation initiatives.",
    "type": "HR",
    "updateDate": "2025-03-25T12:45:40Z",
    "updateDateIncludingText": "2025-03-25T12:45:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
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
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T15:07:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-14T20:35:54Z",
              "name": "Referred to"
            }
          },
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
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
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "CA"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr985ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 985\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Van Orden (for himself and Mr. Carbajal ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agriculture Improvement Act of 2018 to reauthorize the dairy business innovation initiatives.\n#### 1. Dairy business innovation initiatives\nSection 12513 of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 1632d ) is amended\u2014\n**(1)**\nin subsection (b), by striking 3 and inserting 4 ;\n**(2)**\nin subsection (g)(1)(A), by striking 3 and inserting 4 ; and\n**(3)**\nin subsection (i), by striking $20,000,000 and inserting $36,000,000 .",
      "versionDate": "2025-02-05",
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
        "updateDate": "2025-03-20T18:41:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
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
          "measure-id": "id119hr985",
          "measure-number": "985",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-05",
          "originChamber": "HOUSE",
          "update-date": "2025-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr985v00",
            "update-date": "2025-03-24"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill increases the authorization of appropriations for the Dairy Business Innovation\u00a0(DBI) Initiatives<strong> </strong>for each fiscal year.\u00a0The bill also requires that there be a minimum of four regionally-located DBI\u00a0Initiatives, instead of the currently required three.</p><p>Under the Agricultural Marketing Service, the DBI Initiatives support dairy businesses in the development, production, marketing, and distribution of dairy products. The current program includes four DBI Initiatives selected to\u00a0provide direct technical assistance and subawards to dairy businesses, including for niche dairy products and dairy products derived from cow milk, sheep milk, and goat milk.</p>"
        },
        "title": "To amend the Agriculture Improvement Act of 2018 to reauthorize the dairy business innovation initiatives."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr985.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill increases the authorization of appropriations for the Dairy Business Innovation\u00a0(DBI) Initiatives<strong> </strong>for each fiscal year.\u00a0The bill also requires that there be a minimum of four regionally-located DBI\u00a0Initiatives, instead of the currently required three.</p><p>Under the Agricultural Marketing Service, the DBI Initiatives support dairy businesses in the development, production, marketing, and distribution of dairy products. The current program includes four DBI Initiatives selected to\u00a0provide direct technical assistance and subawards to dairy businesses, including for niche dairy products and dairy products derived from cow milk, sheep milk, and goat milk.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119hr985"
    },
    "title": "To amend the Agriculture Improvement Act of 2018 to reauthorize the dairy business innovation initiatives."
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill increases the authorization of appropriations for the Dairy Business Innovation\u00a0(DBI) Initiatives<strong> </strong>for each fiscal year.\u00a0The bill also requires that there be a minimum of four regionally-located DBI\u00a0Initiatives, instead of the currently required three.</p><p>Under the Agricultural Marketing Service, the DBI Initiatives support dairy businesses in the development, production, marketing, and distribution of dairy products. The current program includes four DBI Initiatives selected to\u00a0provide direct technical assistance and subawards to dairy businesses, including for niche dairy products and dairy products derived from cow milk, sheep milk, and goat milk.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119hr985"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr985ih.xml"
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
      "title": "To amend the Agriculture Improvement Act of 2018 to reauthorize the dairy business innovation initiatives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:38Z"
    },
    {
      "title": "To amend the Agriculture Improvement Act of 2018 to reauthorize the dairy business innovation initiatives.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T09:07:23Z"
    }
  ]
}
```
