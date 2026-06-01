# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4042?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4042
- Title: STATES Act
- Congress: 119
- Bill type: HR
- Bill number: 4042
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2025-07-17T15:29:20Z
- Update date including text: 2025-07-17T15:29:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Armed Services.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4042",
    "number": "4042",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001218",
        "district": "7",
        "firstName": "Richard",
        "fullName": "Rep. McCormick, Richard [R-GA-7]",
        "lastName": "McCormick",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "STATES Act",
    "type": "HR",
    "updateDate": "2025-07-17T15:29:20Z",
    "updateDateIncludingText": "2025-07-17T15:29:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "text": "Referred to the House Committee on Armed Services.",
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
          "date": "2025-06-17T15:03:50Z",
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
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "WI"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "AZ"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4042ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4042\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Mr. McCormick (for himself, Mr. Wied , Mr. Hamadeh of Arizona , and Mr. Harrigan ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo require a State to reimburse the Federal Government for the deployment of the National Guard to such State.\n#### 1. Short title\nThis Act may be cited as the States Taking Accountability for Troops Engaged in Safety Act or the STATES Act .\n#### 2. National guard in Federal service\nSection 12406 of title 10, United States Code, is amended to read as follows:\n12406. National guard in Federal service: call (a) In general Whenever\u2014 (1) the United States, or any of the Commonwealths or possessions, is invaded or is in danger of invasion by a foreign nation; (2) there is a rebellion or danger of a rebellion against the authority of the Government of the United States; or (3) the President is unable with the regular forces to execute the laws of the United States; the President may call into Federal service members and units of the National Guard of any State in such numbers as he considers necessary to repel the invasion, suppress the rebellion, or execute those laws. Orders for these purposes shall be issued through the governors of the States or, in the case of the District of Columbia, through the commanding general of the National Guard of the District of Columbia. (b) Adjustment of disbursements in certain circumstances If the President\u2014 (1) calls into Federal service members and units of the National Guard of any State in such numbers as he considers necessary to repel the invasion, suppress the rebellion, or execute those laws pursuant to subsection (a); and (2) within 30 days of the conclusion of an action described in subsection (a), provides a determination to the Governor of the State in which the National Guard was called into Federal Service that the calling into service was the result of an action or act of negligence carried out by the State government; the President shall direct the Secretary of Defense to coordinate with the Secretary of the Treasury, and any other appropriate officials or agencies, to determine the cost incurred to the Federal Government as a result of calling the National Guard into service, and shall, after notifying the Governor of the State, reduce funds made available to such State equal to 100 percent of the costs incurred by the Federal Government. (c) Waiver The President may waive the reimbursement requirement under this section in cases of extreme financial hardship to the State or when the deployment is primarily to protect Federal property or enforce Federal law, as determined by the President. (d) Regulations The Secretary of Defense may prescribe regulations to implement this section. .\n#### 3. Effective date\nThis Act shall take effect retroactively on June 1, 2025, and apply to all National Guard deployments required thereafter.",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-17T15:29:20Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4042ih.xml"
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
      "title": "STATES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-26T12:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STATES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "States Taking Accountability for Troops Engaged in Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a State to reimburse the Federal Government for the deployment of the National Guard to such State.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T12:18:21Z"
    }
  ]
}
```
