# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6733?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6733
- Title: VISN Reform Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6733
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-05-21T08:07:41Z
- Update date including text: 2026-05-21T08:07:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-05-20 - Committee: Committee Hearings Held
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-05-20 - Committee: Committee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6733",
    "number": "6733",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001295",
        "district": "12",
        "firstName": "Mike",
        "fullName": "Rep. Bost, Mike [R-IL-12]",
        "lastName": "Bost",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "VISN Reform Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:41Z",
    "updateDateIncludingText": "2026-05-21T08:07:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
        "item": [
          {
            "date": "2026-05-20T13:24:47Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-18T16:44:03Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-12-16T15:00:50Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6733ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6733\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mr. Bost introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to make certain improvements to the administration of Veterans Integrated Service Networks under laws administered by the Secretary of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the VISN Reform Act of 2025 .\n#### 2. Administration of Veterans Integrated Service Networks\n##### (a) Veterans integrated service networks\nSubchapter I of chapter 73 of title 38, United States Code, is amended by inserting after section 7305 following new section:\n7305A. Veterans Integrated Service Networks (a) Organization The Secretary shall organize the Veterans Health Administration in eight geographically defined Veterans Integrated Service Networks (hereinafter referred to as VISNs ). (b) Alignment with mission of department The Secretary shall ensure that the employees, services, and programs of each VISN are aligned with the mission of the Department and the specific health care requirements of each population of veterans in each Network. (c) Integrated health care system The Secretary shall maintain a regional integrated health care system within the geographic area served by each VISN by\u2014 (1) entering into agreements with such other governmental, public, and private health care organizations and practitioners as the Secretary considers appropriate to meet the needs of veterans who reside in the geographic area served by the VISN; (2) providing oversight and management of, and taking responsibility for, a regional budget for the activities of each VISN that\u2014 (A) is aligned with the budget guidelines of the Department and the Veterans Health Administration; and (B) is balanced at the end of each fiscal year; and (3) using national metrics to develop systems to provide effective, efficient, and safe delivery of health care that is rated as highly satisfactory by patients and families of patients. (d) Reduction in duplicate functions The Secretary shall identify functions that are duplicated across the clinical, administrative, and operational processes and practices of the Veterans Health Administration and operate the system of VISNs in a manner designed to reduce the duplication of such functions. (e) Collaboration and cooperation (1) The Secretary shall operate the VISN system by working to achieve maximum effectiveness with respect to the provision hospital care, medical services, and nursing home care, graduate medical education, and research; and (2) The Secretary shall assess, on an ongoing basis, the consolidation or realignment of institutional functions, including capital asset, safety, and operational support functions, in collaboration and cooperation with other VISNs and the following offices or entities within the geographic area served by the VISN: (A) The offices of the Veterans Benefits Administration and the National Cemetery Administration. (B) Offices of State and local agencies that have a mission to provide assistance to veterans. (C) Medical schools and other affiliates. (D) Federal, State, and local emergency preparedness organizations. (E) Such other offices of the Federal Government as the Secretary considers appropriate. (3) The Director of each VISN shall be responsible for oversight and for the enforcement of Department policies authorities applicable to medical facilities of the Department with respect to such medical facilities located in the geographic area served by such VISN. (f) Headquarters (1) There shall be only one headquarters office for each VISN. The Secretary shall choose the location of each such office and shall ensure each such office is colocated with a medical center of the Department. (2) (A) Each headquarters office established under paragraph (1) shall have not more than 50 full-time employees. Of such 50 full-time employees, not more than 10 shall be contractor employees. (B) (i) The Secretary may waive the limitation under subparagraph (A) with respect to a VISN headquarters if the Secretary\u2014 (I) determines the waiver is necessary to maintain essential operations of the VISN headquarters during the implementation of the plan required under paragraph (3); and (II) before the date on which the waiver becomes effective, submits to the Committees on Veterans\u2019 Affairs of the Senate and the House of Representatives a written certification of such determination. (ii) The term of any wavier issued pursuant to clause (i) may not exceed one year. (C) Not less frequently than once each fiscal year, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and the House of Representatives a report on employment at the VISN headquarters offices during the preceding fiscal year. Each such report shall include the following for the year covered by the report: (i) The number of individuals employed at each VISN headquarters office. (ii) The number of individuals employed by the Veterans Health Administration in each VISN who are not employed at the same location as the headquarters office of that VISN. (iii) The title for each position of employment at a headquarters office. (iv) The title for each position of employment with the Veterans Health Administration in each VISN whose duty station is not at the same location as the headquarters office of that VISN. (v) An assessment of the effect of the employment of individuals at VISN headquarters offices on the budget of the Department. (3) (A) Not later than 180 days after the date of the enactment of this section, the Secretary shall develop and submit to the Committees on Veterans\u2019 Affairs of the Senate and the House of Representatives a comprehensive plan for the reorganization and right-sizing of the workforce of each VISN headquarters to achieve compliance with the limitation under paragraph (2)(A). (B) The plan under subparagraph (A) shall include, for each VISN headquarters\u2014 (i) an identification of all positions currently assigned to the headquarters, including duty location, occupational services, pay grade, and primary function; (ii) a determination of which positions\u2014 (I) are essential to execute the mission of the VISN; and (II) are duplicative or administrative in nature; (iii) a phased implementation schedule for such plan; (iv) a description of any workforce realignments, reassignments, or separations required to comply with the limitation under paragraph (2)(A), including voluntary separation incentive payments or retraining opportunities under title 5; and (v) a certification that the implementation of such plan will not result in a reduction in access to care or services furnished to veterans under the laws administered by the Secretary. (C) In developing and implementing the plan required under this subsection, the Secretary shall\u2014 (i) ensure that each VISN headquarters is in compliance with the limitation under paragraph (2)(A) not later than the date that is three years after the date of the enactment of this section; and (ii) to the maximum extent practicable, offer each employee of a VISN headquarters who is a licensed physician, nurse, psychologist, or other healthcare professional such the opportunity to transfer, without loss of pay or benefits, to a position appointed under chapter 74 of this title to furnish direct patient care or clinical support at a Department medical facility. (g) Personnel (1) The head of each VISN shall be the Director, who shall be appointed by the President, by and with the advice and consent of the Senate. The position of Director of a VISN shall be a noncareer appointee position. The Director of a VISN shall\u2014 (A) be responsible for the functions of the VISN; and (B) have the authority and responsibility to enforce the policies and standards of the Department with respect to all Department personnel employed within the VISN. (2) Each employee employed at a facility of the Veterans Health Administration located in the geographic area served by a VISN shall\u2014 (A) report directly to the Director of the VISN; (B) in the case of an employee who is licensed to practice in a hospital, work at least one day each week in a Department medical center located in such geographic area; and (C) visit routinely with service line chiefs at Department medical centers, as directed by the Secretary. (h) Triennial structure review, reassessment and report (1) Not later than three years after the date of the enactment of this section, and not less frequently than once every three years thereafter, the Secretary shall conduct a review and assessment of the structure and operations of the VISNs. (2) Not later than 180 days after conducting a review and assessment under paragraph (1), the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and the House of Representatives a report on such review and assessment, which shall include such recommendations for legislative or regulatory action as the Secretary considers appropriate to improve the VISNs. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 73 of such title is amended by inserting after the item relating to section 7305 the following new item:\n7305A. Veterans Integrated Service Networks .\n#### 3. Consolidation of Veterans Integrated Service Networks\nIn order to comply with section 7305A of title 38, United States Code, as added by section 2, not later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall geographically realign and combine the Veterans Integrated Service Networks in effect on the day before the date of enactment of this Act into geographically defined Veterans Integrated Service Networks as follows:\n**(1)**\nVeterans Integrated Service Network 1, Veterans Integrated Service Network 2, and Veterans Integrated Service Network 4 shall be Combined into a single Veterans Integrated Service Network.\n**(2)**\nVeterans Integrated Service Network 5, Veterans Integrated Service Network 6, and Veterans Integrated Service Network 9 shall be combined into a single Veterans Integrated Service Network.\n**(3)**\nVeterans Integrated Service Network 10, Veterans Integrated Service Network 12, and Veteran Integrated Service Network 23 shall be combined into a single Veterans Integrated Service Network.\n**(4)**\nVeterans Integrated Service Network 7, Veterans Integrated Service Network 8, and Veteran Integrated Service Network 16 shall be combined into a single Veterans Integrated Service Network.\n**(5)**\nVeterans Integrated Service Network 15 and Veteran Integrated Service Network 19 shall be combined into a single Veterans Integrated Service Network.\n**(6)**\nVeterans Integrated Service Network 17 and Veteran Integrated Service Network 22 shall be combined into a single Veterans Integrated Service Network.\n**(7)**\nVeterans Integrated Service Network 20 shall remain a single Veterans Integrated Service Network.\n**(8)**\nVeterans Integrated Service Network 21 shall remain a single Veterans Integrated Service Network.",
      "versionDate": "2025-12-16",
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
        "updateDate": "2026-01-08T16:56:49Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6733ih.xml"
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
      "title": "VISN Reform Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-08T06:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VISN Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-08T06:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to make certain improvements to the administration of Veterans Integrated Service Networks under laws administered by the Secretary of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-08T06:03:19Z"
    }
  ]
}
```
