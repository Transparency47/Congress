# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/661?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/661
- Title: MIRACLE Medical Technology Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 661
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-04-08T17:33:35Z
- Update date including text: 2026-04-08T17:33:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/661",
    "number": "661",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "MIRACLE Medical Technology Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-08T17:33:35Z",
    "updateDateIncludingText": "2026-04-08T17:33:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
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
        "item": {
          "date": "2025-01-23T15:05:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr661ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 661\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Buchanan (for himself, Mr. Soto , and Mrs. Miller-Meeks ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Secretary of Health and Human Services, in consultation with the Secretary of Commerce, the Council for Technology and Innovation of the Centers for Medicare & Medicaid Services, and the Commissioner of Food and Drugs, to carry out a program to facilitate and coordinate efforts between the United States and Israel to expand and enhance collaboration on the development and delivery of health care products and services.\n#### 1. Short title\nThis Act may be cited as the Maximizing Israel-U.S. Research Advancement and Collaborative Leadership in Emerging Medical Technology Act of 2025 or the MIRACLE Medical Technology Act of 2025 .\n#### 2. Program for facilitation and coordination of United States-Israel efforts on the development and delivery of health care products and services\n##### (a) In general\nSubject to the availability of appropriations, the Secretary of Health and Human Services, in consultation with the Secretary of Commerce, the Council for Technology and Innovation of the Centers for Medicare & Medicaid Services, and the Commissioner of Food and Drugs, shall carry out a program to facilitate and coordinate efforts between the United States and Israel to expand and enhance collaboration on\u2014\n**(1)**\nthe development of health care products and services; and\n**(2)**\nthe delivery of such products and services to those in need.\n##### (b) Program components\nThe program under subsection (a) shall include facilitation and coordination of efforts including each of the following:\n**(1) Research and development**\n**(A)**\nJoint research projects between United States and Israeli institutions and companies.\n**(B)**\nPromoting collaboration in areas such as medical device technology, pharmaceuticals (including biological products, genomics, and innovative digital health care solutions), and health care systems management, including a special focus on early-stage clinical trials.\n**(C)**\nWith respect to biological products, supporting\u2014\n**(i)**\ninnovation;\n**(ii)**\nprocess optimization; and\n**(iii)**\nthe development of advanced manufacturing techniques that can enhance productivity, reduce costs, and improve product quality.\n**(D)**\nWork toward developing a framework for sharing health data for research purposes with the Ministry of Health of Israel.\n**(2) Innovation and start-up ecosystem**\n**(A)**\nFostering collaboration between United States and Israeli start-up and other companies in the health care sector.\n**(B)**\nFacilitating innovative technology acceptance by the marketplace.\n**(C)**\nFacilitating mechanisms for technology transfer and joint venture opportunities.\n**(D)**\nSupporting innovation hubs to accelerate the development and commercialization of United States health care technologies in the Israeli market, including by encouraging cybersecurity standards for sharing data, promoting patient privacy, and encouraging research.\n**(3) Regulatory harmonization and intellectual property protection**\nEstablishing joint efforts\u2014\n**(A)**\nto ensure intellectual property protection;\n**(B)**\nto increase regulatory harmonization, including with respect to regulatory data protection for biological products;\n**(C)**\nto formulate plans for a commercialization framework for medical device technologies;\n**(D)**\nto encourage a potential mutual recognition agreement for pharmaceutical good manufacturing Practices between the Food and Drug Administration and Israeli regulators;\n**(E)**\nto strengthen and reaffirm the confidentiality commitment with the Food and Drug Administration and the Pharmaceutical Division, the Medical Devices Department, and the National Food Services and Nutrition Division of the Ministry of Health of Israel;\n**(F)**\nto encourage Israel\u2019s participation in regulatory harmonization and cooperation organizations; and\n**(G)**\nto expand international collaboration under Project Orbis for concurrent submission and review of oncology products.\n**(4) Health care system strengthening**\nFacilitating the sharing of best practices, knowledge, and skills in areas such as clinical care and health care management.\n**(5) Telemedicine and digital health cooperation**\nEstablishing initiatives\u2014\n**(A)**\nto enhance telemedicine infrastructure;\n**(B)**\nto promote interoperability between United States and Israeli health care systems; and\n**(C)**\nto facilitate collaboration on digital health technologies, data analytics, and cybersecurity.\n**(6) Disease prevention initiatives**\nCollaborating in disease prevention, including joint efforts to combat infectious diseases, develop vaccines, and share epidemiological data.\n**(7) Biological product manufacturing**\n**(A)**\nPromoting biological product manufacturing.\n**(B)**\nEstablishing joint manufacturing facilities for biological products in facilities in the United States that leverage the strengths and expertise of both countries.\n**(C)**\nPursuing accelerated development of life-saving treatments and new sources of nutrition that are both healthier and more available at an affordable cost.\n**(D)**\nWorkforce training and skill development, including promoting exchange programs and training initiatives to develop a skilled workforce in biological product manufacturing.\n**(E)**\nSupply chain resilience through strategic collaboration to identify and develop contingency plans to mitigate biological product supply disruptions.\n**(F)**\nFacilitating public-private partnerships to support the development and scale-up of biological product manufacturing capabilities.\n##### (c) United States-Israel Health Care Collaboration Center\nIn carrying out the program under subsection (a), the Secretary of Health and Human Services may establish a joint United States-Israel Health Care Collaboration Center in the United States leveraging the experience, knowledge, and expertise of institutions of higher education, national laboratories, entities in the private sector, and others in the development and delivery of health care products and services.\n##### (d) Commencement of implementation\nNot later than 6 months after the date of enactment of this Act, the Secretary of Health and Human Services shall commence implementation of the program under this section.\n##### (e) Authorization of appropriations\nTo carry out this Act, there is authorized to be appropriated $8,000,000 for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-01-23",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-03-17T17:40:41Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2025-03-17T17:41:21Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-08T17:33:14Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-03-17T17:40:21Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-03-17T17:41:04Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-03-17T17:40:54Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-03-17T17:40:36Z"
          },
          {
            "name": "Intellectual property",
            "updateDate": "2025-03-17T17:40:47Z"
          },
          {
            "name": "Israel",
            "updateDate": "2025-03-17T17:40:13Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-03-17T17:40:59Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-03-17T17:40:26Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-03-17T17:41:25Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-03-17T17:41:16Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-08T17:33:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-24T14:01:51Z"
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
          "measure-id": "id119hr661",
          "measure-number": "661",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr661v00",
            "update-date": "2025-04-02"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Maximizing Israel-U.S. Research Advancement and Collaborative Leadership in Emerging Medical Technology Act of 2025 or the MIRACLE Medical Technology Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to implement a program for the United States and Israel to collaborate on developing and delivering health care products and services. The program must include coordinated activities in specified areas, including research and development, use of innovative technology, intellectual property protection, regulatory harmonization, disease prevention, and biological product manufacturing. The bill authorizes\u00a0HHS to establish a joint United States-Israel Health Care Collaboration Center in the United States to leverage existing expertise for advancing the program\u2019s purposes.</p>"
        },
        "title": "MIRACLE Medical Technology Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr661.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Maximizing Israel-U.S. Research Advancement and Collaborative Leadership in Emerging Medical Technology Act of 2025 or the MIRACLE Medical Technology Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to implement a program for the United States and Israel to collaborate on developing and delivering health care products and services. The program must include coordinated activities in specified areas, including research and development, use of innovative technology, intellectual property protection, regulatory harmonization, disease prevention, and biological product manufacturing. The bill authorizes\u00a0HHS to establish a joint United States-Israel Health Care Collaboration Center in the United States to leverage existing expertise for advancing the program\u2019s purposes.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr661"
    },
    "title": "MIRACLE Medical Technology Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Maximizing Israel-U.S. Research Advancement and Collaborative Leadership in Emerging Medical Technology Act of 2025 or the MIRACLE Medical Technology Act of 2025</strong></p><p>This bill requires the Department of Health and Human Services (HHS) to implement a program for the United States and Israel to collaborate on developing and delivering health care products and services. The program must include coordinated activities in specified areas, including research and development, use of innovative technology, intellectual property protection, regulatory harmonization, disease prevention, and biological product manufacturing. The bill authorizes\u00a0HHS to establish a joint United States-Israel Health Care Collaboration Center in the United States to leverage existing expertise for advancing the program\u2019s purposes.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119hr661"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr661ih.xml"
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
      "title": "MIRACLE Medical Technology Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:50Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MIRACLE Medical Technology Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Maximizing Israel-U.S. Research Advancement and Collaborative Leadership in Emerging Medical Technology Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Health and Human Services, in consultation with the Secretary of Commerce, the Council for Technology and Innovation of the Centers for Medicare & Medicaid Services, and the Commissioner of Food and Drugs, to carry out a program to facilitate and coordinate efforts between the United States and Israel to expand and enhance collaboration on the development and delivery of health care products and services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:43Z"
    }
  ]
}
```
