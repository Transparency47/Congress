# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3399?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3399
- Title: Care for Military Kids Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3399
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2026-02-18T20:18:20Z
- Update date including text: 2026-02-18T20:18:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-05-14: Introduced in House

## Actions

- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3399",
    "number": "3399",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Care for Military Kids Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-18T20:18:20Z",
    "updateDateIncludingText": "2026-02-18T20:18:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
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
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T14:01:25Z",
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
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3399ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3399\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Mrs. Kiggans of Virginia (for herself and Ms. Kaptur ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to establish State plan requirements for determining residency and coverage for military families, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Care for Military Kids Act of 2025 .\n#### 2. Medicaid State plan requirement for determining residency and coverage for military families\n##### (a) In general\nSection 1902 of the Social Security Act ( 42 U.S.C. 1396a ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (86), by striking and at the end;\n**(B)**\nin paragraph (87)(D), by striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting after paragraph (87)(D), the following new paragraph:\n(88) beginning January 1, 2028, provide, with respect to an active duty relocated individual (as defined in subsection (uu)(1))\u2014 (A) that, for purposes of determining eligibility for medical assistance under the State plan (or waiver of such plan), such active duty relocated individual is treated as a resident of the State unless such individual voluntarily elects not to be so treated for such purposes; (B) that if, at the time of relocation (as described in subsection (uu)(1)), such active duty relocated individual is on a home and community-based services waiting list (as defined in subsection (uu)(2)), such individual remains on such list until\u2014 (i) the State completes an assessment and renders a decision with respect to the eligibility of such individual to receive the relevant home and community-based services at the time a slot for such services becomes available and, in the case such decision is a denial of such eligibility, such individual has exhausted the individual\u2019s opportunity for a fair hearing; or (ii) such individual elects to be removed from such list; and (C) payment for medical assistance furnished under the State plan (or a waiver of the plan) on behalf of such active duty relocated individual in the military service relocation State (as referred to in subsection (uu)(1)(B)(i)), to the extent that such assistance is available in such military service relocation State in accordance with such guidance as the Secretary may issue to ensure access to such assistance. ; and\n**(2)**\nby adding at the end the following new subsection:\n(uu) Active duty relocated individual; Home and community-Based services waiting list For purposes of subsection (a)(88) and this subsection: (1) Active duty relocated individual The term active duty relocated individual means an individual\u2014 (A) who\u2014 (i) is enrolled under the State plan (or waiver of such plan); or (ii) with respect to an individual described in subparagraph (C)(ii), would be so enrolled pursuant to subsection (a)(10)(A)(ii)(VI) if such individual began receiving home and community-based services; (B) who\u2014 (i) is a member of the Armed Forces engaged in active duty service and is relocated to another State (in this subsection referred to as the military service relocation State ) by reason of such service; (ii) would be described in clause (i) except that the individual stopped being engaged in active duty service (including by reason of retirement from such service) and the last day on which the individual was engaged in active duty service occurred not more than 12 months ago; or (iii) is a dependent (as defined by the Secretary) of a member described in clause (i) or (ii) who relocates to the military service relocation State with such member; and (C) who\u2014 (i) was receiving home and community-based services (as defined in section 9817(a)(2)(B) of the American Rescue Plan Act of 2021) at the time of such relocation; or (ii) if the State maintains a home and community-based services waiting list, was on such home and community-based services waiting list at the time of such relocation. (2) Home and community-based services waiting list The term home and community-based services waiting list means, in the case of a State that has a limit on the number of individuals who may receive home and community-based services under section 1115(a), section 1915(c), or section 1915(j), a list maintained by such State of individuals who are requesting to receive such services under 1 or more such sections but for whom the State has not yet completed an assessment and rendered a decision with respect to the eligibility of such individuals to receive the relevant home and community-based services at the time a slot for such services becomes available due to such limit. .\n##### (b) Implementation funding\nThere are appropriated, out of any funds in the Treasury not otherwise obligated, $1,000,000 for each of fiscal years 2026 through 2030, to remain available until expended, to the Secretary of Health and Human Services for purposes of implementing the amendments made by subsection (a).\n##### (c) Effective date\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by subsection (a) shall take effect on the date of enactment of this Act.\n**(2) Delay permitted if state legislation required**\nIn the case of a State plan approved under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) which the Secretary of Health and Human Services determines requires State legislation (other than legislation appropriating funds) in order for the plan to meet the additional requirements imposed by the amendments made by this section, the State plan shall not be regarded as failing to comply with the requirements of such title XIX solely on the basis of the failure of the plan to meet such additional requirements before the first day of the first calendar quarter beginning after the close of the first regular session of the State legislature that ends after the 1-year period beginning with the date of the enactment of this section. For purposes of the preceding sentence, in the case of a State that has a 2-year legislative session, each year of the session is deemed to be a separate regular session of the State legislature.",
      "versionDate": "2025-05-14",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1855",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Care for Military Kids Act",
      "type": "S"
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
        "updateDate": "2026-02-18T20:18:20Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3399ih.xml"
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
      "title": "Care for Military Kids Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Care for Military Kids Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to establish State plan requirements for determining residency and coverage for military families, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:20Z"
    }
  ]
}
```
