# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4366?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4366
- Title: Know Your Labor Rights Act
- Congress: 119
- Bill type: S
- Bill number: 4366
- Origin chamber: Senate
- Introduced date: 2026-04-21
- Update date: 2026-05-01T18:53:01Z
- Update date including text: 2026-05-01T18:53:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-21: Introduced in Senate
- 2026-04-21 - IntroReferral: Introduced in Senate
- 2026-04-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-04-21: Introduced in Senate

## Actions

- 2026-04-21 - IntroReferral: Introduced in Senate
- 2026-04-21 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4366",
    "number": "4366",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Know Your Labor Rights Act",
    "type": "S",
    "updateDate": "2026-05-01T18:53:01Z",
    "updateDateIncludingText": "2026-05-01T18:53:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-21",
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
          "date": "2026-04-21T21:27:47Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4366is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4366\nIN THE SENATE OF THE UNITED STATES\nApril 21, 2026 Mr. Hawley (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the National Labor Relations Act to require employers to post notice regarding the rights and protections under that Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Know Your Labor Rights Act .\n#### 2. Amendments to the National Labor Relations Act\n##### (a) Notice-Posting and transparency\nSection 8 of the National Labor Relations Act ( 29 U.S.C. 158 ) is amended by adding at the end the following:\n(h) The Board shall promulgate regulations requiring each employer to post and maintain, in conspicuous places where notices to employees and applicants for employment are customarily posted both physically and electronically, a notice setting forth the rights and protections afforded employees under this Act. The Board shall readily make available to the public, including employers, the form and text of such notice at no cost on the website of the Board. The Board shall promulgate regulations requiring employers to notify each new employee of the information contained in the notice described in the preceding two sentences. .\n##### (b) Penalties\nSection 12 of the National Labor Relations Act ( 29 U.S.C. 162 ) is amended\u2014\n**(1)**\nby striking Sec. 12. Any person and inserting the following:\n12. Penalties (a) Violations for interference with board Any person ; and\n**(2)**\nby adding at the end the following:\n(b) Violations for posting requirements If the Board, or any agent or agency designated by the Board for such purposes, determines that an employer has violated section 8(h) or regulations issued thereunder, the Board shall\u2014 (1) state the findings of fact supporting such determination; (2) issue and cause to be served on such employer an order requiring that such employer comply with section 8(h) or regulations issued thereunder; and (3) impose a civil penalty in an amount determined appropriate by the Board, except that in no case shall the amount of such penalty exceed $500 for each such violation. .",
      "versionDate": "2026-04-21",
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
        "actionDate": "2026-04-21",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "8418",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Know Your Labor Rights Act",
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
        "name": "Labor and Employment",
        "updateDate": "2026-05-01T18:53:01Z"
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
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4366is.xml"
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
      "title": "Know Your Labor Rights Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T04:53:36Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Know Your Labor Rights Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T04:53:34Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the National Labor Relations Act to require employers to post notice regarding the rights and protections under that Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-29T04:48:45Z"
    }
  ]
}
```
