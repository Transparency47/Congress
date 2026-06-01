# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3902?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3902
- Title: Restoring Federalism in Clean Water Permitting Act
- Congress: 119
- Bill type: HR
- Bill number: 3902
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2025-06-26T14:39:20Z
- Update date including text: 2025-06-26T14:39:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-13 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-06-11: Introduced in House

## Actions

- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-13 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3902",
    "number": "3902",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "P000622",
        "district": "1",
        "firstName": "Jimmy",
        "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
        "lastName": "Patronis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Restoring Federalism in Clean Water Permitting Act",
    "type": "HR",
    "updateDate": "2025-06-26T14:39:20Z",
    "updateDateIncludingText": "2025-06-26T14:39:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-13",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
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
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T14:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-13T15:22:13Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3902ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3902\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Mr. Patronis introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Administrator of the Environmental Protection Agency to review the regulations applicable to the approval of State permit programs under section 404 of the Federal Water Pollution Control Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restoring Federalism in Clean Water Permitting Act .\n#### 2. State assumption of section 404 permit program regulation review\nNot later than 180 days after the date of enactment of this Act, the Administrator of the Environmental Protection Agency shall complete a review of the regulations applicable to the approval of State permit programs under section 404 of the Federal Water Pollution Control Act ( 33 U.S.C. 1344 ) in order to identify revisions to such regulations necessary to streamline the approval process, reduce administrative burdens, and encourage additional States to administer a permit program under such section, and the Administrator shall implement any such revisions as appropriate.\n#### 3. Judicial review timeline clarity\nSection 404 of the Federal Water Pollution Control Act ( 33 U.S.C. 1344 ) is amended\u2014\n**(1)**\nby redesignating subsection (t) as subsection (u);\n**(2)**\nin subsection (u), as so redesignated, by striking Nothing in the section and inserting Savings provision.\u2014 Nothing in this section ; and\n**(3)**\nby inserting after subsection (s) the following:\n(t) Judicial review (1) Statute of limitations Notwithstanding any applicable provision of law relating to statutes of limitations, an action seeking judicial review of the approval by the Administrator of a State permit program pursuant to this section shall be filed not later than the date that is 60 days after the date on which the approval was issued. (2) Limitation on commencement of certain actions Notwithstanding any other provision of law, no action described in paragraph (1) may be commenced unless the action\u2014 (A) is filed by a party that submitted a comment\u2014 (i) during the public comment period for the administrative proceedings related to such action; and (ii) which was sufficiently detailed to put the Administrator on notice of the issue upon which the party seeks judicial review; and (B) is related to such comment. (3) Remedy If a court determines that the Administrator did not comply with the requirements of this section in issuing an approval of a State permit program pursuant to this section\u2014 (A) the court shall remand the matter to the Administrator for further proceedings consistent with the determination of the court; and (B) the court may not vacate, revoke, enjoin, or otherwise limit the authority of the State to issue permits under such State permit program, unless the court finds that activities authorized under any permit issued under the program would present an imminent and substantial danger to human health or the environment for which there is no other equitable remedy available under the law. (4) Timeline to act on court order If a court remands a matter under paragraph (2), the court shall set and enforce a reasonable schedule and deadline, which may not exceed 180 days from the date on which the court remands such matter, except as otherwise required by law, for the Administrator to take such actions as the court may order. .",
      "versionDate": "2025-06-11",
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
        "name": "Environmental Protection",
        "updateDate": "2025-06-26T14:39:20Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3902ih.xml"
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
      "title": "Restoring Federalism in Clean Water Permitting Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T08:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restoring Federalism in Clean Water Permitting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T08:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Environmental Protection Agency to review the regulations applicable to the approval of State permit programs under section 404 of the Federal Water Pollution Control Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T08:18:18Z"
    }
  ]
}
```
