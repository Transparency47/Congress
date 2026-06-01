# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7605?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7605
- Title: African Development Foundation Termination Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7605
- Origin chamber: House
- Introduced date: 2026-02-20
- Update date: 2026-04-15T16:20:22Z
- Update date including text: 2026-04-15T16:20:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-20: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 26 - 20.
- Latest action: 2026-02-20: Introduced in House

## Actions

- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 26 - 20.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-20",
    "latestAction": {
      "actionDate": "2026-02-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7605",
    "number": "7605",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001309",
        "district": "2",
        "firstName": "Tim",
        "fullName": "Rep. Burchett, Tim [R-TN-2]",
        "lastName": "Burchett",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "African Development Foundation Termination Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-15T16:20:22Z",
    "updateDateIncludingText": "2026-04-15T16:20:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 26 - 20.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-20",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-20",
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
        "item": [
          {
            "date": "2026-03-26T16:34:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-20T16:33:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7605ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7605\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 20, 2026 Mr. Burchett introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo abolish the United States African Development Foundation.\n#### 1. Short title\nThis Act may be cited as the African Development Foundation Termination Act of 2026 .\n#### 2. Abolishment of the United States African Development Foundation\nThe United States African Development Foundation (in this Act referred to as the Foundation ) is hereby abolished effective on the date that is 120 days after the date of the enactment of this Act.\n#### 3. Wind-down and transfer of assets\n##### (a) Conclusion period\nDuring the 120-day period beginning on the date of the enactment of this Act, the President shall take such actions as may be necessary to conclude the outstanding affairs of the Foundation.\n##### (b) Transfer of remaining funds and property\n**(1) Unexpended balances**\nAny unexpended balances of appropriations, allocations, or other funds available to the Foundation shall be deposited into the general fund of the Department of the Treasury.\n**(2) Assets including records**\nAll assets, liabilities, contracts, property, and records of the Foundation shall be transferred to the Department of State, as determined by the Director of the Office of Management and Budget, solely for the purpose of liquidation or oversight of existing multi-year grants until their expiration.\n##### (c) No new awards\nNo new grants, loans, loan guarantees, or project agreements may be entered into by the Foundation on or after the date of the enactment of this Act.\n#### 4. Repeal of the African Development Foundation Act\n##### (a) Repeal\nThe African Development Foundation Act (title V of Public Law 96\u2013533 ; 22 U.S.C. 290h et seq. ) is repealed.\n##### (b) Conforming amendments\nThe Secretary of State shall submit to Congress a report containing proposed legislation making such technical and conforming amendments to the United States Code as are necessary to reflect the repeal made by subsection (a).\n#### 5. Personnel\nThe Foundation shall provide appropriate notice to employees of the Foundation in accordance with applicable Federal law regarding reductions in force, including the principles set forth in sections 3501 through 3504 of title 5, United States Code, and regulations prescribed thereunder.",
      "versionDate": "2026-02-20",
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
        "name": "International Affairs",
        "updateDate": "2026-02-25T15:50:30Z"
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
      "date": "2026-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7605ih.xml"
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
      "title": "African Development Foundation Termination Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T05:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "African Development Foundation Termination Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To abolish the United States African Development Foundation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T05:48:34Z"
    }
  ]
}
```
