# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/99?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hjres/99
- Title: Proposing an amendment to the Constitution of the United States to provide that new States may be admitted to the United States upon a concurrence of two thirds of each house of Congress.
- Congress: 119
- Bill type: HJRES
- Bill number: 99
- Origin chamber: House
- Introduced date: 2025-06-06
- Update date: 2025-07-18T13:09:03Z
- Update date including text: 2025-07-18T13:09:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-06: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-06: Introduced in House

## Actions

- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-06",
    "latestAction": {
      "actionDate": "2025-06-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hjres/99",
    "number": "99",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001177",
        "district": "5",
        "firstName": "Tom",
        "fullName": "Rep. McClintock, Tom [R-CA-5]",
        "lastName": "McClintock",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States to provide that new States may be admitted to the United States upon a concurrence of two thirds of each house of Congress.",
    "type": "HJRES",
    "updateDate": "2025-07-18T13:09:03Z",
    "updateDateIncludingText": "2025-07-18T13:09:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-06",
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
      "actionDate": "2025-06-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-06",
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
          "date": "2025-06-06T13:00:20Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "AZ"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "PA"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres99ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 99\nIN THE HOUSE OF REPRESENTATIVES\nJune 6, 2025 Mr. McClintock (for himself, Mr. Biggs of Arizona , and Mr. Perry ) submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to provide that new States may be admitted to the United States upon a concurrence of two thirds of each house of Congress.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States:\n\u2014 New States may be admitted by the Congress into this Union upon the Concurrence of two thirds of each House. .",
      "versionDate": "2025-06-06",
      "versionType": "IH"
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-07-18T13:09:03Z"
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
      "date": "2025-06-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres99ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States to provide that new States may be admitted to the United States upon a concurrence of two thirds of each house of Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-07T08:18:25Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States to provide that new States may be admitted to the United States upon a concurrence of two thirds of each house of Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-07T08:06:12Z"
    }
  ]
}
```
