# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1022?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1022
- Title: Supporting the contributions of Catholic schools in the United States and celebrating the 52nd annual National Catholic Schools Week.
- Congress: 119
- Bill type: HRES
- Bill number: 1022
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-04-10T16:28:04Z
- Update date including text: 2026-04-10T16:28:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-27 - IntroReferral: Submitted in House
- 2026-01-27 - IntroReferral: Submitted in House
- Latest action: 2026-01-27: Submitted in House

## Actions

- 2026-01-27 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-01-27 - IntroReferral: Submitted in House
- 2026-01-27 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1022",
    "number": "1022",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "L000585",
        "district": "16",
        "firstName": "Darin",
        "fullName": "Rep. LaHood, Darin [R-IL-16]",
        "lastName": "LaHood",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Supporting the contributions of Catholic schools in the United States and celebrating the 52nd annual National Catholic Schools Week.",
    "type": "HRES",
    "updateDate": "2026-04-10T16:28:04Z",
    "updateDateIncludingText": "2026-04-10T16:28:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-27",
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
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T17:32:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "N000015",
      "district": "1",
      "firstName": "Richard",
      "fullName": "Rep. Neal, Richard E. [D-MA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Neal",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MA"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "MD"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "NJ"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "PA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "FL"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley M. [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "WV"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "NY"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "PA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "PA"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "AR"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "NY"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "IA"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "NE"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "NY"
    },
    {
      "bioguideId": "D000600",
      "district": "26",
      "firstName": "Mario",
      "fullName": "Rep. Diaz-Balart, Mario [R-FL-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Diaz-Balart",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1022ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1022\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Mr. LaHood (for himself, Mr. Neal , Mr. Harris of Maryland , Mr. Smith of New Jersey , Mr. Joyce of Pennsylvania , Mr. Rutherford , Mr. Moore of West Virginia , Mr. Garbarino , Mr. Kelly of Pennsylvania , Mr. Costa , Mr. Fitzpatrick , Mr. Hill of Arkansas , Mr. Lawler , and Mrs. Miller-Meeks ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nSupporting the contributions of Catholic schools in the United States and celebrating the 52nd annual National Catholic Schools Week.\nThat the House of Representatives\u2014\n**(1)**\nsupports the goals of National Catholic Schools Week, an event\u2014\n**(A)**\ncosponsored by the National Catholic Educational Association and the United States Conference of Catholic Bishops; and\n**(B)**\nestablished to recognize the vital contributions of the thousands of Catholic elementary and secondary schools in the United States;\n**(2)**\napplauds the National Catholic Educational Association and the United States Conference of Catholic Bishops on their selection of a theme that all can celebrate; and\n**(3)**\nsupports\u2014\n**(A)**\nthe dedication of Catholic schools, students, parents, and teachers across the United States toward academic excellence; and\n**(B)**\nthe key role they play in promoting and ensuring a brighter, stronger future for the United States.",
      "versionDate": "2026-01-27",
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
        "actionDate": "2025-01-28",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "74",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supporting the contributions of Catholic schools in the United States and celebrating the 51st annual \"National Catholic Schools Week\".",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-29",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S487-488; text: CR S486-487)"
      },
      "number": "45",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution supporting the contributions of Catholic schools in the United States and celebrating the 51st annual National Catholic Schools Week.",
      "type": "SRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-29",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S397; text: CR S382)"
      },
      "number": "594",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution supporting the contributions of Catholic schools in the United States and celebrating the 52nd annual National Catholic Schools Week.",
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
        "name": "Education",
        "updateDate": "2026-02-02T14:56:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-27",
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
          "measure-id": "id119hres1022",
          "measure-number": "1022",
          "measure-type": "hres",
          "orig-publish-date": "2026-01-27",
          "originChamber": "HOUSE",
          "update-date": "2026-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1022v00",
            "update-date": "2026-04-10"
          },
          "action-date": "2026-01-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the goals of National Catholic Schools Week, an event cosponsored by the National Catholic Educational Association and the U.S. Conference of Catholic Bishops and established to recognize the contributions of Catholic elementary and secondary schools in the United States. </p>"
        },
        "title": "Supporting the contributions of Catholic schools in the United States and celebrating the 52nd annual National Catholic Schools Week."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1022.xml",
    "summary": {
      "actionDate": "2026-01-27",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the goals of National Catholic Schools Week, an event cosponsored by the National Catholic Educational Association and the U.S. Conference of Catholic Bishops and established to recognize the contributions of Catholic elementary and secondary schools in the United States. </p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hres1022"
    },
    "title": "Supporting the contributions of Catholic schools in the United States and celebrating the 52nd annual National Catholic Schools Week."
  },
  "summaries": [
    {
      "actionDate": "2026-01-27",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the goals of National Catholic Schools Week, an event cosponsored by the National Catholic Educational Association and the U.S. Conference of Catholic Bishops and established to recognize the contributions of Catholic elementary and secondary schools in the United States. </p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hres1022"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1022ih.xml"
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
      "title": "Supporting the contributions of Catholic schools in the United States and celebrating the 52nd annual National Catholic Schools Week.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-29T05:18:23Z"
    },
    {
      "title": "Supporting the contributions of Catholic schools in the United States and celebrating the 52nd annual National Catholic Schools Week.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-28T09:05:21Z"
    }
  ]
}
```
