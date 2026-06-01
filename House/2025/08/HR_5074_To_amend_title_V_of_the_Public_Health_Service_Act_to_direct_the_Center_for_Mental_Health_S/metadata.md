# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5074?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5074
- Title: Protecting Young Minds Online Act
- Congress: 119
- Bill type: HR
- Bill number: 5074
- Origin chamber: House
- Introduced date: 2025-08-29
- Update date: 2025-12-19T09:07:14Z
- Update date including text: 2025-12-19T09:07:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-29: Introduced in House
- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-08-29: Introduced in House

## Actions

- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-29",
    "latestAction": {
      "actionDate": "2025-08-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5074",
    "number": "5074",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001213",
        "district": "1",
        "firstName": "Bryan",
        "fullName": "Rep. Steil, Bryan [R-WI-1]",
        "lastName": "Steil",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Protecting Young Minds Online Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:14Z",
    "updateDateIncludingText": "2025-12-19T09:07:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-29",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-29",
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
          "date": "2025-08-29T17:31:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "VT"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "NJ"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "VA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5074ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5074\nIN THE HOUSE OF REPRESENTATIVES\nAugust 29, 2025 Mr. Steil (for himself and Ms. Balint ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title V of the Public Health Service Act to direct the Center for Mental Health Services to develop and disseminate a strategy to address the effects of new technologies on children\u2019s mental health.\n#### 1. Short title\nThis Act may be cited as the Protecting Young Minds Online Act .\n#### 2. Center for Mental Health Services strategy to address effects of new technologies on children\u2019s mental health\nSection 520(b) of the Public Health Service Act ( 42 U.S.C. 290bb\u201331(b) ) is amended\u2014\n**(1)**\nin paragraph (16), by striking and at the end;\n**(2)**\nin paragraph (17), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(18) develop and implement a strategy to help local communities address the effects of new technologies, such as social media, on children\u2019s mental health. .",
      "versionDate": "2025-08-29",
      "versionType": "Introduced in House"
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
        "name": "Health",
        "updateDate": "2025-09-22T15:27:47Z"
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
      "date": "2025-08-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5074ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Protecting Young Minds Online Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T08:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Young Minds Online Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-03T08:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title V of the Public Health Service Act to direct the Center for Mental Health Services to develop and disseminate a strategy to address the effects of new technologies on children's mental health.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-03T08:48:20Z"
    }
  ]
}
```
