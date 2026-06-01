# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/345?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/345
- Title: Expressing support for designation of the month of April 2025 as "Parkinsons Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 345
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2026-05-08T18:14:13Z
- Update date including text: 2026-05-08T18:14:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-04-24 - IntroReferral: Submitted in House
- 2025-04-24 - IntroReferral: Submitted in House
- Latest action: 2025-04-24: Submitted in House

## Actions

- 2025-04-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-04-24 - IntroReferral: Submitted in House
- 2025-04-24 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/345",
    "number": "345",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001324",
        "district": "1",
        "firstName": "Wesley",
        "fullName": "Rep. Bell, Wesley [D-MO-1]",
        "lastName": "Bell",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "Expressing support for designation of the month of April 2025 as \"Parkinsons Awareness Month\".",
    "type": "HRES",
    "updateDate": "2026-05-08T18:14:13Z",
    "updateDateIncludingText": "2026-05-08T18:14:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-04-24T15:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "FL"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres345ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 345\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Mr. Bell (for himself and Mr. Bilirakis ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for designation of the month of April 2025 as Parkinsons Awareness Month .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of Parkinson\u2019s Awareness Month ;\n**(2)**\nsupports the goals and ideals of Parkinson\u2019s Awareness Month;\n**(3)**\ncontinues to support research to find better treatments and a cure for Parkinson\u2019s disease;\n**(4)**\nrecognizes the individuals living with Parkinson\u2019s disease who participate in vital clinical trials to advance the knowledge of the disease; and\n**(5)**\ncommends the dedication of organizations, volunteers, researchers, and millions of individuals across the country working to improve the quality of life of people living with Parkinson\u2019s disease and their families.",
      "versionDate": "2025-04-24",
      "versionType": "IH"
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
        "actionDate": "2026-04-28",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2076-2077; text: CR S2085-2086)"
      },
      "number": "696",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution expressing support for the designation of the month of April 2026 as \"Parkinson's Awareness Month\".",
      "type": "SRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-14",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1167",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the designation of the month of April 2026 as \"Parkinson's Awareness Month\".",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-30",
        "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2719)"
      },
      "number": "194",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution expressing support for the designation of the month of April 2025 as \"Parkinson's Awareness Month\".",
      "type": "SRES"
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
        "name": "Health",
        "updateDate": "2025-05-19T14:49:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-24",
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
          "measure-id": "id119hres345",
          "measure-number": "345",
          "measure-type": "hres",
          "orig-publish-date": "2025-04-24",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres345v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-04-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of Parkinson's Awareness Month.</p>"
        },
        "title": "Expressing support for designation of the month of April 2025 as \"Parkinsons Awareness Month\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres345.xml",
    "summary": {
      "actionDate": "2025-04-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of Parkinson's Awareness Month.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres345"
    },
    "title": "Expressing support for designation of the month of April 2025 as \"Parkinsons Awareness Month\"."
  },
  "summaries": [
    {
      "actionDate": "2025-04-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of Parkinson's Awareness Month.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres345"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres345ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Expressing support for designation of the month of April 2025 as \"Parkinsons Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T08:18:33Z"
    },
    {
      "title": "Expressing support for designation of the month of April 2025 as \"Parkinsons Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T08:05:36Z"
    }
  ]
}
```
