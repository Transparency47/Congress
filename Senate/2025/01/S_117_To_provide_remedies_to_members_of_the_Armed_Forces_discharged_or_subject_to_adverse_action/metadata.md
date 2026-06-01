# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/117?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/117
- Title: AMERICANS Act
- Congress: 119
- Bill type: S
- Bill number: 117
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2025-12-05T22:03:03Z
- Update date including text: 2025-12-05T22:03:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Armed Services.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/117",
    "number": "117",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "AMERICANS Act",
    "type": "S",
    "updateDate": "2025-12-05T22:03:03Z",
    "updateDateIncludingText": "2025-12-05T22:03:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T18:19:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TN"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AL"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ID"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MO"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ND"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "UT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ID"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "J000293",
      "firstName": "Ron",
      "fullName": "Sen. Johnson, Ron [R-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WI"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s117is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 117\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Cruz (for himself, Mrs. Blackburn , Mrs. Britt , Mr. Budd , Mr. Cornyn , Mr. Crapo , Mr. Daines , Mr. Hawley , Mr. Hoeven , Mr. Lee , Mr. Risch , Mr. Scott of Florida , Mr. Sheehy , and Mr. Johnson ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo provide remedies to members of the Armed Forces discharged or subject to adverse action under the COVID\u201319 vaccine mandate.\n#### 1. Short title\nThis Act may be cited as the Allowing Military Exemptions, Recognizing Individual Concerns About New Shots Act of 2025 or the AMERICANS Act .\n#### 2. Remedies for members of the Armed Forces discharged or subject to adverse action under the COVID\u201319 vaccine mandate\n##### (a) Limitation on imposition of new mandate\nThe Secretary of Defense may not issue any COVID\u201319 vaccine mandate as a replacement for the mandate rescinded under section 525 of the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 absent a further Act of Congress expressly authorizing a replacement mandate.\n##### (b) Remedies\nSection 736 of the National Defense Authorization Act for Fiscal Year 2022 ( Public Law 117\u201381 ; 10 U.S.C. 1161 note prec.) is amended\u2014\n**(1)**\nin the section heading, by striking to obey lawful order to receive and inserting to receive ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby striking a lawful order and inserting an order ; and\n**(B)**\nby striking shall be and all that follows through the period at the end and inserting shall be an honorable discharge. ;\n**(3)**\nby redesignating subsection (b) as subsection (g); and\n**(4)**\nby inserting after subsection (a) the following new subsections:\n(b) Prohibition on adverse action The Secretary of Defense may not take any adverse action against a covered member based solely on the refusal of such member to receive a vaccine for COVID\u201319. (c) Remedies available for a covered member discharged or subject to adverse action based on COVID\u201319 status At the election of a covered member discharged or subject to adverse action based on the member's COVID\u201319 vaccination status, and upon application through a process established by the Secretary of Defense, the Secretary shall\u2014 (1) adjust to honorable discharge the status of the member if\u2014 (A) the member was separated from the Armed Forces based solely on the failure of the member to obey an order to receive a vaccine for COVID\u201319; and (B) the discharge status of the member would have been an honorable discharge but for the refusal to obtain such vaccine; (2) reinstate the member to service at the highest grade held by the member immediately prior to the involuntary separation, allowing, however, for any reduction in rank that was not related to the member\u2019s COVID\u201319 vaccination status, with an effective date of reinstatement as of the date of involuntary separation; (3) for any member who was subject to any adverse action other than involuntary separation based solely on the member\u2019s COVID\u201319 vaccination status\u2014 (A) restore the member to the highest grade held prior to such adverse action, allowing, however, for any reduction in rank that was not related to the member\u2019s COVID\u201319 vaccination status, with an effective date of reinstatement as of the date of involuntary separation; and (B) compensate such member for any pay and benefits lost as a result of such adverse action; (4) expunge from the service record of the member any adverse action, to include non-punitive adverse action and involuntary separation, as well as any reference to any such adverse action, based solely on COVID\u201319 vaccination status; and (5) include the time of involuntary separation of the member reinstated under paragraph (2) in the computation of the retired or retainer pay of the member. (d) Retention and development of unvaccinated members The Secretary of Defense shall\u2014 (1) make every effort to retain covered members who are not vaccinated against COVID\u201319 and provide such members with professional development, promotion and leadership opportunities, and consideration equal to that of their peers; (2) only consider the COVID\u201319 vaccination status of a covered member in making deployment, assignment, and other operational decisions where\u2014 (A) the law or regulations of a foreign country require covered members to be vaccinated against COVID\u201319 in order to enter that country; and (B) the covered member\u2019s presence in that foreign country is necessary in order to perform their assigned role; and (3) for purposes of deployments, assignments, and operations described in paragraph (2), create a process to provide COVID\u201319 vaccination exemptions to covered members with\u2014 (A) a natural immunity to COVID\u201319; (B) an underlying health condition that would make COVID\u201319 vaccination a greater risk to that individual than the general population; or (C) sincerely held religious beliefs in conflict with receiving the COVID\u201319 vaccination. (e) Termination of obligation To repay bonuses of members separated for refusing covid\u201319 vaccine (1) In general A former member of the Armed Forces who was separated from the Armed Forces because the former member refused to obtain a COVID\u201319 vaccine shall be released for any obligation to repay any bonus received by the former member. (2) Reimbursement of repayments A former member of the Armed Forces described in subsection (a) who, before the date of the enactment of this Act, repaid any portion of a bonus described in that subsection shall be reimbursed for such repayment. (f) Applicability of remedies contained in this section The prohibitions and remedies described in this section shall apply to covered members regardless of whether or not they sought an accommodation to any Department of Defense COVID\u201319 vaccination policy on any grounds. .",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-01-16",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "511",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "AMERICANS Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative remedies",
            "updateDate": "2025-03-10T14:53:17Z"
          },
          {
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2025-03-10T14:53:17Z"
          },
          {
            "name": "Immunology and vaccination",
            "updateDate": "2025-03-10T14:53:17Z"
          },
          {
            "name": "Infectious and parasitic diseases",
            "updateDate": "2025-03-10T14:53:17Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-03-10T14:53:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-26T16:28:29Z"
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
          "measure-id": "id119s117",
          "measure-number": "117",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-03-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s117v00",
            "update-date": "2025-03-14"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Allowing Military Exemptions, Recognizing Individual Concerns About New Shots Act of 2025 or the AMERICANS Act</strong></p><p>This bill prohibits the Department of Defense (DOD) from issuing any COVID-19 vaccine mandate as a replacement for the rescinded vaccine mandate of August 24, 2021, unless the mandate is expressly authorized by Congress. The bill also provides that DOD must establish an application process for remedies for members of the Armed Forces who were discharged or subject to adverse action under the rescinded mandate.</p><p>Any administrative discharge of a member on the sole basis of a failure to receive a COVID-19 vaccine must be categorized as an honorable discharge, and DOD is prohibited from taking any adverse action against such a member for that reason.</p><p>DOD must try to retain unvaccinated members and provide such members with professional development, promotion and leadership opportunities, and consideration equal to that of their peers.</p><p>Additionally, DOD may only consider the COVID-19 vaccination status of members in making certain decisions (e.g., deployments in countries where it is the law) and must establish a process to provide exemptions to certain members for such decisions.</p><p>Members who were separated from the Armed Forces for refusing to receive\u00a0a COVID-19 vaccine are not required\u00a0to repay any bonuses and must be reimbursed if they repaid any portion of a bonus prior to this bill's enactment.</p><p>This bill applies to all members of the Armed Forces, regardless of whether they sought an accommodation to any DOD COVID-19 vaccination policy.</p>"
        },
        "title": "AMERICANS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s117.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Allowing Military Exemptions, Recognizing Individual Concerns About New Shots Act of 2025 or the AMERICANS Act</strong></p><p>This bill prohibits the Department of Defense (DOD) from issuing any COVID-19 vaccine mandate as a replacement for the rescinded vaccine mandate of August 24, 2021, unless the mandate is expressly authorized by Congress. The bill also provides that DOD must establish an application process for remedies for members of the Armed Forces who were discharged or subject to adverse action under the rescinded mandate.</p><p>Any administrative discharge of a member on the sole basis of a failure to receive a COVID-19 vaccine must be categorized as an honorable discharge, and DOD is prohibited from taking any adverse action against such a member for that reason.</p><p>DOD must try to retain unvaccinated members and provide such members with professional development, promotion and leadership opportunities, and consideration equal to that of their peers.</p><p>Additionally, DOD may only consider the COVID-19 vaccination status of members in making certain decisions (e.g., deployments in countries where it is the law) and must establish a process to provide exemptions to certain members for such decisions.</p><p>Members who were separated from the Armed Forces for refusing to receive\u00a0a COVID-19 vaccine are not required\u00a0to repay any bonuses and must be reimbursed if they repaid any portion of a bonus prior to this bill's enactment.</p><p>This bill applies to all members of the Armed Forces, regardless of whether they sought an accommodation to any DOD COVID-19 vaccination policy.</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119s117"
    },
    "title": "AMERICANS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Allowing Military Exemptions, Recognizing Individual Concerns About New Shots Act of 2025 or the AMERICANS Act</strong></p><p>This bill prohibits the Department of Defense (DOD) from issuing any COVID-19 vaccine mandate as a replacement for the rescinded vaccine mandate of August 24, 2021, unless the mandate is expressly authorized by Congress. The bill also provides that DOD must establish an application process for remedies for members of the Armed Forces who were discharged or subject to adverse action under the rescinded mandate.</p><p>Any administrative discharge of a member on the sole basis of a failure to receive a COVID-19 vaccine must be categorized as an honorable discharge, and DOD is prohibited from taking any adverse action against such a member for that reason.</p><p>DOD must try to retain unvaccinated members and provide such members with professional development, promotion and leadership opportunities, and consideration equal to that of their peers.</p><p>Additionally, DOD may only consider the COVID-19 vaccination status of members in making certain decisions (e.g., deployments in countries where it is the law) and must establish a process to provide exemptions to certain members for such decisions.</p><p>Members who were separated from the Armed Forces for refusing to receive\u00a0a COVID-19 vaccine are not required\u00a0to repay any bonuses and must be reimbursed if they repaid any portion of a bonus prior to this bill's enactment.</p><p>This bill applies to all members of the Armed Forces, regardless of whether they sought an accommodation to any DOD COVID-19 vaccination policy.</p>",
      "updateDate": "2025-03-14",
      "versionCode": "id119s117"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s117is.xml"
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
      "title": "AMERICANS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AMERICANS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T01:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Allowing Military Exemptions, Recognizing Individual Concerns About New Shots Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T01:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide remedies to members of the Armed Forces discharged or subject to adverse action under the COVID-19 vaccine mandate.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T01:48:17Z"
    }
  ]
}
```
