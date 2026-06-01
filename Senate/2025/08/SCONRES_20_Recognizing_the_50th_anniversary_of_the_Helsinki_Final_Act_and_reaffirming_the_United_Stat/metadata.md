# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sconres/20?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/20
- Title: A concurrent resolution recognizing the 50th anniversary of the Helsinki Final Act and reaffirming the United States' commitment to its principles and values.
- Congress: 119
- Bill type: SCONRES
- Bill number: 20
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2025-09-18T20:55:50Z
- Update date including text: 2025-09-18T20:55:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S5213-5214)
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S5213-5214)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/20",
    "number": "20",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "W000437",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Wicker, Roger F. [R-MS]",
        "lastName": "Wicker",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "A concurrent resolution recognizing the 50th anniversary of the Helsinki Final Act and reaffirming the United States' commitment to its principles and values.",
    "type": "SCONRES",
    "updateDate": "2025-09-18T20:55:50Z",
    "updateDateIncludingText": "2025-09-18T20:55:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S5213-5214)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T17:50:06Z",
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
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "RI"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "NC"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MN"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "AR"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "PA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "AL"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres20is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. CON. RES. 20\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Mr. Wicker (for himself, Mr. Whitehouse , Mr. Tillis , Ms. Smith , Mr. Boozman , Mr. Fetterman , Mrs. Britt , and Mrs. Shaheen ) submitted the following concurrent resolution; which was referred to the Committee on Foreign Relations\nCONCURRENT RESOLUTION\nRecognizing the 50th anniversary of the Helsinki Final Act and reaffirming the United States\u2019 commitment to its principles and values.\nThat Congress\u2014\n**(1)**\ncommemorates the 50th anniversary of the signing of the Final Act of the Conference on Security and Cooperation in Europe and recognizes the importance of the Helsinki Principles and the OSCE;\n**(2)**\nreasserts the commitment of the United States to the full implementation of the Helsinki Final Act and to continued participation in the OSCE;\n**(3)**\nurges all participating states to abide by their respective obligations under the Helsinki Final Act, including respecting human rights and fundamental freedoms, which are vital to the functioning of democracy;\n**(4)**\ncalls on public officials, educators, librarians, and the people of the United States to join Congress in observance of this anniversary with appropriate programs, ceremonies, and activities; and\n**(5)**\nconveys to all signatory states of the Helsinki Final Act that respect for human rights and fundamental freedoms, democratic principles, economic liberty, peaceful resolution of conflicts among participating states, respect for the sovereignty and territorial integrity of participating states, and the implementation of related commitments continue to be vital elements in promoting security, prosperity, and peace throughout the region covered by the OSCE.",
      "versionDate": "2025-08-01",
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
        "updateDate": "2025-09-18T20:55:50Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres20is.xml"
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
      "title": "A concurrent resolution recognizing the 50th anniversary of the Helsinki Final Act and reaffirming the United States' commitment to its principles and values.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:30Z"
    },
    {
      "title": "A concurrent resolution recognizing the 50th anniversary of the Helsinki Final Act and reaffirming the United States' commitment to its principles and values.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T10:56:20Z"
    }
  ]
}
```
