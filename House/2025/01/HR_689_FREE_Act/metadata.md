# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/689?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/689
- Title: FREE Act
- Congress: 119
- Bill type: HR
- Bill number: 689
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-02-04T05:06:19Z
- Update date including text: 2026-02-04T05:06:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2025-05-21 - Committee: Ordered to be Reported by the Yeas and Nays: 23 - 19.
- 2025-10-28 - Calendars: Placed on the Union Calendar, Calendar No. 303.
- 2025-10-28 - Committee: Reported (Amended) by the Committee on Oversight and Government Reform. H. Rept. 119-351.
- 2025-10-28 - Committee: Reported (Amended) by the Committee on Oversight and Government Reform. H. Rept. 119-351.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2025-05-21 - Committee: Ordered to be Reported by the Yeas and Nays: 23 - 19.
- 2025-10-28 - Calendars: Placed on the Union Calendar, Calendar No. 303.
- 2025-10-28 - Committee: Reported (Amended) by the Committee on Oversight and Government Reform. H. Rept. 119-351.
- 2025-10-28 - Committee: Reported (Amended) by the Committee on Oversight and Government Reform. H. Rept. 119-351.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/689",
    "number": "689",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001228",
        "district": "2",
        "firstName": "Celeste",
        "fullName": "Rep. Maloy, Celeste [R-UT-2]",
        "lastName": "Maloy",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "FREE Act",
    "type": "HR",
    "updateDate": "2026-02-04T05:06:19Z",
    "updateDateIncludingText": "2026-02-04T05:06:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-10-28",
      "calendarNumber": {
        "calendar": "U00303"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 303.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-10-28",
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
      "text": "Reported (Amended) by the Committee on Oversight and Government Reform. H. Rept. 119-351.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Oversight and Government Reform. H. Rept. 119-351.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 23 - 19.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
            "date": "2025-10-28T17:46:24Z",
            "name": "Reported By"
          },
          {
            "date": "2025-05-21T14:15:19Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-23T15:00:15Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MN"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "UT"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "UT"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AZ"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MN"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MN"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "WA"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "GA"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "GU"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IN"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AZ"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ID"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "UT"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "WY"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr689ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 689\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Ms. Maloy (for herself, Mr. Finstad , Mr. Moore of Utah , Mr. Valadao , Mr. Arrington , Mr. Owens , Mr. Pfluger , Mr. Ciscomani , Mr. Stauber , Mrs. Fischbach , Mr. Newhouse , Mr. Collins , Mr. Moylan , Mr. Yakym , Mr. Fong , Mr. Gosar , Mr. Fulcher , and Mr. Kennedy of Utah ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require each agency to evaluate the permitting system of the agency, to consider whether permitting by rule could replace that system, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Full Responsibility and Expedited Enforcement Act or the FREE Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAgencies near unanimously operate under a permitting system that gives agencies broad discretion and requires the Government to review each permitting application.\n**(2)**\nAgencies near unanimously operate under a permitting system that either does not have time constraints, or has time constraints that agencies do not follow.\n**(3)**\nThe combination of broad discretion and the lack of time constraints often results in a tedious, time consuming, and often expensive permitting system for the Government and applicants. Moreover, agencies will sometimes use their discretion and the time consuming nature of permitting to stall or discourage permit issuance.\n**(4)**\nThere is a compelling interest in avoiding unnecessary delay and expense in Federal permitting.\n**(5)**\nPermit by rule is a process that seeks to overcome agency delay and the cumbersome cost of agency review to Government and private interests.\n**(6)**\nPermit by rule is a process of permitting that includes specific written standards for obtaining a permit, a simple requirement for an applicant to certify compliance with each of the standards, and a streamlined approval process with a prompt deadline for agency action on applications that only allows the Government to verify that all conditions are met. The Government retains the right and responsibility to audit and enforce compliance with permitting requirements. Focusing upon permittees who are violating the law or standards rather than gatekeeping will make permitting more efficient while allowing an agency to protect the compelling interests for which permitting systems are intended.\n#### 3. Permitting by rule\n##### (a) Report to Congress required\n**(1) Submission of report**\nNot later than 240 days after the date of the enactment of this section, the head of each agency shall submit to Congress, including any committee of Congress with jurisdiction over permits for that agency, and the Comptroller General a report on the following:\n**(A)**\nA list and description of each type of permit issued by the agency.\n**(B)**\nThe statutory and regulatory requirements for obtaining each such type of permit.\n**(C)**\nFor each type of permit issued by the agency, a specific description of each step the agency follows to review a permit application.\n**(D)**\nFor each type of permit issued by the agency, an estimate of the time the agency typically takes to review an application, beginning on the date on which an application is submitted and ending on the date on which a successful application is granted.\n**(E)**\nFor each type of permit issued by the agency, a description of each action typically taken for a case in which an application is found not to meet statutory or regulatory requirements for the issuance of a permit.\n**(F)**\nA list of primary interests that each type of permit is intended to foster or protect.\n**(G)**\nAn individual determination for each type of permit issued by the agency of whether permitting by rule could in whole or in part replace the current system for issuing the type of permit.\n**(H)**\nFor each type of permit issued by the agency for which permitting by rule could in whole or in part replace the current system for issuing the type of permit, an identification of any administrative or other practical challenges the head of the agency anticipates in transitioning to permitting by rule for the type of permit.\n**(I)**\nAn identification of each type of permit for which the head of the agency has determined the agency could not reasonably, in whole or in part, issue permits by rule under current facts and circumstances, describing with particularity each reason why permitting by rule could not reasonably be used for any such permit and what legal or practical measures could be pursued to eliminate or mitigate said reason.\n**(2) Public comment**\nIn preparing the report required pursuant to paragraph (1), the head of an agency may solicit and consider public comment regarding the report.\n**(3) Extension of submission deadline**\nIn the case that the head of an agency is not able to submit the report required pursuant to paragraph (1), the deadline to submit the report shall be extended by an additional 90 days if the head of the agency submits to Congress, including any committee of Congress with jurisdiction over permits for that agency, and the Comptroller General a notification of the intended extension of the deadline under this paragraph.\n**(4) Attorney fees**\nIf the head of an agency does not file the report required pursuant to paragraph (1) by the applicable deadline under this subsection, the agency shall pay, from any funds made available to the agency by appropriation or otherwise, the attorney fees and costs of an applicant for a claim filed by the applicant for the failure or delay of the agency to take action with respect to an application for a permit submitted to the agency by the applicant if\u2014\n**(A)**\nthe claim is filed against the agency in an appropriate United States district court during the period beginning on the expiration of the applicable deadline under this subsection and ending on the date on which the agency files the report;\n**(B)**\nthe court determines that the agency unreasonably delayed such action; and\n**(C)**\nthe applicant prevails in the claim.\n##### (b) Establishment of processes for permitting by rule\n**(1) Application for and approval of permits**\nNot later than 12 months after the date on which the report is submitted pursuant to subsection (a), for each type of permit issued by the agency for which the head of the agency determined under subsection (a)(1)(G) that permitting by rule could in whole or in part replace the current system for issuing the type of permit, the head of each agency shall establish by rule a permitting by rule application process that does the following:\n**(A)**\nSpecifies in writing each requirement and substantive standard that must be certified to be met by an applicant who files an application to qualify for a permit under permitting by rule.\n**(B)**\nAllows an applicant to file an application that contains only each required certification described in subparagraph (A) and any supporting documentation the applicant chooses to submit in support of each such certification.\n**(C)**\nDeems an application for a permit under permitting by rule granted if\u2014\n**(i)**\nthe application contains each certification described in subparagraph (A); and\n**(ii)**\na period of 180 days after the date on which the completed application was submitted has expired and the head of the agency has not otherwise approved or disapproved the application.\n**(2) Correction of application**\nThe head of an agency shall contact an applicant within 7 days after the date on which an application is submitted under paragraph (1) if any required certification is missing from the application.\n**(3) Audit of application**\nThe head of an agency may audit an application for a permit under permitting by rule and verify certifications of compliance with requirements and substantive standards for permitting by rule and may include reasonable requests for documentation.\n**(4) Disapproval of application and enforcement**\n**(A) Reason for disapproval**\nThe head of an agency may only disapprove an application submitted for a permit under permitting by rule if the head of the agency identifies a requirement or substantive standard described in paragraph (1)(A) that was not met by the application, informs the applicant of how to correct the application, provides a reasonable opportunity for the applicant to make such correction before the final action of the agency on the application, and states with particularity in any final action disapproving the application the facts and reasoning for such denial.\n**(B) Audit of compliance and enforcement following grant of a permit under permitting by rule**\n**(i) Audit**\nThe head of an agency may audit a permit granted under permitting by rule and verify compliance with requirements and substantive standards for permitting by rule, which may include reasonable requests for documentation.\n**(ii) Enforcement**\nThe head of an agency may require corrective action, suspend, or revoke a permit granted under permitting by rule at any time if the head of the agency finds that a requirement or substantive standard under permitting by rule is not being met by the recipient of the permit.\n**(C) Direct appeal**\nAn applicant whose application for a permit under permitting by rule is disapproved, of whom corrective action is required under a permit granted under permitting by rule, or whose permit granted under permitting by rule is suspended or revoked may appeal such disapproval, corrective action, suspension, or revocation in an appropriate United States district court.\n**(D) Burden of proof**\nIn an appeal under subparagraph (C), the agency shall bear the burden of proof to show that an application was lawfully disapproved or that the agency lawfully required corrective action or suspended or revoked a permit.\n**(E) Attorney fees**\nIf the court finds for the applicant or permit holder under this paragraph and that the agency was not substantially justified in disapproving, requiring corrective action under, suspending, or revoking a permit, the agency shall pay the attorney fees and costs of the applicant from any funds made available to the agency by appropriation or otherwise.\n##### (c) Congressional oversight\nNot later than 2 years after the date on which the report is submitted pursuant to subsection (a), the head of each agency shall submit to Congress a report on the implementation by the agency of permitting by rule for each type of permit issued by the agency for which the head of the agency determined under subsection (a)(1)(G) that permitting by rule could in whole or in part replace the current system for issuing the type of permit.\n##### (d) Concurrent use of previous permitting system\nIf the head of the agency determines in the report submitted pursuant to subsection (a) that the permitting system in effect at the agency before the date of the enactment of this Act for any type of permit provides value that permitting by rule does not, but that permitting by rule could in whole or in part replace the current system for issuing the type of permit, the head of the agency may maintain for that type of permit both the permitting system previously in effect and permitting by rule, and the applicant may choose which system to use to apply for a permit of that type from the agency.\n##### (e) GAO reports\n**(1) Report on accuracy of agency reports**\nNot later than 90 days after the expiration of the deadline to submit the reports required under subsection (a), the Comptroller General shall submit to Congress a report on the completeness and accuracy of the reports, including the recommendations of the Comptroller General concerning legal or practical measures that could be pursued to eliminate or mitigate any legal or practical challenges to the transition by agencies to permitting by rule for any type of permit.\n**(2) Report on progress by agencies**\nNot later than 180 days after submission by the agencies of the reports required under subsection (c), the Comptroller General shall submit to Congress a report on the progress by agencies in the implementation of this Act, including any recommendation concerning legal or practical measures that could be pursued to eliminate or mitigate any remaining legal or practical challenges to the transition by agencies to issuance of permits under permitting by rule for any type of permit.\n**(3) Supplements to the reports**\nThe Comptroller General may submit supplements to the report described in paragraph (1) or (2) with regard to a report submitted by the head of an agency after the Comptroller General submits the report required pursuant to paragraph (1) or (2).\n##### (f) Definitions\nIn this section:\n**(1) Agency; Rule**\nThe terms agency and rule have the meaning given those terms in section 551 of title 5, United States Code.\n**(2) Completed application**\nThe term completed application means an application submitted under subsection (b) that contains certifications that the applicant meets each requirement and substantive standard specified under subsection (b)(1)(A).\n**(3) Permitting by rule**\nThe term permitting by rule means the application process that an agency establishes by rule for granting a certain type of permit described in subsection (b).\n**(4) Substantive standard**\nThe term substantive standard means all qualities, statuses, actions, benchmarks, measurements, or other written descriptions that would qualify a party to perform the permitted action.",
      "versionDate": "2025-01-23",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr689rh.xml",
      "text": "IB\nUnion Calendar No. 303\n119th CONGRESS\n1st Session\nH. R. 689\n[Report No. 119\u2013351]\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Ms. Maloy (for herself, Mr. Finstad , Mr. Moore of Utah , Mr. Valadao , Mr. Arrington , Mr. Owens , Mr. Pfluger , Mr. Ciscomani , Mr. Stauber , Mrs. Fischbach , Mr. Newhouse , Mr. Collins , Mr. Moylan , Mr. Yakym , Mr. Fong , Mr. Gosar , Mr. Fulcher , and Mr. Kennedy of Utah ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nOctober 28, 2025 Additional sponsors: Ms. Hageman and Mr. Hurd of Colorado\nOctober 28, 2025 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on January 23, 2025\nA BILL\nTo require each agency to evaluate the permitting system of the agency, to consider whether permitting by rule could replace that system, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Full Responsibility and Expedited Enforcement Act or the FREE Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAgencies near unanimously operate under a permitting system that gives agencies broad discretion and requires the Government to review each permitting application.\n**(2)**\nAgencies near unanimously operate under a permitting system that either does not have time constraints, or has time constraints that agencies do not follow.\n**(3)**\nThe combination of broad discretion and the lack of time constraints often results in a tedious, time consuming, and often expensive permitting system for the Government and applicants. Moreover, agencies will sometimes use their discretion and the time consuming nature of permitting to stall or discourage permit issuance.\n**(4)**\nThere is a compelling interest in avoiding unnecessary delay and expense in Federal permitting.\n**(5)**\nPermit by rule is a process that seeks to overcome agency delay and the cumbersome cost of agency review to Government and private interests.\n**(6)**\nPermit by rule is a process of permitting that includes specific written standards for obtaining a permit, a simple requirement for an applicant to certify compliance with each of the standards, and a streamlined approval process with a prompt deadline for agency action on applications that only allows the Government to verify that all conditions are met. The Government retains the right and responsibility to audit and enforce compliance with permitting requirements. Focusing upon permittees who are violating the law or standards rather than gatekeeping will make permitting more efficient while allowing an agency to protect the compelling interests for which permitting systems are intended.\n#### 3. Permitting by rule\n##### (a) Office of management and budget guidance\nNot later than 120 days after the date of the enactment of this Act, the Director of the Office of Management and Budget shall issue a memorandum to the head of each agency that establishes guidance for the implementation of the requirements of this section, including on the meaning of the terms permitting by rule and permit .\n##### (b) Report to congress required\n**(1) Submission of report**\nNot later than 240 days after the date on which the guidance required under subsection (a) is issued, the head of each agency shall submit to Congress, including any committee of Congress with jurisdiction over permits for that agency, and the Comptroller General a report on the following:\n**(A)**\nA list and description of each type of permit issued by the agency.\n**(B)**\nThe statutory and regulatory requirements for obtaining each such type of permit.\n**(C)**\nFor each type of permit issued by the agency, a specific description of each step the agency follows to review a permit application.\n**(D)**\nFor each type of permit issued by the agency, an estimate of the time the agency typically takes to review an application, beginning on the date on which an application is submitted and ending on the date on which a successful application is granted.\n**(E)**\nFor each type of permit issued by the agency, a description of each action typically taken for a case in which an application is found not to meet statutory or regulatory requirements for the issuance of a permit.\n**(F)**\nA list of primary interests that each type of permit is intended to foster or protect.\n**(G)**\nAn individual determination for each type of permit issued by the agency of whether permitting by rule could in whole or in part replace the current system for issuing the type of permit.\n**(H)**\nFor each type of permit issued by the agency for which permitting by rule could in whole or in part replace the current system for issuing the type of permit, an identification of any administrative or other practical challenges the head of the agency anticipates in transitioning to permitting by rule for the type of permit.\n**(I)**\nAn identification of each type of permit for which the head of the agency has determined the agency could not reasonably, in whole or in part, issue permits by rule under current facts and circumstances, describing with particularity each reason why permitting by rule could not reasonably be used for any such permit and what legal or practical measures could be pursued to eliminate or mitigate said reason.\n**(2) Public comment**\nIn preparing the report required pursuant to paragraph (1), the head of an agency may solicit and consider public comment regarding the report.\n**(3) Extension of submission deadline**\nIn the case that the head of an agency is not able to submit the report required pursuant to paragraph (1), the deadline to submit the report shall be extended by an additional 90 days if the head of the agency submits to Congress, including any committee of Congress with jurisdiction over permits for that agency, and the Comptroller General a notification of the intended extension of the deadline under this paragraph.\n**(4) Attorney fees**\nIf the head of an agency does not file the report required pursuant to paragraph (1) by the applicable deadline under this subsection, the agency shall pay, from any funds made available to the agency by appropriation or otherwise, the attorney fees and costs of an applicant for a claim filed by the applicant for the failure or delay of the agency to take action with respect to an application for a permit submitted to the agency by the applicant if\u2014\n**(A)**\nthe claim is filed against the agency in an appropriate United States district court during the period beginning on the expiration of the applicable deadline under this subsection and ending on the date on which the agency files the report;\n**(B)**\nthe court determines that the agency unreasonably delayed such action; and\n**(C)**\nthe applicant prevails in the claim.\n##### (c) Establishment of processes for permitting by rule\n**(1) Application for and approval of permits**\nNot later than 12 months after the date on which the report is submitted pursuant to subsection (b), for each type of permit issued by the agency for which the head of the agency determined under subsection (b)(1)(G) that permitting by rule could in whole or in part replace the current system for issuing the type of permit, the head of each agency shall establish by rule a permitting by rule application process that does the following:\n**(A)**\nSpecifies in writing each requirement and substantive standard that must be certified to be met by an applicant who files an application to qualify for a permit under permitting by rule.\n**(B)**\nAllows an applicant to file an application that contains only each required certification described in subparagraph (A) and any supporting documentation the applicant chooses to submit in support of each such certification.\n**(C)**\nDeems an application for a permit under permitting by rule granted if\u2014\n**(i)**\nthe application contains each certification described in subparagraph (A); and\n**(ii)**\na period of 180 days after the date on which the completed application was submitted has expired and the head of the agency has not otherwise approved or disapproved the application.\n**(2) Correction of application**\nThe head of an agency shall contact an applicant within 7 days after the date on which an application is submitted under paragraph (1) if any required certification is missing from the application.\n**(3) Audit of application**\nThe head of an agency may audit an application for a permit under permitting by rule and verify certifications of compliance with requirements and substantive standards for permitting by rule and may include reasonable requests for documentation.\n**(4) Disapproval of application and enforcement**\n**(A) Reason for disapproval**\nThe head of an agency may only disapprove an application submitted for a permit under permitting by rule if the head of the agency identifies a requirement or substantive standard described in paragraph (1)(A) that was not met by the application, informs the applicant of how to correct the application, provides a reasonable opportunity for the applicant to make such correction before the final action of the agency on the application, and states with particularity in any final action disapproving the application the facts and reasoning for such denial.\n**(B) Audit of compliance and enforcement following grant of a permit under permitting by rule**\n**(i) Audit**\nThe head of an agency may audit a permit granted under permitting by rule and verify compliance with requirements and substantive standards for permitting by rule, which may include reasonable requests for documentation.\n**(ii) Enforcement**\nThe head of an agency may require corrective action, suspend, or revoke a permit granted under permitting by rule at any time if the head of the agency finds that a requirement or substantive standard under permitting by rule is not being met by the recipient of the permit.\n**(C) Direct appeal**\nAn applicant whose application for a permit under permitting by rule is disapproved, of whom corrective action is required under a permit granted under permitting by rule, or whose permit granted under permitting by rule is suspended or revoked may appeal such disapproval, corrective action, suspension, or revocation in an appropriate United States district court.\n**(D) Burden of proof**\nIn an appeal under subparagraph (C), the agency shall bear the burden of proof to show that an application was lawfully disapproved or that the agency lawfully required corrective action or suspended or revoked a permit.\n**(E) Attorney fees**\nIf the court finds for the applicant or permit holder under this paragraph and that the agency was not substantially justified in disapproving, requiring corrective action under, suspending, or revoking a permit, the agency shall pay the attorney fees and costs of the applicant from any funds made available to the agency by appropriation or otherwise.\n##### (d) Congressional oversight\nNot later than 2 years after the date on which the report is submitted pursuant to subsection (b), the head of each agency shall submit to Congress a report on the implementation by the agency of permitting by rule for each type of permit issued by the agency for which the head of the agency determined under subsection (b)(1)(G) that permitting by rule could in whole or in part replace the current system for issuing the type of permit.\n##### (e) Concurrent use of previous permitting system\nIf the head of the agency determines in the report submitted pursuant to subsection (b) that the permitting system in effect at the agency before the date of the enactment of this Act for any type of permit provides value that permitting by rule does not, but that permitting by rule could in whole or in part replace the current system for issuing the type of permit, the head of the agency may maintain for that type of permit both the permitting system previously in effect and permitting by rule, and the applicant may choose which system to use to apply for a permit of that type from the agency.\n##### (f) Gao reports\n**(1) Report on accuracy of agency reports**\nNot later than 90 days after the expiration of the deadline to submit the reports required under subsection (b), the Comptroller General shall submit to Congress a report on the completeness and accuracy of the reports, including the recommendations of the Comptroller General concerning legal or practical measures that could be pursued to eliminate or mitigate any legal or practical challenges to the transition by agencies to permitting by rule for any type of permit.\n**(2) Report on progress by agencies**\nNot later than 180 days after submission by the agencies of the reports required under subsection (c), the Comptroller General shall submit to Congress a report on the progress by agencies in the implementation of this Act, including any recommendation concerning legal or practical measures that could be pursued to eliminate or mitigate any remaining legal or practical challenges to the transition by agencies to issuance of permits under permitting by rule for any type of permit.\n**(3) Supplements to the reports**\nThe Comptroller General may submit supplements to the report described in paragraph (1) or (2) with regard to a report submitted by the head of an agency after the Comptroller General submits the report required pursuant to paragraph (1) or (2).\n##### (g) Definitions\nIn this section:\n**(1) Agency; rule**\nThe terms agency and rule have the meaning given those terms in section 551 of title 5, United States Code.\n**(2) Completed application**\nThe term completed application means an application submitted under subsection (c) that contains certifications that the applicant meets each requirement and substantive standard specified under subsection (c)(1)(A).\n**(3) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(4) Permit**\nThe term permit has the meaning given the term license in section 551 of title 5, United States Code, and as further elucidated by the Director in the guidance issued under subsection (a).\n**(5) Permitting by rule**\nThe term permitting by rule means the application process that an agency establishes by rule for granting a certain type of permit described in subsection (b), as further elucidated by the Director in the guidance issued under subsection (a).\n**(6) Substantive standard**\nThe term substantive standard means all qualities, statuses, actions, benchmarks, measurements, or other written descriptions that would qualify a party to perform the permitted action.",
      "versionDate": "2025-10-28",
      "versionType": "Reported in House"
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
        "actionDate": "2025-01-23",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "238",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FREE Act",
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
            "name": "Accounting and auditing",
            "updateDate": "2025-03-19T16:14:28Z"
          },
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-03-19T16:14:28Z"
          },
          {
            "name": "Administrative remedies",
            "updateDate": "2025-03-19T16:14:28Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-19T16:14:28Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2025-03-19T16:14:28Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-03-19T16:14:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-28T20:45:11Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr689ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr689rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "FREE Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-10-29T06:08:15Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Full Responsibility and Expedited Enforcement Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-10-29T06:08:15Z"
    },
    {
      "title": "FREE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:48Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FREE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Full Responsibility and Expedited Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require each agency to evaluate the permitting system of the agency, to consider whether permitting by rule could replace that system, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:35Z"
    }
  ]
}
```
