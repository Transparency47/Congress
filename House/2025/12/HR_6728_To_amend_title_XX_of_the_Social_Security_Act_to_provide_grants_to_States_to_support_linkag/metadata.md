# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6728?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6728
- Title: Linking Seniors to Needed Legal Services Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6728
- Origin chamber: House
- Introduced date: 2025-12-15
- Update date: 2026-01-09T15:15:53Z
- Update date including text: 2026-01-09T15:15:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-15: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-15: Introduced in House

## Actions

- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-15",
    "latestAction": {
      "actionDate": "2025-12-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6728",
    "number": "6728",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Linking Seniors to Needed Legal Services Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-09T15:15:53Z",
    "updateDateIncludingText": "2026-01-09T15:15:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-15",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-15",
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
          "date": "2025-12-15T17:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6728ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6728\nIN THE HOUSE OF REPRESENTATIVES\nDecember 15, 2025 Mr. Vindman (for himself and Mr. Garbarino ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XX of the Social Security Act to provide grants to States to support linkages to legal services and medical legal partnerships.\n#### 1. Short title\nThis Act may be cited as the Linking Seniors to Needed Legal Services Act of 2025 .\n#### 2. Incentives for developing and sustaining structural competency in providing health and human services\n##### (a) In general\nPart II of subtitle B of title XX of the Social Security Act ( 42 U.S.C. 1397m\u20135 ) is amended by adding at the end the following:\n2047. Incentives for developing and sustaining structural competency in providing health and human services (a) Grants to States To support linkages to legal services and medical legal partnerships (1) In general Within 2 years after the date of the enactment of this section, the Secretary shall establish and administer a program of grants to States to support the adoption of evidence-based approaches to establishing or improving and maintaining real-time linkages between health and social services and supports for vulnerable elders or in conjunction with authorized representatives of vulnerable elders, including through the following: (A) Medical-legal partnerships The establishment and support of medical-legal partnerships, the incorporation of the partnerships in the elder justice framework and health and human services safety net, and the implementation and operation of such a partnership by an eligible grantee\u2014 (i) at the option of a State, in conjunction with an area agency on aging; (ii) in a solo provider practice in a health professional shortage area (as defined in section 332(a) of the Public Health Service Act), a medically underserved community (as defined in section 399V of such Act), or a rural area (as defined in section 330J of such Act); (iii) in a minority-serving institution of higher learning with health, law, and social services professional programs; (iv) in a federally qualified health center, as described in section 330 of the Public Health Service Act, or look-alike, as described in section 1905(l)(2)(B) of this Act; or (v) in certain hospitals that are critical access hospitals, Medicare-dependent hospitals, sole community hospitals, rural emergency hospitals, or that serve a high proportion of Medicare or Medicaid patients. (B) Legal hotlines development or expansion The provision of incentives to develop, enhance, and integrate platforms, such as legal assistance hotlines, that help to facilitate the identification of older adults who could benefit from linkages to available legal services such as those described in subparagraph (A). (2) State reports Each State to which a grant is made under this subsection shall submit to the Secretary biannual reports on the activities carried out by the State pursuant to this subsection, which shall include assessments of the effectiveness of the activities with respect to\u2014 (A) the number of unique individuals identified through the mechanism outlined in paragraph (1)(B) who are referred to services described in paragraph (1)(A), and the average time period associated with resolving issues; (B) the success rate for referrals to community-based resources; and (C) other factors determined relevant by the Secretary. (3) Evaluation The Secretary shall, by grant, contract, or interagency agreement, evaluate the activities conducted pursuant to this subsection, which shall include a comparison among the States. (4) Report to the Congress Every 4 years, the Secretary shall submit to the Congress a written report on the activities conducted under this subsection. (5) Appropriation Out of any money in the Treasury not otherwise appropriated, there are appropriated to the Secretary $125,000,000 for each of fiscal years 2026 through 2029 to carry out this subsection. (6) Supplement not supplant Support provided to area agencies on aging, State units on aging, eligible entities, or other community-based organizations pursuant to this subsection shall be used to supplement and not supplant any other Federal, State, or local funds expended to provide the same or comparable services described in this subsection. (b) Definitions In this section: (1) Area agency on aging The term area agency on aging means an area agency on aging designated under section 305 of the Older Americans Act of 1965. (2) Community-based organization The term community-based organization includes, except as otherwise provided by the Secretary, a nonprofit community-based organization, a consortium of nonprofit community-based organizations, a national nonprofit organization acting as an intermediary for a community-based organization, or a community-based organization that has a fiscal sponsor that allows the organization to function as an organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code. .\n##### (b) Clarification that medical-Legal partnerships are authorized adult protective services activities\nSection 2011 of such Act ( 42 U.S.C. 1397j ) is amended\u2014\n**(1)**\nin paragraph (2)(D), by inserting , including through a medical-legal partnership before the period; and\n**(2)**\nby redesignating paragraphs (16) through (22) as paragraphs (17) through (23), respectively, and inserting after paragraph (15) the following:\n(16) Medical-legal partnership The term medical-legal partnership means an arrangement in a health care or social services setting which integrates lawyers and social workers to address the needs of an individual patient related to social determinants of health, and to help clinicians, case managers, and social workers address structural problems at the root of many health inequities, including a multidisciplinary team integrated into such a setting to address the needs and establish and maintain structural competence within clinicians, case managers, and social workers to best address structural problems at the root of many health inequities. .",
      "versionDate": "2025-12-15",
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
        "name": "Social Welfare",
        "updateDate": "2026-01-09T15:15:53Z"
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
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6728ih.xml"
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
      "title": "Linking Seniors to Needed Legal Services Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-07T06:38:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Linking Seniors to Needed Legal Services Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-07T06:38:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XX of the Social Security Act to provide grants to States to support linkages to legal services and medical legal partnerships.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-07T06:33:20Z"
    }
  ]
}
```
