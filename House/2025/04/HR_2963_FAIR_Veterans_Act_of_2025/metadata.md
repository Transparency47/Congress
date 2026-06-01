# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2963?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2963
- Title: FAIR Veterans Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2963
- Origin chamber: House
- Introduced date: 2025-04-17
- Update date: 2025-12-12T09:07:52Z
- Update date including text: 2025-12-12T09:07:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-17: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Sponsor introductory remarks on measure. (CR H1433)
- 2025-04-17 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-12 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Sponsor introductory remarks on measure. (CR H1433)
- 2025-04-17 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-12 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-17",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2963",
    "number": "2963",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000472",
        "district": "39",
        "firstName": "Mark",
        "fullName": "Rep. Takano, Mark [D-CA-39]",
        "lastName": "Takano",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "FAIR Veterans Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:52Z",
    "updateDateIncludingText": "2025-12-12T09:07:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-12",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-17",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H1433)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
          "date": "2025-04-17T13:33:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-12T15:36:47Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2963ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2963\nIN THE HOUSE OF REPRESENTATIVES\nApril 17, 2025 Mr. Takano introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo express the sense of Congress regarding the exercise by the Department of Veterans Affairs of the authority under the Veterans Affairs Servicing Purchasing program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Foreclosure Assistance Immediately Reinstated for Veterans Act of 2025 or the FAIR Veterans Act of 2025 .\n#### 2. Sense of Congress regarding Department of Veterans Affairs exercise of authority under Veterans Affairs Servicing Purchasing program\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe foreclosure on a home purchased by a veteran with a loan guaranteed by the Department of Veterans Affairs should be the last resort; and\n**(2)**\nthe Department should use the authority under section 3732(a)(2) of title 38, United States Code, and other authorities under the laws administered by the Secretary to help as many veterans as possible keep their homes.\n##### (b) Clarification regarding VASP program\nSection 3732(a)(2)(A) of title 38, United States Code, is amended by striking Before and inserting The Secretary shall carry out a program under which the Secretary may pay the holder of the obligation the unpaid balance of the obligation plus accrued interest and receive an assignment of the loan and security. To participate in the program, before .",
      "versionDate": "2025-04-17",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-28T20:43:49Z"
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
      "date": "2025-04-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2963ih.xml"
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
      "title": "FAIR Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T03:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAIR Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Foreclosure Assistance Immediately Reinstated for Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To express the sense of Congress regarding the exercise by the Department of Veterans Affairs of the authority under the Veterans Affairs Servicing Purchasing program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T03:03:21Z"
    }
  ]
}
```
