# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6821?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6821
- Title: Protect Our Students Act
- Congress: 119
- Bill type: HR
- Bill number: 6821
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-02-03T09:05:22Z
- Update date including text: 2026-02-03T09:05:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6821",
    "number": "6821",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "T000468",
        "district": "1",
        "firstName": "Dina",
        "fullName": "Rep. Titus, Dina [D-NV-1]",
        "lastName": "Titus",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Protect Our Students Act",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:22Z",
    "updateDateIncludingText": "2026-02-03T09:05:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
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
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:06:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:43:27Z",
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
      "sponsorshipDate": "2026-01-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6821ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6821\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Ms. Titus introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, with respect to include reducing injuries and deaths resulting from crashes in school zones as eligible programming under State highway safety programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Our Students Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSchool zone safety issues are prevalent across our communities and warrant additional Federal funding and attention.\n**(2)**\nEach year, approximately 100 students are killed in traffic incidents walking to or from school and 25,000 students are injured.\n**(3)**\nNo student should have to fear for their lives when walking to or from school.\n#### 3. Highway safety programs\nSection 402(a)(2)(vi) of title 23, United States Code, is amended by inserting and traffic incidents in school zones after buses .\n#### 4. Regulations\nThe Secretary of Transportation shall issue such regulations as are necessary to clarify that highway safety program uses for school zone safety improvements under section 402(2)(vi) of title 23, United States Code, may include\u2014\n**(1)**\ncrossing guards;\n**(2)**\nflashing lights and beacons;\n**(3)**\nvisible signage and markings;\n**(4)**\ncrosswalks;\n**(5)**\ntraffic calming measures, including pedestrian islands;\n**(6)**\ntraffic lights;\n**(7)**\nschool zones audits and assessments;\n**(8)**\nautomated traffic enforcement; and\n**(9)**\nSafe Routes to School non-infrastructure.\n#### 5. Allocation\nSection 402(b)(1)(C) of title 23, United States Code, is amended by striking 40 percent and inserting 50 percent .",
      "versionDate": "2025-12-17",
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
        "updateDate": "2026-01-15T13:24:53Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6821ih.xml"
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
      "title": "Protect Our Students Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-14T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Our Students Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-14T03:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, with respect to include reducing injuries and deaths resulting from crashes in school zones as eligible programming under State highway safety programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-14T03:18:19Z"
    }
  ]
}
```
