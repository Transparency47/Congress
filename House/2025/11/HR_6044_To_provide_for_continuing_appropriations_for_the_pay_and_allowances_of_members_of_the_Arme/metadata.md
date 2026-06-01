# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6044?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6044
- Title: Pay Our Patriots Act
- Congress: 119
- Bill type: HR
- Bill number: 6044
- Origin chamber: House
- Introduced date: 2025-11-13
- Update date: 2026-01-07T09:05:46Z
- Update date including text: 2026-01-07T09:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-13: Introduced in House
- 2025-11-13 - IntroReferral: Introduced in House
- 2025-11-13 - IntroReferral: Introduced in House
- 2025-11-13 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committees on Armed Services, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-13 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committees on Armed Services, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-13 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committees on Armed Services, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-14 - Committee: Referred to the Subcommittee on Aviation.
- 2025-11-14 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-11-13: Introduced in House

## Actions

- 2025-11-13 - IntroReferral: Introduced in House
- 2025-11-13 - IntroReferral: Introduced in House
- 2025-11-13 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committees on Armed Services, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-13 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committees on Armed Services, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-13 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committees on Armed Services, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-14 - Committee: Referred to the Subcommittee on Aviation.
- 2025-11-14 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-13",
    "latestAction": {
      "actionDate": "2025-11-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6044",
    "number": "6044",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001199",
        "district": "21",
        "firstName": "Brian",
        "fullName": "Rep. Mast, Brian J. [R-FL-21]",
        "lastName": "Mast",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Pay Our Patriots Act",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:46Z",
    "updateDateIncludingText": "2026-01-07T09:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-14",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-14",
      "committees": {
        "item": {
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-13",
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
      "text": "Referred to the Committee on Appropriations, and in addition to the Committees on Armed Services, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-13",
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
      "text": "Referred to the Committee on Appropriations, and in addition to the Committees on Armed Services, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-13",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Appropriations, and in addition to the Committees on Armed Services, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-13",
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
          "date": "2025-11-13T14:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-11-14T18:19:03Z",
                "name": "Referred to"
              }
            },
            "name": "Aviation Subcommittee",
            "systemCode": "hspw05"
          },
          {
            "activities": {
              "item": {
                "date": "2025-11-14T18:19:03Z",
                "name": "Referred to"
              }
            },
            "name": "Coast Guard and Maritime Transportation Subcommittee",
            "systemCode": "hspw07"
          }
        ]
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-13T14:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-13T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "MS"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6044ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6044\nIN THE HOUSE OF REPRESENTATIVES\nNovember 13, 2025 Mr. Mast introduced the following bill; which was referred to the Committee on Appropriations , and in addition to the Committees on Armed Services , and Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for continuing appropriations for the pay and allowances of members of the Armed Forces and certain essential employees of the Federal Aviation Administration in the event of a lapse in appropriations. and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pay Our Patriots Act .\n#### 2. Continuing appropriations for essential Armed Forces and FAA personnel\n##### (a) In general\nDuring a covered lapse in appropriations, there are appropriated, out of any money in the Treasury not otherwise appropriated, such sums as may be necessary to provide covered pay and allowances to covered employees.\n##### (b) Rate of appropriations\nAppropriations made under subsection (a) shall be available to provide covered pay and allowances at the rate in effect immediately before the beginning of the covered lapse in appropriations.\n##### (c) Duration of appropriations\nAppropriations and authority made available under this section shall continue until the earlier of\u2014\n**(1)**\nthe date on which the applicable regular appropriations Act or continuing resolution are enacted into law; or\n**(2)**\nthe last day of the fiscal year in which the covered lapse in appropriations begins.\n#### 3. Ensuring seamless payment\n##### (a) Obligation and disbursement\nThe Secretary of Defense, the Secretary of Homeland Security, and the Secretary of Transportation shall, for their respective covered employees, continue to incur obligations and disburse payments for covered pay and allowances as if appropriations had been enacted in a timely manner.\n##### (b) Availability of funds\nFunds appropriated by this Act shall be immediately available and shall not be subject to any reduction or sequestration.\n#### 4. Definitions\nIn this Act\u2014\n**(1)**\nthe term covered employee means\u2014\n**(A)**\na member of the Armed Forces (as defined in section 101 of title 10, United States Code), including reserve components, who performs active service during a covered lapse in appropriations; and\n**(B)**\na civilian employee of the Federal Aviation Administration who is determined by the Administrator of the Federal Aviation Administration to be performing duties during a covered lapse in appropriations essential to the safe operation of the national airspace system, including air traffic controllers, safety inspectors, and operational support technicians;\n**(2)**\nthe term covered pay and allowances means the pay, allowances, and benefits, including statutory bonuses and retired pay, to which a covered employee is entitled under law; and\n**(3)**\nthe term covered lapse in appropriations means any period beginning on or after the date of the enactment of this Act during which appropriations are not available for any component of the Armed Forces or the Federal Aviation Administration.",
      "versionDate": "2025-11-13",
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
        "updateDate": "2025-11-19T16:38:21Z"
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
      "date": "2025-11-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6044ih.xml"
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
      "title": "Pay Our Patriots Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-18T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pay Our Patriots Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-18T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for continuing appropriations for the pay and allowances of members of the Armed Forces and certain essential employees of the Federal Aviation Administration in the event of a lapse in appropriations. and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-18T09:18:20Z"
    }
  ]
}
```
