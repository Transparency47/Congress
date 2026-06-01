# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/697?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/697
- Title: Air Traffic Control Workforce Development Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 697
- Origin chamber: Senate
- Introduced date: 2025-02-24
- Update date: 2026-01-20T15:26:01Z
- Update date including text: 2026-01-20T15:26:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-24: Introduced in Senate
- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-02-24: Introduced in Senate

## Actions

- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/697",
    "number": "697",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "H001061",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hoeven, John [R-ND]",
        "lastName": "Hoeven",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Air Traffic Control Workforce Development Act of 2025",
    "type": "S",
    "updateDate": "2026-01-20T15:26:01Z",
    "updateDateIncludingText": "2026-01-20T15:26:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-24",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T23:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NH"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "KS"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "IL"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "GA"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "ID"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "ID"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "NH"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "MT"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "NJ"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "MS"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s697is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 697\nIN THE SENATE OF THE UNITED STATES\nFebruary 24, 2025 Mr. Hoeven (for himself, Mrs. Shaheen , and Mr. Moran ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend title 49, United States Code, to provide for air traffic control training improvements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Air Traffic Control Workforce Development Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Federal Aviation Administration.\n**(2) FAA**\nThe term FAA means the Federal Aviation Administration.\n#### 3. Collegiate Training Initiative program improvements\n##### (a) In general\nSection 44506(c) of title 49, United States Code, is amended to read as follows:\n(c) Collegiate Training Initiative (1) In general The Administrator of the Federal Aviation Administration shall maintain the Collegiate Training Initiative program (including the Enhanced-Collegiate Training Initiative program) by making new agreements and continuing existing agreements with institutions of higher education (as defined by the Administrator) under which the institutions prepare students for the position of air traffic controller with the Department of Transportation (as defined in section 2109 of title 5). The Administrator may establish standards for the entry of institutions into the program and for their continued participation. (2) Appointment of program graduates The Administrator of the Federal Aviation Administration may appoint an individual who has successfully completed a course of training in a program described in paragraph (1) to the position of air traffic controller noncompetitively in the excepted service (as defined in section 2103 of title 5). An individual appointed under this paragraph serves at the pleasure of the Administrator, subject to section 7511 of title 5. However, an appointment under this paragraph may be converted from one in the excepted service to a career conditional or career appointment in the competitive civil service (as defined in section 2102 of title 5) when the individual achieves full performance level air traffic controller status, as determined by the Administrator. (3) Enhanced-CTI grant program (A) Establishment The Administrator of the Federal Aviation Administration shall establish and carry out a grant program to award grants to institutions of higher education (as defined by the Administrator) that have been approved to, or are seeking to (as determined appropriate by the Administrator), participate in the Enhanced-Collegiate Training Initiative program described in paragraph (1). (B) Grants (i) In general For the purpose of carrying out the grant program established under subparagraph (A), the Secretary shall make grants to institutions of higher education. (ii) Use of funds An institution of higher education shall use a grant awarded under this paragraph for the following purposes: (I) To develop curriculum for the Enhanced-Collegiate Training Initiative program required under paragraph (1). (II) To provide faculty, simulators, and other necessary classroom supplies (including medical certificates and FAA-required tests) to the Enhanced-Collegiate Training Initiative program. (III) For any other purpose determined appropriate by the Administrator of the Federal Aviation Administration. (iii) Eligibility To be eligible to receive a grant under this paragraph, an institution of higher education shall submit an application to the Administrator of the Federal Aviation Administration at such time, in such form, and containing such information as the Administrator may require. (iv) Funding There is authorized to be appropriated $20,000,000 for each of fiscal years 2026 through 2031 to carry out this paragraph. .\n##### (b) Enhanced-Collegiate Training Initiative program faculty annuity supplement\nSection 8421a(c) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by striking ; or and inserting a semicolon;\n**(2)**\nin paragraph (2), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following new paragraph:\n(3) air traffic control instructor, or supervisor thereof, at an institution of higher education participating in the Enhanced-Collegiate Training Initiative program described in section 44506(c) of title 49. .\n##### (c) FAA Academy and Collegiate Training Initiative program curriculum aviation rulemaking committee\n**(1) In general**\nThe Administrator shall convene an aviation rulemaking committee to\u2014\n**(A)**\nreview\u2014\n**(i)**\nthe curricula of the air traffic technical training academy of the FAA, the Collegiate Training Initiative program, and the Enhanced-Collegiate Training Initiative program; and\n**(ii)**\nthe Air Traffic Skills Assessment (in this section referred to as the ATSA ) exam;\n**(B)**\ndevelop findings and recommendations regarding the improvement and modernization of such curricula and the ATSA exam; and\n**(C)**\nprovide to the Administrator a report on such findings and recommendations and for other related purposes as determined by the Administrator.\n**(2) Composition**\nThe aviation rulemaking committee established under paragraph (1) shall consist of members appointed by the Administrator, including representatives of\u2014\n**(A)**\ninstitutions of higher education that are accredited by the Aviation Accreditation Board International;\n**(B)**\naviation industry organizations;\n**(C)**\nFAA subject matter experts;\n**(D)**\nthe exclusive bargaining representative of the air traffic controllers certified under section 7111 of title 5, United States Code; and\n**(E)**\nother aviation safety experts determined appropriate by the Administrator.\n**(3) Considerations**\nThe aviation rulemaking committee established under paragraph (1) shall consider the following:\n**(A)**\nThe advancements in education technology, including digital resources that may be incorporated into a modern curriculum.\n**(B)**\nThe appropriate balance between the use of theoretical knowledge and practical application.\n**(C)**\nA review of instructional techniques to improve the effectiveness of learning outcomes.\n**(D)**\nThe real-world applicability of air traffic operations procedures included in the curriculum.\n**(E)**\nStudent success rates, including outcomes of air traffic controller trainees when placed at facilities for on-the-job training.\n**(F)**\nMethods for reducing the subjectivity of instructional techniques.\n**(G)**\nMethods for improving the ATSA exam to support controller facility placement determinations.\n**(H)**\nStudent success rates correlated to the Collegiate Training Initiative program and the Enhanced-Collegiate Training Initiative program described in section 44506(c) of title 49, United States Code.\n**(I)**\nOther considerations as determined appropriate by the Administrator.\n**(4) Duties**\nThe Administrator shall\u2014\n**(A)**\nnot later than 1 year after the date of enactment of this section, submit to Congress a copy of the aviation rulemaking committee report provided to the Administrator under paragraph (1)(C); and\n**(B)**\nnot later than 180 days after the date of submission of the report under subparagraph (A), in consultation with other agencies as determined appropriate by the Administrator\u2014\n**(i)**\ninitiate a rulemaking activity or make such policy and guidance updates necessary to address any consensus recommendations reached by the aviation rulemaking committee; or\n**(ii)**\nsubmit to Congress a supplemental report with an explanation for each such consensus recommendation not adopted by the Administrator through an action under clause (i).\n**(5) Prohibition on Compensation**\nThe members of the aviation rulemaking committee convened under this subsection shall not receive pay, allowances, or benefits from the Federal Government by reason of their service on such committee.\n#### 4. Air traffic control training improvements and retention incentives\n##### (a) FAA facility training equipment improvements\nSection 415 of the FAA Reauthorization Act of 2024 ( 49 U.S.C. 44506 note) is amended by adding at the end the following new subsection:\n(f) Funding There is authorized to be appropriated $20,000,000 for each of fiscal years 2026 through 2031 for the purpose of the procurement and placement of TSS at air traffic control facilities in the United States, consistent with the requirements of this section. .\n##### (b) Air traffic controller qualification incentives and retention enhancements\nSection 44506 of title 49, United States Code, is amended by adding at the end the following new subsection:\n(g) Retention bonuses (1) CPC qualification incentive The Secretary of Transportation shall establish, in accordance with the requirements described in section 40122(a), a qualification incentive program for trainees for the position of air traffic controller (as defined in section 2109 of title 5, United States Code) with the Department of Transportation. (2) ATC retention incentive The Secretary of Transportation shall establish, in accordance with the requirements described in section 40122(a), a retention incentive program for air traffic controllers (as defined in section 2109 of title 5, United States Code) with the Department of Transportation who are Certified Professional Controllers. .\n#### 5. Other improvements\n##### (a) Air traffic controller mental health improvements\n**(1) In general**\nNot later than 180 days after the date of enactment of this subsection, the Administrator shall establish, in consultation with aviation industry stakeholders and aviation medical professionals, a training course to\u2014\n**(A)**\nsupport the development of mental health providers with an innate knowledge and understanding of the FAA criteria and decision making regarding mental health conditions for air traffic controllers; and\n**(B)**\ndevelop advanced training programs for Aviation Medical Examiners with respect to mental health.\n**(2) Considerations**\nIn establishing the training course under paragraph (1), the Administrator shall consider\u2014\n**(A)**\nthe feasibility of virtual and in-person course offerings; and\n**(B)**\nthe need for an advisory board to ensure continuous improvement of the training course.\n##### (b) Report on the Airport Non-Cooperative Surveillance Radar program\nNot later than 90 days after the date of enactment of this subsection, the Administrator shall submit to the Committees on Commerce, Science, and Transportation and Appropriations of the Senate and the Committees on Transportation and Infrastructure and Appropriations of the House of Representatives a report on the status of the Airport Non-cooperative Surveillance Radar (in this subsection referred to as ANSR ) program, including\u2014\n**(1)**\na determination of funding needs for the ANSR program;\n**(2)**\na cost-benefit analysis of the most effective solutions to provide ongoing ANSR services, including a comparison of a sustainment approach versus a replacement approach;\n**(3)**\nan analysis of how the FAA intends to provide commercial service airports with the necessary equipment, including radar, to detect and mitigate any threat posed by non-cooperative flying objects, including aircraft, unmanned aerial systems, balloons, and other objects determined appropriate by the Administrator;\n**(4)**\nan update on the Radar Divestiture Program;\n**(5)**\nthe projected lifecycle support needs of the existing inventory of non-cooperative Airport Surveillance Radar Models 8, 9, and 11; and\n**(6)**\nany other information determined appropriate by the Administrator.",
      "versionDate": "2025-02-24",
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
        "actionDate": "2025-05-08",
        "text": "Referred to the Subcommittee on Aviation."
      },
      "number": "3270",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Air Traffic Control Workforce Development Act of 2025",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-03-21T13:53:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-24",
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
          "measure-id": "id119s697",
          "measure-number": "697",
          "measure-type": "s",
          "orig-publish-date": "2025-02-24",
          "originChamber": "SENATE",
          "update-date": "2026-01-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s697v00",
            "update-date": "2026-01-20"
          },
          "action-date": "2025-02-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Air Traffic Control Workforce Development Act of 2025</strong></p><p>This bill expands and modifies Air Traffic Control (ATC) workforce training and programs.</p><p>The bill provides statutory authority for the Enhanced Air Traffic-Collegiate Training Initiative (AT-CTI) program. As background, standard AT-CTI institutions of higher education offer nonengineering aviation degrees that teach basic courses in\u00a0ATC and aviation administration, and graduates complete training at the Federal Aviation Administration (FAA) Academy. Students at Enhanced AT-CTI schools are provided with equivalent FAA Academy ATC training and may be placed directly into an ATC facility.</p><p>The bill establishes a grant program for\u00a0schools participating in the Enhanced AT-CTI program and provides for a faculty annuity supplement for ATC instructors at participating institution of higher education.</p><p>The FAA must convene an aviation rulemaking committee to review and provide recommendations on the (1) curricula of the FAA Academy, AT-CTI program,\u00a0and Enhanced AT-CTI program; and (2) Air Traffic Skills Assessment exam.\u00a0Based on the committee's recommendations, the FAA must initiate a rulemaking or make policy and guidance updates, with an exception.</p><p>The bill authorizes funding through FY2031 for the procurement and placement at ATC facilities of Tower Simulator Systems, which are used to train air traffic controllers on airport tower operations.</p><p>The bill also requires</p><ul><li>DOT to establish ATC recruitment and retention incentive programs,</li><li>the FAA to support the development of mental health services training related to conditions for ATCs, and</li><li>the FAA to submit a report to Congress on the status of the Airspace\u00a0Non-cooperative Surveillance Radar program.</li></ul>"
        },
        "title": "Air Traffic Control Workforce Development Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s697.xml",
    "summary": {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Air Traffic Control Workforce Development Act of 2025</strong></p><p>This bill expands and modifies Air Traffic Control (ATC) workforce training and programs.</p><p>The bill provides statutory authority for the Enhanced Air Traffic-Collegiate Training Initiative (AT-CTI) program. As background, standard AT-CTI institutions of higher education offer nonengineering aviation degrees that teach basic courses in\u00a0ATC and aviation administration, and graduates complete training at the Federal Aviation Administration (FAA) Academy. Students at Enhanced AT-CTI schools are provided with equivalent FAA Academy ATC training and may be placed directly into an ATC facility.</p><p>The bill establishes a grant program for\u00a0schools participating in the Enhanced AT-CTI program and provides for a faculty annuity supplement for ATC instructors at participating institution of higher education.</p><p>The FAA must convene an aviation rulemaking committee to review and provide recommendations on the (1) curricula of the FAA Academy, AT-CTI program,\u00a0and Enhanced AT-CTI program; and (2) Air Traffic Skills Assessment exam.\u00a0Based on the committee's recommendations, the FAA must initiate a rulemaking or make policy and guidance updates, with an exception.</p><p>The bill authorizes funding through FY2031 for the procurement and placement at ATC facilities of Tower Simulator Systems, which are used to train air traffic controllers on airport tower operations.</p><p>The bill also requires</p><ul><li>DOT to establish ATC recruitment and retention incentive programs,</li><li>the FAA to support the development of mental health services training related to conditions for ATCs, and</li><li>the FAA to submit a report to Congress on the status of the Airspace\u00a0Non-cooperative Surveillance Radar program.</li></ul>",
      "updateDate": "2026-01-20",
      "versionCode": "id119s697"
    },
    "title": "Air Traffic Control Workforce Development Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Air Traffic Control Workforce Development Act of 2025</strong></p><p>This bill expands and modifies Air Traffic Control (ATC) workforce training and programs.</p><p>The bill provides statutory authority for the Enhanced Air Traffic-Collegiate Training Initiative (AT-CTI) program. As background, standard AT-CTI institutions of higher education offer nonengineering aviation degrees that teach basic courses in\u00a0ATC and aviation administration, and graduates complete training at the Federal Aviation Administration (FAA) Academy. Students at Enhanced AT-CTI schools are provided with equivalent FAA Academy ATC training and may be placed directly into an ATC facility.</p><p>The bill establishes a grant program for\u00a0schools participating in the Enhanced AT-CTI program and provides for a faculty annuity supplement for ATC instructors at participating institution of higher education.</p><p>The FAA must convene an aviation rulemaking committee to review and provide recommendations on the (1) curricula of the FAA Academy, AT-CTI program,\u00a0and Enhanced AT-CTI program; and (2) Air Traffic Skills Assessment exam.\u00a0Based on the committee's recommendations, the FAA must initiate a rulemaking or make policy and guidance updates, with an exception.</p><p>The bill authorizes funding through FY2031 for the procurement and placement at ATC facilities of Tower Simulator Systems, which are used to train air traffic controllers on airport tower operations.</p><p>The bill also requires</p><ul><li>DOT to establish ATC recruitment and retention incentive programs,</li><li>the FAA to support the development of mental health services training related to conditions for ATCs, and</li><li>the FAA to submit a report to Congress on the status of the Airspace\u00a0Non-cooperative Surveillance Radar program.</li></ul>",
      "updateDate": "2026-01-20",
      "versionCode": "id119s697"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s697is.xml"
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
      "title": "Air Traffic Control Workforce Development Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-29T11:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Air Traffic Control Workforce Development Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 49, United States Code, to provide for air traffic control training improvements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T03:18:24Z"
    }
  ]
}
```
