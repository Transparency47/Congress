# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/222?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/222
- Title: A resolution expressing support for the designation of May 2025 as "Motorcycle Safety Awareness Month".
- Congress: 119
- Bill type: SRES
- Bill number: 222
- Origin chamber: Senate
- Introduced date: 2025-05-13
- Update date: 2026-05-14T17:51:26Z
- Update date including text: 2026-05-14T17:51:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-13: Introduced in Senate
- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-05-13 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2901; text: CR S2900)
- Latest action: 2025-05-13: Introduced in Senate

## Actions

- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-05-13 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2901; text: CR S2900)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/222",
    "number": "222",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
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
    "title": "A resolution expressing support for the designation of May 2025 as \"Motorcycle Safety Awareness Month\".",
    "type": "SRES",
    "updateDate": "2026-05-14T17:51:26Z",
    "updateDateIncludingText": "2026-05-14T17:51:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2901; text: CR S2900)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-13",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "MI"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-05-13",
      "state": "ME"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres222ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 222\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2025 Ms. Ernst (for herself, Mr. Peters , Mr. King , and Mr. Curtis ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nExpressing support for the designation of May 2025 as Motorcycle Safety Awareness Month .\nThat the Senate\u2014\n**(1)**\nsupports the designation of May 2025 as Motorcycle Safety Awareness Month ;\n**(2)**\nrecognizes the contribution of motorcycles to the transportation mix;\n**(3)**\nencourages motorcycle awareness by all road users;\n**(4)**\nrecognizes that motorcyclists have a right to the road and that all motorists should safely share the roadways;\n**(5)**\nencourages rider safety education, training, and proper gear for safe motorcycle operation; and\n**(6)**\nsupports the goals of Motorcycle Safety Awareness Month.",
      "versionDate": "2025-05-13",
      "versionType": "ATS"
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
        "actionDate": "2026-04-29",
        "text": "Referred to the House Committee on Transportation and Infrastructure."
      },
      "number": "1236",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the designation of May 2026 as \"Motorcycle Safety Awareness Month\".",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-01",
        "text": "Referred to the Subcommittee on Highways and Transit."
      },
      "number": "367",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the designation of May 2025 as \"Motorcycle Safety Awareness Month\".",
      "type": "HRES"
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
            "name": "Commemorative events and holidays",
            "updateDate": "2025-06-02T15:37:31Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2025-06-02T15:37:31Z"
          },
          {
            "name": "Transportation safety and security",
            "updateDate": "2025-06-02T15:37:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-22T15:50:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-13",
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
          "measure-id": "id119sres222",
          "measure-number": "222",
          "measure-type": "sres",
          "orig-publish-date": "2025-05-13",
          "originChamber": "SENATE",
          "update-date": "2025-08-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres222v00",
            "update-date": "2025-08-15"
          },
          "action-date": "2025-05-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution expresses support for the designation of May 2025 as Motorcycle Safety Awareness Month. It also recognizes the contribution of motorcycles to transportation.</p>"
        },
        "title": "A resolution expressing support for the designation of May 2025 as \"Motorcycle Safety Awareness Month\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres222.xml",
    "summary": {
      "actionDate": "2025-05-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses support for the designation of May 2025 as Motorcycle Safety Awareness Month. It also recognizes the contribution of motorcycles to transportation.</p>",
      "updateDate": "2025-08-15",
      "versionCode": "id119sres222"
    },
    "title": "A resolution expressing support for the designation of May 2025 as \"Motorcycle Safety Awareness Month\"."
  },
  "summaries": [
    {
      "actionDate": "2025-05-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution expresses support for the designation of May 2025 as Motorcycle Safety Awareness Month. It also recognizes the contribution of motorcycles to transportation.</p>",
      "updateDate": "2025-08-15",
      "versionCode": "id119sres222"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres222ats.xml"
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
      "title": "A resolution expressing support for the designation of May 2025 as \"Motorcycle Safety Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-14T10:56:21Z"
    },
    {
      "title": "A resolution expressing support for the designation of May 2025 as \"Motorcycle Safety Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T10:56:21Z"
    }
  ]
}
```
