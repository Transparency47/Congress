# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/107?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/107
- Title: A resolution expressing support for the designation of the week of March 3 through March 7, 2025, as "National Social and Emotional Learning Week" to recognize the critical role social and emotional learning plays in supporting the academic success and overall well-being of students, educators, and families.
- Congress: 119
- Bill type: SRES
- Bill number: 107
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2026-03-05T16:41:07Z
- Update date including text: 2026-03-05T16:41:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1583)
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1583)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/107",
    "number": "107",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "A resolution expressing support for the designation of the week of March 3 through March 7, 2025, as \"National Social and Emotional Learning Week\" to recognize the critical role social and emotional learning plays in supporting the academic success and overall well-being of students, educators, and families.",
    "type": "SRES",
    "updateDate": "2026-03-05T16:41:07Z",
    "updateDateIncludingText": "2026-03-05T16:41:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1583)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T17:12:17Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CT"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-03-05",
      "state": "VT"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-05",
      "state": "ME"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MD"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "VA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres107is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 107\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mr. Durbin (for himself, Mr. Blumenthal , Ms. Duckworth , Mr. Sanders , Mr. King , Mr. Booker , Mr. Van Hollen , and Mr. Kaine ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nExpressing support for the designation of the week of March 3 through March 7, 2025, as National Social and Emotional Learning Week to recognize the critical role social and emotional learning plays in supporting the academic success and overall well-being of students, educators, and families.\nThat the Senate\u2014\n**(1)**\nsupports the designation of National Social and Emotional Learning Week ;\n**(2)**\nrecognizes the role that social and emotional learning plays in promoting academic achievement, mental and behavioral health, and future career success for students;\n**(3)**\nexpresses support for expanding access to social and emotional learning for each student and teacher; and\n**(4)**\nencourages the people of the United States to identify opportunities among Federal agencies to advance social and emotional learning to support the academic success and overall well-being of students, parents, educators, and their communities.",
      "versionDate": "2025-03-05",
      "versionType": "IS"
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
        "actionDate": "2026-03-02",
        "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S734-735)"
      },
      "number": "624",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution expressing support for the designation of the week of March 2 through March 6, 2026, as \"National Social and Emotional Learning Week\" to recognize the critical role social and emotional learning plays in supporting the academic success and overall well-being of students, educators, and families.",
      "type": "SRES"
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
        "name": "Education",
        "updateDate": "2025-03-10T17:52:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119sres107",
          "measure-number": "107",
          "measure-type": "sres",
          "orig-publish-date": "2025-03-05",
          "originChamber": "SENATE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres107v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution supports the designation of National Social and Emotional Learning Week.</p>"
        },
        "title": "A resolution expressing support for the designation of the week of March 3 through March 7, 2025, as \"National Social and Emotional Learning Week\" to recognize the critical role social and emotional learning plays in supporting the academic success and overall well-being of students, educators, and families."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres107.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution supports the designation of National Social and Emotional Learning Week.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119sres107"
    },
    "title": "A resolution expressing support for the designation of the week of March 3 through March 7, 2025, as \"National Social and Emotional Learning Week\" to recognize the critical role social and emotional learning plays in supporting the academic success and overall well-being of students, educators, and families."
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution supports the designation of National Social and Emotional Learning Week.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119sres107"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres107is.xml"
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
      "title": "A resolution expressing support for the designation of the week of March 3 through March 7, 2025, as \"National Social and Emotional Learning Week\" to recognize the critical role social and emotional learning plays in supporting the academic success and overall well-being of students, educators, and families.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T04:18:30Z"
    },
    {
      "title": "A resolution expressing support for the designation of the week of March 3 through March 7, 2025, as \"National Social and Emotional Learning Week\" to recognize the critical role social and emotional learning plays in supporting the academic success and overall well-being of students, educators, and families.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T11:56:21Z"
    }
  ]
}
```
