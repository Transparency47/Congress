# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1720?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1720
- Title: Due Process Continuity of Care Act
- Congress: 119
- Bill type: S
- Bill number: 1720
- Origin chamber: Senate
- Introduced date: 2025-05-12
- Update date: 2026-02-24T12:03:19Z
- Update date including text: 2026-02-24T12:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-12: Introduced in Senate
- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-12: Introduced in Senate

## Actions

- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-12",
    "latestAction": {
      "actionDate": "2025-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1720",
    "number": "1720",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Due Process Continuity of Care Act",
    "type": "S",
    "updateDate": "2026-02-24T12:03:19Z",
    "updateDateIncludingText": "2026-02-24T12:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-12",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-12",
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
            "date": "2025-05-13T00:52:42Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-13T00:52:42Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "OR"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "NC"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "MA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "GA"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1720is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1720\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2025 Mr. Cassidy (for himself, Mr. Merkley , Mr. Tillis , and Mr. Markey ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XIX of the Social Security Act to remove the Medicaid coverage exclusion for inmates in custody pending disposition of charges, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Due Process Continuity of Care Act .\n#### 2. Removal of inmate limitation on benefits under Medicaid\n##### (a) Removal of limitation\n**(1) In general**\nThe subdivision (A) of section 1905(a) of the Social Security Act ( 42 U.S.C. 1396d(a) ) following the last numbered paragraph of such section is amended by striking for an individual and all that follows through charges and inserting for any individual while in custody pending disposition of charges .\n**(2) Effective date**\nThe amendment made by paragraph (1) shall take effect on the 1st day of the 1st calendar quarter that begins on or after the date that is 60 days after the date of the enactment of this Act and shall apply to items and services furnished for periods beginning on or after such date.\n##### (b) Conforming amendment\nEffective January 2, 2026, subparagraph (A) of section 1902(a)(84) of the Social Security Act ( 42 U.S.C. 1396a(a)(84) ) is amended to read as follows:\n(A) the State shall not terminate eligibility for medical assistance under the State plan (or waiver of such plan) for an individual because the individual is an inmate of a public institution (as defined in subsection (nn)(3)) (or, if the State has elected the option described in the subdivision (A) following the last numbered paragraph of section 1905(a), while the individual is in custody pending disposition of charges) but, subject to subparagraph (D), may suspend coverage during the period the individual is such an inmate (or if the State has made such an election, during the period the individual is in custody pending disposition of charges); .\n#### 3. Planning grants\n##### (a) In general\nThe Secretary shall award planning grants to States to support providing medical assistance under the State Medicaid program to individuals who are eligible for such assistance as a result of the amendment made by section 2(a). The grants shall be used to prepare an application that meets the requirements of subsection (b).\n##### (b) Application requirements\nIn order to be awarded a planning grant under this section, a State shall submit an application to the Secretary at such time and in such form and manner as the Secretary shall require, that includes the following information along with such additional information, provisions, and assurances, as the Secretary may require:\n**(1)**\nA proposed process for carrying out each of the activities described in subsection (c) in the State.\n**(2)**\nA review of State policies regarding the population of individuals who are eligible for medical assistance under the State Medicaid program as a result of the amendment made by section 2(a) with respect to whether such policies may create barriers to increasing the number of health care providers who can provide items and services for that population.\n**(3)**\nThe development of a plan, taking into account activities described in subsection (c)(2), that will ensure a sustainable number of Medicaid-enrolled providers under the State Medicaid program that can offer a full array of treatment and services to the patient population described in paragraph (2) as needed. Such plan shall include the following:\n**(A)**\nSpecific activities to increase the number of providers that will offer physical health treatment, as well as services related to behavioral health treatment, including substance use disorder treatment, recovery, or support services (including short-term detoxification services, outpatient substance use disorder services, and evidence-based peer recovery services).\n**(B)**\nMilestones and timeliness for implementing activities set forth in the plan.\n**(C)**\nSpecific measurable targets for increasing the number of providers under the State Medicaid program who will treat the patient population described in paragraph (2).\n**(4)**\nAn assurance that the State consulted with relevant stakeholders, including the State agency responsible for administering the State Medicaid program, Medicaid managed care plans, health care providers, law enforcement personnel, officials from jails, and Medicaid beneficiary advocates, with respect to the preparation and completion of the application and a description of such consultation.\n##### (c) Activities described\nFor purposes of subsection (b)(1), the activities described in this subsection are the following:\n**(1)**\nActivities that support the development of an initial assessment of the health treatment needs of patients who are in custody pending disposition of charges to determine the extent to which providers are needed (including the types of such providers and geographic area of need) to improve the number of providers that will treat patients in custody pending disposition of charges under the State Medicaid program, including the following:\n**(A)**\nAn estimate of the number of individuals enrolled under the State Medicaid program who are in custody pending disposition of charges.\n**(B)**\nInformation on the capacity of providers to provide treatment or services to such individuals enrolled under the State Medicaid program, including information on providers who provide such services and their participation under the State Medicaid program.\n**(C)**\nInformation on the health care services provided under programs other than the State Medicaid program in jails to individuals who are in custody pending disposition of charges.\n**(2)**\nActivities that, taking into account the results of the assessment described in paragraph (1) with respect to the provision of treatment or services under the State Medicaid program, support the development of State infrastructure to recruit or contract with prospective health care providers, provide training and technical assistance to such providers, and secure a process for an electronic health record system for billing to reimburse for services provided by the correctional facility, outpatient providers, medical vendors, and contracted telehealth service providers to patients who are in custody pending disposition of charges that are compliant with applicable requirements and regulations for State Medicaid programs.\n**(3)**\nActivities that ensure the quality of care for patients who are in custody pending disposition of charges, including formal reporting mechanisms for patient outcomes, and activities that promote participation in learning collaboratives among providers treating this population.\n##### (d) Geographic diversity\nThe Secretary shall select States for planning grants under this section in a manner that ensures geographic diversity.\n##### (e) Funding\nThere are authorized to be appropriated $50,000,000 to carry out this section.\n##### (f) Definitions\nIn this section:\n**(1) Medicaid program**\nThe term Medicaid program means, with respect to a State, the State program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) including any waiver or demonstration under such title or under section 1115 of such Act ( 42 U.S.C. 1315 ) relating to such title.\n**(2) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(3) State**\nThe term State has the meaning given that term for purposes of title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) in section 1101(a)(1) of such Act ( 42 U.S.C. 1301(a)(1) ).",
      "versionDate": "2025-05-12",
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
        "actionDate": "2025-09-08",
        "actionTime": "19:04:01",
        "text": "ASSUMING FIRST SPONSORSHIP - Ms. Dexter asked unanimous consent that she may hereafter be considered as the first sponsor of H.R. 1510, a bill originally introduced by Representative Turner (TX), for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection."
      },
      "number": "1510",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Due Process Continuity of Care Act",
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
            "name": "Correctional facilities and imprisonment",
            "updateDate": "2025-07-17T18:42:13Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-07-17T18:42:13Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-07-17T18:42:13Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-07-17T18:42:13Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-07-17T18:42:13Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-07-17T18:42:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-29T15:42:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-12",
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
          "measure-id": "id119s1720",
          "measure-number": "1720",
          "measure-type": "s",
          "orig-publish-date": "2025-05-12",
          "originChamber": "SENATE",
          "update-date": "2025-06-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1720v00",
            "update-date": "2025-06-06"
          },
          "action-date": "2025-05-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Due Process Continuity of Care Act</b></p> <p>This bill allows an otherwise eligible individual who\u00a0is in custody pending disposition of charges (i.e., pretrial detainees) to receive Medicaid benefits at the option of the state. The bill also provides for state planning grants to support the provision of such benefits.</p>"
        },
        "title": "Due Process Continuity of Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1720.xml",
    "summary": {
      "actionDate": "2025-05-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Due Process Continuity of Care Act</b></p> <p>This bill allows an otherwise eligible individual who\u00a0is in custody pending disposition of charges (i.e., pretrial detainees) to receive Medicaid benefits at the option of the state. The bill also provides for state planning grants to support the provision of such benefits.</p>",
      "updateDate": "2025-06-06",
      "versionCode": "id119s1720"
    },
    "title": "Due Process Continuity of Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Due Process Continuity of Care Act</b></p> <p>This bill allows an otherwise eligible individual who\u00a0is in custody pending disposition of charges (i.e., pretrial detainees) to receive Medicaid benefits at the option of the state. The bill also provides for state planning grants to support the provision of such benefits.</p>",
      "updateDate": "2025-06-06",
      "versionCode": "id119s1720"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1720is.xml"
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
      "title": "Due Process Continuity of Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Due Process Continuity of Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XIX of the Social Security Act to remove the Medicaid coverage exclusion for inmates in custody pending disposition of charges, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:03:48Z"
    }
  ]
}
```
