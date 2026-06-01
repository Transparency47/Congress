# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/301?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/301
- Title: A resolution condemning the attacks on Minnesota lawmakers in Brooklyn Park and Champlin, Minnesota and calling for unity and the rejection of political violence in Minnesota and across the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 301
- Origin chamber: Senate
- Introduced date: 2025-06-24
- Update date: 2026-03-30T20:06:01Z
- Update date including text: 2026-03-30T20:06:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-24: Introduced in Senate
- 2025-06-24 - IntroReferral: Introduced in Senate
- 2025-06-24 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-06-26 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-06-26 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S3577; text: 6/24/2025 CR S3519)
- 2025-06-26 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-06-26 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- Latest action: 2025-06-24: Introduced in Senate

## Actions

- 2025-06-24 - IntroReferral: Introduced in Senate
- 2025-06-24 - IntroReferral: Referred to the Committee on the Judiciary.
- 2025-06-26 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.
- 2025-06-26 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S3577; text: 6/24/2025 CR S3519)
- 2025-06-26 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-06-26 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/301",
    "number": "301",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "A resolution condemning the attacks on Minnesota lawmakers in Brooklyn Park and Champlin, Minnesota and calling for unity and the rejection of political violence in Minnesota and across the United States.",
    "type": "SRES",
    "updateDate": "2026-03-30T20:06:01Z",
    "updateDateIncludingText": "2026-03-30T20:06:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent. (consideration: CR S3577; text: 6/24/2025 CR S3519)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-26",
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
      "actionDate": "2025-06-26",
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
      "actionDate": "2025-06-24",
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
      "actionDate": "2025-06-24",
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
            "date": "2025-06-26T23:20:52Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-06-24T22:34:05Z",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MN"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "SD"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "IA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "WI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres301is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 301\nIN THE SENATE OF THE UNITED STATES\nJune 24, 2025 Ms. Klobuchar (for herself, Ms. Smith , Mr. Thune , Mr. Schumer , Mr. Grassley , and Ms. Baldwin ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCondemning the attacks on Minnesota lawmakers in Brooklyn Park and Champlin, Minnesota and calling for unity and the rejection of political violence in Minnesota and across the United States.\nThat the Senate, in this moment of tragic loss\u2014\n**(1)**\nstrongly condemns and denounces the attacks on Minnesota State legislators in Brooklyn Park and Champlin, Minnesota on June 14, 2025;\n**(2)**\nhonors the life of Speaker Emerita Melissa Hortman for her devotion to public service and her tireless efforts to serve the people of Minnesota and the life of her husband, Mark Hortman;\n**(3)**\nhonors Senator John Hoffman and his wife, Yvette Hoffman, who were shot and critically injured, and wishes for their full and speedy recovery;\n**(4)**\nhonors the courageous law enforcement officers who saved additional lives with their rapid response to the attack and successfully apprehended and charged the suspected perpetrator on June 15, 2025;\n**(5)**\ncalls on all community leaders and elected officials to publicly and unequivocally denounce acts of political violence; and\n**(6)**\ncalls on all people of the United States to unite in this moment of pain and tragedy and reaffirm the commitment of the people of the United States to a safe, civil, and peaceful democracy in which violent rhetoric and acts are not tolerated.",
      "versionDate": "2025-06-24",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres301ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 301\nIN THE SENATE OF THE UNITED STATES\nJune 24, 2025 Ms. Klobuchar (for herself, Ms. Smith , Mr. Thune , Mr. Schumer , Mr. Grassley , Ms. Baldwin , and Mr. Durbin ) submitted the following resolution; which was referred to the Committee on the Judiciary\nJune 26 (legislative day, June 24), 2025 Committee discharged; considered and agreed to\nRESOLUTION\nCondemning the attacks on Minnesota lawmakers in Brooklyn Park and Champlin, Minnesota and calling for unity and the rejection of political violence in Minnesota and across the United States.\nThat the Senate, in this moment of tragic loss\u2014\n**(1)**\nstrongly condemns and denounces the attacks on Minnesota State legislators in Brooklyn Park and Champlin, Minnesota on June 14, 2025;\n**(2)**\nhonors the life of Speaker Emerita Melissa Hortman for her devotion to public service and her tireless efforts to serve the people of Minnesota and the life of her husband, Mark Hortman;\n**(3)**\nhonors Senator John Hoffman and his wife, Yvette Hoffman, who were shot and critically injured, and wishes for their full and speedy recovery;\n**(4)**\nhonors the courageous law enforcement officers who saved additional lives with their rapid response to the attack and successfully apprehended and charged the suspected perpetrator on June 15, 2025;\n**(5)**\ncalls on all community leaders and elected officials to publicly and unequivocally denounce acts of political violence; and\n**(6)**\ncalls on all people of the United States to unite in this moment of pain and tragedy and reaffirm the commitment of the people of the United States to a safe, civil, and peaceful democracy in which violent rhetoric and acts are not tolerated.",
      "versionDate": "2025-06-26",
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
        "actionDate": "2025-06-25",
        "actionTime": "16:46:48",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "519",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Condemning the attacks on Minnesota lawmakers in Brooklyn Park and Champlin, Minnesota, and calling for unity and the rejection of political violence in Minnesota and across the United States.",
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
            "name": "Congressional tributes",
            "updateDate": "2025-07-09T13:26:39Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-07-09T13:26:39Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-07-09T13:26:39Z"
          },
          {
            "name": "Minnesota",
            "updateDate": "2025-07-09T13:26:39Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-07-09T13:26:39Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-07-09T13:26:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-07-08T13:27:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-24",
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
          "measure-id": "id119sres301",
          "measure-number": "301",
          "measure-type": "sres",
          "orig-publish-date": "2025-06-24",
          "originChamber": "SENATE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres301v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2025-06-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution condemns the June 14, 2025, attacks on Minnesota state legislators\u00a0and calls on the people of the United States to reaffirm our commitment to a safe, civil, and peaceful democracy.</p><p>The resolution also honors (1) the lives of Speaker Emerita Melissa Hortman and her husband Mark Hortman who were killed, (2) Senator John Hoffman and his wife Yvette Hoffman who were critically injured, and (3) the law enforcement officers who rapidly responded to the attacks and apprehended the suspected perpetrator.</p>"
        },
        "title": "A resolution condemning the attacks on Minnesota lawmakers in Brooklyn Park and Champlin, Minnesota and calling for unity and the rejection of political violence in Minnesota and across the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres301.xml",
    "summary": {
      "actionDate": "2025-06-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution condemns the June 14, 2025, attacks on Minnesota state legislators\u00a0and calls on the people of the United States to reaffirm our commitment to a safe, civil, and peaceful democracy.</p><p>The resolution also honors (1) the lives of Speaker Emerita Melissa Hortman and her husband Mark Hortman who were killed, (2) Senator John Hoffman and his wife Yvette Hoffman who were critically injured, and (3) the law enforcement officers who rapidly responded to the attacks and apprehended the suspected perpetrator.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119sres301"
    },
    "title": "A resolution condemning the attacks on Minnesota lawmakers in Brooklyn Park and Champlin, Minnesota and calling for unity and the rejection of political violence in Minnesota and across the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-06-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution condemns the June 14, 2025, attacks on Minnesota state legislators\u00a0and calls on the people of the United States to reaffirm our commitment to a safe, civil, and peaceful democracy.</p><p>The resolution also honors (1) the lives of Speaker Emerita Melissa Hortman and her husband Mark Hortman who were killed, (2) Senator John Hoffman and his wife Yvette Hoffman who were critically injured, and (3) the law enforcement officers who rapidly responded to the attacks and apprehended the suspected perpetrator.</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119sres301"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres301is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres301ats.xml"
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
      "title": "A resolution condemning the attacks on Minnesota lawmakers in Brooklyn Park and Champlin, Minnesota and calling for unity and the rejection of political violence in Minnesota and across the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T06:48:21Z"
    },
    {
      "title": "A resolution condemning the attacks on Minnesota lawmakers in Brooklyn Park and Champlin, Minnesota and calling for unity and the rejection of political violence in Minnesota and across the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T10:56:19Z"
    }
  ]
}
```
