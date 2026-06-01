# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4126?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4126
- Title: ARMS Act
- Congress: 119
- Bill type: HR
- Bill number: 4126
- Origin chamber: House
- Introduced date: 2025-06-25
- Update date: 2026-05-16T08:07:24Z
- Update date including text: 2026-05-16T08:07:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-25: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-06-26 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.
- Latest action: 2025-06-25: Introduced in House

## Actions

- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-06-26 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4126",
    "number": "4126",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001132",
        "district": "2",
        "firstName": "Elijah",
        "fullName": "Rep. Crane, Elijah [R-AZ-2]",
        "lastName": "Crane",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "ARMS Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:24Z",
    "updateDateIncludingText": "2026-05-16T08:07:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Transportation and Maritime Security.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-25",
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
          "date": "2025-06-25T14:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-26T20:26:24Z",
              "name": "Referred to"
            }
          },
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4126ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4126\nIN THE HOUSE OF REPRESENTATIVES\nJune 25, 2025 Mr. Crane introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo direct the Transportation Security Administration to carry out covert testing and risk mitigation improvement of aviation security operations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Aviation Risk Mitigation and Security Act or the ARMS Act .\n#### 2. TSA covert testing and risk mitigation improvement\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Administrator of the Transportation Security Administration (TSA) shall establish the following to strengthen aviation security operations:\n**(1)**\nIn accordance with subsection (b), a system for conducting risk-informed, headquarters-based covert testing project scenarios for aviation security operations, including relating to airport passenger and baggage security screening operations, that can yield statistically valid data that can be utilized to identify and assess the nature and extent of any vulnerabilities to such operations that are not mitigated by current security operations.\n**(2)**\nA long-term headquarters-based covert testing program, employing static but risk-informed threat vectors, based on annual risk assessments of emerging threats, designed to assess the effectiveness of aviation security operations on an annual basis.\n##### (b) Methodology\nThe Administrator of the TSA shall conduct the risk-informed, headquarters-based covert testing project scenarios for aviation security operations under paragraph (1) of subsection (a) based on annual risk assessments of emerging threats. The Administrator shall\u2014\n**(1)**\nconduct not fewer than three such covert testing project scenarios to identify any systemic vulnerabilities in aviation security operations, and ensure that each Category X airport in the United States is included in such covert testing project scenarios at least once per fiscal year; and\n**(2)**\ndocument the methodology, assumptions, and rationale guiding the selection and execution of such covert testing project scenarios to ensure statistical validity and actionable results.\n##### (c) Mitigation\n**(1) In general**\nThe Administrator of the TSA shall establish a process to address and mitigate any vulnerabilities to aviation security operations identified and assessed pursuant to the covert testing project scenarios conducted under paragraph (1) of subsection (a).\n**(2) Analysis**\nNot later than 90 days after identifying a vulnerability referred to in paragraph (1), the Administrator of the TSA shall conduct a root cause analysis to determine the origin and contributing factors relating to such vulnerability.\n**(3) Determination**\nNot later than 150 days after conducting the analysis under paragraph (2), the Administrator of the TSA shall make a determination regarding whether or not to mitigate the vulnerability referred to in such paragraph, and shall prioritize mitigating such vulnerability based on the ability to reduce risk. If the Administrator determines\u2014\n**(A)**\nto not mitigate such vulnerability, the Administrator shall document the justification relating thereto; or\n**(B)**\nto mitigate such vulnerability, the Administrator shall establish and document\u2014\n**(i)**\nkey milestones appropriate for the level of effort required to so mitigate such vulnerability; and\n**(ii)**\na date by which measures to so mitigate such vulnerability shall be implemented by the TSA.\n**(4) Retesting**\nNot later than 180 days after the date on which measures to mitigate a vulnerability are completed by the TSA pursuant to paragraph (3)(B)(ii), and to the extent applicable, the Administrator of the TSA shall conduct a covert testing project scenario in accordance with subsection (a)(1) for the aviation security operation with respect to which such vulnerability was identified to assess the effectiveness of such measures to mitigate such vulnerability.\n##### (d) Annual reporting\n**(1) Compilation of test results**\nNot later than November 30 of the first full fiscal year that begins after the date of the enactment of this Act and annually thereafter, the Administrator of the TSA, in consultation with the Secretary of Homeland Security, shall produce a report detailing the results of all covert testing project scenarios for aviation security operations under subsection (a)(1) conducted in the immediately preceding fiscal year by the TSA. Each such report shall\u2014\n**(A)**\nbe submitted in unclassified form, but may contain a classified annex in accordance with paragraph (2); and\n**(B)**\ninclude\u2014\n**(i)**\na summary of all vulnerabilities to aviation security operations that were identified and the respective dates of such identifications;\n**(ii)**\nthe status of mitigation efforts under subsection (c), including key milestones and expected completion dates;\n**(iii)**\nthe results of retesting under such subsection on previously mitigated vulnerabilities;\n**(iv)**\njustifications for vulnerabilities that remain unmitigated under such subsection, and a determination of whether full mitigation is feasible; and\n**(v)**\nan assessment of security improvements based on covert testing data trends.\n**(2) Submission to Congress**\nThe Administrator of the TSA shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate each report required under paragraph (1) together with the Transportation Security Administration\u2019s annual budget request. Each such report may include classified and sensitive security information, and any such information shall be submitted as a classified annex.\n**(3) Public disclosure of covert testing performance at Category X airports**\n**(A) In general**\nNot later than November 30 of the first full fiscal year that begins after the date of the enactment of this Act and annually thereafter, the Administrator of the TSA shall publish, and maintain on a publicly accessible website of the TSA, a summary of performance data acquired as a result of covert testing project scenarios conducted at Category X airports under subsection (b)(1) during the immediately preceding fiscal year. Each such summary shall\u2014\n**(i)**\ninclude, at a minimum\u2014\n**(I)**\nthe total number of tests carried out as part of such covert testing project scenarios conducted at Category X airports;\n**(II)**\nthe aggregate pass rate and failure rate, expressed as percentages, for all such covert tests, calculated across all tested locations and covert testing project scenarios; and\n**(III)**\ngeneral observations or trend data regarding changes in performance compared to the prior fiscal year; and\n**(ii)**\nnot include test scenario details, methodologies, or airport-specific data that could compromise aviation security operations.\n**(B) Exception**\nClause (ii) of subparagraph (A) shall not apply with respect to summary-level statistics regarding the overall performance of TSA screening operations at Category X airports for purposes of public availability of the annual summaries under such subparagraph.\n##### (e) GAO review\nNot later than three years after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the Administrator of the TSA, the Committee on Homeland Security of the House of Representatives, and the Committee on Commerce, Science, and Transportation of the Senate a report on the effectiveness of the TSA\u2019s processes for conducting covert testing that yields statistically valid data that can be utilized to assess the nature and extent of any vulnerabilities to aviation security operations that are not effectively mitigated by current security operations.",
      "versionDate": "2025-06-25",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-07-17T11:06:12Z"
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
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4126ih.xml"
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
      "title": "ARMS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:48Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ARMS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-09T06:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Aviation Risk Mitigation and Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-09T06:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Transportation Security Administration to carry out covert testing and risk mitigation improvement of aviation security operations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-09T06:49:12Z"
    }
  ]
}
```
