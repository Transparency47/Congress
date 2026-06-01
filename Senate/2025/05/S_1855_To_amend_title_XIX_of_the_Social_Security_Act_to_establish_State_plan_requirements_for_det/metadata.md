# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1855?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1855
- Title: Care for Military Kids Act
- Congress: 119
- Bill type: S
- Bill number: 1855
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-03-11T21:41:33Z
- Update date including text: 2026-03-11T21:41:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1855",
    "number": "1855",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Care for Military Kids Act",
    "type": "S",
    "updateDate": "2026-03-11T21:41:33Z",
    "updateDateIncludingText": "2026-03-11T21:41:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T15:02:28Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1855is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1855\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Blumenthal (for himself and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XIX of the Social Security Act to establish State plan requirements for determining residency and coverage for military families, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Care for Military Kids Act .\n#### 2. Medicaid State plan requirement for determining residency and coverage for military families\n##### (a) In general\nSection 1902 of the Social Security Act ( 42 U.S.C. 1396a ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (86), by striking and at the end;\n**(B)**\nin paragraph (87)(D), by striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting after paragraph (87)(D), the following new paragraph:\n(88) beginning January 1, 2028, provide, with respect to an active duty relocated individual (as defined in subsection (uu)(1))\u2014 (A) that, for purposes of determining eligibility for medical assistance under the State plan (or waiver of such plan), such active duty relocated individual is treated as a resident of the State unless such individual voluntarily elects not to be so treated for such purposes; (B) that if, at the time of relocation (as described in subsection (uu)(1)), such active duty relocated individual is on a home and community-based services waiting list (as defined in subsection (uu)(2)), such individual remains on such list until\u2014 (i) the State completes an assessment and renders a decision with respect to the eligibility of such individual to receive the relevant home and community-based services at the time a slot for such services becomes available and, in the case such decision is a denial of such eligibility, such individual has exhausted the individual\u2019s opportunity for a fair hearing; or (ii) such individual elects to be removed from such list; and (C) payment for medical assistance furnished under the State plan (or a waiver of the plan) on behalf of such active duty relocated individual in the military service relocation State (as referred to in subsection (uu)(1)(B)(i)), to the extent that such assistance is available in such military service relocation State in accordance with such guidance as the Secretary may issue to ensure access to such assistance. ; and\n**(2)**\nby adding at the end the following new subsection:\n(uu) Active duty relocated individual; Home and community-Based services waiting list For purposes of subsection (a)(88) and this subsection: (1) Active duty relocated individual The term active duty relocated individual means an individual\u2014 (A) who\u2014 (i) is enrolled under the State plan (or waiver of such plan); or (ii) with respect to an individual described in subparagraph (C)(ii), would be so enrolled pursuant to subsection (a)(10)(A)(ii)(VI) if such individual began receiving home and community-based services; (B) who\u2014 (i) is a member of the Armed Forces engaged in active duty service and is relocated to another State (in this subsection referred to as the military service relocation State ) by reason of such service; (ii) would be described in clause (i) except that the individual stopped being engaged in active duty service (including by reason of retirement from such service) and the last day on which the individual was engaged in active duty service occurred not more than 12 months ago; or (iii) is a dependent (as defined by the Secretary) of a member described in clause (i) or (ii) who relocates to the military service relocation State with such member; and (C) who\u2014 (i) was receiving home and community-based services (as defined in section 9817(a)(2)(B) of the American Rescue Plan Act of 2021) at the time of such relocation; or (ii) if the State maintains a home and community-based services waiting list, was on such home and community-based services waiting list at the time of such relocation. (2) Home and community-based services waiting list The term home and community-based services waiting list means, in the case of a State that has a limit on the number of individuals who may receive home and community-based services under section 1115(a), section 1915(c), or section 1915(j), a list maintained by such State of individuals who are requesting to receive such services under 1 or more such sections but for whom the State has not yet completed an assessment and rendered a decision with respect to the eligibility of such individuals to receive the relevant home and community-based services at the time a slot for such services becomes available due to such limit. .\n##### (b) Implementation funding\nThere are appropriated, out of any funds in the Treasury not otherwise obligated, $1,000,000 for each of fiscal years 2026 through 2030, to remain available until expended, to the Secretary of Health and Human Services for purposes of implementing the amendments made by subsection (a).\n##### (c) Effective date\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by subsection (a) shall take effect on the date of enactment of this Act.\n**(2) Delay permitted if state legislation required**\nIn the case of a State plan approved under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) which the Secretary of Health and Human Services determines requires State legislation (other than legislation appropriating funds) in order for the plan to meet the additional requirements imposed by the amendments made by this section, the State plan shall not be regarded as failing to comply with the requirements of such title XIX solely on the basis of the failure of the plan to meet such additional requirements before the first day of the first calendar quarter beginning after the close of the first regular session of the State legislature that ends after the 1-year period beginning with the date of the enactment of this section. For purposes of the preceding sentence, in the case of a State that has a 2-year legislative session, each year of the session is deemed to be a separate regular session of the State legislature.",
      "versionDate": "2025-05-22",
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
        "actionDate": "2025-05-14",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "3399",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Care for Military Kids Act of 2025",
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
        "updateDate": "2026-02-18T20:18:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-22",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s1855",
          "measure-number": "1855",
          "measure-type": "s",
          "orig-publish-date": "2025-05-22",
          "originChamber": "SENATE",
          "update-date": "2026-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1855v00",
            "update-date": "2026-03-11"
          },
          "action-date": "2025-05-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Care for Military Kids Act</strong></p><p>This bill requires a state Medicaid program to consider active-duty members of the Armed Forces and their dependents who are receiving home- and community-based services to be residents of that state even if they are relocated to another state because of their military service, unless the member chooses not to be considered as such. The requirement applies beginning in 2028.</p><p>The bill provides funds through FY2030 for the Centers for Medicare & Medicaid Services to implement the bill.</p>"
        },
        "title": "Care for Military Kids Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1855.xml",
    "summary": {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Care for Military Kids Act</strong></p><p>This bill requires a state Medicaid program to consider active-duty members of the Armed Forces and their dependents who are receiving home- and community-based services to be residents of that state even if they are relocated to another state because of their military service, unless the member chooses not to be considered as such. The requirement applies beginning in 2028.</p><p>The bill provides funds through FY2030 for the Centers for Medicare & Medicaid Services to implement the bill.</p>",
      "updateDate": "2026-03-11",
      "versionCode": "id119s1855"
    },
    "title": "Care for Military Kids Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Care for Military Kids Act</strong></p><p>This bill requires a state Medicaid program to consider active-duty members of the Armed Forces and their dependents who are receiving home- and community-based services to be residents of that state even if they are relocated to another state because of their military service, unless the member chooses not to be considered as such. The requirement applies beginning in 2028.</p><p>The bill provides funds through FY2030 for the Centers for Medicare & Medicaid Services to implement the bill.</p>",
      "updateDate": "2026-03-11",
      "versionCode": "id119s1855"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1855is.xml"
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
      "title": "Care for Military Kids Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-04T03:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Care for Military Kids Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XIX of the Social Security Act to establish State plan requirements for determining residency and coverage for military families, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:32Z"
    }
  ]
}
```
