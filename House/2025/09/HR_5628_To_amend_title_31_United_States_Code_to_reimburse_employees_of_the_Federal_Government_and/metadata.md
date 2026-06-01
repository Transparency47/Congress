# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5628?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5628
- Title: Pay Workers What They’ve Earned Act
- Congress: 119
- Bill type: HR
- Bill number: 5628
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2025-10-15T08:05:26Z
- Update date including text: 2025-10-15T08:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5628",
    "number": "5628",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "H001066",
        "district": "4",
        "firstName": "Steven",
        "fullName": "Rep. Horsford, Steven [D-NV-4]",
        "lastName": "Horsford",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Pay Workers What They\u2019ve Earned Act",
    "type": "HR",
    "updateDate": "2025-10-15T08:05:26Z",
    "updateDateIncludingText": "2025-10-15T08:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
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
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:06:45Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "DC"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "AZ"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CT"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NJ"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "LA"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "MO"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "VI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5628ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5628\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Horsford (for himself, Ms. Norton , and Ms. Ansari ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 31, United States Code, to reimburse employees of the Federal Government and the District of Columbia, Federal contractors, and the States for certain costs incurred as a result of a Government shutdown, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pay Workers What They\u2019ve Earned Act .\n#### 2. Reimbursement for individuals affected by Government shutdowns\nSection 1341 of title 31, United States Code, is amended by adding at the end the following:\n(d) (1) In this subsection\u2014 (A) the term covered employee means\u2014 (i) any employee of the United States Government or of a District of Columbia public employer furloughed as a result of a lapse in appropriations; (ii) any excepted employee who is required to perform work during such lapse; and (iii) any contractor with the Federal Government (or an employee of such contractor) placed on unpaid leave as a result of such lapse; (B) the term shutdown cost means any cost incurred by a covered employee as a direct result of a lapse in appropriations, including expenses for loans and credit cards, and any fees, fine, or interest resulting from the employees inability to make payments as a direct result of a loss in salary due to such lapse; (C) the terms District of Columbia public employer , employee , and excepted employee have the meaning given those terms in subsection (c); and (D) the term State means any of the 50 States, the District of Columbia, the Commonwealth of Puerto Rico, Guam, the Virgin Islands, American Samoa, the Commonwealth of the Northern Mariana Islands, and any territory or possession of the United States, and includes Indian Tribes. (2) (A) With respect to the lapse in appropriations beginning on or about October 1, 2025, each covered employee shall be paid for any shutdown cost at the earliest date possible after the date of enactment of this subsection, and subject to the enactment of appropriations Acts ending the lapse. (B) With respect to any other lapse in appropriations of a duration of 14 days or longer occurring after the lapse in appropriations described in subparagraph (A), any covered employee shall, subject to the availability of appropriations, be paid for any shutdown cost at the earliest date possible after the lapse in appropriations ends. (3) (A) Any State that makes an expenditure of State funds for payments for assistance programs that would be, but for a lapse in appropriations of a duration of 14 days or longer (including the lapse described in subparagraph (A)), provided by the Federal Government shall be reimbursed for such payments not later than 90 days after the lapse in appropriations ends. (B) This paragraph shall not apply to any State expenditure with respect to which reimbursement is provided by the Federal Government under any other provision of law, including unemployment compensation. (4) (A) In order to receive reimbursement under paragraph (2) or (3), a covered employee or State (as the case may be) shall submit an application to the Secretary of the Treasury, in such form and manner as the Secretary deems appropriate, not later than 1 year after the applicable lapse in appropriations ends. (B) The Secretary shall determine what documentation shall be included with such an application to verify the shutdown costs or expenditure submitted by a covered employee or a State, respectively. (C) Upon approval by the Secretary, reimbursement shall be provided to the covered employee or State, consistent with the requirements of this subsection. (5) (A) There is established in the general fund of the Treasury a fund, to be known as the Reserve Fund for Employees Affected By Government Shutdowns (in this paragraph referred to as the Fund ), which shall consist of amounts appropriated into the Fund after the date of enactment of this subsection. (B) Subject to the availability of appropriations, amounts in the Fund shall be available for purposes of paying the shutdown costs of any covered employee during a lapse in appropriations beginning after the lapse referred to in paragraph (2)(A). .",
      "versionDate": "2025-09-30",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-10-06T16:34:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-30",
    "originChamber": "House",
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
          "measure-id": "id119hr5628",
          "measure-number": "5628",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-30",
          "originChamber": "HOUSE",
          "update-date": "2025-10-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5628v00",
            "update-date": "2025-10-08"
          },
          "action-date": "2025-09-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Pay Workers What They\u2019ve Earned Act</strong></p><p>This bill requires the federal government to reimburse states and employees of the federal government, the District of Columbia government, or federal contractors for certain costs incurred as a result of a lapse in appropriations (i.e., a government shutdown).\u00a0</p><p>Employee costs that must be reimbursed include costs incurred by an employee as a direct result of a lapse in appropriations, including expenses for loans and credit cards, and any fees, fines, or interest resulting from the employee's inability to make payments as a direct result of a loss in salary due to the lapse in appropriations.\u00a0</p><p>With respect to a lapse in appropriations that begins on or about October 1, 2025, employees must be reimbursed for any shutdown costs on the earliest date possible after the enactment of this bill (subject to the enactment of an appropriations act ending the lapse). For subsequent lapses in appropriations, the bill requires that each employee be reimbursed for any shutdown costs on the earliest date possible after the end of a lapse in appropriations that lasts at least 14 days.</p><p>States must be reimbursed for payments for assistance programs that would otherwise be provided by the federal government but\u00a0for a lapse in appropriations that lasts at least 14 days. The states must be reimbursed no later than 90 days after the end of the lapse in appropriations.\u00a0</p><p>The reimbursements required by this bill are subject to the availability of appropriations.\u00a0</p>"
        },
        "title": "Pay Workers What They\u2019ve Earned Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5628.xml",
    "summary": {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pay Workers What They\u2019ve Earned Act</strong></p><p>This bill requires the federal government to reimburse states and employees of the federal government, the District of Columbia government, or federal contractors for certain costs incurred as a result of a lapse in appropriations (i.e., a government shutdown).\u00a0</p><p>Employee costs that must be reimbursed include costs incurred by an employee as a direct result of a lapse in appropriations, including expenses for loans and credit cards, and any fees, fines, or interest resulting from the employee's inability to make payments as a direct result of a loss in salary due to the lapse in appropriations.\u00a0</p><p>With respect to a lapse in appropriations that begins on or about October 1, 2025, employees must be reimbursed for any shutdown costs on the earliest date possible after the enactment of this bill (subject to the enactment of an appropriations act ending the lapse). For subsequent lapses in appropriations, the bill requires that each employee be reimbursed for any shutdown costs on the earliest date possible after the end of a lapse in appropriations that lasts at least 14 days.</p><p>States must be reimbursed for payments for assistance programs that would otherwise be provided by the federal government but\u00a0for a lapse in appropriations that lasts at least 14 days. The states must be reimbursed no later than 90 days after the end of the lapse in appropriations.\u00a0</p><p>The reimbursements required by this bill are subject to the availability of appropriations.\u00a0</p>",
      "updateDate": "2025-10-08",
      "versionCode": "id119hr5628"
    },
    "title": "Pay Workers What They\u2019ve Earned Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pay Workers What They\u2019ve Earned Act</strong></p><p>This bill requires the federal government to reimburse states and employees of the federal government, the District of Columbia government, or federal contractors for certain costs incurred as a result of a lapse in appropriations (i.e., a government shutdown).\u00a0</p><p>Employee costs that must be reimbursed include costs incurred by an employee as a direct result of a lapse in appropriations, including expenses for loans and credit cards, and any fees, fines, or interest resulting from the employee's inability to make payments as a direct result of a loss in salary due to the lapse in appropriations.\u00a0</p><p>With respect to a lapse in appropriations that begins on or about October 1, 2025, employees must be reimbursed for any shutdown costs on the earliest date possible after the enactment of this bill (subject to the enactment of an appropriations act ending the lapse). For subsequent lapses in appropriations, the bill requires that each employee be reimbursed for any shutdown costs on the earliest date possible after the end of a lapse in appropriations that lasts at least 14 days.</p><p>States must be reimbursed for payments for assistance programs that would otherwise be provided by the federal government but\u00a0for a lapse in appropriations that lasts at least 14 days. The states must be reimbursed no later than 90 days after the end of the lapse in appropriations.\u00a0</p><p>The reimbursements required by this bill are subject to the availability of appropriations.\u00a0</p>",
      "updateDate": "2025-10-08",
      "versionCode": "id119hr5628"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5628ih.xml"
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
      "title": "Pay Workers What They\u2019ve Earned Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T10:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pay Workers What They\u2019ve Earned Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T10:23:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 31, United States Code, to reimburse employees of the Federal Government and the District of Columbia, Federal contractors, and the States for certain costs incurred as a result of a Government shutdown, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T10:18:21Z"
    }
  ]
}
```
