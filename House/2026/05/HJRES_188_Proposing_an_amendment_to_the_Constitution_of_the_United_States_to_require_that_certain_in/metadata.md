# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/188?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/188
- Title: Proposing an amendment to the Constitution of the United States to require that certain individuals are natural born citizens.
- Congress: 119
- Bill type: HJRES
- Bill number: 188
- Origin chamber: House
- Introduced date: 2026-05-20
- Update date: 2026-05-22T02:18:38Z
- Update date including text: 2026-05-22T02:18:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-20: Introduced in House

## Actions

- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/188",
    "number": "188",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States to require that certain individuals are natural born citizens.",
    "type": "HJRES",
    "updateDate": "2026-05-22T02:18:38Z",
    "updateDateIncludingText": "2026-05-22T02:18:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-05-20T15:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres188ih.xml",
      "text": "IA\n119th CONGRESS\n2d Session\nH. J. RES. 188\nIN THE HOUSE OF REPRESENTATIVES\nMay 20, 2026 Ms. Mace submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to require that certain individuals are natural born citizens.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. No person who is not a natural born citizen may be a Representative. This section shall take effect on the 3rd day of January on the first odd number calendar year following the ratification of this article. 2. No person who is not a natural born citizen may be a Senator. This section shall take effect on the 3rd day of January on the first odd number calendar year following the ratification of this article and shall apply to a Senator beginning on the date on which the term for which they were elected ends. 3. Notwithstanding Article III of the Constitution, no person who is not a natural born citizen may be a Judge, either of the supreme or inferior courts. This section shall take effect on the date that is six months following the ratification of this article. 4. No person who is not a natural born citizen may be an Ambassador, public Minister or Consul, or any other Officer of the United States if such position requires advice and consent by the Senate. This section shall take effect on the date that is six months following the ratification of this article. .",
      "versionDate": "2026-05-20",
      "versionType": "IH"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres188ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Proposing an amendment to the Constitution of the United States to require that certain individuals are natural born citizens.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T02:18:38Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States to require that certain individuals are natural born citizens.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-21T08:07:45Z"
    }
  ]
}
```
