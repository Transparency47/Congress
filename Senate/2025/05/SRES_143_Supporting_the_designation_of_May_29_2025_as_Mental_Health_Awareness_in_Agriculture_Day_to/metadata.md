# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/143?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/143
- Title: A resolution supporting the designation of May 29, 2025, as "Mental Health Awareness in Agriculture Day" to raise awareness around mental health in the agricultural industry and workforce and to continue to reduce stigma associated with mental illness.
- Congress: 119
- Bill type: SRES
- Bill number: 143
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2026-05-29T15:48:38Z
- Update date including text: 2026-05-29T15:48:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1877-1878)
- 2025-05-19 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-05-19 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2965-2966; text: 03/26/2025 CR S1877-1878)
- 2025-05-19 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-05-19 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1877-1878)
- 2025-05-19 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-05-19 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2965-2966; text: 03/26/2025 CR S1877-1878)
- 2025-05-19 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-05-19 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/143",
    "number": "143",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "A resolution supporting the designation of May 29, 2025, as \"Mental Health Awareness in Agriculture Day\" to raise awareness around mental health in the agricultural industry and workforce and to continue to reduce stigma associated with mental illness.",
    "type": "SRES",
    "updateDate": "2026-05-29T15:48:38Z",
    "updateDateIncludingText": "2026-05-29T15:48:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-19",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S2965-2966; text: 03/26/2025 CR S1877-1878)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-05-19",
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
      "actionDate": "2025-05-19",
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
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S1877-1878)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-26",
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
            "date": "2025-05-20T01:32:56Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-03-27T00:16:01Z",
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CO"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "KS"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "MN"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "KS"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "NC"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "DE"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "IA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "MI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "IL"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "SD"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "NE"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "ND"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "MN"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres143is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 143\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mrs. Fischer (for herself, Mr. Bennet , Mr. Marshall , Ms. Smith , Mr. Moran , Mr. Tillis , Mr. Coons , Ms. Ernst , Mr. Schiff , Mr. Peters , Mr. Durbin , Mr. Rounds , Mr. Ricketts , and Mr. Hoeven ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nSupporting the designation of May 29, 2025, as Mental Health Awareness in Agriculture Day to raise awareness around mental health in the agricultural industry and workforce and to continue to reduce stigma associated with mental illness.\nThat the Senate\u2014\n**(1)**\ndesignates May 29, 2025, as Mental Health Awareness in Agriculture Day to raise awareness around mental health in the agricultural industry and reduce the stigma associated with mental illness;\n**(2)**\nrecognizes the important role of individuals in agriculture as providers of high-quality products to the United States and the world;\n**(3)**\nseeks to create awareness for the unique challenges agricultural producers and workers face, such as weather unpredictability, labor intensity and shortages, farm succession, and fluctuating commodity and market prices;\n**(4)**\nhighlights the resources available through the Farm and Ranch Stress Assistance Network of the Department of Agriculture in connecting agricultural producers and workers to stress assistance programs; and\n**(5)**\nencourages all individuals to observe Mental Health Awareness in Agriculture Day as an opportunity to promote mental well-being and awareness for current and future agricultural producers and workers.",
      "versionDate": "2025-03-26",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres143ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 143\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mrs. Fischer (for herself, Mr. Bennet , Mr. Marshall , Ms. Smith , Mr. Moran , Mr. Tillis , Mr. Coons , Ms. Ernst , Mr. Schiff , Mr. Peters , Mr. Durbin , Mr. Rounds , Mr. Ricketts , Mr. Hoeven , Ms. Klobuchar , and Mr. Boozman ) submitted the following resolution; which was referred to the Committee on the Judiciary\nMay 19, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nSupporting the designation of May 29, 2025, as Mental Health Awareness in Agriculture Day to raise awareness around mental health in the agricultural industry and workforce and to continue to reduce stigma associated with mental illness.\nThat the Senate\u2014\n**(1)**\ndesignates May 29, 2025, as Mental Health Awareness in Agriculture Day to raise awareness around mental health in the agricultural industry and reduce the stigma associated with mental illness;\n**(2)**\nrecognizes the important role of individuals in agriculture as providers of high-quality products to the United States and the world;\n**(3)**\nseeks to create awareness for the unique challenges agricultural producers and workers face, such as weather unpredictability, labor intensity and shortages, farm succession, and fluctuating commodity and market prices;\n**(4)**\nhighlights the resources available through the Farm and Ranch Stress Assistance Network of the Department of Agriculture in connecting agricultural producers and workers to stress assistance programs; and\n**(5)**\nencourages all individuals to observe Mental Health Awareness in Agriculture Day as an opportunity to promote mental well-being and awareness for current and future agricultural producers and workers.",
      "versionDate": "2025-05-19",
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
        "actionDate": "2026-05-13",
        "text": "Referred to the Committee on the Judiciary. (text: CR S2281-2282)"
      },
      "number": "727",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution supporting the designation of May 29, 2026, as \"Mental Health Awareness in Agriculture Day\" to raise awareness around mental health in the agricultural industry and workforce and to continue to reduce stigma associated with mental illness.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Agricultural practices and innovations",
            "updateDate": "2025-05-20T15:37:42Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-05-20T15:37:55Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-05-20T15:36:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T17:08:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-26",
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
          "measure-id": "id119sres143",
          "measure-number": "143",
          "measure-type": "sres",
          "orig-publish-date": "2025-03-26",
          "originChamber": "SENATE",
          "update-date": "2025-06-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres143v00",
            "update-date": "2025-06-06"
          },
          "action-date": "2025-03-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution designates May 29, 2025, as Mental Health Awareness in Agriculture Day to raise awareness around mental health in the agricultural industry and reduce the stigma associated with mental illness.</p>"
        },
        "title": "A resolution supporting the designation of May 29, 2025, as \"Mental Health Awareness in Agriculture Day\" to raise awareness around mental health in the agricultural industry and workforce and to continue to reduce stigma associated with mental illness."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres143.xml",
    "summary": {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates May 29, 2025, as Mental Health Awareness in Agriculture Day to raise awareness around mental health in the agricultural industry and reduce the stigma associated with mental illness.</p>",
      "updateDate": "2025-06-06",
      "versionCode": "id119sres143"
    },
    "title": "A resolution supporting the designation of May 29, 2025, as \"Mental Health Awareness in Agriculture Day\" to raise awareness around mental health in the agricultural industry and workforce and to continue to reduce stigma associated with mental illness."
  },
  "summaries": [
    {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates May 29, 2025, as Mental Health Awareness in Agriculture Day to raise awareness around mental health in the agricultural industry and reduce the stigma associated with mental illness.</p>",
      "updateDate": "2025-06-06",
      "versionCode": "id119sres143"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres143is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres143ats.xml"
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
      "title": "A resolution supporting the designation of May 29, 2025, as \"Mental Health Awareness in Agriculture Day\" to raise awareness around mental health in the agricultural industry and workforce and to continue to reduce stigma associated with mental illness.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:08:23Z"
    },
    {
      "title": "A resolution supporting the designation of May 29, 2025, as \"Mental Health Awareness in Agriculture Day\" to raise awareness around mental health in the agricultural industry and workforce and to continue to reduce stigma associated with mental illness.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T10:56:21Z"
    }
  ]
}
```
