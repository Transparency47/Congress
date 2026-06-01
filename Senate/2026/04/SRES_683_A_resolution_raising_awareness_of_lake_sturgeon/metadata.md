# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/683?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/683
- Title: A resolution raising awareness of lake sturgeon.
- Congress: 119
- Bill type: SRES
- Bill number: 683
- Origin chamber: Senate
- Introduced date: 2026-04-22
- Update date: 2026-05-15T10:56:34Z
- Update date including text: 2026-05-15T10:56:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in Senate
- 2026-04-22 - IntroReferral: Referred to the Committee on Environment and Public Works. (text: CR S1937-1938)
- 2026-04-22 - IntroReferral: Submitted in Senate
- Latest action: 2026-04-22: Submitted in Senate

## Actions

- 2026-04-22 - IntroReferral: Referred to the Committee on Environment and Public Works. (text: CR S1937-1938)
- 2026-04-22 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/683",
    "number": "683",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "A resolution raising awareness of lake sturgeon.",
    "type": "SRES",
    "updateDate": "2026-05-15T10:56:34Z",
    "updateDateIncludingText": "2026-05-15T10:56:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Environment and Public Works. (text: CR S1937-1938)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
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
        "item": {
          "date": "2026-04-22T18:11:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres683is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 683\nIN THE SENATE OF THE UNITED STATES\nApril 22, 2026 Mr. Welch submitted the following resolution; which was referred to the Committee on Environment and Public Works\nRESOLUTION\nRaising awareness of lake sturgeon.\nThat the Senate encourages\u2014\n**(1)**\ncontinued collaboration among Federal, State, Tribal, and other partners to manage and increase lake sturgeon populations across their extensive range;\n**(2)**\ncontinued collaboration with Canada to jointly manage and increase lake sturgeon populations in our shared waters;\n**(3)**\ncontinued efforts to identify, protect, and restore the habitat of lake sturgeon;\n**(4)**\ncontinued efforts to prevent and control the spread of invasive species and restore the reproductive habitat of lake sturgeon;\n**(5)**\nincreased public awareness of lake sturgeon; and\n**(6)**\nthe education of anglers and local communities on the proper ways to handle lake sturgeon if caught.",
      "versionDate": "2026-04-22",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-04-29T20:55:02Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres683is.xml"
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
      "title": "A resolution raising awareness of lake sturgeon.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-28T05:48:28Z"
    },
    {
      "title": "A resolution raising awareness of lake sturgeon.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T10:56:22Z"
    }
  ]
}
```
