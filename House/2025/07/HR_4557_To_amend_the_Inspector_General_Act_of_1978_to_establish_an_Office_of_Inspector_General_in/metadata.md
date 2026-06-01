# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4557?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4557
- Title: BEACON Act
- Congress: 119
- Bill type: HR
- Bill number: 4557
- Origin chamber: House
- Introduced date: 2025-07-21
- Update date: 2026-03-31T22:59:48Z
- Update date including text: 2026-03-31T22:59:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-21: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-07-21: Introduced in House

## Actions

- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4557",
    "number": "4557",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "D000216",
        "district": "3",
        "firstName": "Rosa",
        "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
        "lastName": "DeLauro",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "BEACON Act",
    "type": "HR",
    "updateDate": "2026-03-31T22:59:48Z",
    "updateDateIncludingText": "2026-03-31T22:59:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-21",
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
      "actionDate": "2025-07-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-21",
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
          "date": "2025-07-21T16:03:15Z",
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
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "VA"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "MI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "DC"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4557ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4557\nIN THE HOUSE OF REPRESENTATIVES\nJuly 21, 2025 Ms. DeLauro (for herself, Mr. Vindman , and Ms. Scholten ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend the Inspector General Act of 1978 to establish an Office of Inspector General in the Executive Office of the President, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bringing Executive Accountability, Clarity, and Oversight Now Act or the BEACON Act .\n#### 2. Office of Inspector General in the Executive Office of the President\n##### (a) Establishment\n**(1) In general**\nSection 401 of title 5, United States Code (commonly referred to as the Inspector General Act of 1978 ) is amended\u2014\n**(A)**\nin paragraph (1), by striking or the National Reconnaissance Office and inserting the National Reconnaissance Office, or the Executive Office of the President ; and\n**(B)**\nin paragraph (3), by striking or the Director of the National Reconnaissance Office and inserting the Director of the National Reconnaissance Office; or the President (with respect to the Executive Office of the President) .\n**(2) Appointment of Inspector General**\nNot later than 120 days after the date of enactment of this Act, the President shall appoint an individual as the Inspector General of the Executive Office of the President in accordance with the requirements of section 403(a) of title 5, United States Code.\n##### (b) Special provisions\nChapter 4 of title 5, United States Code, is amended by inserting after section 424 the following:\n425. Special provisions concerning the Executive Office of the President (a) Audits, investigations, and issuance of subpoenas (1) Authority, direction, and control Notwithstanding the last 2 sentences of section 403(a), the Inspector General of the Executive Office of the President shall be under the authority, direction, and control of the President with respect to audits or investigations, or the issuance of subpoenas, that require access to information concerning any of the following: (A) The identity of a confidential source, including a protected witness. (B) An intelligence or counterintelligence matter. (C) An undercover operation. (2) Prohibition in certain situations With respect to the information described in paragraph (1), the President may prohibit the Inspector General of the Executive Office of the President from initiating, carrying out, or completing any audit or investigation, or from issuing any subpoena, after the Inspector General has decided to initiate, carry out, or complete such audit or investigation, or to issue such subpoena, if the President determines that such prohibition is necessary to prevent the disclosure of any information described in paragraph (1). (3) Notice after prohibition (A) To Inspector General If the President exercises any power under paragraph (2), not later than 30 days after exercising any such power, the President shall notify the Inspector General of the Executive Office of the President in writing, stating the reasons for exercising that power. (B) To Congress Not later than 30 days after receiving a notice under subparagraph (A), the Inspector General of the Executive Office of the President shall transmit a copy of the notice to the chair and ranking member of each of the following: (i) The Committee on Homeland Security and Governmental Affairs of the Senate . (ii) The Committee on the Judiciary of the Senate . (iii) The Committee on Oversight and Government Reform of the House of Representatives . (iv) The Committee on the Judiciary of the House of Representatives . (v) Any other appropriate committee or subcommittee of Congress. (b) Semiannual reports (1) Additional information to be included Any semiannual report prepared by the Inspector General of the Executive Office of the President under section 405(b) shall also include the following: (A) With respect to each significant recommendation on which corrective action has been completed, a description of the corrective action. (B) A certification of whether the Inspector General of the Executive Office of the President has had full and direct access to all information relevant to the performance of the functions of the Inspector General. (C) A description of any audit, inspection, or evaluation occurring during the reporting period in which the Inspector General of the Executive Office of the President could not obtain relevant information due to an exercise of power by the President under subsection (a)(2). (D) Such recommendations as the Inspector General of the Executive Office of the President considers appropriate with respect to efficiency in the administration of programs and operations undertaken by the President, and the detection and elimination of fraud, waste, and abuse in such programs and operations. (2) Submission to President Notwithstanding section 405(c), the Inspector General of the Executive Office of the President shall submit to the President the semiannual reports prepared under section 405(b), including the additional information required under paragraph (1), not later than April 30 and October 31 of each year. (3) Transmission to Congress Not later than 30 days after submitting the semiannual report to the President under paragraph (2), the Inspector General of the Executive Office of the President shall transmit the semiannual report to the chair and ranking member of each of the following: (A) The Committee on Homeland Security and Governmental Affairs of the Senate . (B) The Committee on the Judiciary of the Senate . (C) The Committee on Oversight and Government Reform of the House of Representatives . (D) The Committee on the Judiciary of the House of Representatives . (c) Audit of the Office of the Inspector General of the Executive Office of the President (1) In general Not later than 120 days after the President appoints an individual as the Inspector General of the Executive Office of the President, and annually thereafter, the Council of Inspectors General on Integrity and Efficiency shall conduct an audit of the Office of the Inspector General of the Executive Office of the President to ensure that the office is able to effectively provide oversight of the Executive Office of the President. (2) Report Not later than October 31 after the first audit is completed under paragraph (1), and annually thereafter, the Council of Inspectors General on Integrity and Efficiency shall submit to Congress a report on the findings of the audit. .\n##### (c) Technical and conforming amendments\n**(1) In general**\nChapter 4 of title 5, United States Code, is amended\u2014\n**(A)**\nin section 415(a)(2)\u2014\n**(i)**\nby striking subparagraph (C); and\n**(ii)**\nby redesignating subparagraphs (D) through (F) as subparagraphs (C) through (E), respectively; and\n**(B)**\nin section 418, by striking or 421 and inserting , 421, or 425 .\n**(2) Table of sections**\nThe table of sections for chapter 4 of title 5, United States Code, is amended by adding at the end the following:\n425. Special provisions concerning the Executive Office of the President. .\n##### (d) Over-Classification audit\n**(1) Evaluations required**\nThe Inspector General of the Executive Office of the President, in consultation with the Information Security Oversight Office of the National Archives and Records Administration, shall carry out 2 evaluations of the Executive Office of the President\u2014\n**(A)**\nto assess whether applicable classification policies, procedures, rules, and regulations have been adopted, followed, and effectively administered within the Executive Office of the President; and\n**(B)**\nto identify policies, procedures, rules, regulations, or management practices that may be contributing to persistent misclassification of material within the Executive Office of the President.\n**(2) Deadlines for evaluations**\n**(A) Initial evaluation**\nThe first evaluation required under paragraph (1) shall be completed not later than 1 year after the date of enactment of this Act.\n**(B) Second evaluation**\nThe second evaluation required under paragraph (1) shall review progress made pursuant to the results of the first evaluation and shall be completed not later than 1 year after the date on which the first evaluation is completed.\n**(3) Coordination**\nThe Inspector General of the Executive Office of the President shall coordinate with other Inspectors General and the Information Security Oversight Office to ensure that evaluations follow a consistent methodology, as appropriate, that allows for cross-agency comparisons.\n**(4) Reports required**\n**(A) In general**\nNot later than 45 days after the completion of an evaluation, the Inspector General of the Executive Office of the President shall submit to the appropriate entities a report on that evaluation.\n**(B) Content**\nEach report submitted under subparagraph (A) shall include a description of\u2014\n**(i)**\nthe policies, procedures, rules, regulations, or management practices, if any, identified by the Inspector General under paragraph (1)(B); and\n**(ii)**\nthe recommendations, if any, of the Inspector General to address any such identified policies, procedures, rules, regulations, or management practices.\n**(5) Appropriate entities defined**\nIn this subsection, the term appropriate entities means each of the following:\n**(A)**\nThe Committee on Homeland Security and Governmental Affairs of the Senate .\n**(B)**\nThe Committee on the Judiciary of the Senate .\n**(C)**\nThe Committee on Oversight and Government Reform of the House of Representatives .\n**(D)**\nThe Committee on the Judiciary of the House of Representatives .\n**(E)**\nAny other appropriate committee or subcommittee of Congress.\n**(F)**\nThe President.\n**(G)**\nThe Director of the Information Security Oversight Office.",
      "versionDate": "2025-07-21",
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
        "actionDate": "2025-09-17",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "2838",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protecting Our Democracy Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-09",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "2219",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "BEACON Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-17T20:51:34Z"
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
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4557ih.xml"
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
      "title": "BEACON Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T09:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BEACON Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T09:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bringing Executive Accountability, Clarity, and Oversight Now Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T09:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Inspector General Act of 1978 to establish an Office of Inspector General in the Executive Office of the President, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T09:33:17Z"
    }
  ]
}
```
