# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1139?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1139
- Title: HOPE for Heroes Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1139
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2025-11-24T18:50:17Z
- Update date including text: 2025-11-24T18:50:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1139",
    "number": "1139",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "HOPE for Heroes Act of 2025",
    "type": "S",
    "updateDate": "2025-11-24T18:50:17Z",
    "updateDateIncludingText": "2025-11-24T18:50:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-26",
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
        "item": [
          {
            "date": "2025-07-30T20:00:24Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-26T16:08:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1139is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1139\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Moran introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend the Commander John Scott Hannon Veterans Mental Health Care Improvement Act of 2019 to modify and reauthorize the Staff Sergeant Parker Gordon Fox Suicide Prevention Grant Program of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helping Optimize Prevention and Engagement for Heroes Act of 2025 or the HOPE for Heroes Act of 2025 .\n#### 2. Modifications to and reauthorization of the Staff Sergeant Parker Gordon Fox Suicide Prevention Grant Program of the Department of Veterans Affairs\n##### (a) Coordination by Secretary\nSubsection (b) of section 201 of the Commander John Scott Hannon Veterans Mental Health Care Improvement Act of 2019 ( 38 U.S.C. 1720F note; Public Law 116\u2013171 ) is amended, in the second sentence, by striking the Office of Mental Health and Suicide Prevention and inserting the Assistant Under Secretary for Health for Clinical Services .\n##### (b) Use of grant funds\nSubsection (c) of such section is amended\u2014\n**(1)**\nin the subsection heading, by inserting ; use of grant funds after grants ;\n**(2)**\nin paragraph (2)(A)\u2014\n**(A)**\nby striking a maximum and inserting except as provided in paragraph (3), a maximum ; and\n**(B)**\nby striking $750,000 and inserting $1,000,000 ; and\n**(3)**\nby adding at the end the following new paragraphs:\n(3) Additional amounts (A) In general The Secretary may award amounts to a grantee in addition to the maximum amount under paragraph (2)(A) based on a performance-based metric established by the Secretary. (B) Performance The performance-based metric established under subparagraph (A) with respect to a grantee shall be based on the number of individuals who go through the intake process to receive suicide prevention services from the grantee under this section. (C) Limit The additional amount authorized under subparagraph (A) may not exceed $500,000 per grantee per fiscal year. (4) Use of grant funds For any grant awarded under this section\u2014 (A) not more than 30 percent of the grant funds may be spent on administrative costs; and (B) not more than five percent of the grant funds may be spent on food and beverages. .\n##### (c) Coordination by grant recipients\nSubsection (e)(3) of such section is amended\u2014\n**(1)**\nby redesignating subparagraphs (B) and (C) as subparagraphs (C) and (D), respectively; and\n**(2)**\nby inserting after subparagraph (A) the following new subparagraph (B):\n(B) coordinate with the Secretary to develop a plan for communication between the entity and local suicide prevention coordinators regarding whether veterans receiving assistance under this section from the entity are attending appointments to ensure continuity of care; .\n##### (d) Training and technical assistance\nSubsection (g) of such section is amended\u2014\n**(1)**\nin paragraph (1)(A), by inserting , including training on how to properly use the Columbia Protocol (also known as the Columbia-Suicide Severity Rating Scale (C\u2013SSRS)) after management ; and\n**(2)**\nby adding at the end the following new paragraph:\n(3) Training for Department employees The Secretary shall provide training to employees of the Department on the grant program under this section. .\n##### (e) Briefing for local VAMCs\nSubsection (h) of such section is amended by adding at the end the following new paragraph:\n(5) Briefing for local VAMCs Not less frequently than once per calendar quarter, the Secretary shall provide, to the appropriate personnel of each medical center of the Department located not more than 100 miles from the primary location of a recipient of a grant under this section, a briefing about the grant program under this section in order to improve coordination between such recipient and personnel. .\n##### (f) Duration\nSubsection (j) of such section is amended by striking the date that is three years after the date on which the first grant is awarded under this section and inserting September 30, 2030 .\n##### (g) Interim report\nSubsection (k)(1)(B) of such section is amended by adding at the end the following new clause:\n(xiii) A description of the Secretary's compliance with the requirement to train employees of the Department under subsection (g)(3). .\n##### (h) Emergent suicide care\nSubsection (n) of such section is amended\u2014\n**(1)**\nby striking When the Secretary and inserting the following:\n(1) In general When the Secretary ; and\n**(2)**\nby adding at the end the following new paragraph:\n(2) Emergent suicide care If the Secretary does not provide mental health or behavioral health care services under paragraph (1) to an eligible individual during the 72-hour period following a referral under subsection (m), such eligible individual shall be treated as eligible for emergent suicide care under section 1720J of title 38, United States Code. .\n##### (i) Reauthorization\nSubsection (p) of such section is amended by striking 2025 and inserting 2030 .\n##### (j) Technical correction to definitions\nSubsection (q)(5) of such section is amended, in the first sentence\u2014\n**(1)**\nby striking Medical services and inserting The term emergency treatment means medical services ; and\n**(2)**\nby striking was rendered and inserting rendered .\n##### (k) Definition of risk of suicide\nSubsection (q)(8)(A) of such section is amended by striking any of the following (to a degree determined by the Secretary pursuant to regulations) and inserting any of the following health, environmental, or historical risk factors (to any degree) .\n##### (l) Suicide prevention services\n**(1) Required use of certain screening protocol**\nSubsection (q)(11)(A)(ii) of such section is amended by adding at the end the following new sentence: In the case of a recipient of a grant awarded under this section on or after the date of the enactment of the Helping Optimize Prevention and Engagement for Heroes Act of 2025 , such screening shall be the Columbia Protocol (also known as the Columbia-Suicide Severity Rating Scale (C\u2013SSRS)). .\n**(2) Transportation**\nSubsection (q)(11)(A) of such section is amended\u2014\n**(A)**\nby redesignating clause (xi) as clause (xii); and\n**(B)**\nby inserting after clause (x) the following new clause:\n(xi) Transportation and rideshare services for eligible individuals to use for appointments. .",
      "versionDate": "2025-03-26",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Employment and training programs",
            "updateDate": "2025-08-07T17:54:45Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-08-07T17:54:39Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-08-07T17:54:54Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-08-07T17:54:28Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-08-07T17:54:49Z"
          },
          {
            "name": "Transportation costs",
            "updateDate": "2025-08-07T17:54:59Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-08-07T17:54:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T13:59:25Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1139is.xml"
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
      "title": "HOPE for Heroes Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HOPE for Heroes Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Helping Optimize Prevention and Engagement for Heroes Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Commander John Scott Hannon Veterans Mental Health Care Improvement Act of 2019 to modify and reauthorize the Staff Sergeant Parker Gordon Fox Suicide Prevention Grant Program of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:48:34Z"
    }
  ]
}
```
