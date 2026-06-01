# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4293?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4293
- Title: To amend the Sikes Act to increase flexibility with respect to cooperative and interagency agreements for land management off of installations.
- Congress: 119
- Bill type: HR
- Bill number: 4293
- Origin chamber: House
- Introduced date: 2025-07-07
- Update date: 2025-09-30T18:02:02Z
- Update date including text: 2025-09-30T18:02:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-07: Introduced in House
- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-07 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-16 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-07-22 - Committee: Subcommittee Hearings Held
- Latest action: 2025-07-07: Introduced in House

## Actions

- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Introduced in House
- 2025-07-07 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-07 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-16 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2025-07-22 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-07",
    "latestAction": {
      "actionDate": "2025-07-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4293",
    "number": "4293",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001133",
        "district": "6",
        "firstName": "Juan",
        "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
        "lastName": "Ciscomani",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "To amend the Sikes Act to increase flexibility with respect to cooperative and interagency agreements for land management off of installations.",
    "type": "HR",
    "updateDate": "2025-09-30T18:02:02Z",
    "updateDateIncludingText": "2025-09-30T18:02:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-22",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-07",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-07",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-07",
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
          "date": "2025-07-07T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-07-22T18:30:14Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-07-16T15:10:57Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-07T14:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4293ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4293\nIN THE HOUSE OF REPRESENTATIVES\nJuly 7, 2025 Mr. Ciscomani introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Sikes Act to increase flexibility with respect to cooperative and interagency agreements for land management off of installations.\n#### 1. Cooperative and interagency agreements for land management off of installations\nSection 103A(a)(2) of the Sikes Act ( 16 U.S.C. 670c\u20131(a)(2) ) is amended by inserting or the operations of the military installation or State-owned National Guard installation after current or anticipated military activities .",
      "versionDate": "2025-07-07",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-09-30T18:01:57Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-09-30T18:02:02Z"
          },
          {
            "name": "Military facilities and property",
            "updateDate": "2025-09-30T18:01:47Z"
          },
          {
            "name": "National Guard and reserves",
            "updateDate": "2025-09-30T18:01:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-19T17:06:19Z"
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
      "date": "2025-07-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4293ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Sikes Act to increase flexibility with respect to cooperative and interagency agreements for land management off of installations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-22T04:48:27Z"
    },
    {
      "title": "To amend the Sikes Act to increase flexibility with respect to cooperative and interagency agreements for land management off of installations.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:09Z"
    }
  ]
}
```
