# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/122?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/122
- Title: A resolution recognizing the contributions of AmeriCorps members and alumni and AmeriCorps Seniors volunteers in the lives of the people and communities of the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 122
- Origin chamber: Senate
- Introduced date: 2025-03-10
- Update date: 2026-03-27T01:18:52Z
- Update date including text: 2026-03-27T01:18:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in Senate
- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1633)
- Latest action: 2025-03-10: Introduced in Senate

## Actions

- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1633)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/122",
    "number": "122",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "A resolution recognizing the contributions of AmeriCorps members and alumni and AmeriCorps Seniors volunteers in the lives of the people and communities of the United States.",
    "type": "SRES",
    "updateDate": "2026-03-27T01:18:52Z",
    "updateDateIncludingText": "2026-03-27T01:18:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1633)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T22:11:57Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "DE"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "ME"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "WI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "IL"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NM"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "HI"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-10",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "NM"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "RI"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres122is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 122\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2025 Mr. Cassidy (for himself, Mr. Coons , Ms. Collins , Ms. Baldwin , Mr. Durbin , Mr. Heinrich , Ms. Hirono , Mr. King , Ms. Klobuchar , Mr. Luj\u00e1n , Mr. Reed , and Mrs. Shaheen ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nRecognizing the contributions of AmeriCorps members and alumni and AmeriCorps Seniors volunteers in the lives of the people and communities of the United States.\nThat the Senate\u2014\n**(1)**\nencourages the people of the United States to join in a national effort\u2014\n**(A)**\nto salute AmeriCorps members and alumni and AmeriCorps Seniors volunteers; and\n**(B)**\nto raise awareness about the importance of national and community service;\n**(2)**\nacknowledges the significant accomplishments across a 30-year history of the volunteers, members, alumni, and community partners of AmeriCorps and AmeriCorps Seniors;\n**(3)**\nrecognizes the important contributions made by AmeriCorps members and alumni and AmeriCorps Seniors volunteers to the lives of the people of the United States; and\n**(4)**\nencourages individuals of all ages to consider opportunities to serve in AmeriCorps and AmeriCorps Seniors.",
      "versionDate": "2025-03-10",
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
        "name": "Labor and Employment",
        "updateDate": "2025-03-17T15:42:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-10",
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
          "measure-id": "id119sres122",
          "measure-number": "122",
          "measure-type": "sres",
          "orig-publish-date": "2025-03-10",
          "originChamber": "SENATE",
          "update-date": "2026-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres122v00",
            "update-date": "2026-03-27"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution encourages (1) the people of the United States to join in a national effort to salute AmeriCorps members, alumni, and AmeriCorps Seniors volunteers and to raise awareness about the importance of national and community service; and (2) all individuals to consider opportunities to serve in AmeriCorps and AmeriCorps Seniors.</p>"
        },
        "title": "A resolution recognizing the contributions of AmeriCorps members and alumni and AmeriCorps Seniors volunteers in the lives of the people and communities of the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres122.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution encourages (1) the people of the United States to join in a national effort to salute AmeriCorps members, alumni, and AmeriCorps Seniors volunteers and to raise awareness about the importance of national and community service; and (2) all individuals to consider opportunities to serve in AmeriCorps and AmeriCorps Seniors.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119sres122"
    },
    "title": "A resolution recognizing the contributions of AmeriCorps members and alumni and AmeriCorps Seniors volunteers in the lives of the people and communities of the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution encourages (1) the people of the United States to join in a national effort to salute AmeriCorps members, alumni, and AmeriCorps Seniors volunteers and to raise awareness about the importance of national and community service; and (2) all individuals to consider opportunities to serve in AmeriCorps and AmeriCorps Seniors.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119sres122"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres122is.xml"
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
      "title": "A resolution recognizing the contributions of AmeriCorps members and alumni and AmeriCorps Seniors volunteers in the lives of the people and communities of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:33:31Z"
    },
    {
      "title": "A resolution recognizing the contributions of AmeriCorps members and alumni and AmeriCorps Seniors volunteers in the lives of the people and communities of the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-11T10:56:17Z"
    }
  ]
}
```
