# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2505?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2505
- Title: Primacy Certainty Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2505
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2026-04-29T11:03:32Z
- Update date including text: 2026-04-29T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2505",
    "number": "2505",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "Primacy Certainty Act of 2025",
    "type": "S",
    "updateDate": "2026-04-29T11:03:32Z",
    "updateDateIncludingText": "2026-04-29T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-29",
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
            "date": "2025-07-29T18:34:41Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-29T18:34:41Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "NE"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2505is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2505\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Mr. Sullivan (for himself and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Safe Drinking Water Act to clarify the requisite timeline for making a decision on the approval or disapproval of a State underground injection control program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Primacy Certainty Act of 2025 .\n#### 2. State primary enforcement responsibility for Class VI wells\n##### (a) Amendments\nSection 1422(b) of the Safe Drinking Water Act (42 U.S.C. 300h\u20131(b)) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nby striking (2) Within ninety days and inserting the following:\n(2) Required timeline (A) Definition of Class VI well In this paragraph, the term Class VI well has the meaning given the term in section 40306(a) of the Infrastructure Investment and Jobs Act (42 U.S.C. 300h\u20139(a)). (B) General deadline for response Within 90 days ; and\n**(B)**\nby adding at the end the following:\n(C) Notice related to State primary enforcement responsibility for class VI wells (i) Notice to State If the Administrator does not approve, disapprove, or approve in part and disapprove in part the State's underground injection control program for Class VI wells by not later than 180 days after the date on which the application of the State is submitted under paragraph (1)(A) or notice of the State is submitted under paragraph (1)(B), the Administrator shall transmit to the State, in writing, a detailed explanation that describes\u2014 (I) the status of the review of the application or notice, as applicable; (II) the reason for which a decision with respect to that application or notice has not yet been made; and (III) an itemized list of specific deficiencies with the application or notice to be addressed to receive approval of that application or notice, in accordance with the requirements of this title. (ii) Automatic approval for Class VI wells (I) In general If the Administrator has not approved, disapproved, or approved in part and disapproved in part a complete application submitted under paragraph (1)(A) or notice submitted under paragraph (1)(B) of a State's underground injection control program to regulate Class VI wells in writing by not later than the date that is 30 days after the end of the 180-day period described in clause (i), that application or notice shall be considered approved by the Administrator if the State has established and implemented a primary enforcement authority program for 1 or more other classes of underground injection control wells (including adequate recordkeeping and reporting) to prevent underground injection that endangers drinking water sources. (II) Determination of completeness (aa) Deadline The Administrator shall determine whether an application submitted under paragraph (1)(A) or notice submitted under paragraph (1)(B) is complete for purposes of subclause (I), and provide notice to the State of any deficiencies in that application or notice, by not later than 10 days after the date on which the State submits the application or notice. (bb) Failure to make determination concerning completeness of Class VI primacy application or notice If the Administrator has not made a determination under item (aa) by the end of the 10-day period described in that item, on request of the State that submitted the application or notice, the application or notice shall be considered administratively complete. (D) Pending permits and applications for Class VI wells With respect to Class VI wells and the efforts of a State to obtain from the Administrator primary enforcement responsibility of Class VI wells, following the approval of an application under paragraph (1)(A) or notice under paragraph (1)(B) for a State, the Administrator shall, as expeditiously as possible\u2014 (i) render a decision on any pending permits or applications for the operation of Class VI wells in the State prior to that State assuming primary enforcement responsibility for Class VI wells; and (ii) transfer to that State all pending permits, applications, and other information relevant to operating an underground injection control program to regulate Class VI wells not already in possession of the State following that State assuming primary enforcement responsibility for Class VI wells. (E) Grounds for denial of class VI well applications A denial or approval in part and disapproval in part with respect to an application under paragraph (1)(A) or notice under paragraph (1)(B) for a State to operate an underground injection control program to regulate Class VI wells shall be based solely on a finding by the Administrator that the State does not meet the criteria described in paragraph (1)(A). (F) No conditions for decisions The Administrator shall not condition the approval of an application under paragraph (1)(A) or notice under paragraph (1)(B) for a State to operate an underground injection control program to regulate Class VI wells on the inclusion of\u2014 (i) provisions not otherwise included in the application or notice on the date of submission; or (ii) any other provision not otherwise explicitly required by this title. ; and\n**(2)**\nby adding at the end the following:\n(5) Preapplication activities for Class VI wells With respect to Class VI wells (as defined in paragraph (2)(A)) and the efforts of a State to obtain from the Administrator primary enforcement responsibility of Class VI wells (as so defined), the Administrator, acting through the individual designated under paragraph (6), shall work as expeditiously as possible with States to complete any necessary activities prior to the submission of an application under paragraph (1)(A) or notice under paragraph (1)(B), taking into consideration the need for a thorough and detailed application or notice, as applicable. (6) Application coordination for Class VI wells With respect to underground injection control programs of States, or portions of underground injection control programs of States, that regulate Class VI wells (as defined in paragraph (2)(A)), the Administrator shall designate 1 individual to be responsible for coordinating for each State\u2014 (A) in accordance with paragraph (5), the completion of any necessary activities prior to the submission of an application submitted under paragraph (1)(A) or notice submitted under paragraph (1)(B); (B) the review of an application submitted under paragraph (1)(A) or notice submitted under paragraph (1)(B); and (C) the hiring of any additional staff necessary to carry out subparagraphs (A) and (B). (7) Evaluation of resources Not later than 90 days after the date of enactment of this paragraph, the Administrator, in consultation with the individual designated under paragraph (6), shall submit to the Committees on Environment and Public Works and Appropriations of the Senate and the Committees on Energy and Commerce and Appropriations of the House of Representatives a report that describes\u2014 (A) the availability of staff and resources to promptly carry out the requirements of the amendments made by section 2(a) of the Primacy Certainty Act of 2025 ; and (B) any funding necessary to promptly carry out the requirements of the amendments made by section 2(a) of the Primacy Certainty Act of 2025 . .\n##### (b) Use of IIJA funds\n**(1) Use for report**\nAmounts made available to carry out section 40306(b) of the Infrastructure Investment and Jobs Act (42 U.S.C. 300h\u20139(b)) may, beginning on the date of enactment of this Act, be used to carry out paragraph (7) of section 1422(b) of the Safe Drinking Water Act (42 U.S.C. 300h\u20131(b)).\n**(2) Conforming amendment**\nSection 40306(b) of the Infrastructure Investment and Jobs Act (42 U.S.C. 300h\u20139(b)) is amended by inserting (including carrying out paragraph (7) of section 1422(b) of the Safe Drinking Water Act (42 U.S.C. 300h\u20131(b)) in accordance with section 2(b)(1) of the Primacy Certainty Act of 2025 ) after 2010)) .\n##### (c) Rules of construction\n**(1) Definitions**\nIn this subsection:\n**(A) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(B) Class VI well**\nThe term Class VI well has the meaning given the term in section 40306(a) of the Infrastructure Investment and Jobs Act (42 U.S.C. 300h\u20139(a)).\n**(2) Ability to deny or withdraw State primary enforcement responsibility**\nNothing in the amendments made by this section limits the ability of the Administrator\u2014\n**(A)**\nto deny an application under paragraph (1)(A) of subsection (b) of section 1422 of the Safe Drinking Water Act (42 U.S.C. 300h\u20131) or notice under paragraph (1)(B) of that subsection of a State to operate an underground injection control program to regulate Class VI wells; or\n**(B)**\nto revoke primary enforcement responsibility in accordance with that Act (42 U.S.C. 300f et seq.).\n**(3) Applicability to new submissions**\nThe amendments made by this section shall apply to all applications under paragraph (1)(A) of subsection (b) of section 1422 of the Safe Drinking Water Act (42 U.S.C. 300h\u20131) and notices under paragraph (1)(B) of that subsection for underground injection control programs of States, or portions of underground injection control programs of States, that regulate Class VI wells submitted to the Administrator pursuant to that section on and after the date of enactment of this Act.\n**(4) Applicability to prior submissions**\nWith respect to applications under paragraph (1)(A) of subsection (b) of section 1422 of the Safe Drinking Water Act (42 U.S.C. 300h\u20131) and notices under paragraph (1)(B) of that subsection for underground injection control programs of States, or portions of underground injection control programs of States, that regulate Class VI wells that were submitted to the Administrator, but not approved, before the date of enactment of this Act\u2014\n**(A)**\nthe 180-day period described in paragraph (2)(C)(i) of that section shall begin on the date of enactment of this Act; and\n**(B)**\nthe Administrator shall process and make decisions, pursuant to the requirements of this Act and the amendments made by this Act, on those applications and notices in the order in which the applications and notices were submitted.",
      "versionDate": "",
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
        "actionDate": "2025-08-05",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "4880",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Primacy Certainty Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-09-17T17:04:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-29",
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
          "measure-id": "id119s2505",
          "measure-number": "2505",
          "measure-type": "s",
          "orig-publish-date": "2025-07-29",
          "originChamber": "SENATE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2505v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-07-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Primacy Certainty Act of 2025</strong></p><p>This bill modifies provisions of the underground injection control program established under the Safe Drinking Water Act related to the review of state applications to obtain responsibility for regulating Class VI wells, which are used to store captured carbon. The bill sets forth a process to give states primary enforcement responsibility for such wells if the Environmental Protection Agency (EPA) fails to meet specified deadlines.</p><p>In addition, the bill prohibits the EPA from conditioning the approval of state applications on the inclusion of provisions that are not included in the applications or not explicitly required by the Safe Drinking Water Act.</p>"
        },
        "title": "Primacy Certainty Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2505.xml",
    "summary": {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Primacy Certainty Act of 2025</strong></p><p>This bill modifies provisions of the underground injection control program established under the Safe Drinking Water Act related to the review of state applications to obtain responsibility for regulating Class VI wells, which are used to store captured carbon. The bill sets forth a process to give states primary enforcement responsibility for such wells if the Environmental Protection Agency (EPA) fails to meet specified deadlines.</p><p>In addition, the bill prohibits the EPA from conditioning the approval of state applications on the inclusion of provisions that are not included in the applications or not explicitly required by the Safe Drinking Water Act.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119s2505"
    },
    "title": "Primacy Certainty Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Primacy Certainty Act of 2025</strong></p><p>This bill modifies provisions of the underground injection control program established under the Safe Drinking Water Act related to the review of state applications to obtain responsibility for regulating Class VI wells, which are used to store captured carbon. The bill sets forth a process to give states primary enforcement responsibility for such wells if the Environmental Protection Agency (EPA) fails to meet specified deadlines.</p><p>In addition, the bill prohibits the EPA from conditioning the approval of state applications on the inclusion of provisions that are not included in the applications or not explicitly required by the Safe Drinking Water Act.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119s2505"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2505is.xml"
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
      "title": "Primacy Certainty Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Primacy Certainty Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Safe Drinking Water Act to clarify the requisite timeline for making a decision on the approval or disapproval of a State underground injection control program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:30Z"
    }
  ]
}
```
