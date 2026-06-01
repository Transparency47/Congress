# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/754?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/754
- Title: A resolution reaffirming congressional support for the Taiwan Relations Act and longstanding bipartisan Taiwan policy.
- Congress: 119
- Bill type: SRES
- Bill number: 754
- Origin chamber: Senate
- Introduced date: 2026-05-21
- Update date: 2026-05-29T16:40:48Z
- Update date including text: 2026-05-29T16:40:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-21: Introduced in Senate
- 2026-05-21 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S2448)
- 2026-05-21 - IntroReferral: Submitted in Senate
- Latest action: 2026-05-21: Submitted in Senate

## Actions

- 2026-05-21 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S2448)
- 2026-05-21 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-21",
    "latestAction": {
      "actionDate": "2026-05-21",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/754",
    "number": "754",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "A resolution reaffirming congressional support for the Taiwan Relations Act and longstanding bipartisan Taiwan policy.",
    "type": "SRES",
    "updateDate": "2026-05-29T16:40:48Z",
    "updateDateIncludingText": "2026-05-29T16:40:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S2448)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2026-05-21",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
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
          "date": "2026-05-21T18:52:56Z",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "NC"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "ME"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres754is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 754\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2026 Mrs. Shaheen (for herself, Mr. Tillis , Ms. Collins , and Mr. Coons ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nReaffirming congressional support for the Taiwan Relations Act and longstanding bipartisan Taiwan policy.\nThat the Senate reaffirms the Taiwan Relations Act ( Public Law 96\u20138 ; 22 U.S.C. 3301 et seq. ), the Three Joint Communiqu\u00e9s, and the Six Assurances as cornerstones of United States policy regarding Taiwan and supports the longstanding bipartisan United States policy toward Taiwan, which includes support for Taiwan\u2019s self-defense and opposition to efforts to determine the future of Taiwan by other than peaceful means.",
      "versionDate": "2026-05-21",
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
        "updateDate": "2026-05-29T16:40:48Z"
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
      "date": "2026-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres754is.xml"
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
      "title": "A resolution reaffirming congressional support for the Taiwan Relations Act and longstanding bipartisan Taiwan policy.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-23T06:48:28Z"
    },
    {
      "title": "A resolution reaffirming congressional support for the Taiwan Relations Act and longstanding bipartisan Taiwan policy.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T10:56:28Z"
    }
  ]
}
```
