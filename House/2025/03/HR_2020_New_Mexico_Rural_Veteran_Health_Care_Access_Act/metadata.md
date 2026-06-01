# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2020?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2020
- Title: New Mexico Rural Veteran Health Care Access Act
- Congress: 119
- Bill type: HR
- Bill number: 2020
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2025-05-08T15:20:28Z
- Update date including text: 2025-05-08T15:20:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-01 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-01 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2020",
    "number": "2020",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000136",
        "district": "2",
        "firstName": "Gabe",
        "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
        "lastName": "Vasquez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "New Mexico Rural Veteran Health Care Access Act",
    "type": "HR",
    "updateDate": "2025-05-08T15:20:28Z",
    "updateDateIncludingText": "2025-05-08T15:20:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-01T18:07:16Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2020ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2020\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mr. Vasquez (for himself and Mr. Murphy ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to include two counties in New Mexico in a certain Veterans Integrated Service Network.\n#### 1. Short title\nThis Act may be cited as the New Mexico Rural Veteran Health Care Access Act .\n#### 2. Inclusion of two counties in New Mexico in a certain Veterans Integrated Service Network\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall redraw the boundaries of the Veterans Integrated Service Networks to include Otero County and Eddy County, New Mexico, in Veterans Integrated Service Network 17.",
      "versionDate": "2025-03-10",
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
        "updateDate": "2025-05-08T15:20:28Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2020ih.xml"
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
      "title": "New Mexico Rural Veteran Health Care Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "New Mexico Rural Veteran Health Care Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to include two counties in New Mexico in a certain Veterans Integrated Service Network.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:21Z"
    }
  ]
}
```
