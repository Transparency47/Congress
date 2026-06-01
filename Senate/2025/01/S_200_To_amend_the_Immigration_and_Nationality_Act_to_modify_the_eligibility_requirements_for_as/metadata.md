# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/200?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/200
- Title: RULES Act
- Congress: 119
- Bill type: S
- Bill number: 200
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2026-01-10T07:29:56Z
- Update date including text: 2026-01-10T07:29:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/200",
    "number": "200",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001242",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Moreno, Bernie [R-OH]",
        "lastName": "Moreno",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "RULES Act",
    "type": "S",
    "updateDate": "2026-01-10T07:29:56Z",
    "updateDateIncludingText": "2026-01-10T07:29:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:45:57Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-01-27",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s200is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 200\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Moreno introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to modify the eligibility requirements for asylum.\n#### 1. Short title\nThis Act may be cited as the Refugees Using Legal Entry Safely Act or RULES Act .\n#### 2. Modification of asylum eligibility\nSection 208(a) of the Immigration and Nationality Act ( 8 U.S.C. 1158(a) ) is amended\u2014\n**(1)**\nby amending paragraph (1) to read as follows:\n(1) Application at ports of entry (A) In general Any alien who arrives at a port of entry of the United States, irrespective of such alien's status, may, only at such a port of entry, apply for asylum in accordance with this section or, as applicable, section 235(b). (B) Prohibition on parole or release into the United States Notwithstanding section 236(a)(2), an alien applying for asylum at a port of entry may not be paroled or released into the United States. ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby striking subparagraph (B)\n**(B)**\nin subparagraph (C), by striking Subject to subparagraph (D), paragraph and inserting Paragraph ;\n**(C)**\nby striking subparagraph (D);\n**(D)**\nin subparagraph (E), by striking Subparagraphs (A) and (B) and inserting Subparagraph (A) ;\n**(E)**\nby redesignating subparagraphs (C) and (E) as subparagraphs (B) and (C), respectively; and\n**(F)**\nby adding at the end the following:\n(D) Effect of apprehension in the United States Paragraph (1) shall not apply to any alien who is apprehended by or referred to the Secretary of Homeland Security as an alien who has entered the United States without inspection and admission or who has remained in the United States beyond the alien's period of authorized stay. ; and\n**(3)**\nby striking Attorney General each place it appears and inserting Attorney General or the Secretary of Homeland Security, as applicable, .",
      "versionDate": "2025-01-23",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-01-31",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "871",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "RULES Act",
      "type": "HR"
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
        "name": "Immigration",
        "updateDate": "2025-03-01T13:27:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119s200",
          "measure-number": "200",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s200v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Refugees Using Legal Entry Safely Act or RULES Act</strong></p><p>This bill requires\u00a0non-U.S. nationals (<em>aliens</em> under federal law) applying for asylum to arrive and apply at a U.S. port of entry. Applicants are prohibited from being paroled into the U.S. pending approval of such application. Further, individuals apprehended in the U.S. without legal immigration status are ineligible for asylum. Applicants rejected for asylum are barred from applying for asylum in the future. Under current law, an applicant may reapply in changed or extraordinary circumstances.</p>"
        },
        "title": "RULES Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s200.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Refugees Using Legal Entry Safely Act or RULES Act</strong></p><p>This bill requires\u00a0non-U.S. nationals (<em>aliens</em> under federal law) applying for asylum to arrive and apply at a U.S. port of entry. Applicants are prohibited from being paroled into the U.S. pending approval of such application. Further, individuals apprehended in the U.S. without legal immigration status are ineligible for asylum. Applicants rejected for asylum are barred from applying for asylum in the future. Under current law, an applicant may reapply in changed or extraordinary circumstances.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119s200"
    },
    "title": "RULES Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Refugees Using Legal Entry Safely Act or RULES Act</strong></p><p>This bill requires\u00a0non-U.S. nationals (<em>aliens</em> under federal law) applying for asylum to arrive and apply at a U.S. port of entry. Applicants are prohibited from being paroled into the U.S. pending approval of such application. Further, individuals apprehended in the U.S. without legal immigration status are ineligible for asylum. Applicants rejected for asylum are barred from applying for asylum in the future. Under current law, an applicant may reapply in changed or extraordinary circumstances.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119s200"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s200is.xml"
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
      "title": "RULES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-25T05:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RULES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Refugees Using Legal Entry Safely Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Immigration and Nationality Act to modify the eligibility requirements for asylum.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:18:38Z"
    }
  ]
}
```
