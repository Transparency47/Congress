# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/238?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/238
- Title: FREE Act
- Congress: 119
- Bill type: S
- Bill number: 238
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-11-30T06:56:28Z
- Update date including text: 2025-11-30T06:56:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/238",
    "number": "238",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "FREE Act",
    "type": "S",
    "updateDate": "2025-11-30T06:56:28Z",
    "updateDateIncludingText": "2025-11-30T06:56:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T23:22:24Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NC"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NC"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NE"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s238is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 238\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Ms. Lummis (for herself, Mr. Budd , Mr. Tillis , Mr. Ricketts , Mr. Scott of Florida , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require each agency to evaluate the permitting system of the agency, to consider whether permitting by rule could replace that system, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Full Responsibility and Expedited Enforcement Act or the FREE Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAgencies near unanimously operate under a permitting system that gives agencies broad discretion and requires the Government to review each permitting application.\n**(2)**\nAgencies near unanimously operate under a permitting system that either does not have time constraints, or has time constraints that agencies do not follow.\n**(3)**\nThe combination of broad discretion and the lack of time constraints often results in a tedious, time consuming, and often expensive permitting system for the Government and applicants. Moreover, agencies will sometimes use their discretion and the time consuming nature of permitting to stall or discourage permit issuance.\n**(4)**\nThere is a compelling interest in avoiding unnecessary delay and expense in Federal permitting.\n**(5)**\nPermit by rule is a process that seeks to overcome agency delay and the cumbersome cost of agency review to Government and private interests.\n**(6)**\nPermit by rule is a process of permitting that includes specific written standards for obtaining a permit, a simple requirement for an applicant to certify compliance with each of the standards, and a streamlined approval process with a prompt deadline for agency action on applications that only allows the Government to verify that all conditions are met. The Government retains the right and responsibility to audit and enforce compliance with permitting requirements. Focusing upon permittees who are violating the law or standards rather than gatekeeping will make permitting more efficient while allowing an agency to protect the compelling interests for which permitting systems are intended.\n#### 3. Permitting by rule\n##### (a) Report to Congress required\n**(1) Submission of report**\nNot later than 240 days after the date of the enactment of this section, the head of each agency shall submit to Congress, including any committee of Congress with jurisdiction over permits for that agency, and the Comptroller General a report on the following:\n**(A)**\nA list and description of each type of permit issued by the agency.\n**(B)**\nThe statutory and regulatory requirements for obtaining each such type of permit.\n**(C)**\nFor each type of permit issued by the agency, a specific description of each step the agency follows to review a permit application.\n**(D)**\nFor each type of permit issued by the agency, an estimate of the time the agency typically takes to review an application, beginning on the date on which an application is submitted and ending on the date on which a successful application is granted.\n**(E)**\nFor each type of permit issued by the agency, a description of each action typically taken for a case in which an application is found not to meet statutory or regulatory requirements for the issuance of a permit.\n**(F)**\nA list of primary interests that each type of permit is intended to foster or protect.\n**(G)**\nAn individual determination for each type of permit issued by the agency of whether permitting by rule could in whole or in part replace the current system for issuing the type of permit.\n**(H)**\nFor each type of permit issued by the agency for which permitting by rule could in whole or in part replace the current system for issuing the type of permit, an identification of any administrative or other practical challenges the head of the agency anticipates in transitioning to permitting by rule for the type of permit.\n**(I)**\nAn identification of each type of permit for which the head of the agency has determined the agency could not reasonably, in whole or in part, issue permits by rule under current facts and circumstances, describing with particularity each reason why permitting by rule could not reasonably be used for any such permit and what legal or practical measures could be pursued to eliminate or mitigate said reason.\n**(2) Public comment**\nIn preparing the report required pursuant to paragraph (1), the head of an agency may solicit and consider public comment regarding the report.\n**(3) Extension of submission deadline**\nIn the case that the head of an agency is not able to submit the report required pursuant to paragraph (1), the deadline to submit the report shall be extended by an additional 90 days if the head of the agency submits to Congress, including any committee of Congress with jurisdiction over permits for that agency, and the Comptroller General a notification of the intended extension of the deadline under this paragraph.\n**(4) Attorney fees**\nIf the head of an agency does not file the report required pursuant to paragraph (1) by the applicable deadline under this subsection, the agency shall pay, from any funds made available to the agency by appropriation or otherwise, the attorney fees and costs of an applicant for a claim filed by the applicant for the failure or delay of the agency to take action with respect to an application for a permit submitted to the agency by the applicant if\u2014\n**(A)**\nthe claim is filed against the agency in an appropriate United States district court during the period beginning on the expiration of the applicable deadline under this subsection and ending on the date on which the agency files the report;\n**(B)**\nthe court determines that the agency unreasonably delayed such action; and\n**(C)**\nthe applicant prevails in the claim.\n##### (b) Establishment of processes for permitting by rule\n**(1) Application for and approval of permits**\nNot later than 12 months after the date on which the report is submitted pursuant to subsection (a), for each type of permit issued by the agency for which the head of the agency determined under subsection (a)(1)(G) that permitting by rule could in whole or in part replace the current system for issuing the type of permit, the head of each agency shall establish by rule a permitting by rule application process that does the following:\n**(A)**\nSpecifies in writing each requirement and substantive standard that must be certified to be met by an applicant who files an application to qualify for a permit under permitting by rule.\n**(B)**\nAllows an applicant to file an application that contains only each required certification described in subparagraph (A) and any supporting documentation the applicant chooses to submit in support of each such certification.\n**(C)**\nDeems an application for a permit under permitting by rule granted if\u2014\n**(i)**\nthe application contains each certification described in subparagraph (A); and\n**(ii)**\na period of 180 days after the date on which the completed application was submitted has expired and the head of the agency has not otherwise approved or disapproved the application.\n**(2) Correction of application**\nThe head of an agency shall contact an applicant within 7 days after the date on which an application is submitted under paragraph (1) if any required certification is missing from the application.\n**(3) Audit of application**\nThe head of an agency may audit an application for a permit under permitting by rule and verify certifications of compliance with requirements and substantive standards for permitting by rule and may include reasonable requests for documentation.\n**(4) Disapproval of application and enforcement**\n**(A) Reason for disapproval**\nThe head of an agency may only disapprove an application submitted for a permit under permitting by rule if the head of the agency identifies a requirement or substantive standard described in paragraph (1)(A) that was not met by the application, informs the applicant of how to correct the application, provides a reasonable opportunity for the applicant to make such correction before the final action of the agency on the application, and states with particularity in any final action disapproving the application the facts and reasoning for such denial.\n**(B) Audit of compliance and enforcement following grant of a permit under permitting by rule**\n**(i) Audit**\nThe head of an agency may audit a permit granted under permitting by rule and verify compliance with requirements and substantive standards for permitting by rule, which may include reasonable requests for documentation.\n**(ii) Enforcement**\nThe head of an agency may require corrective action, suspend, or revoke a permit granted under permitting by rule at any time if the head of the agency finds that a requirement or substantive standard under permitting by rule is not being met by the recipient of the permit.\n**(C) Direct appeal**\nAn applicant whose application for a permit under permitting by rule is disapproved, of whom corrective action is required under a permit granted under permitting by rule, or whose permit granted under permitting by rule is suspended or revoked may appeal such disapproval, corrective action, suspension, or revocation in an appropriate United States district court.\n**(D) Burden of proof**\nIn an appeal under subparagraph (C), the agency shall bear the burden of proof to show that an application was lawfully disapproved or that the agency lawfully required corrective action or suspended or revoked a permit.\n**(E) Attorney fees**\nIf the court finds for the applicant or permit holder under this paragraph and that the agency was not substantially justified in disapproving, requiring corrective action under, suspending, or revoking a permit, the agency shall pay the attorney fees and costs of the applicant from any funds made available to the agency by appropriation or otherwise.\n##### (c) Congressional oversight\nNot later than 2 years after the date on which the report is submitted pursuant to subsection (a), the head of each agency shall submit to Congress a report on the implementation by the agency of permitting by rule for each type of permit issued by the agency for which the head of the agency determined under subsection (a)(1)(G) that permitting by rule could in whole or in part replace the current system for issuing the type of permit.\n##### (d) Concurrent use of previous permitting system\nIf the head of the agency determines in the report submitted pursuant to subsection (a) that the permitting system in effect at the agency before the date of the enactment of this Act for any type of permit provides value that permitting by rule does not, but that permitting by rule could in whole or in part replace the current system for issuing the type of permit, the head of the agency may maintain for that type of permit both the permitting system previously in effect and permitting by rule, and the applicant may choose which system to use to apply for a permit of that type from the agency.\n##### (e) GAO reports\n**(1) Report on accuracy of agency reports**\nNot later than 90 days after the expiration of the deadline to submit the reports required under subsection (a), the Comptroller General shall submit to Congress a report on the completeness and accuracy of the reports, including the recommendations of the Comptroller General concerning legal or practical measures that could be pursued to eliminate or mitigate any legal or practical challenges to the transition by agencies to permitting by rule for any type of permit.\n**(2) Report on progress by agencies**\nNot later than 180 days after submission by the agencies of the reports required under subsection (c), the Comptroller General shall submit to Congress a report on the progress by agencies in the implementation of this Act, including any recommendation concerning legal or practical measures that could be pursued to eliminate or mitigate any remaining legal or practical challenges to the transition by agencies to issuance of permits under permitting by rule for any type of permit.\n**(3) Supplements to the reports**\nThe Comptroller General may submit supplements to the report described in paragraph (1) or (2) with regard to a report submitted by the head of an agency after the Comptroller General submits the report required pursuant to paragraph (1) or (2).\n##### (f) Definitions\nIn this section:\n**(1) Agency; Rule**\nThe terms agency and rule have the meaning given those terms in section 551 of title 5, United States Code.\n**(2) Completed application**\nThe term completed application means an application submitted under subsection (b) that contains certifications that the applicant meets each requirement and substantive standard specified under subsection (b)(1)(A).\n**(3) Permitting by rule**\nThe term permitting by rule means the application process that an agency establishes by rule for granting a certain type of permit described in subsection (b).\n**(4) Substantive standard**\nThe term substantive standard means all qualities, statuses, actions, benchmarks, measurements, or other written descriptions that would qualify a party to perform the permitted action.",
      "versionDate": "2025-01-23",
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
        "actionDate": "2025-10-28",
        "text": "Placed on the Union Calendar, Calendar No. 303."
      },
      "number": "689",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FREE Act",
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
            "name": "Accounting and auditing",
            "updateDate": "2025-03-19T16:14:41Z"
          },
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-03-19T16:14:41Z"
          },
          {
            "name": "Administrative remedies",
            "updateDate": "2025-03-19T16:14:41Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-19T16:14:41Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2025-03-19T16:14:41Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-03-19T16:14:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-28T19:42:01Z"
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
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s238is.xml"
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
      "title": "FREE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FREE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Full Responsibility and Expedited Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require each agency to evaluate the permitting system of the agency, to consider whether permitting by rule could replace that system, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:33:46Z"
    }
  ]
}
```
