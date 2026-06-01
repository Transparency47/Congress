# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4039?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4039
- Title: CNMI Ferry Act
- Congress: 119
- Bill type: HR
- Bill number: 4039
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2025-07-24T21:37:07Z
- Update date including text: 2025-07-24T21:37:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-18 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-18 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4039",
    "number": "4039",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "K000404",
        "district": "",
        "firstName": "Kimberlyn",
        "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
        "lastName": "King-Hinds",
        "party": "R",
        "state": "MP"
      }
    ],
    "title": "CNMI Ferry Act",
    "type": "HR",
    "updateDate": "2025-07-24T21:37:07Z",
    "updateDateIncludingText": "2025-07-24T21:37:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
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
      "actionDate": "2025-06-17",
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
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-18T20:54:09Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4039ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4039\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Ms. King-Hinds introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Infrastructure Investment and Jobs Act to allow the Commonwealth of the Northern Mariana Islands to be eligible to receive certain funding for use providing basic essential ferry service in rural areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Connecting the Northern Mariana Islands through Ferry Services Act or the CNMI Ferry Act .\n#### 2. Ferry service funding for the Commonwealth of the Northern Mariana Islands\nSection 71103 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 147 note) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nby striking means a ferry service and all that follows through the period and inserting means\u2014 ; and\n**(ii)**\nby adding at the end the following:\n(A) a ferry service that\u2014 (i) operated a regular schedule at any time during the 5-year period ending on March 1, 2020; and (ii) served not less than 2 rural areas located more than 50 sailing miles apart; and (B) a ferry service operating, or being planned or established with the intent that the ferry service operate, a regular schedule in the Commonwealth of the Northern Mariana Islands. ;\n**(B)**\nin paragraph (3) to read as follows:\n(3) Rural area (A) In general The term rural area has the meaning given the term in section 5302 of title 49, United States Code. (B) Commonwealth of the Northern Mariana Islands For purposes of the program established under subsection (b), the Commonwealth of the Northern Mariana Islands, and any area therein, shall be deemed to be a rural area. ; and\n**(C)**\nby adding at the end the following:\n(5) State The term State means any State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Commonwealth of the Northern Mariana Islands, the United States Virgin Islands, Guam, American Samoa, and any other territory or possession of the United States. ; and\n**(2)**\nin subsection (c) by striking including requirements for the provision of funds to States. and inserting\nincluding\u2014 (1) requirements for the provision of funds to States; and (2) requirements for the provision of funds to the Commonwealth of the Northern Mariana Islands for the establishment and operation of an eligible service. .",
      "versionDate": "2025-06-17",
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
        "updateDate": "2025-07-24T21:37:07Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4039ih.xml"
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
      "title": "CNMI Ferry Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-26T12:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CNMI Ferry Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Connecting the Northern Mariana Islands through Ferry Services Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Infrastructure Investment and Jobs Act to allow the Commonwealth of the Northern Mariana Islands to be eligible to receive certain funding for use providing basic essential ferry service in rural areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T12:18:19Z"
    }
  ]
}
```
