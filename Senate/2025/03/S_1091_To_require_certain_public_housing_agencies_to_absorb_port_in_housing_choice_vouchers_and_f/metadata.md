# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1091?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1091
- Title: Rural Housing Accessibility Act
- Congress: 119
- Bill type: S
- Bill number: 1091
- Origin chamber: Senate
- Introduced date: 2025-03-24
- Update date: 2026-04-06T19:41:19Z
- Update date including text: 2026-04-06T19:41:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-24: Introduced in Senate
- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-03-24: Introduced in Senate

## Actions

- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1091",
    "number": "1091",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Rural Housing Accessibility Act",
    "type": "S",
    "updateDate": "2026-04-06T19:41:19Z",
    "updateDateIncludingText": "2026-04-06T19:41:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-24",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-24",
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
          "date": "2025-03-24T20:42:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1091is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1091\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2025 Ms. Ernst (for herself and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require certain public housing agencies to absorb port-in housing choice vouchers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Housing Accessibility Act .\n#### 2. Requiring certain public housing agencies to absorb port-in vouchers and limiting billing initial public housing agencies beyond 12 months\nSection 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ) is amended by adding at the end the following:\n(23) Portability of vouchers (A) Definitions In this paragraph\u2014 (i) the term covered public housing agency means a public housing agency that, in a given fiscal year, utilizes less than 95 percent of the budget authority available to the public housing agency; (ii) the term initial public housing agency has the meaning given the term initial PHA in section 982.4 of title 24, Code of Federal Regulations, or any successor regulation; and (iii) the term portable family means a family holding a voucher under this subsection that seeks to rent a dwelling unit outside of the jurisdiction of the initial public housing agency. (B) Requirement A covered public housing agency that has jurisdiction over the area in which a portable family is seeking to use the voucher received from an initial public housing agency\u2014 (i) shall notify the initial public housing agency whether the covered public housing agency will\u2014 (I) absorb the voucher by using funds of the covered public housing agency; or (II) bill the initial public housing agency for a period of not more than 12 months; (ii) shall make assistance payments to the portable family under an annual contributions contract entered into between the covered public housing agency and the Secretary; and (iii) may not bill the initial public housing agency for the assistance payments described in clause (ii) for a period of more than 12 months beginning on the effective date of the initial billing. .",
      "versionDate": "2025-03-24",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-04-04T16:12:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-24",
    "originChamber": "Senate",
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
          "measure-id": "id119s1091",
          "measure-number": "1091",
          "measure-type": "s",
          "orig-publish-date": "2025-03-24",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1091v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-03-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Rural Housing Accessibility Act</strong></p><p>This bill requires a public housing agency (PHA) that uses less than 95% of its budget authority in a given year to accept a housing choice voucher from a family that received the voucher from an agency in a different jurisdiction.\u00a0The PHA that accepts the voucher (1) must make assistance payments to the family under an annual contributions contract, and (2) may not bill the initial PHA for the assistance payments for more than 12 months.\u00a0\u00a0</p>"
        },
        "title": "Rural Housing Accessibility Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1091.xml",
    "summary": {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Housing Accessibility Act</strong></p><p>This bill requires a public housing agency (PHA) that uses less than 95% of its budget authority in a given year to accept a housing choice voucher from a family that received the voucher from an agency in a different jurisdiction.\u00a0The PHA that accepts the voucher (1) must make assistance payments to the family under an annual contributions contract, and (2) may not bill the initial PHA for the assistance payments for more than 12 months.\u00a0\u00a0</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s1091"
    },
    "title": "Rural Housing Accessibility Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Housing Accessibility Act</strong></p><p>This bill requires a public housing agency (PHA) that uses less than 95% of its budget authority in a given year to accept a housing choice voucher from a family that received the voucher from an agency in a different jurisdiction.\u00a0The PHA that accepts the voucher (1) must make assistance payments to the family under an annual contributions contract, and (2) may not bill the initial PHA for the assistance payments for more than 12 months.\u00a0\u00a0</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s1091"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1091is.xml"
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
      "title": "Rural Housing Accessibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rural Housing Accessibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require certain public housing agencies to absorb port-in housing choice vouchers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:18Z"
    }
  ]
}
```
