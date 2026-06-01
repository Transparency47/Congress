# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/296?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/296
- Title: A resolution condemning antisemitism and recent antisemitic attacks in the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 296
- Origin chamber: Senate
- Introduced date: 2025-06-23
- Update date: 2025-07-22T19:37:12Z
- Update date including text: 2025-07-22T19:37:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-23: Introduced in Senate
- 2025-06-23 - IntroReferral: Introduced in Senate
- 2025-06-23 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S3494-3495)
- 2025-06-24 - Floor: Star Print ordered on the resolution.
- Latest action: 2025-06-23: Introduced in Senate

## Actions

- 2025-06-23 - IntroReferral: Introduced in Senate
- 2025-06-23 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S3494-3495)
- 2025-06-24 - Floor: Star Print ordered on the resolution.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-23",
    "latestAction": {
      "actionDate": "2025-06-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/296",
    "number": "296",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "A resolution condemning antisemitism and recent antisemitic attacks in the United States.",
    "type": "SRES",
    "updateDate": "2025-07-22T19:37:12Z",
    "updateDateIncludingText": "2025-07-22T19:37:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Star Print ordered on the resolution.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S3494-3495)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-23",
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
          "date": "2025-06-23T22:00:28Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "NV"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CO"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CO"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "PA"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "PA"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "KS"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
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
      "sponsorshipDate": "2025-06-23",
      "state": "NY"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-07-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres296is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 296\nIN THE SENATE OF THE UNITED STATES\nJune 23, 2025 Mr. Lankford (for himself, Ms. Rosen , Mr. Bennet , Mr. Hickenlooper , Mr. McCormick , Mr. Fetterman , Mr. Moran , Mr. Thune , and Mr. Schumer ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCondemning antisemitism and recent antisemitic attacks in the United States.\nThat the Senate\u2014\n**(1)**\nmourns the loss of Sarah Milgrim and Yaron Lischinsky;\n**(2)**\nunequivocally condemns antisemitism in all its forms, including the antisemitic attack on and murder of Sarah Milgrim and Yaron Lischinsky, and the antisemitic attack in Boulder, Colorado;\n**(3)**\nstands with the Jewish communities in the United States and throughout the world and all those effected by the antisemitic attacks that occurred in Washington, DC, on May 21, 2025, and in Boulder, Colorado, on June 1, 2025;\n**(4)**\nwishes for the swift recovery of all victims of the attack in Boulder, Colorado;\n**(5)**\nencourages all of society to denounce and combat all manifestations of antisemitism and ensure that antisemitism is not normalized;\n**(6)**\nrecognizes the importance of resources and action in the aftermath of attacks, including the distribution of resources from the Nonprofit Security Grant Program of the Federal Emergency Management Agency; and\n**(7)**\nreaffirms the commitment of the people of the United States to combat hate, bigotry, antisemitism, and violence against Jewish Americans.",
      "versionDate": "2025-06-12",
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
            "name": "Colorado",
            "updateDate": "2025-07-22T19:37:04Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-07-22T19:36:59Z"
          },
          {
            "name": "District of Columbia",
            "updateDate": "2025-07-22T19:37:08Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-07-22T19:37:12Z"
          },
          {
            "name": "Religion",
            "updateDate": "2025-07-22T19:36:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-21T15:14:22Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres296is.xml"
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
      "title": "A resolution condemning antisemitism and recent antisemitic attacks in the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T06:48:20Z"
    },
    {
      "title": "A resolution condemning antisemitism and recent antisemitic attacks in the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-24T10:56:20Z"
    }
  ]
}
```
