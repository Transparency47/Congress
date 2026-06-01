# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/215?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/215
- Title: Adoption Information Act
- Congress: 119
- Bill type: HR
- Bill number: 215
- Origin chamber: House
- Introduced date: 2025-01-06
- Update date: 2025-03-07T19:47:58Z
- Update date including text: 2025-03-07T19:47:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-06: Introduced in House
- 2025-01-06 - IntroReferral: Introduced in House
- 2025-01-06 - IntroReferral: Introduced in House
- 2025-01-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-06: Introduced in House

## Actions

- 2025-01-06 - IntroReferral: Introduced in House
- 2025-01-06 - IntroReferral: Introduced in House
- 2025-01-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-06",
    "latestAction": {
      "actionDate": "2025-01-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/215",
    "number": "215",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000804",
        "district": "1",
        "firstName": "Robert",
        "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
        "lastName": "Wittman",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Adoption Information Act",
    "type": "HR",
    "updateDate": "2025-03-07T19:47:58Z",
    "updateDateIncludingText": "2025-03-07T19:47:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-06",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-01-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-06",
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
          "date": "2025-01-06T17:00:20Z",
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
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-01-06",
      "state": "WI"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-06",
      "state": "LA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr215ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 215\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 6, 2025 Mr. Wittman (for himself, Mr. Grothman , Mr. LaMalfa , and Mr. Higgins of Louisiana ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title V of the Social Security Act to require assurances that certain family planning service projects and programs will provide pamphlets containing the contact information of adoption centers.\n#### 1. Short title\nThis Act may be cited as the Adoption Information Act .\n#### 2. Provision in family planning services of pamphlets containing adoption center contact information\nTitle V of the Social Security Act ( 42 U.S.C. 701 et seq. ) is amended by adding at the end the following:\n514. Limitation (a) In general Notwithstanding any other provision of this title, a grant may be made or contract entered into under section 501 for a family planning service project or program only upon assurances satisfactory to the Secretary that the project or program will\u2014 (1) provide to each person to whom the medical professional provides family planning medical services, at the time the person inquires about medical or abortion services, a pamphlet that contains\u2014 (A) a comprehensive list of the adoption centers located in the region (as determined by the Secretary) where the adoption services are provided; and (B) the address and telephone number of each such center; and (2) provide each such person an opportunity to read the pamphlet. (b) Pamphlets The Secretary shall prepare, annually update, and distribute to each project or program referred to in subsection (a) pamphlets described in such subsection. (c) No additional funds No funds may be used to carry out this section, except funds that are appropriated to carry out this title. .",
      "versionDate": "2025-01-06",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Abortion",
            "updateDate": "2025-02-05T21:04:25Z"
          },
          {
            "name": "Adoption and foster care",
            "updateDate": "2025-02-05T21:04:25Z"
          },
          {
            "name": "Family planning and birth control",
            "updateDate": "2025-02-05T21:04:25Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-05T21:04:25Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2025-02-05T21:04:25Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-02-05T21:04:25Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-02-05T21:04:25Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-04T12:34:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-06",
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
          "measure-id": "id119hr215",
          "measure-number": "215",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-06",
          "originChamber": "HOUSE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr215v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Adoption Information Act</strong></p><p>This bill requires federally funded family planning programs to provide each person who inquires about medical or abortion\u00a0services with specified information about adoption centers in their region. The Department of Health and Human Services must provide the programs with pamphlets containing the required information.</p>"
        },
        "title": "Adoption Information Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr215.xml",
    "summary": {
      "actionDate": "2025-01-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Adoption Information Act</strong></p><p>This bill requires federally funded family planning programs to provide each person who inquires about medical or abortion\u00a0services with specified information about adoption centers in their region. The Department of Health and Human Services must provide the programs with pamphlets containing the required information.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr215"
    },
    "title": "Adoption Information Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Adoption Information Act</strong></p><p>This bill requires federally funded family planning programs to provide each person who inquires about medical or abortion\u00a0services with specified information about adoption centers in their region. The Department of Health and Human Services must provide the programs with pamphlets containing the required information.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr215"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr215ih.xml"
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
      "title": "Adoption Information Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Adoption Information Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T06:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title V of the Social Security Act to require assurances that certain family planning service projects and programs will provide pamphlets containing the contact information of adoption centers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T06:18:25Z"
    }
  ]
}
```
