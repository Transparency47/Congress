# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5423?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5423
- Title: Predatory Truck Leasing Prevention Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5423
- Origin chamber: House
- Introduced date: 2025-09-17
- Update date: 2025-10-07T08:05:43Z
- Update date including text: 2025-10-07T08:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-18 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-09-17: Introduced in House

## Actions

- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-18 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5423",
    "number": "5423",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Predatory Truck Leasing Prevention Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-07T08:05:43Z",
    "updateDateIncludingText": "2025-10-07T08:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-17",
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
      "actionDate": "2025-09-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-17",
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
          "date": "2025-09-17T14:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-18T21:46:04Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5423ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5423\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 17, 2025 Ms. Brownley introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to prohibit the use of predatory commercial motor vehicle lease-purchase programs by certain motor carriers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Predatory Truck Leasing Prevention Act of 2025 .\n#### 2. Prohibition on predatory commercial motor vehicle lease-purchase agreement programs\nSection 14102 of title 49, United States Code, is amended by adding at the end the following:\n(c) Prohibition on predatory commercial motor vehicle lease-Purchase agreement program (1) In general Not later than 1 year after the date of enactment of this subsection, the Secretary shall promulgate regulations to prohibit the use of predatory commercial motor vehicle lease-purchase programs by motor carriers providing transportation subject to jurisdiction under subchapter I of chapter 135. (2) Relief provision In promulgating regulations pursuant to paragraph (1), the Secretary shall establish a process by which drivers can be granted relief from the terms of a lease-purchase agreement if\u2014 (A) the Secretary finds that the terms of the lease-purchase agreement violated regulations issued pursuant to paragraph (1); and (B) the lease-purchase agreement was entered into after the effective date of the regulations issued pursuant to paragraph (1). (3) Definitions In this subsection: (A) Predatory commercial motor vehicle lease-purchase agreement program The term predatory commercial motor vehicle lease-purchase agreement program means the framework of motor carrier-driver relationship, including the lease-purchase agreement, the contract for the driver\u2019s work for the motor carrier, and the motor carrier\u2019s practices in implementing the contracts that are not provided in the contract, including the motor carrier\u2019s recruitment practices, operational practices, and tax and finance practices, whereby the motor carrier controls the work, compensation, and debts of the driver, and the driver accrues no equity or is forced to give up equity accrued in the contracted truck. (B) Lease purchase agreement The term lease-purchase agreement means a financial contract by which a driver leases a commercial motor vehicle from a motor carrier (or a firm affiliated with such motor carrier) to haul freight while driving for the same motor carrier under a separate contract. .",
      "versionDate": "2025-09-17",
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
        "updateDate": "2025-09-29T13:36:13Z"
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
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5423ih.xml"
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
      "title": "Predatory Truck Leasing Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-27T03:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Predatory Truck Leasing Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to prohibit the use of predatory commercial motor vehicle lease-purchase programs by certain motor carriers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T03:33:19Z"
    }
  ]
}
```
