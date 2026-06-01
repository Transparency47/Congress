# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6794?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6794
- Title: VA Medical Center Facility Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 6794
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-03-07T09:06:39Z
- Update date including text: 2026-03-07T09:06:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-23 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-23 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6794",
    "number": "6794",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001098",
        "district": "8",
        "firstName": "Abraham",
        "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
        "lastName": "Hamadeh",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "VA Medical Center Facility Transparency Act",
    "type": "HR",
    "updateDate": "2026-03-07T09:06:39Z",
    "updateDateIncludingText": "2026-03-07T09:06:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-23",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-23T15:17:55Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6794ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6794\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Mr. Hamadeh of Arizona (for himself and Ms. Lee of Nevada ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo require directors of medical centers of the Department of Veterans Affairs to submit annual fact sheets to the Secretary of Veterans Affairs on the status of such facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the VA Medical Center Facility Transparency Act .\n#### 2. Requirement for timely scheduling of appointments at medical facilities of Department of Veterans Affairs\n##### (a) Requirement\nChapter 17 of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating section 1706A as section 1706B; and\n**(2)**\nby inserting after section 1706 the following new section:\n1706A. Management of health care: timely scheduling of appointments at Department facilities (a) Requirement for scheduling In managing the provision of hospital care and medical services at medical facilities of the Department of Veterans Affairs under this chapter, the Secretary shall ensure that whenever a covered veteran contacts the Department by telephone to request the scheduling of an appointment for care or services for the covered veteran at such a facility, the scheduling for the appointment occurs during that telephone call (regardless of the prospective date of the appointment being scheduled). (b) Covered veteran defined In this section, the term covered veteran means a veteran who is enrolled in the system of patient enrollment of the Department under section 1705(a) of this title. (c) Sunset This section shall terminate on the date that is three years after the date of the enactment of the VA Medical Center Facility Transparency Act. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by striking the item relating to section 1706A and inserting the following new items:\n1706A. Management of health care: timely scheduling of appointments at Department facilities. 1706B. Remediation of medical service lines. .\n##### (c) Applicability\nThe amendments made by subsection (a) shall apply with respect to requests for appointment scheduling occurring on or after the date that is 180 days after the date of the enactment of this Act.\n#### 3. Information on medical facilities of the Department of Veterans Affairs\n##### (a) Fact sheets\nThe Secretary of Veterans Affairs shall ensure that each director of a medical center of the Department of Veterans Affairs submits to the Secretary, the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate, and the appropriate Members of Congress the following:\n**(1)**\nAn annual concise, easy-to-read fact sheet containing, with respect to the year covered by the fact sheet each of the following:\n**(A)**\nStatistics regarding\u2014\n**(i)**\nthe number of veterans who were treated at a medical facility of the Department under the jurisdiction of the director;\n**(ii)**\nthe number of appointments conducted by each such facility;\n**(iii)**\nthe most common illnesses or conditions for which treatment was furnished;\n**(iv)**\nthe satisfaction of veterans who were treated at each such facility;\n**(v)**\nhow each such facility compares with other facilities with respect to the satisfaction of veterans who were treated at the facilities; and\n**(vi)**\nother matters the director determines appropriate.\n**(B)**\nA description of any successes or achievements experienced by such facilities, including\u2014\n**(i)**\nactions taken to improve such facilities;\n**(ii)**\nactions taken to improve the access to and quality of the care provided at such facilities; and\n**(iii)**\nany other accomplishments determined appropriate by the director.\n**(C)**\nA description of special areas of emphasis or specialization by such facilities, such as efforts aimed at meeting the needs of women veterans, suicide prevention and other mental health initiatives, opioid abuse prevention and pain management, or special efforts on veteran homelessness, or other matters as the director determines appropriate.\n**(D)**\nA description of matters concerning such facilities that have previously been identified as deficient and needing remediation that are still in need of such remediation.\n**(2)**\nA quarterly fact sheet containing, with respect to the quarter covered by the fact sheet, the average wait time for veterans to receive treatment at the medical facility of the Department under the jurisdiction of the director.\n##### (b) Availability\nEach fact sheet under subsection (a) shall be made publicly available\u2014\n**(1)**\nin a physical form at the relevant medical facility of the Department in a conspicuous location; and\n**(2)**\nin an electronic form on the internet website of the facility.\n##### (c) Timing of fact sheets\nThe fact sheets under subsection (a) shall be submitted during the first fiscal year beginning after the date that is 180 days after the date of the enactment of this Act and not less frequently than\u2014\n**(1)**\nonce each fiscal year thereafter with respect to the annual fact sheet under paragraph (1) of such subsection; and\n**(2)**\nonce each fiscal quarter thereafter with respect to the quarterly fact sheet under paragraph (2) of such subsection.\n##### (d) Standardized format\nThe Secretary shall establish a standard format for the fact sheets under subsection (a) to ensure that each director of a medical center of the Department carries out such subsection in a consistent manner.\n##### (e) Definitions\nIn this section:\n**(1)**\nThe term appropriate Members of Congress means, with respect to a medical facility of the Department of Veterans Affairs about which a fact sheet is submitted under subsection (a), the Senators representing the State, and the Member, Delegate, or Resident Commissioner of the House of Representatives representing the district, that includes the facility.\n**(2)**\nThe term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, and any territory or possession of the United States.\n#### 4. Limitation on detail of directors of medical centers of Department of Veterans Affairs to different positions\n##### (a) Notification\n**(1) In general**\nNot later than 90 days after detailing a director of a medical center of the Department of Veterans Affairs to a different position within the Department, the Secretary of Veterans Affairs shall notify the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives of such detail.\n**(2) Matters To be included**\nThe notification required by paragraph (1) shall include, with respect to a director of a medical center who is detailed to a different position within the Department, the following information:\n**(A)**\nThe location at which the director is detailed.\n**(B)**\nThe position title of the detail.\n**(C)**\nThe estimated time the director is expected to be absent from their duties at the medical center.\n**(D)**\nSuch other information as the Secretary may determine appropriate.\n##### (b) Appointment of acting director\nNot later than 120 days after detailing a director of a medical center of the Department to a different position within the Department, the Secretary shall appoint an individual as acting director of such medical center with all of the authority and responsibilities of the detailed director.\n##### (c) Update on detail\nNot later than 120 days after detailing a director of a medical center of the Department to a different position within the Department, and not less frequently than every 30 days thereafter while the detail is in effect or while the director position at the medical center is vacant, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives an update regarding the status of the detail.\n##### (d) Return to position or reassignment\n**(1) In general**\nExcept as provided in paragraph (2), not later than 180 days after detailing a director of a medical center of the Department to a different position within the Department, for a reason other than an ongoing investigation or administrative action with respect to the director, the Secretary shall\u2014\n**(A)**\nreturn the individual to the position as director of the medical center; or\n**(B)**\nreassign the individual from the position as director of the medical center and begin the process of hiring a new director for such position.\n**(2) Waiver**\n**(A) In general**\nThe Secretary may waive the requirement under paragraph (1) with respect to an individual for successive 90-day increments for a total period of not more than 540 days from the original date the individual was detailed away from their position as director of a medical center.\n**(B) Notification**\nNot later than 30 days after exercising a waiver under subparagraph (A), the Secretary shall notify Congress of the waiver and provide to Congress information as to why the waiver is necessary.\n#### 5. Sunset\nThe requirements of this Act shall terminate on the date that is three years after the date of the enactment of this Act.",
      "versionDate": "2025-12-17",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-22T20:38:42Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6794ih.xml"
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
      "title": "VA Medical Center Facility Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA Medical Center Facility Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require directors of medical centers of the Department of Veterans Affairs to submit annual fact sheets to the Secretary of Veterans Affairs on the status of such facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:26Z"
    }
  ]
}
```
