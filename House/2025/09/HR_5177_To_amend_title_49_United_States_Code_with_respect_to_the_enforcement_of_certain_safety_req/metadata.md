# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5177?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5177
- Title: To amend title 49, United States Code, with respect to the enforcement of certain safety requirements relating to commercial motor vehicle drivers, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 5177
- Origin chamber: House
- Introduced date: 2025-09-08
- Update date: 2025-10-07T08:05:34Z
- Update date including text: 2025-10-07T08:05:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-08: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-09 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-09-08: Introduced in House

## Actions

- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-09 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-08",
    "latestAction": {
      "actionDate": "2025-09-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5177",
    "number": "5177",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "D000032",
        "district": "19",
        "firstName": "Byron",
        "fullName": "Rep. Donalds, Byron [R-FL-19]",
        "lastName": "Donalds",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "To amend title 49, United States Code, with respect to the enforcement of certain safety requirements relating to commercial motor vehicle drivers, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-10-07T08:05:34Z",
    "updateDateIncludingText": "2025-10-07T08:05:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-09",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-08",
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
          "date": "2025-09-08T16:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-09T21:39:42Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5177ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5177\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 8, 2025 Mr. Donalds introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, with respect to the enforcement of certain safety requirements relating to commercial motor vehicle drivers, and for other purposes.\n#### 1. Weigh station enforcement of certain safety requirements\n##### (a) In general\nSubchapter III of chapter 311 of title 49, United States Code, is amended by adding at the end the following:\n31152. Weigh station enforcement of certain safety requirements Notwithstanding any other provision of law, the Secretary shall ensure that each State enforces sections 3 and 4 of Executive Order 14286 (relating to Enforcing Commonsense Rules of the Road for America's Truck Drivers (signed on April 28, 2025)) on each commercial motor vehicle that enters a weigh station. .\n##### (b) Clerical amendment\nThe analysis for chapter 311 of title 49, United States Code, is amended by inserting after the item relating to section 31151 the following:\n31152. Weigh station enforcement of certain safety requirements. .",
      "versionDate": "2025-09-08",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-23T17:36:24Z"
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
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5177ih.xml"
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
      "title": "To amend title 49, United States Code, with respect to the enforcement of certain safety requirements relating to commercial motor vehicle drivers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T04:48:22Z"
    },
    {
      "title": "To amend title 49, United States Code, with respect to the enforcement of certain safety requirements relating to commercial motor vehicle drivers, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T08:05:27Z"
    }
  ]
}
```
