# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6545?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6545
- Title: Anesthesia for All Act
- Congress: 119
- Bill type: HR
- Bill number: 6545
- Origin chamber: House
- Introduced date: 2025-12-09
- Update date: 2025-12-19T09:07:57Z
- Update date including text: 2025-12-19T09:07:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-09: Introduced in House

## Actions

- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Introduced in House
- 2025-12-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6545",
    "number": "6545",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Anesthesia for All Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:57Z",
    "updateDateIncludingText": "2025-12-19T09:07:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T17:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6545ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6545\nIN THE HOUSE OF REPRESENTATIVES\nDecember 9, 2025 Mr. Torres of New York introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit health insurers, including Medicaid managed care organizations and other private health plans, from imposing arbitrary time caps on reimbursement for anesthesia services and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Anesthesia for All Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAnesthesia care is essential and must be determined by medical necessity, not arbitrary limits.\n**(2)**\nTime caps on reimbursement jeopardize patient safety, impose financial burdens, and interfere with informed medical decisions.\n**(3)**\nProhibiting such practices protects patients, promotes fairness, and ensures equitable access to essential healthcare services.\n#### 3. Prohibition on arbitrary time caps for anesthesia services\n##### (a) In general\nPart A of title XXVII of the Public Health Service Act ( 42 U.S.C. 300gg et seq. ) is amended by adding at the end the following new section:\n2730. Prohibition on arbitrary time caps for anesthesia services (a) Prohibition on time limits A group health plan, and a health insurance issuer offering group or individual health insurance coverage, may not impose arbitrary time caps on reimbursement for anesthesia services provided during medically necessary procedures. (b) Requirement for reimbursement based on medical necessity Reimbursement for anesthesia services shall be determined based on medical necessity as assessed by the attending anesthesiologist, certified registered nurse anesthetist, or licensed anesthesia provider. (c) Denial of payment A group health plan, and a health insurance issuer offering group or individual health insurance coverage, are prohibited from denying payment for anesthesia services solely because the duration of care exceeded a pre-set time limit. .\n##### (b) Medicaid\nSection 1902(a) of the Social Security Act ( 42 U.S.C. 1396a(a) ) is amended\u2014\n**(1)**\nin paragraph (86), by striking and at the end;\n**(2)**\nin paragraph (87), by striking the period and inserting ; and ; and\n**(3)**\nby inserting after paragraph (87) the following new paragraph:\n(88) provide that medical assistance consisting of anesthesia, including such assistance furnished through a managed care organization, is not subject to arbitrary time caps on reimbursement when furnished during medically necessary procedures (as determined by the attending anesthesiologist, certified registered nurse anesthetist, or other provider of such anesthesia) and that payment is not denied for such assistance solely because the duration of such assistance exceeded a pre-set time limit. .\n#### 4. Oversight by inspector general\n##### (a) Monitoring and audits\nThe Office of the Inspector General of the Department of Health and Human Services shall\u2014\n**(1)**\nconduct periodic audits of health insurers to assess compliance with the provisions of this Act; and\n**(2)**\ninvestigate allegations of noncompliance submitted by patients, providers, or other stakeholders.\n##### (b) Reporting to congress\nNot later than one year after the date of enactment of this Act, and every 3 years thereafter, the Inspector General described in subsection (a) shall submit a report to Congress that includes\u2014\n**(1)**\nthe findings of audits conducted under subsection (a);\n**(2)**\nthe number and nature of violations referred to the Secretary of Health and Human Services; and\n**(3)**\nrecommendations, if any, for improving compliance with the provisions of this Act.",
      "versionDate": "2025-12-09",
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
        "name": "Health",
        "updateDate": "2025-12-11T15:28:48Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6545ih.xml"
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
      "title": "Anesthesia for All Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T12:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Anesthesia for All Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-10T12:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit health insurers, including Medicaid managed care organizations and other private health plans, from imposing arbitrary time caps on reimbursement for anesthesia services and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-10T12:18:25Z"
    }
  ]
}
```
