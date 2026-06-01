# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/528?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/528
- Title: A resolution supporting after-school programs and Lights On Afterschool, a national celebration of after-school programs held on October 23, 2025.
- Congress: 119
- Bill type: SRES
- Bill number: 528
- Origin chamber: Senate
- Introduced date: 2025-12-03
- Update date: 2026-04-01T19:35:07Z
- Update date including text: 2026-04-01T19:35:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-03: Introduced in Senate
- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-12-03 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S8487; text: CR S8486-8487)
- Latest action: 2025-12-03: Introduced in Senate

## Actions

- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-12-03 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S8487; text: CR S8486-8487)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/528",
    "number": "528",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "S001203",
        "district": "",
        "firstName": "Tina",
        "fullName": "Sen. Smith, Tina [D-MN]",
        "lastName": "Smith",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "A resolution supporting after-school programs and Lights On Afterschool, a national celebration of after-school programs held on October 23, 2025.",
    "type": "SRES",
    "updateDate": "2026-04-01T19:35:07Z",
    "updateDateIncludingText": "2026-04-01T19:35:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S8487; text: CR S8486-8487)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-03",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "ME"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres528ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 528\nIN THE SENATE OF THE UNITED STATES\nDecember 3, 2025 Ms. Smith (for herself, Ms. Collins , Ms. Warren , and Mr. Kaine ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nSupporting after-school programs and Lights On Afterschool, a national celebration of after-school programs held on October 23, 2025.\nThat the Senate supports Lights On Afterschool, a national celebration of after-school programs held on October 23, 2025.",
      "versionDate": "2025-12-03",
      "versionType": "ATS"
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
            "name": "Child care and development",
            "updateDate": "2025-12-08T16:39:32Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-12-08T16:39:32Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-12-08T16:39:32Z"
          },
          {
            "name": "Family services",
            "updateDate": "2025-12-08T16:39:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-12-06T13:12:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-03",
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
          "measure-id": "id119sres528",
          "measure-number": "528",
          "measure-type": "sres",
          "orig-publish-date": "2025-12-03",
          "originChamber": "SENATE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres528v55",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-12-03",
          "action-desc": "Passed Senate",
          "summary-text": "<p>This resolution expresses support for Lights On Afterschool, a national celebration of after-school programs held on October 23, 2025.</p>"
        },
        "title": "A resolution supporting after-school programs and Lights On Afterschool, a national celebration of after-school programs held on October 23, 2025."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres528.xml",
    "summary": {
      "actionDate": "2025-12-03",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution expresses support for Lights On Afterschool, a national celebration of after-school programs held on October 23, 2025.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119sres528"
    },
    "title": "A resolution supporting after-school programs and Lights On Afterschool, a national celebration of after-school programs held on October 23, 2025."
  },
  "summaries": [
    {
      "actionDate": "2025-12-03",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution expresses support for Lights On Afterschool, a national celebration of after-school programs held on October 23, 2025.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119sres528"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres528ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A resolution supporting after-school programs and Lights On Afterschool, a national celebration of after-school programs held on October 23, 2025.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T11:56:22Z"
    },
    {
      "title": "A resolution supporting after-school programs and Lights On Afterschool, a national celebration of after-school programs held on October 23, 2025.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T11:56:22Z"
    }
  ]
}
```
