# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/711?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/711
- Title: A resolution expressing support for the designation of May 2026 as "National Beef Month" to recognize the important role cattle play in the United States, and to consumers.
- Congress: 119
- Bill type: SRES
- Bill number: 711
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-20T18:28:55Z
- Update date including text: 2026-05-20T18:28:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2176)
- 2026-04-30 - IntroReferral: Submitted in Senate
- 2026-05-13 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-05-13 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-05-13 - Committee: Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent.
- 2026-05-13 - Discharge: Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent. (consideration: CR S2283)
- Latest action: 2026-04-30: Submitted in Senate

## Actions

- 2026-04-30 - IntroReferral: Referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2176)
- 2026-04-30 - IntroReferral: Submitted in Senate
- 2026-05-13 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-05-13 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2026-05-13 - Committee: Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent.
- 2026-05-13 - Discharge: Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent. (consideration: CR S2283)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/711",
    "number": "711",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "A resolution expressing support for the designation of May 2026 as \"National Beef Month\" to recognize the important role cattle play in the United States, and to consumers.",
    "type": "SRES",
    "updateDate": "2026-05-20T18:28:55Z",
    "updateDateIncludingText": "2026-05-20T18:28:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent. (consideration: CR S2283)",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Agriculture, Nutrition, and Forestry discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S2176)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
            "date": "2026-05-13T23:11:26Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-04-30T17:51:26Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MN"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "MS"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "KS"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "NE"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres711is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 711\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Ricketts (for himself, Ms. Klobuchar , Mrs. Hyde-Smith , Mr. Marshall , Mrs. Fischer , and Mr. Lankford ) submitted the following resolution; which was referred to the Committee on Agriculture, Nutrition, and Forestry\nRESOLUTION\nExpressing support for the designation of May 2026 as National Beef Month to recognize the important role cattle play in the United States, and to consumers.\nThat the Senate\u2014\n**(1)**\nsupports the designation of May 2026 as National Beef Month ; and\n**(2)**\nrecognizes that\u2014\n**(A)**\nhistorically, cattle production has contributed about 22 percent of the total cash receipts for agricultural commodities of the United States;\n**(B)**\nthe United States is also the largest consumer of beef in the world and primarily consumes high-value, grain-fed beef; and\n**(C)**\nbeef is an excellent source of nutritious protein.",
      "versionDate": "2026-04-30",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres711ats.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 711\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Ricketts (for himself, Ms. Klobuchar , Mrs. Hyde-Smith , Mr. Marshall , Mrs. Fischer , and Mr. Lankford ) submitted the following resolution; which was referred to the Committee on Agriculture, Nutrition, and Forestry\nMay 13, 2026 Committee discharged; considered and agreed to\nRESOLUTION\nExpressing support for the designation of May 2026 as National Beef Month to recognize the important role cattle play in the United States, and to consumers.\nThat the Senate\u2014\n**(1)**\nsupports the designation of May 2026 as National Beef Month ; and\n**(2)**\nrecognizes that\u2014\n**(A)**\nhistorically, cattle production has contributed about 22 percent of the total cash receipts for agricultural commodities of the United States;\n**(B)**\nthe United States is also the largest consumer of beef in the world and primarily consumes high-value, grain-fed beef; and\n**(C)**\nbeef is an excellent source of nutritious protein.",
      "versionDate": "2026-05-11",
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
            "updateDate": "2026-05-20T18:28:44Z"
          },
          {
            "name": "Livestock",
            "updateDate": "2026-05-20T18:28:50Z"
          },
          {
            "name": "Meat",
            "updateDate": "2026-05-20T18:28:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2026-05-18T20:56:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-05-13",
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
          "measure-id": "id119sres711",
          "measure-number": "711",
          "measure-type": "sres",
          "orig-publish-date": "2026-05-13",
          "originChamber": "SENATE",
          "update-date": "2026-05-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres711v55",
            "update-date": "2026-05-19"
          },
          "action-date": "2026-05-13",
          "action-desc": "Passed Senate",
          "summary-text": "<p>This resolution supports the designation of May 2026 as National Beef Month.</p>"
        },
        "title": "A resolution expressing support for the designation of May 2026 as \"National Beef Month\" to recognize the important role cattle play in the United States, and to consumers."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres711.xml",
    "summary": {
      "actionDate": "2026-05-13",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution supports the designation of May 2026 as National Beef Month.</p>",
      "updateDate": "2026-05-19",
      "versionCode": "id119sres711"
    },
    "title": "A resolution expressing support for the designation of May 2026 as \"National Beef Month\" to recognize the important role cattle play in the United States, and to consumers."
  },
  "summaries": [
    {
      "actionDate": "2026-05-13",
      "actionDesc": "Passed Senate",
      "text": "<p>This resolution supports the designation of May 2026 as National Beef Month.</p>",
      "updateDate": "2026-05-19",
      "versionCode": "id119sres711"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres711is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-05-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres711ats.xml"
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
      "title": "A resolution expressing support for the designation of May 2026 as \"National Beef Month\" to recognize the important role cattle play in the United States, and to consumers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T02:33:39Z"
    },
    {
      "title": "A resolution expressing support for the designation of May 2026 as \"National Beef Month\" to recognize the important role cattle play in the United States, and to consumers.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T10:56:31Z"
    }
  ]
}
```
