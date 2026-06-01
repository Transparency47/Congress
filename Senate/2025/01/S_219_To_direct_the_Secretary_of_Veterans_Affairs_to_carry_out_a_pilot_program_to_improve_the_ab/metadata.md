# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/219?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/219
- Title: Veterans Health Care Freedom Act
- Congress: 119
- Bill type: S
- Bill number: 219
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2026-04-15T11:03:26Z
- Update date including text: 2026-04-15T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/219",
    "number": "219",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Veterans Health Care Freedom Act",
    "type": "S",
    "updateDate": "2026-04-15T11:03:26Z",
    "updateDateIncludingText": "2026-04-15T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
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
        "item": [
          {
            "date": "2025-05-21T20:00:02Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-21T20:00:02Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-01-23T18:40:36Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AL"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ND"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "SD"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
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
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "MT"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s219is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 219\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mrs. Blackburn (for herself, Mr. Tuberville , Mr. Cramer , Mr. Wicker , Mr. Rounds , Mr. Cruz , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to carry out a pilot program to improve the ability of veterans to access medical care in medical facilities of the Department of Veterans Affairs and in the community by providing veterans the ability to choose health care providers.\n#### 1. Short title\nThis Act may be cited as the Veterans Health Care Freedom Act .\n#### 2. Pilot program on ability of veterans to choose health care providers\n##### (a) Pilot program\n**(1) Requirement**\nThe Secretary of Veterans Affairs, acting through the Center for Innovation for Care and Payment of the Department of Veterans Affairs, shall carry out a pilot program to improve the ability of eligible veterans to access hospital care, medical services, and extended care services through the covered care system by providing eligible veterans the ability to choose health care providers.\n**(2) Locations**\nThe Secretary shall select a minimum of four Veterans Integrated Service Networks in which to carry out the pilot program.\n##### (b) Removal of certain requirements To access care\nIn carrying out the pilot program, the Secretary shall furnish hospital care, medical services, and extended care services to eligible veterans through the covered care system as follows:\n**(1)**\nAt medical facilities of the Department of Veterans Affairs, regardless of whether the facility is in the same Veterans Integrated Service Network as the Network in which the veteran resides.\n**(2)**\nAt non-Department facilities pursuant to, as appropriate\u2014\n**(A)**\nsection 1703 of title 38, United States Code, without regard to the requirements specified in subsection (d) of such section; or\n**(B)**\nsection 1703A of such title, without regard to whether the care or service is not feasibly available to the eligible veteran from a facility of the Department or through a contract or sharing agreement entered into pursuant to a provision of law other than such section as required under subparagraphs (A) and (C) of subsection (a)(1) of such section.\n##### (c) Election of veteran\nIn accordance with subsections (d) and (e), an eligible veteran participating in the pilot program may elect to receive hospital care, medical services, and extended care services at any provider in the covered care system.\n##### (d) Coordination of care\n**(1) Selection**\nEach eligible veteran participating in the pilot program shall select a primary care provider in the covered care system.\n**(2) Coordination**\nThe primary care provider of an eligible veteran selected under paragraph (1) shall\u2014\n**(A)**\ncoordinate with the Secretary and other health care providers with respect to the hospital care, medical services, and extended care services furnished to the veteran under the pilot program; and\n**(B)**\nrefer the veteran to specialty care providers in the covered care system, as clinically necessary.\n**(3) Systems**\nThe Secretary shall establish systems as the Secretary determines appropriate to ensure that a primary care provider can effectively coordinate the hospital care, medical services, and extended care services furnished to a veteran under the pilot program.\n##### (e) Specialty care\n**(1) Access**\nSubject to subsection (d)(2)(B), an eligible veteran participating in the pilot program may select any specialty care provider in the covered care system from which to receive specialty care.\n**(2) Designation**\nThe Secretary may designate a specialty care provider as a primary care provider of an eligible veteran participating in the pilot program if the Secretary determines that such designation is in the health interests of the veteran (such as an endocrinologist with respect to a veteran diagnosed with diabetes, a neurologist with respect to a veteran diagnosed with Parkinson\u2019s disease, or an obstetrician-gynecologist with respect to a female veteran).\n##### (f) Mental health care\nAn eligible veteran participating in the pilot program may select a mental health care provider in the covered care system from which to receive mental health care.\n##### (g) Information\nIn carrying out the pilot program, the Secretary shall furnish to eligible veterans the information on eligibility, cost sharing, treatments, and providers required for veterans to make informed decisions with respect to\u2014\n**(1)**\nselecting primary care providers and specialty care providers; and\n**(2)**\ntreatments available to the veteran.\n##### (h) Duration\n**(1) Phase in**\nThe Secretary shall carry out the pilot program during the three-year period beginning on the date that is one year after the date of the enactment of this Act.\n**(2) Permanent requirement**\n**(A) Veterans Community Care Program**\nSection 1703(d) of title 38, United States Code, is amended\u2014\n**(i)**\nin paragraph (1), by striking The Secretary shall and inserting Except as provided by paragraph (4), the Secretary shall ; and\n**(ii)**\nby adding at the end the following new paragraph:\n(5) Beginning on the date that is four years after the date of the enactment of the Veterans Health Care Freedom Act \u2014 (A) the requirements under paragraphs (1), (2), (3), and (4) shall not apply with respect to furnishing hospital care, medical services, and extended care services to a covered veteran under this section; and (B) the Secretary shall furnish hospital care, medical services, and extended care services to a covered veteran under this section with the same conditions on the ability of the veteran to choose health care providers as specified in the pilot program described in section 2 of such Act. .\n**(B) Veterans Care Agreements**\nSection 1703A(a)(1) of such title is amended\u2014\n**(i)**\nin subparagraph (C), by striking For purposes and inserting Except as provided by subparagraph (E), for purposes ; and\n**(ii)**\nby adding at the end the following new subparagraph:\n(E) Beginning on the date that is four years after the date of the enactment of the Veterans Health Care Freedom Act \u2014 (i) the requirement under subparagraph (A) and (C) that care or services may only be furnished under this section to covered individuals when such care or services are not feasibly available to the covered individual from a facility of the Department or through a contract or sharing agreement entered into pursuant to a provision of law other than this section shall not apply with respect to furnishing hospital care, medical services, and extended care services to a covered individual under this section; and (ii) the Secretary shall furnish hospital care, medical services, and extended care services to a covered individual under this section with the same conditions on the ability of the individual to choose health care providers as specified in the pilot program described in section 2 of such Act. .\n**(C) V ISN s**\nBeginning on the date that is four years after the date of the enactment of this Act, the Secretary shall furnish hospital care, medical services, and extended care services to veterans under chapter 17 of title 38, United States Code, at medical facilities of the Department of Veterans Affairs, regardless of whether the facility is in the same Veterans Integrated Service Network as the Network in which the veteran resides.\n##### (i) Reports\n**(1) Implementation**\n**(A) In general**\nOn a quarterly basis during the two-year period beginning on the date of the enactment of this Act, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the implementation of the pilot program.\n**(B) Final design**\nOne of the reports required under subparagraph (A) shall contain a description of the final design of the pilot program.\n**(2) Annual**\nOn an annual basis during the period beginning on the date that is one year after the date of the submission of the final report under paragraph (1) and ending on the date of the conclusion of the pilot program, the Secretary shall submit to the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives a report on the results of the pilot program.\n##### (j) Regulations\nThe Secretary, in consultation with the Committee on Veterans\u2019 Affairs of the Senate and the Committee on Veterans\u2019 Affairs of the House of Representatives, may prescribe regulations to carry out this section.\n##### (k) No additional appropriations\nNo additional funds are authorized to be appropriated to carry out this section and the amendments made by this section, and this section and the amendments made by this section shall be carried out using amounts otherwise made available to the Veterans Health Administration.\n##### (l) Definitions\nIn this section:\n**(1) Covered care system**\nThe term covered care system means each\u2014\n**(A)**\nmedical facility of the Department;\n**(B)**\nhealth care provider specified in subsection 1703(c) of title 38, United States Code; and\n**(C)**\neligible entity or provider that has entered into a Veterans Care Agreement under section 1703A of such title.\n**(2) Eligible veteran**\nThe term eligible veteran means a veteran who is enrolled in the patient enrollment system of the Department of Veterans Affairs under section 1705 of title 38, United States Code.\n**(3) Hospital care; medical services; non-Department facilities**\nThe terms hospital care , medical services , and non-Department facilities have the meanings given those terms in section 1701 of title 38, United States Code.",
      "versionDate": "2025-01-23",
      "versionType": "Introduced in Senate"
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-21T19:23:17Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-03-21T19:23:27Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-03-21T19:23:38Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-03-21T19:23:48Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-21T19:23:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-25T14:56:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119s219",
          "measure-number": "219",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-03-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s219v00",
            "update-date": "2025-03-06"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Veterans Health Care Freedom Act</strong></p><p>This bill requires the Center for Innovation for Care and Payment within the Department of Veterans Affairs (VA) to implement a three-year pilot program to provide veterans who are enrolled in the VA health care system with the ability to choose health care providers through the covered care system. Under the bill, the<em> covered care system</em> includes VA medical facilities, health care providers participating in the Veterans Community Care Program (VCCP), and eligible entities or providers that have entered into a Veterans Care Agreement.</p><p>A veteran participating in the program may elect to receive care at any provider in the covered care system.</p><p>The pilot program removes certain requirements (e.g., location of the veteran) to access care at VA and non-VA facilities. After four years, the bill permanently phases out the requirements for accessing care under the VCCP and Veterans Care Agreements and requires the VA to provide such care under the same conditions of the pilot program. Additionally, after four years, veterans may receive care at a VA medical facility regardless of whether the facility is in the same Veterans Integrated Service Network as the veteran.</p>"
        },
        "title": "Veterans Health Care Freedom Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s219.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans Health Care Freedom Act</strong></p><p>This bill requires the Center for Innovation for Care and Payment within the Department of Veterans Affairs (VA) to implement a three-year pilot program to provide veterans who are enrolled in the VA health care system with the ability to choose health care providers through the covered care system. Under the bill, the<em> covered care system</em> includes VA medical facilities, health care providers participating in the Veterans Community Care Program (VCCP), and eligible entities or providers that have entered into a Veterans Care Agreement.</p><p>A veteran participating in the program may elect to receive care at any provider in the covered care system.</p><p>The pilot program removes certain requirements (e.g., location of the veteran) to access care at VA and non-VA facilities. After four years, the bill permanently phases out the requirements for accessing care under the VCCP and Veterans Care Agreements and requires the VA to provide such care under the same conditions of the pilot program. Additionally, after four years, veterans may receive care at a VA medical facility regardless of whether the facility is in the same Veterans Integrated Service Network as the veteran.</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119s219"
    },
    "title": "Veterans Health Care Freedom Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Veterans Health Care Freedom Act</strong></p><p>This bill requires the Center for Innovation for Care and Payment within the Department of Veterans Affairs (VA) to implement a three-year pilot program to provide veterans who are enrolled in the VA health care system with the ability to choose health care providers through the covered care system. Under the bill, the<em> covered care system</em> includes VA medical facilities, health care providers participating in the Veterans Community Care Program (VCCP), and eligible entities or providers that have entered into a Veterans Care Agreement.</p><p>A veteran participating in the program may elect to receive care at any provider in the covered care system.</p><p>The pilot program removes certain requirements (e.g., location of the veteran) to access care at VA and non-VA facilities. After four years, the bill permanently phases out the requirements for accessing care under the VCCP and Veterans Care Agreements and requires the VA to provide such care under the same conditions of the pilot program. Additionally, after four years, veterans may receive care at a VA medical facility regardless of whether the facility is in the same Veterans Integrated Service Network as the veteran.</p>",
      "updateDate": "2025-03-06",
      "versionCode": "id119s219"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s219is.xml"
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
      "title": "Veterans Health Care Freedom Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Veterans Health Care Freedom Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Veterans Affairs to carry out a pilot program to improve the ability of veterans to access medical care in medical facilities of the Department of Veterans Affairs and in the community by providing veterans the ability to choose health care providers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:49Z"
    }
  ]
}
```
