# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8464?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8464
- Title: Stopping Fraudulent Payments Act
- Congress: 119
- Bill type: HR
- Bill number: 8464
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-08T16:14:51Z
- Update date including text: 2026-05-08T16:14:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 23 - 17.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 23 - 17.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8464",
    "number": "8464",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001108",
        "district": "1",
        "firstName": "James",
        "fullName": "Rep. Comer, James [R-KY-1]",
        "lastName": "Comer",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Stopping Fraudulent Payments Act",
    "type": "HR",
    "updateDate": "2026-05-08T16:14:51Z",
    "updateDateIncludingText": "2026-05-08T16:14:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 23 - 17.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-29",
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
      "actionDate": "2026-04-23",
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
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
            "date": "2026-04-29T13:08:20Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-23T13:00:45Z",
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
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "TX"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8464ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8464\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Mr. Comer (for himself and Mr. Arrington ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 31, United States Code, to authorize pausing and segmenting payments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stopping Fraudulent Payments Act .\n#### 2. Authority to pause and segment payments\n##### (a) Treasury payment voucher waiver authority\n**(1) Amendment**\nSubchapter II of chapter 33 of title 31, United States Code, is amended by adding at the end the following:\n3337. Authority to pause and segment payments (a) Agency obligation To pause disbursement requests for corrective action The head of an agency that administers a federally funded financial assistance or public benefit program shall take a corrective action to temporarily delay, condition, or segment a disbursement request before the certification of a payment voucher under section 3325 if, as determined by an official designated by the head of the agency, the agency\u2014 (1) has sufficient reason to determine that the payment presents an elevated risk of fraud based on a fraud-risk indicator or an improper payment resulting in financial loss to the Government as estimated under the requirements of section 3352; or (2) has been notified of an order from the Secretary of the Treasury described under subsection (b). (b) Treasury obligation To return payment voucher and issue corrective action order Except where otherwise required by law, the Secretary of the Treasury shall notify the relevant certifying official of an order to return a certified payment voucher submitted to a disbursing official under section 3325 pursuant to the requirements of this section and issue a corrective action order to the head of an agency if the Secretary of the Treasury determines\u2014 (1) a determination has been made that the payment presents an elevated risk of fraud-based on a fraud-risk indicator or an improper payment under subchapter IV; or (2) a payment payee has been flagged in the Do Not Pay system, as prescribed in guidance prepared by the Secretary of the Treasury, or another Treasury administered payment, account, or payee validation program or service. (c) Agency documentation and time-Limited corrective action An action taken by an agency under subsection (a) shall\u2014 (1) be based on objective, documented fraud-risk indicator; (2) be narrowly applied to the portion of the payment presenting the elevated risk; and (3) be limited in duration to the minimum period of time necessary as determined by the agency to verify eligibility of the payee or accuracy of the payment per the program requirements or as stipulated under another law. (d) Payee notification and time limit of paused disbursement requests With respect to a disbursement request that has been delayed pursuant to subsection (a) or a payment voucher that is returned pursuant subsection (b), the head of the agency shall take the following actions in accordance with any the regulations issued under subsection (i) along with any clarifying guidance issued by the Secretary of the Treasury in consultation with the Director of the Office of Management and Budget: (1) Provide prompt notice to the payee, as appropriate, including a notification that\u2014 (A) a disbursement has been temporarily paused, conditioned, or segmented; (B) identifies the nature of the fraud-risk indicator relied upon by the agency to make the determination; and (C) outline the process for the review period. (2) Establish a process tailored to the specific requirements and design of the agency program for a payee to contest any factual inaccuracy or provide clarifying information during the corrective action review period. (3) Issue such payment not later than 45 days after the determination was made or the agency was notified, but not later than 7 days after the date on which the payee contests the corrective action under the process established pursuant to paragraph (2). (e) Segmentation of low-Risk payments To the maximum extent practicable, the head of each agency shall allow a routine, historically consistent payment amount to proceed while temporarily holding an anomalous, unusually large, or high-risk portion of a payment, or class of payments, pending review and resolution of a corrective action. (f) Exemptions for law enforcement activities The head of an agency, in consultation with the Secretary of the Treasury and the Attorney General, may waive any provision in this section on a case-by-case basis if notified of or instructed by a Federal law enforcement authority, including an agency Inspector General, that the action will jeopardize an active criminal investigation or legal proceeding related to an effort to defraud the Federal Government or violate the False Claims Act ( 31 U.S.C. 3729 et seq. ). (g) Limitation of liability No officer or employee of the Federal Government shall be personally liable for an action taken in good faith under this section. An action taken under this section may not constitute a final determination of eligibility, liability, or wrongdoing on the part of a payee. (h) Rule of construction for program authorizing statute Nothing in this section may be construed to supersede any other provision of law with respect to the statute that authorizes the payment or program the payment is made under. (i) Regulations Not later than 180 days after the date of the enactment of this section, and annually thereafter, the Secretary of the Treasury, in consultation with the Director of the Office of Management and Budget, shall issue regulations and establish procedures to administer the requirements of this section that shall be published in the Federal Register. (j) Routine, historically consistent payment amount defined In this section, the term routine, historically consistent payment amount means a payment amount that is consistent with previous payment history of the payee, established program use patterns, or other objective benchmarks determined by the certifying agency. (k) Fraud-Risk indicator defined In this section, the term fraud-risk indicator means an objective data point or analytic signal that indicates an anomalous payment pattern or increase in the volume of a payment amount, a verified data mismatch, network or behavioral anomaly, or match identified by the Do Not Pay system under section 3354 and any other payment, account, and payee validation program or service provided by the Department of the Treasury that would result in financial loss to the government. .\n**(2) Technical and conforming amendment**\nThe table of sections for chapter 33 of title 31, United States Codes, is amended by inserting after the item for section 3336 the following:\n3337. Authority to pause and segment payments. .\n##### (b) Relief of accountable officers\nSection 3527 of title 31, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(2), by inserting after the loss or deficiency was not the result of an illegal or incorrect payment the following: , or was made as a result of a good faith effort to comply with the requirements of section 3337 ; and\n**(2)**\nin subsection (b)(1)(A)(ii), by inserting after the loss or deficiency was not the result of an illegal or incorrect payment the following: , or was made as a result of a good faith effort to comply with the requirements of section 3337 .",
      "versionDate": "2026-04-23",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2026-05-08T16:14:43Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-05-08T16:14:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-04T22:46:56Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8464ih.xml"
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
      "title": "Stopping Fraudulent Payments Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-01T08:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stopping Fraudulent Payments Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-01T08:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 31, United States Code, to authorize pausing and segmenting payments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-01T08:48:42Z"
    }
  ]
}
```
