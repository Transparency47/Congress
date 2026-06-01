# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/71?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/71
- Title: Veterans Health Care Freedom Act
- Congress: 119
- Bill type: HR
- Bill number: 71
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-15T09:07:12Z
- Update date including text: 2025-02-15T09:07:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-06 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-06 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/71",
    "number": "71",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Veterans Health Care Freedom Act",
    "type": "HR",
    "updateDate": "2025-02-15T09:07:12Z",
    "updateDateIncludingText": "2025-02-15T09:07:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-06T17:43:38Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AZ"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "FL"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "FL"
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
      "sponsorshipDate": "2025-01-03",
      "state": "AZ"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "FL"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "OK"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "FL"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "IL"
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
      "sponsorshipDate": "2025-01-13",
      "state": "WY"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "WI"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "OH"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr71ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 71\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself, Mr. Crane , Mr. Webster of Florida , Ms. Salazar , Mr. Gosar , Mrs. Luna , and Mr. Brecheen ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to carry out a pilot program to improve the ability of veterans to access medical care in medical facilities of the Department of Veterans Affairs and in the community by providing the veterans the ability to choose health care providers.\n#### 1. Short title\nThis Act may be cited as the Veterans Health Care Freedom Act .\n#### 2. Pilot program on ability of veterans to choose health care providers\n##### (a) Pilot program\n**(1) Requirement**\nThe Secretary of Veterans Affairs, acting through the Center for Innovation for Care and Payment, shall carry out a pilot program to improve the ability of eligible veterans to access hospital care, medical services, and extended care services through the covered care system by providing the eligible veterans the ability to choose health care providers.\n**(2) Locations**\nThe Secretary shall select a minimum of four Veterans Integrated Service Networks in which to carry out the pilot program under paragraph (1). In making such selection, the Secretary shall ensure that the pilot program is carried out in varied geographic areas that include both rural and urban locations.\n##### (b) Removal of certain requirements To access care\nIn carrying out the pilot program under subsection (a), the Secretary shall furnish hospital care, medical services, and extended care services to eligible veterans through the covered care system as follows:\n**(1)**\nAt medical facilities of the Department of Veterans Affairs, regardless of whether the facility is in the same Veterans Integrated Service Network as the Network in which the veteran resides.\n**(2)**\nAt non-Department facilities pursuant to, as appropriate\u2014\n**(A)**\nsection 1703 of title 38, United States Code, without regard to the requirements specified in subsection (d) of such section; or\n**(B)**\nsection 1703A of such title, without regard to the requirements specified in subsection (a)(1)(C) of such section.\n##### (c) Election of veteran\nIn accordance with subsections (d) and (e), an eligible veteran participating in the pilot program may elect to receive hospital care, medical services, and extended care services at any provider in the covered care system.\n##### (d) Coordination of care\n**(1) Selection**\nEach eligible veteran participating in the pilot program shall select a primary care provider in the covered care system. The primary care provider shall\u2014\n**(A)**\ncoordinate with the Secretary and other health care providers the hospital care, medical services, and extended care services furnished to the veteran under the pilot program; and\n**(B)**\nrefer the veteran to specialty care providers in the covered care system, as clinically necessary.\n**(2) Systems**\nThe Secretary shall establish systems as the Secretary determines appropriate to ensure that a primary care provider can effectively coordinate the hospital care, medical services, and extended care services furnished to a veteran under the pilot program.\n##### (e) Specialty care\n**(1) Access**\nSubject to subsection (d)(1)(B), an eligible veteran participating in the pilot program may select any specialty care provider in the covered care system from which to receive specialty care.\n**(2) Designation**\nThe Secretary may designate a specialty care provider as a primary care provider of an eligible veteran participating in the pilot program if the Secretary determines that such designation is in the health interests of the veteran (such as an endocrinologist with respect to a veteran diagnosed with diabetes, a neurologist with respect to a veteran diagnosed with Parkinson\u2019s disease, or an obstetrician-gynecologist with respect to a female veteran).\n##### (f) Mental health care\nAn eligible veteran participating in the pilot program may select a mental health care provider in the covered care system from which to receive mental health care.\n##### (g) Information\nIn carrying out the pilot program, the Secretary shall furnish to eligible veterans the information on eligibility, cost sharing, treatments, and providers required for veterans to make informed decisions with respect to\u2014\n**(1)**\nselecting primary care providers and specialty care providers; and\n**(2)**\ntreatments available to the veteran.\n##### (h) Duration\n**(1) Phase in**\nThe Secretary shall carry out the pilot program during the three-year period beginning on the date that is one year after the date of the enactment of this Act.\n**(2) Permanent requirement**\n**(A) Veterans Community Care Program**\nSection 1703(d) of title 38, United States Code, is amended\u2014\n**(i)**\nin paragraph (1), by striking The Secretary shall and inserting Except as provided by paragraph (5), the Secretary shall ; and\n**(ii)**\nby adding at the end the following new paragraph:\n(5) Beginning on the date that is four years after the date of the enactment of the Veterans Health Care Freedom Act\u2014 (A) the requirements under paragraphs (1), (2), and (3) shall not apply with respect to furnishing hospital care, medical services, and extended care services to a covered veteran under this section; and (B) the Secretary shall furnish hospital care, medical services, and extended care services to a covered veteran under this section with the same conditions on the ability of the veteran to choose health care providers as specified in the pilot program described in section 2 of such Act. .\n**(B) Veterans Care Agreements**\nSection 1703A(a)(1) of such title is amended\u2014\n**(i)**\nin subparagraph (C), by striking For purposes and inserting Except as provided by subparagraph (E), for purposes ; and\n**(ii)**\nby adding at the end the following new subparagraph:\n(E) Beginning on the date that is four years after the date of the enactment of the Veterans Health Care Freedom Act\u2014 (i) the requirements under subparagraph (C) shall not apply with respect to furnishing hospital care, medical services, and extended care services to a covered veteran under this section; and (ii) the Secretary shall furnish hospital care, medical services, and extended care services to a covered veteran under this section with the same conditions on the ability of the veteran to choose health care providers as specified in the pilot program described in section 2 of such Act. .\n**(C) V ISN s**\nBeginning on the date that is four years after the date of the enactment of this Act, the Secretary shall furnish hospital care, medical services, and extended care services to veterans under chapter 17 of title 38, United States Code, at medical facilities of the Department of Veterans Affairs, regardless of whether the facility is in the same Veterans Integrated Service Network as the Network in which the veteran resides.\n##### (i) Reports\n**(1) Implementation**\nOn a quarterly basis during the two-year period beginning on the date of the enactment of this Act, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report on the implementation of the pilot program. One such report shall contain a description of the final design of the pilot program.\n**(2) Annual**\nOn an annual basis during the period beginning on the date that is one year after the date of the submission of the final report under paragraph (1) and ending on the date of the conclusion of the pilot program, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report on the results of the pilot program.\n##### (j) Regulations\nThe Secretary, in consultation with the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate, may prescribe regulations to carry out this section.\n##### (k) No additional appropriations\nNo additional funds are authorized to be appropriated to carry out this section, and this section shall be carried out using amounts otherwise made available to the Veterans Health Administration.\n##### (l) Definitions\nIn this section:\n**(1)**\nThe term covered care system means each\u2014\n**(A)**\nmedical facility of the Department;\n**(B)**\nhealth care provider specified in subsection 1703(c) of title 38, United States Code; and\n**(C)**\neligible entity or provider that has entered into a Veterans Care Agreement under section 1703A of such title.\n**(2)**\nThe term eligible veteran means a veteran who is enrolled in the patient enrollment system of the Department of Veterans Affairs under section 1705 of title 38, United States Code.\n**(3)**\nThe term non-Department facility has the meaning given that term in section 1701 of title 38, United States Code.",
      "versionDate": "2025-01-03",
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
            "name": "Congressional oversight",
            "updateDate": "2025-02-05T21:05:30Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-02-05T21:05:30Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-02-05T21:05:30Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-02-05T21:05:30Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-02-05T21:05:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-01-31T16:51:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr71",
          "measure-number": "71",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr71v00",
            "update-date": "2025-02-03"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans Health Care Freedom Act</strong></p> <p>This bill requires the Center for Innovation for Care and Payment within the Department of Veterans Affairs (VA) to implement a three-year pilot program to improve the ability of veterans who are enrolled in the VA health care system to access hospital care, medical services, and extended care services through the covered care system by providing such veterans with the ability to choose health care providers. Under the bill, the<em> covered care system</em> includes VA medical facilities, health care providers participating in the Veterans Community Care Program (VCCP), and eligible entities or providers that have entered into a Veterans Care Agreement.</p> <p>A veteran participating in the program may elect to receive care at any provider in the covered care system.</p> <p>The pilot program removes certain requirements (e.g., location of the veteran) to access care at VA and non-VA facilities. After four years, the bill permanently phases out the requirements for accessing care under the VCCP and Veterans Care Agreements and requires the VA to provide such care under the same conditions of the pilot program. Additionally, after four years, veterans may receive care at a VA medical facility regardless of whether the facility is in the same Veterans Integrated Service Network as the veteran.<br/> </p>"
        },
        "title": "Veterans Health Care Freedom Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr71.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Health Care Freedom Act</strong></p> <p>This bill requires the Center for Innovation for Care and Payment within the Department of Veterans Affairs (VA) to implement a three-year pilot program to improve the ability of veterans who are enrolled in the VA health care system to access hospital care, medical services, and extended care services through the covered care system by providing such veterans with the ability to choose health care providers. Under the bill, the<em> covered care system</em> includes VA medical facilities, health care providers participating in the Veterans Community Care Program (VCCP), and eligible entities or providers that have entered into a Veterans Care Agreement.</p> <p>A veteran participating in the program may elect to receive care at any provider in the covered care system.</p> <p>The pilot program removes certain requirements (e.g., location of the veteran) to access care at VA and non-VA facilities. After four years, the bill permanently phases out the requirements for accessing care under the VCCP and Veterans Care Agreements and requires the VA to provide such care under the same conditions of the pilot program. Additionally, after four years, veterans may receive care at a VA medical facility regardless of whether the facility is in the same Veterans Integrated Service Network as the veteran.<br/> </p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hr71"
    },
    "title": "Veterans Health Care Freedom Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Health Care Freedom Act</strong></p> <p>This bill requires the Center for Innovation for Care and Payment within the Department of Veterans Affairs (VA) to implement a three-year pilot program to improve the ability of veterans who are enrolled in the VA health care system to access hospital care, medical services, and extended care services through the covered care system by providing such veterans with the ability to choose health care providers. Under the bill, the<em> covered care system</em> includes VA medical facilities, health care providers participating in the Veterans Community Care Program (VCCP), and eligible entities or providers that have entered into a Veterans Care Agreement.</p> <p>A veteran participating in the program may elect to receive care at any provider in the covered care system.</p> <p>The pilot program removes certain requirements (e.g., location of the veteran) to access care at VA and non-VA facilities. After four years, the bill permanently phases out the requirements for accessing care under the VCCP and Veterans Care Agreements and requires the VA to provide such care under the same conditions of the pilot program. Additionally, after four years, veterans may receive care at a VA medical facility regardless of whether the facility is in the same Veterans Integrated Service Network as the veteran.<br/> </p>",
      "updateDate": "2025-02-03",
      "versionCode": "id119hr71"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr71ih.xml"
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
      "title": "Veterans Health Care Freedom Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Health Care Freedom Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to carry out a pilot program to improve the ability of veterans to access medical care in medical facilities of the Department of Veterans Affairs and in the community by providing the veterans the ability to choose health care providers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T05:18:38Z"
    }
  ]
}
```
