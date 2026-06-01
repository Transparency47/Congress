# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3300?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3300
- Title: ANCHOR Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3300
- Origin chamber: Senate
- Introduced date: 2025-12-02
- Update date: 2026-01-05T14:41:02Z
- Update date including text: 2026-01-05T14:41:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in Senate
- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-12-02: Introduced in Senate

## Actions

- 2025-12-02 - IntroReferral: Introduced in Senate
- 2025-12-02 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3300",
    "number": "3300",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "ANCHOR Act of 2025",
    "type": "S",
    "updateDate": "2026-01-05T14:41:02Z",
    "updateDateIncludingText": "2026-01-05T14:41:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-12-02T17:03:43Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3300is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3300\nIN THE SENATE OF THE UNITED STATES\nDecember 2, 2025 Mrs. Blackburn introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XIX of the Social Security Act to establish a State option to provide medical assistance to certain individuals with serious mental illness or substance use disorder.\n#### 1. Short title\nThis Act may be cited as the Access to New Community Health Opportunities and Recovery Act of 2025 or the ANCHOR Act of 2025 .\n#### 2. Establishing a State option to provide medical assistance to certain individuals with serious mental illness or substance use disorder\nSection 1902 of the Social Security Act ( 42 U.S.C. 1396a ) is amended\u2014\n**(1)**\nin subsection (a)(10)(A)(ii)\u2014\n**(A)**\nin subclause (XXII), by striking or at the end;\n**(B)**\nin subclause (XXIII), by adding or at the end; and\n**(C)**\nby adding at the end the following new subclause:\n(XXIV) specified individuals (as defined in paragraph (1) of subsection (yy)), subject to the provisions of such subsection; ; and\n**(2)**\nby adding at the end the following new subsection:\n(yy) Specified individuals (1) Definition For purposes of subsection (a)(10)(A)(ii)(XXIV), the term specified individual means an individual\u2014 (A) who is an uninsured individual (as defined in subsection (ss)); (B) whose income (as determined under subsection (e)(14)) does not exceed 100 percent of the poverty line (as defined in section 2110(c)(5)) applicable to a family of the size involved; and (C) who has been determined to have a qualifying condition (as defined in paragraph (2)) by\u2014 (i) a health care provider; or (ii) an entity determined appropriate by the State, which may include\u2014 (I) an emergency department; (II) a clinic certified by the State as a certified community behavioral health clinic in accordance with the criteria described in section 223(a)(1) of the Protecting Access to Medicare Act of 2014; (III) an entity that receives funding from the State to provide mental health or substance use disorder services; (IV) an institution for mental diseases (as defined in section 435.1010 of title 42, Code of Federal Regulations (or a successor regulation)); or (V) a State judicial, law enforcement, or child welfare agency. (2) Qualifying condition defined For purposes of paragraph (1)(C), the term qualifying condition means any of the following: (A) Serious mental illness. (B) Serious emotional disturbance. (C) Opioid use disorder. (D) Stimulant use disorder (including with respect to cocaine or methamphetamine). (3) Conditions (A) Scope Medical assistance shall be made available to a specified individual in the same scope and manner as such assistance is made available to individuals described in subsection (a)(10)(A)(i). (B) Duration Medical assistance shall be made available to a specified individual for an initial continuous 1-year period. At the option of the State, the State may extend the availability of such assistance to such individual for subsequent continuous 1-year periods, provided that, prior to each such extension, the State redetermines that such individual continues to be a specified individual. (4) Ensuring quality of care A State shall, as a condition of exercising the State\u2019s option to make medical assistance available to specified individuals\u2014 (A) ensure such individuals have a care plan developed within 60 days of enrolling for such assistance by a physician, primary care provider, emergency department, clinical practice or clinical group practice, rural clinic, community health center, certified community behavioral health clinic, or other health care provider that is determined by the State to be qualified to develop such a plan; and (B) agree to report the behavioral health measures of the Core Set of Adult Health Care Quality Measures for Medicaid with respect to such individuals in accordance with section 1139B. .",
      "versionDate": "2025-12-02",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-03",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "6408",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ANCHOR Act of 2025",
      "type": "HR"
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
        "updateDate": "2026-01-05T14:40:21Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3300is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XIX of the Social Security Act to establish a State option to provide medical assistance to certain individuals with serious mental illness or substance use disorder.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T07:58:43Z"
    },
    {
      "title": "ANCHOR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ANCHOR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Access to New Community Health Opportunities and Recovery Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:21Z"
    }
  ]
}
```
