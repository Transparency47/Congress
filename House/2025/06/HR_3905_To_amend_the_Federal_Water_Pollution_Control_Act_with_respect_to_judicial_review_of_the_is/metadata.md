# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3905?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3905
- Title: Judicial Review Timeline Clarity Act
- Congress: 119
- Bill type: HR
- Bill number: 3905
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2025-06-26T14:42:14Z
- Update date including text: 2025-06-26T14:42:14Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3905",
    "number": "3905",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "B001316",
        "district": "7",
        "firstName": "Eric",
        "fullName": "Rep. Burlison, Eric [R-MO-7]",
        "lastName": "Burlison",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Judicial Review Timeline Clarity Act",
    "type": "HR",
    "updateDate": "2025-06-26T14:42:14Z",
    "updateDateIncludingText": "2025-06-26T14:42:14Z"
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
          "date": "2025-06-11T14:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-13T15:20:33Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3905ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3905\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Mr. Burlison introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Federal Water Pollution Control Act with respect to judicial review of the issuance of a permit for the discharge of dredged or fill material, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Judicial Review Timeline Clarity Act .\n#### 2. Judicial review timeline clarity\nSection 404 of the Federal Water Pollution Control Act ( 33 U.S.C. 1344 ) is amended\u2014\n**(1)**\nby redesignating subsection (t) as subsection (u);\n**(2)**\nin subsection (u), as so redesignated, by striking Nothing in the section and inserting Savings provision.\u2014 Nothing in this section ; and\n**(3)**\nby inserting after subsection (s) the following:\n(t) Judicial review (1) Statute of limitations Notwithstanding any applicable provision of law relating to statutes of limitations\u2014 (A) an action seeking judicial review of an individual permit or general permit issued under this section shall be filed not later than the date that is 60 days after the date on which the permit was issued; and (B) an action seeking judicial review of a verification that an activity involving a discharge of dredged or fill material is authorized by a general permit issued under this section shall be filed not later than the date that is 60 days after the date on which such verification was issued. (2) Limitation on commencement of certain actions Notwithstanding any other provision of law, no action described in paragraph (1) may be commenced unless the action\u2014 (A) is filed by a party that submitted a comment\u2014 (i) during the public comment period for the administrative proceedings related to the applicable action described in such paragraph; and (ii) which was sufficiently detailed to put the Secretary or the State, as applicable, on notice of the issue upon which the party seeks judicial review; and (B) is related to such comment. (3) Remedy If a court determines that the Secretary or the State, as applicable, did not comply with the requirements of this section in issuing an individual or general permit under this section, or in verifying that an activity involving a discharge of dredged or fill material is authorized by a general permit issued under this section, as applicable\u2014 (A) the court shall remand the matter to the Secretary or the State, as applicable, for further proceedings consistent with the determination of the court; (B) with respect to a determination regarding the issuance of an individual or general permit under this section, the court may not vacate, revoke, enjoin, or otherwise limit the permit, unless the court finds that activities authorized under the permit would present an imminent and substantial danger to human health or the environment for which there is no other equitable remedy available under the law; and (C) with respect to a determination regarding a verification that an activity involving a discharge of dredged or fill material is authorized by a general permit issued under this section, the court may not enjoin or otherwise limit the discharge unless the court finds that the activity would present an imminent and substantial danger to human health or the environment for which there is no other equitable remedy available under the law. (4) Timeline to act on court order If a court remands a matter under paragraph (2), the court shall set and enforce a reasonable schedule and deadline, which may not exceed 180 days from the date on which the court remands such matter, except as otherwise required by law, for the Secretary or the State, as applicable, to take such actions as the court may order. .",
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
        "updateDate": "2025-06-26T14:42:14Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3905ih.xml"
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
      "title": "Judicial Review Timeline Clarity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Judicial Review Timeline Clarity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T08:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Water Pollution Control Act with respect to judicial review of the issuance of a permit for the discharge of dredged or fill material, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T08:18:24Z"
    }
  ]
}
```
