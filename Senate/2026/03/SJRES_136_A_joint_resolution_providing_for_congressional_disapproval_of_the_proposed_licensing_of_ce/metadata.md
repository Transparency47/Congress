# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/136?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/136
- Title: A joint resolution providing for congressional disapproval of the proposed licensing of certain defense articles and services to Israel.
- Congress: 119
- Bill type: SJRES
- Bill number: 136
- Origin chamber: Senate
- Introduced date: 2026-03-19
- Update date: 2026-03-30T22:38:24Z
- Update date including text: 2026-03-30T22:38:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in Senate
- 2026-03-19 - IntroReferral: Introduced in Senate
- 2026-03-19 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2026-03-19: Introduced in Senate

## Actions

- 2026-03-19 - IntroReferral: Introduced in Senate
- 2026-03-19 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/136",
    "number": "136",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S000033",
        "district": "",
        "firstName": "Bernie",
        "fullName": "Sen. Sanders, Bernard [I-VT]",
        "lastName": "Sanders",
        "party": "I",
        "state": "VT"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval of the proposed licensing of certain defense articles and services to Israel.",
    "type": "SJRES",
    "updateDate": "2026-03-30T22:38:24Z",
    "updateDateIncludingText": "2026-03-30T22:38:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T16:40:01Z",
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
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "MD"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "OR"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres136is.xml",
      "text": "IIA\n119th CONGRESS\n2d Session\nS. J. RES. 136\nIN THE SENATE OF THE UNITED STATES\nMarch 19, 2026 Mr. Sanders (for himself, Mr. Van Hollen , Mr. Merkley , and Mr. Welch ) introduced the following joint resolution; which was read twice and referred to the Committee on Foreign Relations\nJOINT RESOLUTION\nProviding for congressional disapproval of the proposed licensing of certain defense articles and services to Israel.\nThat the following proposed licensing of defense articles and services to Israel is prohibited:\n**(1)**\nThe licensing of defense articles and services described in the arms sales notification submitted to Congress pursuant to section 36(c)(2) of the Arms Export Control Act ( 22 U.S.C. 2776(c)(2) ) and published in the Congressional Record on March 12, 2026, including 5,000 defense articles relating to the Small Diameter Bomb Weapon Systems.",
      "versionDate": "2026-03-19",
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
        "updateDate": "2026-03-30T22:38:24Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres136is.xml"
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
      "title": "A joint resolution providing for congressional disapproval of the proposed licensing of certain defense articles and services to Israel.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:42Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval of the proposed licensing of certain defense articles and services to Israel.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T10:56:20Z"
    }
  ]
}
```
