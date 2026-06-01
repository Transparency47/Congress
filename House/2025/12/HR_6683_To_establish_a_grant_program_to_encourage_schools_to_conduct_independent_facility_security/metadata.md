# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6683?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6683
- Title: Safer Schools Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6683
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-04-06T19:37:28Z
- Update date including text: 2026-04-06T19:37:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6683",
    "number": "6683",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "W000816",
        "district": "25",
        "firstName": "Roger",
        "fullName": "Rep. Williams, Roger [R-TX-25]",
        "lastName": "Williams",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Safer Schools Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-06T19:37:28Z",
    "updateDateIncludingText": "2026-04-06T19:37:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-11T16:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "FL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "NC"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6683ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6683\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Williams of Texas (for himself and Mr. Moskowitz ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a grant program to encourage schools to conduct independent facility security risk assessments and make hard security improvements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safer Schools Act of 2025 .\n#### 2. Pilot program for grants for independent facility security risk assessments and hard security improvements\n##### (a) Establishment\nNot later than 120 days after the date of the enactment of this Act the Attorney General shall establish a pilot program (hereinafter referred to as the pilot program ) to issue grants pursuant to subsections (b) and (c), including releasing guidelines and applications with respect to such grant programs.\n##### (b) Independent facility security risk assessment grants\n**(1) In general**\nBeginning not later than 180 days after the date of enactment of this section, the Attorney General shall award grants to public schools to have independent facility security risk assessments performed.\n**(2) Application**\n**(A) In general**\nTo be eligible to receive a grant under this section, a public school shall submit to the Attorney General an application at such time, in such manner, and containing such information as the Attorney General may require, including\u2014\n**(i)**\nthe size of the school;\n**(ii)**\na comprehensive report on the financial state of the school, including any Federal, State, or local funds used in the school\u2019s budget; and\n**(iii)**\na certification to the Attorney General that the school is unable to cover the cost of an independent facility security risk assessment without the grant awarded under this section.\n**(B) Priority**\nThe Attorney General, in awarding a grant under this section, shall give priority to applications of public schools that have experienced an event in which an individual inflicts deadly harm or attempts to inflict deadly harm against multiple individuals.\n**(3) Ineligibility**\n**(A) In general**\nA public school shall be ineligible to receive a grant under this section if it\u2014\n**(i)**\nreceived a grant under this section in the previous 5 fiscal years; or\n**(ii)**\nreceives a grant under this section in the same fiscal year.\n**(B) Exception**\nNotwithstanding paragraph (1), in the case that a grant recipient experiences an event in which an individual inflicts deadly harm or attempts to inflict deadly harm against multiple individuals, such grant recipient shall be eligible to receive an additional grant under this section in the fiscal year after the date of the event.\n##### (c) Hard security improvement grants\n**(1) In general**\nBeginning not later than 180 days after the date of enactment of this section, the Attorney General shall award grants to public schools for the purpose of making hard security improvements to schools.\n**(2) Application**\n**(A) In general**\nTo be eligible to receive a grant under this section, a public school shall submit to the Attorney General an application at such time, in such manner, and containing such information as the Attorney General may require, which application shall include\u2014\n**(i)**\nthe size of the school;\n**(ii)**\na comprehensive report on the financial state of the school, including any Federal, State, or local funds used in the school\u2019s budget;\n**(iii)**\na comprehensive description of previous improvements made to the school meant to address school security related vulnerabilities;\n**(iv)**\nthe specific products and services that will be purchased with the grant funds and an estimate of such costs and services; and\n**(v)**\nthe results of the school\u2019s most recent independent facility security risk assessment.\n**(B) Priority**\nThe Attorney General, in awarding a grant under this section, shall give priority to applications of schools that have experienced an event in which an individual inflicts deadly harm or attempts to inflict deadly harm against multiple individuals.\n**(3) Ineligibility**\n**(A) In general**\nA public school shall be ineligible to receive a grant under this section if\u2014\n**(i)**\na public school received a grant under this section in the previous 5 fiscal years; or\n**(ii)**\na public school receives a grant under this section in the same fiscal year.\n**(B) Exception**\nNotwithstanding paragraph (1), in the case that a grant recipient experiences an event in which an individual inflicts deadly harm or attempts to inflict deadly harm against multiple individuals, such grant recipient shall be eligible to receive an additional grant under this section in any fiscal year after the date on which the event occurred.\n**(4) Matching funds**\n**(A) In general**\nThe Federal share of a grant received under this subsection may not exceed 50 percent of the hard security improvement costs.\n**(B) Waiver**\nThe Attorney General may waive in whole or in part, the matching requirement under paragraph (1) in the case that the recipient has a financial need for such waiver.\n**(5) Grant conditions**\nA recipient of a grant under this section shall\u2014\n**(A)**\nuse the grant to make hard security improvements identified as necessary by the most recent independent facility security risk assessment;\n**(B)**\nin the case that a panic alarm is not installed or operable according to the independent facility risk assessment, use the grant for the installation of at least 1 panic alarm for use in a school security emergency, including a non-fire evacuation, lockdown, or active shooter situation, which alarm\u2014\n**(i)**\nshall be directly linked to the local law enforcement agency that is closest in proximity to the grant recipient;\n**(ii)**\nshall immediately transmit a signal or message to such law enforcement agency upon activation; and\n**(iii)**\nshall not be audible within the public school building;\n**(C)**\nbefore entering into a contract with a vendor, obtain written confirmation from the law enforcement agency or entity that conducted the independent facility security risk assessment that the improvement will mitigate a vulnerability identified in the independent facility security risk assessment; and\n**(D)**\nensure that hard security improvements comply with local building code requirements and standards.\n##### (d) Information dissemination\n**(1) In general**\nThe Attorney General shall disseminate to each local educational agency in the United States information about the availability of grants under this section.\n**(2) Event notice**\nNot later than 30 days after an event in which an individual inflicts deadly harm or attempts to inflict deadly harm against multiple individuals occurs in a public school, the Director shall contact verbally the head of such public school to provide notice of priority eligibility for grants under this section and to offer technical assistance in navigating the application process.\n##### (e) Reports\n**(1) Grant recipient report**\nNot later than one year after receiving a grant under subsection (b) or (c), a recipient shall submit to the Attorney General\u2014\n**(A)**\na copy of the results of each security assessment with how many vulnerabilities were found;\n**(B)**\na list of each hard improvement made and the percentage of vulnerabilities fixed, including the percentage of vulnerabilities outstanding;\n**(C)**\na list of the number of events in which an individual inflicts deadly harm or attempts to inflict deadly harm against multiple individuals, if any, that happened five years before hard security vulnerabilities were fixed or one year after the hard security vulnerabilities were made; and\n**(D)**\na survey assessing how safe students and facility members feel on the school\u2019s campus before hard security improvements were made and one year after they were made.\n**(2) Attorney General Report**\nNot later than two years after the date of enactment, and annually thereafter, the Attorney General shall submit to appropriate Congressional committees a report on the national state of physical security in schools, including\u2014\n**(A)**\nthe contents of grant recipient reports under paragraph (1);\n**(B)**\na percentage breakdown of the type of hard security fixes;\n**(C)**\nthe percentage of outstanding vulnerabilities remaining;\n**(D)**\na percentage breakdown of each type of hard security improvements made; and\n**(E)**\nthe average percentage of vulnerabilities fixed and average percentage of vulnerabilities outstanding after the hard security improvements were made.\n##### (f) Sunset\nThe pilot program shall terminate on the date that is five years after the date on which the pilot program is established.\n##### (g) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means the Committee on the Judiciary and the Committee on Education and Workforce of the House of Representatives and the Committee on the Judiciary and the Committee on Health, Education, Labor, and Pensions of the Senate.\n**(2) Hard security improvements**\nThe term hard security improvements means improvements to the infrastructure of school property perimeter, parking lot perimeter, building perimeter, entrance and exit points of the school building, video monitoring equipment, alert notification equipment, the interior and perimeter of the classroom, and any other physical improvements related to camera systems and related hardware, alarm and notification technology, and visitor management technologies deemed eligible for improvement by the Attorney General.\n**(3) Independent facility security risk assessment**\nThe term independent facility security risk assessment means an assessment that\u2014\n**(A)**\nidentifies active shooter and related security vulnerabilities of public schools, considering security factors, including the strength and maintenance levels of the property perimeter, parking lot perimeter, building perimeter, and classroom and interior perimeter, and the presence of a silent security system signal generated by the manual activation of a device intended to signal a life-threatening or emergency situation requiring a response from law enforcement; and\n**(B)**\nis conducted by a Federal, State, or local entity determined to be qualified by the Department of Justice\u2019s Bureau of Justice Assistance.\n**(4) Public school**\nThe term public school means a public elementary school or a public secondary school, including an elementary school or a secondary school that is predominately funded by an Indian tribal government.\n##### (h) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to carry out the pilot program\u2014\n**(A)**\n$100,000,000 for fiscal year one of the pilot program;\n**(B)**\n$200,000,000 for fiscal year two of the pilot program; and\n**(C)**\n$300,000,000 for fiscal years three through five of the pilot program.\n**(2) Allocation of funds**\nAny funds authorized under paragraph (1) shall be allocated\u2014\n**(A)**\nwith 30 percent of any such funds to the grant program under section 2(b); and\n**(B)**\nwith 70 percent of any such funds to the grant program under section 2(c).",
      "versionDate": "2025-12-11",
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
        "name": "Education",
        "updateDate": "2026-01-09T16:29:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-11",
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
          "measure-id": "id119hr6683",
          "measure-number": "6683",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-11",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6683v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-12-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Safer Schools Act of </strong><strong>2025</strong></p><p>This bill establishes a pilot program through which the Department of Justice must award grants to public elementary and secondary schools to conduct independent facility security risk assessments and make hard security improvements (e.g., video monitoring and alert notification equipment).</p>"
        },
        "title": "Safer Schools Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6683.xml",
    "summary": {
      "actionDate": "2025-12-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safer Schools Act of </strong><strong>2025</strong></p><p>This bill establishes a pilot program through which the Department of Justice must award grants to public elementary and secondary schools to conduct independent facility security risk assessments and make hard security improvements (e.g., video monitoring and alert notification equipment).</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr6683"
    },
    "title": "Safer Schools Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-12-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safer Schools Act of </strong><strong>2025</strong></p><p>This bill establishes a pilot program through which the Department of Justice must award grants to public elementary and secondary schools to conduct independent facility security risk assessments and make hard security improvements (e.g., video monitoring and alert notification equipment).</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr6683"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6683ih.xml"
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
      "title": "Safer Schools Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-08T09:53:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safer Schools Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-08T09:53:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a grant program to encourage schools to conduct independent facility security risk assessments and make hard security improvements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-08T09:48:30Z"
    }
  ]
}
```
