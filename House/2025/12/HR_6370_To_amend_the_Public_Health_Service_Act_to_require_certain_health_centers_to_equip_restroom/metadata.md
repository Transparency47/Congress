# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6370?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6370
- Title: Baby Changing in Health Centers Act
- Congress: 119
- Bill type: HR
- Bill number: 6370
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-01-05T16:06:35Z
- Update date including text: 2026-01-05T16:06:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6370",
    "number": "6370",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "U000040",
        "district": "14",
        "firstName": "Lauren",
        "fullName": "Rep. Underwood, Lauren [D-IL-14]",
        "lastName": "Underwood",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Baby Changing in Health Centers Act",
    "type": "HR",
    "updateDate": "2026-01-05T16:06:35Z",
    "updateDateIncludingText": "2026-01-05T16:06:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:05:15Z",
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6370ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6370\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Ms. Underwood (for herself and Mr. Van Drew ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to require certain health centers to equip restrooms with baby changing tables, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Baby Changing in Health Centers Act .\n#### 2. Equipping certain health centers with baby changing tables\n##### (a) In general\nSection 330 of the Public Health Service Act ( 42 U.S.C. 254b ) is amended by adding at the end the following:\n(s) Baby changing tables (1) In general As a condition for the receipt of a grant under this section, the Secretary shall require a health center receiving assistance under the grant to provide assurances that restrooms in the facilities of the health center are equipped with baby changing tables that are physically safe, sanitary, and appropriate. (2) Exceptions The requirement under subsection (a) shall not apply\u2014 (A) to a restroom in a facility that is not available or accessible for public use; (B) to a restroom in a facility that contains clear and conspicuous signs indicating\u2014 (i) in the case of a men\u2019s restroom, where another men\u2019s restroom, or a gender-neutral restroom, with a baby changing table is located on the same floor of such facility; (ii) in the case of a women\u2019s restroom, where another women\u2019s restroom, or a gender-neutral restroom, with a baby changing table is located on the same floor of such facility; or (iii) in the case of a gender-neutral restroom, where\u2014 (I) another gender-neutral restroom with a baby changing table is located on the same floor of such facility; or (II) a men\u2019s restroom and women\u2019s restroom with a baby changing table are located on the same floor of such facility; or (C) if new construction would be required to install a baby changing table in the facility and the cost of such construction is unfeasible. (3) ADA requirements The requirement of subsection (a) shall be subject to any reasonable accommodations that may be made for individuals in accordance with the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ). (4) Use of grant funds Grant funds received under this section may be used to cover costs associated with acquiring and installing baby changing tables and signs as necessary to comply with the requirements of this subsection. (5) Extensions; waivers The Secretary may extend a deadline for compliance with the requirements of this subsection, or may waive the applicability of such requirements, as the Secretary determines appropriate to account for extenuating circumstances. (6) Baby changing table defined In this subsection, the term baby changing table means an elevated, freestanding structure generally designed to support and retain a child with a body weight of up to 30 pounds in a horizontal position for the purpose of allowing an individual to change the child\u2019s diaper, including pull-out or drop-down changing surfaces. (7) Limitation on statutory construction Nothing in this section may be construed to supercede a more stringent requirement in a State or local law relating to\u2014 (A) equipping restrooms with baby changing tables; or (B) the standards applicable to such baby changing tables. (8) Authorization of appropriations In addition to other amounts authorized to be appropriated to carry out this section, there is authorized to be appropriated a total of $5,000,000 to supplement grant amounts received under this section for the sole purpose of assisting health centers in complying with the requirement of subsection (a). .\n##### (b) Applicability\nSection 330(s) of the Public Health Service Act (as added by subsection (a) of this section) shall apply\u2014\n**(1)**\nbeginning on the date of enactment of this Act, in the case of a facility that is acquired, constructed, or substantially renovated beginning on or after such date of enactment; and\n**(2)**\nbeginning 5 years after such date of enactment, in the case of all other facilities.",
      "versionDate": "2025-12-03",
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
        "updateDate": "2026-01-05T16:06:35Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6370ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to require certain health centers to equip restrooms with baby changing tables, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T07:58:50Z"
    },
    {
      "title": "Baby Changing in Health Centers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Baby Changing in Health Centers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:38:19Z"
    }
  ]
}
```
