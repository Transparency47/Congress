# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/314?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/314
- Title: A resolution recognizing the importance of trademarks in the economy and the role of trademarks in protecting consumer safety, by designating the month of July as "National Anti-Counterfeiting and Consumer Education and Awareness Month".
- Congress: 119
- Bill type: SRES
- Bill number: 314
- Origin chamber: Senate
- Introduced date: 2025-07-08
- Update date: 2026-03-31T11:05:35Z
- Update date including text: 2026-03-31T11:05:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-08: Introduced in Senate
- 2025-07-08 - IntroReferral: Introduced in Senate
- 2025-07-08 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-07-17 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-07-17 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S4490; text: 07/08/2025 CR S4259)
- 2025-07-17 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-07-17 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-07-08: Introduced in Senate

## Actions

- 2025-07-08 - IntroReferral: Introduced in Senate
- 2025-07-08 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-07-17 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-07-17 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S4490; text: 07/08/2025 CR S4259)
- 2025-07-17 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-07-17 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-08",
    "latestAction": {
      "actionDate": "2025-07-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/314",
    "number": "314",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "A resolution recognizing the importance of trademarks in the economy and the role of trademarks in protecting consumer safety, by designating the month of July as \"National Anti-Counterfeiting and Consumer Education and Awareness Month\".",
    "type": "SRES",
    "updateDate": "2026-03-31T11:05:35Z",
    "updateDateIncludingText": "2026-03-31T11:05:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S4490; text: 07/08/2025 CR S4259)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-08",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-08",
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
        "item": [
          {
            "date": "2025-07-17T22:18:53Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-07-08T21:25:23Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "DE"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "NC"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres314is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 314\nIN THE SENATE OF THE UNITED STATES\nJuly 8, 2025 Mr. Grassley (for himself, Mr. Coons , Mr. Tillis , and Ms. Hirono ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing the importance of trademarks in the economy and the role of trademarks in protecting consumer safety, by designating the month of July as National Anti-Counterfeiting and Consumer Education and Awareness Month .\nThat the Senate\u2014\n**(1)**\ndesignates the month of July 2025 as National Anti-Counterfeiting and Consumer Education and Awareness Month ;\n**(2)**\nsupports the goals and ideals of National Anti-Counterfeiting and Consumer Education and Awareness Month to educate the public and raise public awareness about the actual and potential dangers counterfeit products pose to consumer health and safety;\n**(3)**\naffirms the continuing importance and need for comprehensive Federal, State, and private sector-supported education and awareness efforts designed to equip the consumers of the United States with the information and tools needed to safeguard against illegal counterfeit products in traditional commerce, internet commerce, and other electronic commerce platforms; and\n**(4)**\nrecognizes and reaffirms the commitment of the United States to combating counterfeiting by promoting awareness about the actual and potential harm of counterfeiting to consumers and brand owners and by promoting new education programs and campaigns designed to reduce the supply of, and demand for, counterfeit products.",
      "versionDate": "2025-07-08",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres314ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 314\nIN THE SENATE OF THE UNITED STATES\nJuly 8, 2025 Mr. Grassley (for himself, Mr. Coons , Mr. Tillis , and Ms. Hirono ) submitted the following resolution; which was referred to the Committee on the Judiciary\nJuly 17, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nRecognizing the importance of trademarks in the economy and the role of trademarks in protecting consumer safety, by designating the month of July as National Anti-Counterfeiting and Consumer Education and Awareness Month .\nThat the Senate\u2014\n**(1)**\ndesignates the month of July 2025 as National Anti-Counterfeiting and Consumer Education and Awareness Month ;\n**(2)**\nsupports the goals and ideals of National Anti-Counterfeiting and Consumer Education and Awareness Month to educate the public and raise public awareness about the actual and potential dangers counterfeit products pose to consumer health and safety;\n**(3)**\naffirms the continuing importance and need for comprehensive Federal, State, and private sector-supported education and awareness efforts designed to equip the consumers of the United States with the information and tools needed to safeguard against illegal counterfeit products in traditional commerce, internet commerce, and other electronic commerce platforms; and\n**(4)**\nrecognizes and reaffirms the commitment of the United States to combating counterfeiting by promoting awareness about the actual and potential harm of counterfeiting to consumers and brand owners and by promoting new education programs and campaigns designed to reduce the supply of, and demand for, counterfeit products.",
      "versionDate": "2025-07-08",
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
            "name": "Commemorative events and holidays",
            "updateDate": "2025-07-24T14:49:17Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-07-24T14:49:17Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-07-24T14:49:17Z"
          },
          {
            "name": "Intellectual property",
            "updateDate": "2025-07-24T14:49:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-07-17T10:58:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-08",
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
          "measure-id": "id119sres314",
          "measure-number": "314",
          "measure-type": "sres",
          "orig-publish-date": "2025-07-08",
          "originChamber": "SENATE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres314v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-07-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution designates July 2025\u00a0as National Anti-Counterfeiting and Consumer Education and Awareness Month.</p>"
        },
        "title": "A resolution recognizing the importance of trademarks in the economy and the role of trademarks in protecting consumer safety, by designating the month of July as \"National Anti-Counterfeiting and Consumer Education and Awareness Month\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres314.xml",
    "summary": {
      "actionDate": "2025-07-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates July 2025\u00a0as National Anti-Counterfeiting and Consumer Education and Awareness Month.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119sres314"
    },
    "title": "A resolution recognizing the importance of trademarks in the economy and the role of trademarks in protecting consumer safety, by designating the month of July as \"National Anti-Counterfeiting and Consumer Education and Awareness Month\"."
  },
  "summaries": [
    {
      "actionDate": "2025-07-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates July 2025\u00a0as National Anti-Counterfeiting and Consumer Education and Awareness Month.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119sres314"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres314is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-07-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres314ats.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution recognizing the importance of trademarks in the economy and the role of trademarks in protecting consumer safety, by designating the month of July as \"National Anti-Counterfeiting and Consumer Education and Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-10T02:48:24Z"
    },
    {
      "title": "A resolution recognizing the importance of trademarks in the economy and the role of trademarks in protecting consumer safety, by designating the month of July as \"National Anti-Counterfeiting and Consumer Education and Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-09T10:56:22Z"
    }
  ]
}
```
