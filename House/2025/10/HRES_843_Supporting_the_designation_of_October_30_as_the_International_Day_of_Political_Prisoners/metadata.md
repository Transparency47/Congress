# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/843?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/843
- Title: Supporting the designation of October 30 as the "International Day of Political Prisoners".
- Congress: 119
- Bill type: HRES
- Bill number: 843
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2025-12-17T09:06:16Z
- Update date including text: 2025-12-17T09:06:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-10-31 - IntroReferral: Submitted in House
- 2025-10-31 - IntroReferral: Submitted in House
- Latest action: 2025-10-31: Submitted in House

## Actions

- 2025-10-31 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-10-31 - IntroReferral: Submitted in House
- 2025-10-31 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/843",
    "number": "843",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "Supporting the designation of October 30 as the \"International Day of Political Prisoners\".",
    "type": "HRES",
    "updateDate": "2025-12-17T09:06:16Z",
    "updateDateIncludingText": "2025-12-17T09:06:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-10-31T17:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "SC"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "DC"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NH"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "CO"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "IN"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "MA"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres843ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 843\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Mr. Cohen (for himself, Mr. Wilson of South Carolina , Ms. Norton , Mr. McGovern , Ms. Goodlander , Mr. Crow , and Mr. Carson ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nSupporting the designation of October 30 as the International Day of Political Prisoners .\nThat the House of Representatives\u2014\n**(1)**\ndeplores all forms of political repression and imprisonment and conveys its unwavering solidarity with all those imprisoned around the world for peacefully expressing their political or religious beliefs;\n**(2)**\nsupports efforts by the United States Government to condemn political imprisonment, hold accountable those regimes responsible for persecuting and imprisoning dissenters, raise international awareness of political prisoners, and secure their release through bilateral and multilateral negotiations with other states, and urges it to continue such efforts in the future; and\n**(3)**\nsupports the designation of an International Day of Political Prisoners in the United States.",
      "versionDate": "2025-10-31",
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
        "name": "International Affairs",
        "updateDate": "2025-11-19T17:22:37Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres843ih.xml"
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
      "title": "Supporting the designation of October 30 as the \"International Day of Political Prisoners\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-04T06:33:15Z"
    },
    {
      "title": "Supporting the designation of October 30 as the \"International Day of Political Prisoners\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-01T08:05:26Z"
    }
  ]
}
```
