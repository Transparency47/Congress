# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7319?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7319
- Title: VA Bonus and Relocation Recovery Act
- Congress: 119
- Bill type: HR
- Bill number: 7319
- Origin chamber: House
- Introduced date: 2026-02-02
- Update date: 2026-03-26T08:06:39Z
- Update date including text: 2026-03-26T08:06:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-02: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-02 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2026-03-25 - Committee: Subcommittee Hearings Held
- Latest action: 2026-02-02: Introduced in House

## Actions

- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-02 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2026-03-25 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-02",
    "latestAction": {
      "actionDate": "2026-02-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7319",
    "number": "7319",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "VA Bonus and Relocation Recovery Act",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:39Z",
    "updateDateIncludingText": "2026-03-26T08:06:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
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
      "actionDate": "2026-03-02",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight and Investigations.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-02",
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
      "actionDate": "2026-02-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-02",
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
          "date": "2026-02-02T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-03-25T14:37:21Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-02T15:19:57Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
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
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7319ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7319\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 2, 2026 Mr. Self (for himself and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to recoup amounts of awards, bonuses, and relocation expenses paid to former employees of the Department of Veterans Affairs under certain conditions.\n#### 1. Short title\nThis Act may be cited as the VA Bonus and Relocation Recovery Act .\n#### 2. Authority to recoup awards, bonuses, and relocation expenses paid to former Department of Veterans Affairs employees under certain conditions\n##### (a) Awards and bonuses\nSection 721 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by inserting , or a former employee of the Department, after an employee of the Department ; and\n**(2)**\nby adding at the end the following new subsection:\n(c) Authority To collect from former employees (1) If the Director upholds an order of the Secretary under subsection (a) with respect to an individual who is a former employee of the Department, and such individual does not repay the amount of the award or bonus subject to the order within 180 days after the date of the final decision of the Director under subsection (b) with respect to the order, the Secretary may recover such amount from the former employee in the same manner as any other debt due to the United States. (2) Nothing in this subsection may be construed to permit the Secretary to waive the recovery of such amount under section 5302 of this title. .\n##### (b) Relocation expenses\nSection 723 of such title is amended\u2014\n**(1)**\nin subsection (a), by inserting , or a former employee of the Department, after an employee of the Department ; and\n**(2)**\nby adding at the end the following new subsection:\n(c) Authority To collect from former employees (1) If the Director upholds an order of the Secretary under subsection (a) with respect to an individual who is a former employee of the Department, and such individual does not repay the amount of the award or bonus subject to the order within 180 days after the date of the final decision of the Director under subsection (b) with respect to the order, the Secretary may recover such amount from the former employee in the same manner as any other debt due to the United States. (2) Nothing in this subsection may be construed to permit the Secretary to waive the recovery of such amount under section 5302 of this title. .",
      "versionDate": "2026-02-02",
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
        "updateDate": "2026-02-23T17:20:38Z"
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
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7319ih.xml"
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
      "title": "VA Bonus and Relocation Recovery Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T07:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA Bonus and Relocation Recovery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T07:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to recoup amounts of awards, bonuses, and relocation expenses paid to former employees of the Department of Veterans Affairs under certain conditions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T07:48:25Z"
    }
  ]
}
```
