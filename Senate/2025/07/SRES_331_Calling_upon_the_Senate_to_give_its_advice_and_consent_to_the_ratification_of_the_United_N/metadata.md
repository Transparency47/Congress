# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/331?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/331
- Title: A resolution calling upon the Senate to give its advice and consent to the ratification of the United Nations Convention on the Law of the Sea.
- Congress: 119
- Bill type: SRES
- Bill number: 331
- Origin chamber: Senate
- Introduced date: 2025-07-22
- Update date: 2026-03-31T14:52:15Z
- Update date including text: 2026-03-31T14:52:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-22: Introduced in Senate
- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S4531)
- Latest action: 2025-07-22: Introduced in Senate

## Actions

- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S4531)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/331",
    "number": "331",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "A resolution calling upon the Senate to give its advice and consent to the ratification of the United Nations Convention on the Law of the Sea.",
    "type": "SRES",
    "updateDate": "2026-03-31T14:52:15Z",
    "updateDateIncludingText": "2026-03-31T14:52:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S4531)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-22",
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
          "date": "2025-07-22T15:28:34Z",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "AK"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "VA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "LA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "MD"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "IN"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-22",
      "state": "ME"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "RI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "NV"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "HI"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "DE"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres331is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 331\nIN THE SENATE OF THE UNITED STATES\nJuly 22, 2025 Ms. Hirono (for herself, Ms. Murkowski , Mr. Kaine , Mr. Cassidy , Mr. Van Hollen , Mr. Young , and Mr. King ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nCalling upon the Senate to give its advice and consent to the ratification of the United Nations Convention on the Law of the Sea.\nThat the Senate\u2014\n**(1)**\naffirms that it is in the national interest for the United States to become a formal signatory of the United Nations Convention on the Law of the Sea (UNCLOS), done at Montego Bay December 10, 1982;\n**(2)**\nurges the United States Senate to give its advice and consent to the ratification of the UNCLOS; and\n**(3)**\nrecommends the ratification of the UNCLOS remain a top priority for the Federal Government, the importance of which was most recently underscored by the strategic challenges the United States faces in the Indo-Pacific, the Arctic, and the Black Sea regions.",
      "versionDate": "2025-07-22",
      "versionType": "IS"
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
        "updateDate": "2025-07-29T22:22:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-22",
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
          "measure-id": "id119sres331",
          "measure-number": "331",
          "measure-type": "sres",
          "orig-publish-date": "2025-07-22",
          "originChamber": "SENATE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres331v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-07-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution urges the Senate to give its advice and consent to the ratification of the United Nations Convention on the Law of the Sea. The resolution affirms that it is in the national interest for the United States to become a formal signatory of the convention, and it recommends that this ratification remain a top federal priority.</p>"
        },
        "title": "A resolution calling upon the Senate to give its advice and consent to the ratification of the United Nations Convention on the Law of the Sea."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres331.xml",
    "summary": {
      "actionDate": "2025-07-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution urges the Senate to give its advice and consent to the ratification of the United Nations Convention on the Law of the Sea. The resolution affirms that it is in the national interest for the United States to become a formal signatory of the convention, and it recommends that this ratification remain a top federal priority.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119sres331"
    },
    "title": "A resolution calling upon the Senate to give its advice and consent to the ratification of the United Nations Convention on the Law of the Sea."
  },
  "summaries": [
    {
      "actionDate": "2025-07-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution urges the Senate to give its advice and consent to the ratification of the United Nations Convention on the Law of the Sea. The resolution affirms that it is in the national interest for the United States to become a formal signatory of the convention, and it recommends that this ratification remain a top federal priority.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119sres331"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres331is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A resolution calling upon the Senate to give its advice and consent to the ratification of the United Nations Convention on the Law of the Sea.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:48:39Z"
    },
    {
      "title": "A resolution calling upon the Senate to give its advice and consent to the ratification of the United Nations Convention on the Law of the Sea.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T10:56:16Z"
    }
  ]
}
```
