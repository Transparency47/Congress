# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6814?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6814
- Title: Veterans’ Burial Improvement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6814
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-03-07T09:06:41Z
- Update date including text: 2026-03-07T09:06:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-22 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-22 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6814",
    "number": "6814",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000614",
        "district": "1",
        "firstName": "Chris",
        "fullName": "Rep. Pappas, Chris [D-NH-1]",
        "lastName": "Pappas",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Veterans\u2019 Burial Improvement Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-07T09:06:41Z",
    "updateDateIncludingText": "2026-03-07T09:06:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
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
          "date": "2025-12-17T14:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-22T15:19:23Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
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
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6814ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6814\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Mr. Pappas (for himself and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to make certain improvements in the laws administered by the Secretary of Veterans Affairs relating to memorial affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans\u2019 Burial Improvement Act of 2025 .\n#### 2. Permanent authority for certain burial benefits for spouses and children who predecease members of the Armed Forces serving on active duty\n##### (a) Provision of headstones and markers\nSection 2306(b)(2) of title 38, United States Code, is amended\u2014\n**(1)**\nin subparagraph (B), by striking if such death occurs before September 30, 2032 ; and\n**(2)**\nin subparagraph (C), by striking if such death occurs before September 30, 2032 .\n##### (b) Interment in national cemeteries\nSection 2402(a)(5) of title 38, United States Code, is amended by striking if such death occurs before September 30, 2032 .\n#### 3. Department of Veterans Affairs provision of transportation for deceased veterans\n##### (a) Transportation of deceased veterans\n**(1) In general**\nSection 2308 of title 38, United States Code, is amended to read as follows:\n2308. Transportation of deceased veterans for burial (a) In general The Secretary may pay, in addition to any amount paid under this chapter, the cost of transportation of a deceased veteran for burial in accordance with this section. (b) Transportation allowance (1) In the case of the transportation of a covered deceased veteran for burial in a covered veterans\u2019 cemetery, the Secretary may pay a transportation allowance of $745 (as increased from time to time under paragraph (3)). (2) In the case of a covered deceased veteran who did not die in a State and for whom the actual cost of transporting the veteran from the place of death to the covered cemetery exceeds the amount of the transportation allowance in effect under paragraph (1), the Secretary may also pay an additional amount equal to the difference between such transportation allowance and the actual cost of transporting the veteran. The amount of any payment under this paragraph may not exceed the difference between such transportation allowance and the actual cost of transporting the veteran to the national cemetery nearest the veteran\u2019s last place of residence in which burial space is available. (3) With respect to any fiscal year, the Secretary shall provide a percentage increase (rounded to the nearest dollar) in the amount of the transportation allowance payable under paragraph (1) that is equal to the percentage by which\u2014 (A) the Consumer Price Index (all items, United States city average) for the 12-month period ending on the June 30 preceding the beginning of the fiscal year for which the increase is made, exceeds (B) such Consumer Price Index for the 12-month period preceding the 12-month period described in subparagraph (A). (c) Deaths in covered facilities (1) Except as provided in paragraph (2), in the case of a veteran who dies in a covered facility located in a State, the Secretary shall pay the actual cost to transport the body to the place of burial, if the place of burial is located in the same or any other State. (2) In the case of a veteran who is eligible for payment under both paragraph (1) and subsection (b), the amount payable under paragraph (1) may not exceed the difference between the amount of the transportation allowance in effect under subsection (b)(1) and the actual cost of transporting the veteran to the place of burial. (d) Definitions In this section: (1) The term covered deceased veteran means any of the following deceased veterans: (A) A veteran who dies as the result of a service-connected disability. (B) A veteran who dies while in receipt of disability compensation (or who but for the receipt of retirement pay or pension under this title, would have been entitled to compensation). (C) A veteran whom the Secretary determines is eligible for funeral expenses under this chapter by virtue of the Secretary determining that the veteran has no next of kin or other person claiming the body of such veteran and that there are not available sufficient resources to cover burial and funeral expenses for the veteran. (2) The term covered facility means\u2014 (A) a facility of the Department (as defined in section 1701(3) of this title) to which the deceased veteran was properly admitted for hospital, nursing home, or domiciliary care under section 1710 or 1711(a) of this title; or (B) an institution at which the deceased veteran was, at the time of death, receiving\u2014 (i) hospital care in accordance with sections 1703A, 8111, and 8153 of this title; (ii) nursing home care under section 1720 of this title; or (iii) nursing home care for which payments are made under section 1741 of this title. (3) The term covered veterans\u2019 cemetery means a veterans' cemetery\u2014 (A) in which a covered veteran is eligible to be buried; and (B) that\u2014 (i) in the case of deaths occurring before January 5, 2024\u2014 (I) is owned by a State; or (II) is on trust land owned by, or held in trust for, a tribal organization; or (ii) in the case of deaths occurring on or after January 5, 2024\u2014 (I) is a national cemetery; (II) is owned by a State; or (III) is on trust land owned by, or held in trust for, a tribal organization. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of chapter 23 of such title is amended by striking the item relating to section 2308 and inserting the following new item:\n2308. Transportation of deceased veterans for burial. .\n##### (b) Conforming amendments\nSuch title is further amended\u2014\n**(1)**\nby striking paragraph (1) of section 2303(a) and inserting the following new paragraph (1):\n(1) When a veteran described in paragraph (2) dies, the Secretary shall pay the actual cost (not to exceed $700 (as increased from time to time under subsection (c))) of the burial and funeral or, within such limits, may make contracts for such services without regard to the laws requiring advertisement for proposals for supplies and services for the Department. ; and\n**(2)**\nin section 101(20), by striking section 2303 and inserting sections 2303 and 2308 .\n#### 4. Provision of group burial markers\n##### (a) In general\nSection 2306 of title 38, United States Code, is further amended\u2014\n**(1)**\nby redesignating subsection (k) as subsection (l); and\n**(2)**\nby inserting after subsection (j) the following new subsection (k):\n(k) (1) Under such regulations as the Secretary may prescribe, in lieu of a headstone or marker for an individual described in paragraph (1), (2), or (3) of subsection (a), the Secretary may furnish a group headstone or marker at a burial location containing the remains of multiple such individuals. (2) If the Secretary furnishes a group headstone or marker under paragraph (1) for a group of individuals described in paragraph (1), (2), or (3) of subsection (a) at a burial location containing the remains of multiple such individuals, the Secretary may not furnish a new or replacement burial or memorial headstone or marker for any individual whose remains are determined to be interred at that burial location. (3) In the case of an individual who is interred at a burial location marked by a group headstone or marker under paragraph (1), but for whom the Secretary provided an individual headstone or marker before the date of the enactment of this subsection, such individual headstone or marker may remain in place after the placement of the group headstone or marker. (4) The Secretary may provide a group headstone or marker under paragraph (1) at a burial location that is not unmarked, if the Secretary determines that a group headstone or marker at that burial location would assist visitors in understanding or appreciating the significance of the burial location. (5) Any group headstone or marker provided under this subsection shall be provided in coordination with, and with the approval of, the owner of the property on which the burial location is located. (6) Subject to any required consultation with, and approval by, an appropriate historical preservation authority, the Secretary shall make all determinations regarding the appearance of a group headstone or marker provided under paragraph (1), including the size of, the material used for, and the content of the inscription on the marker. (7) A group headstone or marker furnished under paragraph (1) may not include in the inscription the name of a person described in section 2411(b) of this title. .\n##### (b) Noneligibility of parents of certain deceased veterans\nSubsection (a)(2) of such section is amended by striking and (6) and inserting (6), and (9) .\n#### 5. Burial or interment of certain additional person in cemeteries that accept Department of Veterans Affairs plot or interment allowance\nSection 2303(b)(1) of title 38, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (ii), by striking or at the end;\n**(B)**\nin clause (iii), by striking and and inserting or ; and\n**(C)**\nby adding at the end the following new clause:\n(iv) veterans who were discharged or released from service under conditions other than dishonorable and who would be eligible for burial in a national cemetery but for the minimum active duty service requirements under section 5303A of this title and the spouses and dependent children of such veterans; and ; and\n**(2)**\nin subparagraph (B)(ii), by striking the period and inserting ; and .",
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
        "updateDate": "2026-01-21T16:08:15Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6814ih.xml"
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
      "title": "Veterans\u2019 Burial Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans\u2019 Burial Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to make certain improvements in the laws administered by the Secretary of Veterans Affairs relating to memorial affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:35Z"
    }
  ]
}
```
