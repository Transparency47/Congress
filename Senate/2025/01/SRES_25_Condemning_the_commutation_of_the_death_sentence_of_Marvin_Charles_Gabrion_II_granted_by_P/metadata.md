# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/25?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/25
- Title: A resolution condemning the commutation of the death sentence of Marvin Charles Gabrion II granted by President Biden on December 23, 2024.
- Congress: 119
- Bill type: SRES
- Bill number: 25
- Origin chamber: Senate
- Introduced date: 2025-01-14
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in Senate
- 2025-01-14 - IntroReferral: Introduced in Senate
- 2025-01-14 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S140)
- Latest action: 2025-01-14: Introduced in Senate

## Actions

- 2025-01-14 - IntroReferral: Introduced in Senate
- 2025-01-14 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S140)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/25",
    "number": "25",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "A resolution condemning the commutation of the death sentence of Marvin Charles Gabrion II granted by President Biden on December 23, 2024.",
    "type": "SRES",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S140)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-14",
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
          "date": "2025-01-14T21:16:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres25is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 25\nIN THE SENATE OF THE UNITED STATES\nJanuary 14, 2025 Mr. Cotton submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCondemning the commutation of the death sentence of Marvin Charles Gabrion II granted by President Biden on December 23, 2024.\n#### 1. Sense of the Senate regarding the commutation of the death sentence of Marvin Charles Gabrion II granted by President Biden on December 23, 2024\nIt is the sense of the Senate that\u2014\n**(1)**\nPresident Joseph R. Biden undermined the rule of law and robbed victims of justice when he commuted the death sentence of Marvin Charles Gabrion II on December 23, 2024;\n**(2)**\nMarvin Gabrion was sentenced to death for murdering 19-year-old Rachel Timmerman just 2 days before she was scheduled to testify that Gabrion had abducted and raped her;\n**(3)**\nMarvin Gabrion was also the prime suspect in the disappearance and murder of several other individuals, including Rachel Timmerman\u2019s 11-month-old daughter and 2 potential witnesses at his rape trial;\n**(4)**\nthis commutation is a reprehensible insult to the victims of Marvin Gabrion;\n**(5)**\nPresident Biden claimed that he commuted the death sentences of Marvin Gabrion and 36 other murderers out of a principled opposition to the death penalty but refused to commute the death sentences of the 3 most controversial death row inmates, demonstrating that President Biden was motivated by politics, not principles; and\n**(6)**\nthe Senate unequivocally condemns this commutation.",
      "versionDate": "2025-01-14",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Correctional facilities and imprisonment",
            "updateDate": "2025-01-16T20:49:21Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-01-16T20:49:21Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-01-16T20:49:21Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-01-16T20:49:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-01-16T13:40:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
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
          "measure-id": "id119sres25",
          "measure-number": "25",
          "measure-type": "sres",
          "orig-publish-date": "2025-01-14",
          "originChamber": "SENATE",
          "update-date": "2025-02-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres25v00",
            "update-date": "2025-02-07"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution condemns the\u00a0commutation of the death sentence of Marvin Charles Gabrion II by President Biden.</p>"
        },
        "title": "A resolution condemning the commutation of the death sentence of Marvin Charles Gabrion II granted by President Biden on December 23, 2024."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres25.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution condemns the\u00a0commutation of the death sentence of Marvin Charles Gabrion II by President Biden.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119sres25"
    },
    "title": "A resolution condemning the commutation of the death sentence of Marvin Charles Gabrion II granted by President Biden on December 23, 2024."
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution condemns the\u00a0commutation of the death sentence of Marvin Charles Gabrion II by President Biden.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119sres25"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres25is.xml"
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
      "title": "A resolution condemning the commutation of the death sentence of Marvin Charles Gabrion II granted by President Biden on December 23, 2024.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-16T01:18:24Z"
    },
    {
      "title": "A resolution condemning the commutation of the death sentence of Marvin Charles Gabrion II granted by President Biden on December 23, 2024.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-15T11:56:18Z"
    }
  ]
}
```
