# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4243?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4243
- Title: Homecare for Seniors Act
- Congress: 119
- Bill type: HR
- Bill number: 4243
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2026-02-04T04:26:30Z
- Update date including text: 2026-02-04T04:26:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-06-27: Introduced in House

## Actions

- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4243",
    "number": "4243",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001172",
        "district": "3",
        "firstName": "Adrian",
        "fullName": "Rep. Smith, Adrian [R-NE-3]",
        "lastName": "Smith",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Homecare for Seniors Act",
    "type": "HR",
    "updateDate": "2026-02-04T04:26:30Z",
    "updateDateIncludingText": "2026-02-04T04:26:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-27",
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
          "date": "2025-06-27T13:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
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
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4243ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4243\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Mr. Smith of Nebraska (for himself and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow qualified distributions from health savings accounts for certain home care expenses.\n#### 1. Short title\nThis Act may be cited as the Homecare for Seniors Act .\n#### 2. Certain home care expenses treated as qualified distributions from health savings accounts\n##### (a) In general\nSection 223(d)(2) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking medical care (as defined in section 213(d)) in subparagraph (A) and inserting specified medical care , and\n**(2)**\nby adding at the end the following new subparagraph:\n(E) Specified medical care For purposes of this paragraph\u2014 (i) In general The term specified medical care means medical care (as defined in section 213(d)) and qualified home care. (ii) Qualified home care The term qualified home care means a contract to provide 3 or more of the following services in the residence of the service recipient: (I) Assistance with eating. (II) Assistance with toileting. (III) Assistance with transferring. (IV) Assistance with bathing. (V) Assistance with dressing. (VI) Assistance with continence. (VII) Medication adherence. Such term shall not include any contract unless the services provided pursuant to such contract are provided by a service provider which is licensed by the State to provide such services or such services are otherwise provided in a manner that is consistent with State requirements. (iii) Related parties The term qualified home care shall not include any contract which is, directly or indirectly, between a service provider and a service recipient who are related within the meaning of section 267(b) or 707(b). .\n##### (b) Effective date\nThe amendments made by this section shall apply to amounts paid with respect to taxable years beginning after the date of the enactment of this Act.\n##### (c) Promotion of public awareness of in-Home service expenses eligible for tax-Free distribution from health savings accounts\nThe Secretary of Health and Human Services, in consultation with the Secretary of the Treasury, shall carry out a campaign to increase public awareness of the in-home service expenses that are eligible for tax-free distribution from health savings accounts.",
      "versionDate": "2025-06-27",
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
        "name": "Taxation",
        "updateDate": "2025-07-17T19:13:48Z"
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
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4243ih.xml"
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
      "title": "Homecare for Seniors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-16T07:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Homecare for Seniors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T07:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow qualified distributions from health savings accounts for certain home care expenses.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T07:18:31Z"
    }
  ]
}
```
