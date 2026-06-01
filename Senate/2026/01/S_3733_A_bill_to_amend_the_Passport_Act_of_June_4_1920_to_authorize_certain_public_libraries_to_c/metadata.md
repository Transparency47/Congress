# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3733?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3733
- Title: A bill to amend the Passport Act of June 4, 1920, to authorize certain public libraries to collect and retain a fee for the execution of a passport application.
- Congress: 119
- Bill type: S
- Bill number: 3733
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-03-27T10:56:38Z
- Update date including text: 2026-03-27T10:56:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3733",
    "number": "3733",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "F000479",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Fetterman, John [D-PA]",
        "lastName": "Fetterman",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "A bill to amend the Passport Act of June 4, 1920, to authorize certain public libraries to collect and retain a fee for the execution of a passport application.",
    "type": "S",
    "updateDate": "2026-03-27T10:56:38Z",
    "updateDateIncludingText": "2026-03-27T10:56:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-29",
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
      "actionDate": "2026-01-29",
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
        "item": {
          "date": "2026-01-29T17:54:43Z",
          "name": "Referred To"
        }
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
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "PA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "CT"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "CT"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3733is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3733\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mr. Fetterman (for himself and Mr. McCormick ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo amend the Passport Act of June 4, 1920, to authorize certain public libraries to collect and retain a fee for the execution of a passport application.\n#### 1. Authorization of certain public libraries to collect and retain fees for acceptance and execution of passport applications\n##### (a) In general\nSubsection (a) of the Passport Act of June 4, 1920 ( 22 U.S.C. 214(a) ), is amended by adding at the end the following:\n(4) The Secretary of State may authorize a public library that is organized as a nongovernmental organization, a nonprofit, charitable organization, or a trust to serve as a passport acceptance facility and to collect and retain the execution fee for a passport accepted by such public library if such library is in compliance with regulations prescribed by the Secretary of State for the acceptance and execution of passport applications. .\n##### (b) Authorization of public libraries which previously served as passport acceptance facilities\n**(1) In general**\nNot later than 30 days after the date of the enactment of this Act, the Secretary of State shall authorize any public library to serve as a passport acceptance facility and to collect and retain an execution fee for a passport accepted by such library, if, before the date of the enactment of this Act, such public library\u2014\n**(A)**\nserved as a passport acceptance facility; and\n**(B)**\nwas in compliance with the regulations prescribed by the Secretary of State for the acceptance and execution of passport applications.\n**(2) Report**\nNot later than 30 days after the date of the enactment of this Act, the Secretary of State shall submit to the relevant congressional committees a report that includes\u2014\n**(A)**\ndocumentation of the Secretary's compliance with the requirements described in paragraph (1); or\n**(B)**\nif the Secretary is not in compliance with such requirements, an explanation for such noncompliance.\n##### (c) Conforming amendment\nSubsection (a)(1) of the Passport Act of June 4, 1920 ( 22 U.S.C. 214(a)(1) ), is amended\u2014\n**(1)**\nby striking State officials or the United States Postal Service and inserting a State, a local government, the United States Postal Service, or a public library that meets the requirements described in paragraph (4) ; and\n**(2)**\nby striking by such officials or by that Service. and inserting by such State, local government, Postal Service, or public library. .",
      "versionDate": "2026-01-29",
      "versionType": "Introduced in Senate"
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
        "name": "International Affairs",
        "updateDate": "2026-02-27T20:05:23Z"
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
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3733is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Passport Act of June 4, 1920, to authorize certain public libraries to collect and retain a fee for the execution of a passport application.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T11:18:26Z"
    },
    {
      "title": "A bill to amend the Passport Act of June 4, 1920, to authorize certain public libraries to collect and retain a fee for the execution of a passport application.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T11:56:20Z"
    }
  ]
}
```
