# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2101?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2101
- Title: Duplicative Grant Consolidation Act
- Congress: 119
- Bill type: HR
- Bill number: 2101
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2025-04-04T13:32:36Z
- Update date including text: 2025-04-04T13:32:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2101",
    "number": "2101",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Duplicative Grant Consolidation Act",
    "type": "HR",
    "updateDate": "2025-04-04T13:32:36Z",
    "updateDateIncludingText": "2025-04-04T13:32:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:05:25Z",
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
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2101ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2101\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mrs. Bice (for herself and Mr. Self ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit the award of Federal grants to applicants submitting duplicative or fraudulent applications, to require the Director of Office of Management and Budget to establish a tracking and deconfliction system for Federal grant applications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Duplicative Grant Consolidation Act .\n#### 2. Prohibition on award of Federal grants to applicants submitting duplicative or fraudulent applications\n##### (a) No award on basis of duplicative application\n**(1) Prohibition**\n**(A) In general**\nExcept as provided for under subparagraph (B), the head of an executive agency may not award a grant to an applicant determined by the head of the agency or the Inspector General of the agency to have received another grant from the head of another executive agency for the same or identical purpose.\n**(B) Exception**\nThe prohibition under subparagraph (A) related to the award of grants for the same or identical purposes shall not apply to an applicant that is an institution of higher education.\n**(2) Determination**\nIn the case that the head of an executive agency or the Inspector General of the agency determines that an applicant for a grant has submitted an application for another grant from another executive agency for the same or identical purpose, the heads of such agencies shall jointly determine which agency is the appropriate agency to award the grant, if such grant is to be awarded to such applicant.\n##### (b) No award on basis of fraudulent application\nThe head of an executive agency may not award a grant to an applicant determined by the head of the agency or the Inspector General of the agency to have submitted a fraudulent application for such grant.\n#### 3. Tracking and deconfliction system for Federal grant applications\n##### (a) Establishment\nNot later than 1 year after the date of the enactment of this Act, the Director of the Office of Management and Budget shall make available to the heads of executive agencies, including the Inspectors General of such agencies, an electronic system through which the head of an executive agency may determine before awarding a grant, or through which an Inspector General of an executive agency may determine in conducting an audit or investigation, whether any applicant for such grant has received, or submitted an application to the head of another executive agency for, another grant for the same or identical purpose.\n##### (b) Contents of system\nThe system shall contain at a minimum, the name of the awardee, the principal investigator, the award period, agency point of contact, and an abstract.\n##### (c) Essentially equivalent work\nThe Director of the Office of Management and Budget shall establish an electronic system which contains information for all federal research awards through which the head of an executive agency may determine before awarding a grant, or through which an Inspector General of an executive agency may determine in conducting an audit or investigation, whether\u2014\n**(1)**\nsubstantially the same research is proposed for funding in more than one grant application submitted to the same Federal agency;\n**(2)**\nsubstantially the same research is submitted to two or more different Federal agencies for review and funding consideration; or\n**(3)**\na specific research objective and the research design for accomplishing an objective are the same or closely related in two or more proposals or awards, regardless of the funding source.\n#### 4. Report on feasibility of leveraging artificial intelligence to identify duplicative Federal grant applications\nThe Director of the Office of Management and Budget, in consultation with the Secretary of Energy, the Director of the National Science Foundation, and the Director of the National Institute of Standards and Technology, shall submit to the appropriate Congressional committees a report on the feasibility of leveraging artificial intelligence to rapidly identify, with respect to an application for a grant submitted to the head of an executive agency\u2014\n**(1)**\nwhether an applicant for such grant has received, or submitted an application to the head of another executive agency for, another grant for the same or identical purpose; and\n**(2)**\nwaste, fraud, and abuse.\n#### 5. Definitions\nIn this Act:\n**(1) Applicable time period**\nThe term applicable time period means\u2014\n**(A)**\nwith respect to a covered application for a grant awarded after the date on which system is established under section 2(a), during the period\u2014\n**(i)**\nbeginning on the date on which such application is submitted; and\n**(ii)**\nending on the date on which amounts under the grant are no longer being expended; and\n**(B)**\nwith respect to a covered application for a grant awarded before the date on which the system is established under section 2(a), during the period\u2014\n**(i)**\nbeginning on that date; and\n**(ii)**\nending on the date on which amounts under the grant are no longer being expended.\n**(2) Appropriate Congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Oversight and Accountability and the Committee on Appropriations of the House of Representatives; and\n**(B)**\nthe Committee on Homeland Security and Governmental Affairs and the Committee on Appropriations of the Senate.\n**(3) Covered application**\nThe term covered application means an application for a grant submitted to the head of an executive agency\u2014\n**(A)**\nafter the date on which the system is established under section 2(a); and\n**(B)**\nbefore that date, if amounts under the grant are still being expended on such date.\n**(4) Executive agency**\nThe term executive agency means an agency in the executive branch of the Federal Government.\n**(5) Institution of higher education**\nThe term institution of higher education has the meaning given such term in section 102 of the Higher Education Act of 1965 (20 U.S.C.1002).",
      "versionDate": "2025-03-14",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-04-04T13:32:36Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2101ih.xml"
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
      "title": "Duplicative Grant Consolidation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Duplicative Grant Consolidation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the award of Federal grants to applicants submitting duplicative or fraudulent applications, to require the Director of Office of Management and Budget to establish a tracking and deconfliction system for Federal grant applications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:33:46Z"
    }
  ]
}
```
