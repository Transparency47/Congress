# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/337?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/337
- Title: A resolution recognizing the 250th anniversary of the postal service of the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 337
- Origin chamber: Senate
- Introduced date: 2025-07-24
- Update date: 2025-11-14T16:19:27Z
- Update date including text: 2025-11-14T16:19:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-24: Introduced in Senate
- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-10-09 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Voice Vote.
- 2025-10-09 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Voice Vote.
- 2025-10-09 - Discharge: Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.
- 2025-10-09 - Committee: Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.
- Latest action: 2025-07-24: Introduced in Senate

## Actions

- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-10-09 - Floor: Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Voice Vote.
- 2025-10-09 - Floor: Resolution agreed to in Senate without amendment and with a preamble by Voice Vote.
- 2025-10-09 - Discharge: Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.
- 2025-10-09 - Committee: Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-24",
    "latestAction": {
      "actionDate": "2025-07-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/337",
    "number": "337",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000595",
        "district": "",
        "firstName": "Gary",
        "fullName": "Sen. Peters, Gary C. [D-MI]",
        "lastName": "Peters",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "A resolution recognizing the 250th anniversary of the postal service of the United States.",
    "type": "SRES",
    "updateDate": "2025-11-14T16:19:27Z",
    "updateDateIncludingText": "2025-11-14T16:19:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-09",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Resolution agreed to in Senate without amendment and with a preamble by Voice Vote.",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-10-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Resolution agreed to in Senate without amendment and with a preamble by Voice Vote.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-09",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-10-09",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Homeland Security and Governmental Affairs discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-24",
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
            "date": "2025-10-10T01:40:57Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-07-24T18:26:28Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "AK"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "CT"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "AK"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "NH"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "NC"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "MI"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "ID"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "ME"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "NH"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "MT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "ID"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "MA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "ND"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres337is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 337\nIN THE SENATE OF THE UNITED STATES\nJuly 24, 2025 Mr. Peters (for himself, Mr. Sullivan , Mr. Blumenthal , Ms. Murkowski , Ms. Hassan , Mr. Tillis , Ms. Slotkin , Mr. Crapo , Ms. Collins , and Mrs. Shaheen ) submitted the following resolution; which was referred to the Committee on Homeland Security and Governmental Affairs\nRESOLUTION\nRecognizing the 250th anniversary of the postal service of the United States.\nThat the Senate\u2014\n**(1)**\nrecognizes the historic significance of the 250th anniversary of the founding of the postal service;\n**(2)**\nhonors the men and women who served and continue to serve as employees of the postal service;\n**(3)**\ncelebrates 250 years of service by the postal service to the people of the United States and looks forward to another 250 years of service; and\n**(4)**\ninvites the people of the United States to join in the celebration of the 250th anniversary of the postal service by writing a letter, buying stamps, or recognizing a postal employee.",
      "versionDate": "2025-07-24",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres337ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 337\nIN THE SENATE OF THE UNITED STATES\nJuly 24, 2025 Mr. Peters (for himself, Mr. Sullivan , Mr. Blumenthal , Ms. Murkowski , Ms. Hassan , Mr. Tillis , Ms. Slotkin , Mr. Crapo , Ms. Collins , Mrs. Shaheen , Mr. Daines , Mr. Risch , Mr. Markey , Mr. Cramer , and Mr. Whitehouse ) submitted the following resolution; which was referred to the Committee on Homeland Security and Governmental Affairs\nOctober 9, 2025 Committee discharged; considered and agreed to\nRESOLUTION\nRecognizing the 250th anniversary of the postal service of the United States.\nThat the Senate\u2014\n**(1)**\nrecognizes the historic significance of the 250th anniversary of the founding of the postal service;\n**(2)**\nhonors the men and women who served and continue to serve as employees of the postal service;\n**(3)**\ncelebrates 250 years of service by the postal service to the people of the United States and looks forward to another 250 years of service; and\n**(4)**\ninvites the people of the United States to join in the celebration of the 250th anniversary of the postal service by writing a letter, buying stamps, or recognizing a postal employee.",
      "versionDate": "2025-10-09",
      "versionType": "ATS"
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
            "name": "Commemorative events and holidays",
            "updateDate": "2025-11-14T16:19:08Z"
          },
          {
            "name": "Congressional tributes",
            "updateDate": "2025-11-14T16:19:27Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-11-14T16:19:17Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-11-14T16:19:24Z"
          },
          {
            "name": "U.S. Postal Service",
            "updateDate": "2025-11-14T16:19:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-17T21:59:02Z"
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
      "date": "2025-07-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres337is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-10-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres337ats.xml"
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
      "title": "A resolution recognizing the 250th anniversary of the postal service of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-26T03:18:23Z"
    },
    {
      "title": "A resolution recognizing the 250th anniversary of the postal service of the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T10:56:18Z"
    }
  ]
}
```
