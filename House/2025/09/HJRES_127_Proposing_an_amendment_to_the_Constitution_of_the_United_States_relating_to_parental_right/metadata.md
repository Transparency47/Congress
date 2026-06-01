# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/127?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/127
- Title: Proposing an amendment to the Constitution of the United States relating to parental rights.
- Congress: 119
- Bill type: HJRES
- Bill number: 127
- Origin chamber: House
- Introduced date: 2025-09-19
- Update date: 2026-05-15T08:07:23Z
- Update date including text: 2026-05-15T08:07:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-19: Introduced in House

## Actions

- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/127",
    "number": "127",
    "originChamber": "House",
    "policyArea": {
      "name": "Families"
    },
    "sponsors": [
      {
        "bioguideId": "M001211",
        "district": "15",
        "firstName": "Mary",
        "fullName": "Rep. Miller, Mary E. [R-IL-15]",
        "lastName": "Miller",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States relating to parental rights.",
    "type": "HJRES",
    "updateDate": "2026-05-15T08:07:23Z",
    "updateDateIncludingText": "2026-05-15T08:07:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-19",
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
      "actionDate": "2025-09-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-19",
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
          "date": "2025-09-19T13:02:10Z",
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
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "SC"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "IA"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "GA"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "NC"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "VA"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "FL"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "SC"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "FL"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "FL"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "WI"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "NC"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres127ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 127\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 19, 2025 Mrs. Miller of Illinois (for herself, Mrs. Biggs of South Carolina , Mrs. Hinson , Mr. Collins , Mr. McDowell , Mr. Cline , and Mr. Steube ) submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States relating to parental rights.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States:\n\u2014 1. The liberty of parents to direct the upbringing, education, and care of their children is a fundamental right. 2. The parental right to direct education includes the right to choose, as an alternative to public education, private, religious, or home schools, and the right to make reasonable choices within public schools for one\u2019s child. 3. Neither the United States nor any State shall infringe these rights without demonstrating that its governmental interest as applied to the person is of the highest order and not otherwise served. 4. The parental rights guaranteed by this article shall not be denied or abridged on account of disability. .",
      "versionDate": "2025-09-19",
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
        "name": "Families",
        "updateDate": "2025-09-24T15:07:21Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres127ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States relating to parental rights.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-22T17:41:03Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States relating to parental rights.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-22T15:31:11Z"
    }
  ]
}
```
