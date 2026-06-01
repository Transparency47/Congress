# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8792?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8792
- Title: Multigenerational Caregiving Data Act
- Congress: 119
- Bill type: HR
- Bill number: 8792
- Origin chamber: House
- Introduced date: 2026-05-13
- Update date: 2026-05-28T06:53:28Z
- Update date including text: 2026-05-28T06:53:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-13: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-05-13: Introduced in House

## Actions

- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8792",
    "number": "8792",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "H001085",
        "district": "6",
        "firstName": "Chrissy",
        "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
        "lastName": "Houlahan",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Multigenerational Caregiving Data Act",
    "type": "HR",
    "updateDate": "2026-05-28T06:53:28Z",
    "updateDateIncludingText": "2026-05-28T06:53:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-13",
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
          "date": "2026-05-13T14:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "CA"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "FL"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8792ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8792\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2026 Ms. Houlahan (for herself, Mr. Khanna , Mrs. Luna , and Mr. Turner of Ohio ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require the collection of information on multigenerational caregiving in at least one major Federal population survey, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Multigenerational Caregiving Data Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nA growing number of individuals in the United States provide unpaid care to both children and older adults.\n**(2)**\nThese individuals face distinct economic, health, and workforce challenges.\n**(3)**\nExisting Federal data do not adequately capture multigenerational caregiving responsibilities, particularly when care is provided across households.\n**(4)**\nImproved data collection would enhance policymaking related to caregiving, labor force participation, and health outcomes.\n**(5)**\nMajor Federal population surveys, including those conducted by the Bureau of the Census and the National Center for Health Statistics of the Centers for Disease Control and Prevention, are appropriate instruments for collecting such data.\n#### 3. Data collection requirement on multigenerational caregivers\n##### (a) In general\nNot later than 3 years after the date of enactment of this Act, the Secretary, in consultation with the heads of relevant Federal statistical agencies, shall ensure that at least 1 major Federal population survey includes a question designed to identify individuals who provided regular unpaid care or assistance as a multigenerational caregiver within the previous 12 month period.\n##### (b) Flexibility\nThe Secretary may modify the wording, response categories, or placement of the question required under this section as necessary to\u2014\n**(1)**\nensure clarity and reliability of responses;\n**(2)**\nminimize respondent burden; and\n**(3)**\nmaintain consistency with the methodology of the selected survey.\n##### (c) Testing\nBefore full implementation of the question required under this section, the responsible Federal statistical agency shall conduct\u2014\n**(1)**\ncognitive testing; and\n**(2)**\nfield testing, as appropriate.\n##### (d) Voluntary response\nAny response to the question required under this section shall be voluntary.\n##### (e) Report; publication\n**(1) Report**\nNot later than 2 years after the date on which the question required under this section is included in a major Federal population survey, the Secretary shall submit to Congress a report on the implementation of the question that\u2014\n**(A)**\nevaluates data quality and usability;\n**(B)**\nassesses respondent burden and response rates;\n**(C)**\nidentifies which survey or surveys included the question; and\n**(D)**\nprovides recommendations for expanding, modifying, or discontinuing the question.\n**(2) Publication**\nThe Secretary shall publish the report submitted under paragraph (1) on the public website of the Department of Commerce.\n##### (f) Definitions\nIn this Act:\n**(1) Major Federal population survey**\nThe term major Federal population survey means a nationally representative survey of individuals or households conducted by a Federal statistical agency, including\u2014\n**(A)**\nthe American Community Survey;\n**(B)**\nthe Current Population Survey;\n**(C)**\nthe National Health Interview Survey; or\n**(D)**\nany successor or similar survey designated by the Secretary.\n**(2) Multigenerational caregiver**\n**(A) In general**\nThe term multigenerational caregiver means an individual who provides unpaid care or assistance\u2014\n**(i)**\nto at least 1 individual who is described in clause (i), (ii), or (iii) of subparagraph (B); and\n**(ii)**\nto at least 1 individual who is described in a clause of subparagraph (B) other than the clause describing the individual referred to in clause (i) of this subparagraph.\n**(B) Demographic categories**\nThe individuals referred to in clauses (i) and (ii) of subparagraph (A) are the following:\n**(i)**\nA child who is less than 18 years of age.\n**(ii)**\nAn adult who is not less than 18 years of age and less than 65 years of age and who has a health condition or disability.\n**(iii)**\nAn adult who is not less than 65 years of age and who has a health condition or disability.\n**(3) Secretary**\nThe term Secretary means the Secretary of Commerce.",
      "versionDate": "2026-05-13",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8792ih.xml"
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
      "title": "Multigenerational Caregiving Data Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-28T06:53:28Z"
    },
    {
      "title": "Multigenerational Caregiving Data Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-28T06:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the collection of information on multigenerational caregiving in at least one major Federal population survey, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-28T06:48:26Z"
    }
  ]
}
```
