# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/511?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/511
- Title: AMERICANS Act
- Congress: 119
- Bill type: HR
- Bill number: 511
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-02-06T21:26:15Z
- Update date including text: 2026-02-06T21:26:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/511",
    "number": "511",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001101",
        "district": "10",
        "firstName": "Pat",
        "fullName": "Rep. Harrigan, Pat [R-NC-10]",
        "lastName": "Harrigan",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "AMERICANS Act",
    "type": "HR",
    "updateDate": "2026-02-06T21:26:15Z",
    "updateDateIncludingText": "2026-02-06T21:26:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:06:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "UT"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TN"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AZ"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IN"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WI"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "K000405",
      "district": "13",
      "firstName": "Brad",
      "fullName": "Rep. Knott, Brad [R-NC-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Knott",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WV"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert [R-MO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MO"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MI"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "GA"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "KS"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark [R-IN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IN"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "VA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "OH"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "WA"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NC"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "WI"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "IN"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AZ"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "TX"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr511ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 511\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Harrigan (for himself, Mr. Kennedy of Utah , Mr. Ogles , Mr. Hamadeh of Arizona , Mr. Stutzman , Mr. Wied , Mrs. Luna , Mr. Knott , Mr. Harris of North Carolina , Mr. Nehls , Mr. Moore of West Virginia , Mr. Onder , Mr. Barrett , Mr. Edwards , Mr. Murphy , Mr. Self , Mr. Downing , Mr. Jack , Mr. Schmidt , Mr. Messmer , Mr. McGuire , Mr. Haridopolos , and Mr. Rulli ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo provide remedies to members of the Armed Forces discharged or subject to adverse action under the COVID\u201319 vaccine mandate.\n#### 1. Short title\nThis Act may be cited as the Allowing Military Exemptions, Recognizing Individual Concerns About New Shots Act of 2025 or the AMERICANS Act .\n#### 2. Remedies for members of the Armed Forces discharged or subject to adverse action under the COVID\u201319 vaccine mandate\n##### (a) Limitation on imposition of new mandate\nThe Secretary of Defense may not issue any COVID\u201319 vaccine mandate as a replacement for the mandate rescinded under section 525 of the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 absent a further Act of Congress expressly authorizing a replacement mandate.\n##### (b) Remedies\nSection 736 of the National Defense Authorization Act for Fiscal Year 2022 ( Public Law 117\u201381 ; 10 U.S.C. 1161 note prec.) is amended\u2014\n**(1)**\nin the section heading, by striking to obey lawful order to receive and inserting to receive ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby striking a lawful order and inserting an order ; and\n**(B)**\nby striking shall be and all that follows through the period at the end and inserting shall be an honorable discharge. ;\n**(3)**\nby redesignating subsection (b) as subsection (g); and\n**(4)**\nby inserting after subsection (a) the following new subsections:\n(b) Prohibition on adverse action The Secretary of Defense may not take any adverse action against a covered member based solely on the refusal of such member to receive a vaccine for COVID\u201319. (c) Remedies available for a covered member discharged or subject to adverse action based on COVID\u201319 status At the election of a covered member discharged or subject to adverse action based on the member's COVID\u201319 vaccination status, and upon application through a process established by the Secretary of Defense, the Secretary shall\u2014 (1) adjust to honorable discharge the status of the member if\u2014 (A) the member was separated from the Armed Forces based solely on the failure of the member to obey an order to receive a vaccine for COVID\u201319; and (B) the discharge status of the member would have been an honorable discharge but for the refusal to obtain such vaccine; (2) reinstate the member to service at the highest grade held by the member immediately prior to the involuntary separation, allowing, however, for any reduction in rank that was not related to the member\u2019s COVID\u201319 vaccination status, with an effective date of reinstatement as of the date of involuntary separation; (3) for any member who was subject to any adverse action other than involuntary separation based solely on the member\u2019s COVID\u201319 vaccination status\u2014 (A) restore the member to the highest grade held prior to such adverse action, allowing, however, for any reduction in rank that was not related to the member\u2019s COVID\u201319 vaccination status, with an effective date of reinstatement as of the date of involuntary separation; and (B) compensate such member for any pay and benefits lost as a result of such adverse action; (4) expunge from the service record of the member any adverse action, to include non-punitive adverse action and involuntary separation, as well as any reference to any such adverse action, based solely on COVID\u201319 vaccination status; and (5) include the time of involuntary separation of the member reinstated under paragraph (2) in the computation of the retired or retainer pay of the member. (d) Retention and development of unvaccinated members The Secretary of Defense shall\u2014 (1) make every effort to retain covered members who are not vaccinated against COVID\u201319 and provide such members with professional development, promotion and leadership opportunities, and consideration equal to that of their peers; (2) only consider the COVID\u201319 vaccination status of a covered member in making deployment, assignment, and other operational decisions where\u2014 (A) the law or regulations of a foreign country require covered members to be vaccinated against COVID\u201319 in order to enter that country; and (B) the covered member\u2019s presence in that foreign country is necessary in order to perform their assigned role; and (3) for purposes of deployments, assignments, and operations described in paragraph (2), create a process to provide COVID\u201319 vaccination exemptions to covered members with\u2014 (A) a natural immunity to COVID\u201319; (B) an underlying health condition that would make COVID\u201319 vaccination a greater risk to that individual than the general population; or (C) sincerely held religious beliefs in conflict with receiving the COVID\u201319 vaccination. (e) Termination of obligation To repay bonuses of members separated for refusing covid\u201319 vaccine (1) In general A former member of the Armed Forces who was separated from the Armed Forces because the former member refused to obtain a COVID\u201319 vaccine shall be released for any obligation to repay any bonus received by the former member. (2) Reimbursement of repayments A former member of the Armed Forces described in subsection (a) who, before the date of the enactment of this Act, repaid any portion of a bonus described in that subsection shall be reimbursed for such repayment. (f) Applicability of remedies contained in this section The prohibitions and remedies described in this section shall apply to covered members regardless of whether or not they sought an accommodation to any Department of Defense COVID\u201319 vaccination policy on any grounds. .",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-01-16",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "117",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "AMERICANS Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative remedies",
            "updateDate": "2025-03-10T14:52:57Z"
          },
          {
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2025-03-10T14:52:42Z"
          },
          {
            "name": "Immunology and vaccination",
            "updateDate": "2025-03-10T14:51:44Z"
          },
          {
            "name": "Infectious and parasitic diseases",
            "updateDate": "2025-03-10T14:52:49Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-03-10T14:51:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-19T18:04:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr511",
          "measure-number": "511",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-03-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr511v00",
            "update-date": "2025-03-14"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Allowing Military Exemptions, Recognizing Individual Concerns About New Shots Act of 2025 or the AMERICANS Act</strong></p><p>This bill prohibits the Department of Defense (DOD) from issuing any COVID-19 vaccine mandate as a replacement for the rescinded vaccine mandate of August 24, 2021, unless the mandate is expressly authorized by Congress. The bill also provides that DOD must establish an application process for remedies for members of the Armed Forces who were discharged or subject to adverse action under the rescinded mandate.</p><p>Any administrative discharge of a member on the sole basis of a failure to receive a COVID-19 vaccine must be categorized as an honorable discharge, and DOD is prohibited from taking any adverse action against such a member for that reason.</p><p>DOD must try to retain unvaccinated members and provide such members with professional development, promotion and leadership opportunities, and consideration equal to that of their peers.</p><p>Additionally, DOD may only consider the COVID-19 vaccination status of members in making certain decisions (e.g., deployments in countries where it is the law) and must establish a process to provide exemptions to certain members for such decisions.</p><p>Members who were separated from the Armed Forces for refusing to receive\u00a0a COVID-19 vaccine are not required\u00a0to repay any bonuses and must be reimbursed if they repaid any portion of a bonus prior to this bill's enactment.</p><p>This bill applies to all members of the Armed Forces, regardless of whether they sought an accommodation to any DOD COVID-19 vaccination policy.</p>"
        },
        "title": "AMERICANS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr511.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Allowing Military Exemptions, Recognizing Individual Concerns About New Shots Act of 2025 or the AMERICANS Act</strong></p><p>This bill prohibits the Department of Defense (DOD) from issuing any COVID-19 vaccine mandate as a replacement for the rescinded vaccine mandate of August 24, 2021, unless the mandate is expressly authorized by Congress. The bill also provides that DOD must establish an application process for remedies for members of the Armed Forces who were discharged or subject to adverse action under the rescinded mandate.</p><p>Any administrative discharge of a member on the sole basis of a failure to receive a COVID-19 vaccine must be categorized as an honorable discharge, and DOD is prohibited from taking any adverse action against such a member for that reason.</p><p>DOD must try to retain unvaccinated members and provide such members with professional development, promotion and leadership opportunities, and consideration equal to that of their peers.</p><p>Additionally, DOD may only consider the COVID-19 vaccination status of members in making certain decisions (e.g., deployments in countries where it is the law) and must establish a process to provide exemptions to certain members for such decisions.</p><p>Members who were separated from the Armed Forces for refusing to receive\u00a0a COVID-19 vaccine are not required\u00a0to repay any bonuses and must be reimbursed if they repaid any portion of a bonus prior to this bill's enactment.</p><p>This bill applies to all members of the Armed Forces, regardless of whether they sought an accommodation to any DOD COVID-19 vaccination policy.</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119hr511"
    },
    "title": "AMERICANS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Allowing Military Exemptions, Recognizing Individual Concerns About New Shots Act of 2025 or the AMERICANS Act</strong></p><p>This bill prohibits the Department of Defense (DOD) from issuing any COVID-19 vaccine mandate as a replacement for the rescinded vaccine mandate of August 24, 2021, unless the mandate is expressly authorized by Congress. The bill also provides that DOD must establish an application process for remedies for members of the Armed Forces who were discharged or subject to adverse action under the rescinded mandate.</p><p>Any administrative discharge of a member on the sole basis of a failure to receive a COVID-19 vaccine must be categorized as an honorable discharge, and DOD is prohibited from taking any adverse action against such a member for that reason.</p><p>DOD must try to retain unvaccinated members and provide such members with professional development, promotion and leadership opportunities, and consideration equal to that of their peers.</p><p>Additionally, DOD may only consider the COVID-19 vaccination status of members in making certain decisions (e.g., deployments in countries where it is the law) and must establish a process to provide exemptions to certain members for such decisions.</p><p>Members who were separated from the Armed Forces for refusing to receive\u00a0a COVID-19 vaccine are not required\u00a0to repay any bonuses and must be reimbursed if they repaid any portion of a bonus prior to this bill's enactment.</p><p>This bill applies to all members of the Armed Forces, regardless of whether they sought an accommodation to any DOD COVID-19 vaccination policy.</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119hr511"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr511ih.xml"
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
      "title": "AMERICANS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-19T03:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AMERICANS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Allowing Military Exemptions, Recognizing Individual Concerns About New Shots Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide remedies to members of the Armed Forces discharged or subject to adverse action under the COVID-19 vaccine mandate.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:27Z"
    }
  ]
}
```
