# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4473?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4473
- Title: BIRD Health Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4473
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2026-05-16T08:08:01Z
- Update date including text: 2026-05-16T08:08:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4473",
    "number": "4473",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000814",
        "district": "14",
        "firstName": "Randy",
        "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
        "lastName": "Weber",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "BIRD Health Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:08:01Z",
    "updateDateIncludingText": "2026-05-16T08:08:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
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
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:01:05Z",
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
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NH"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "NY"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "NY"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "MN"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "FL"
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
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-05-15",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4473ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4473\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Mr. Weber of Texas (for himself, Mr. Pappas , and Ms. Tenney ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services to establish a bilateral research and innovation program to facilitate and coordinate efforts between the United States and Israel in certain health-related areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the United States-Israel Bilateral Innovation for Research and Development in Health Act of 2025 or the BIRD Health Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Binational Industrial Research and Development Foundation (in this Act referred to as the BIRD Foundation ) was established in 1977 as a joint initiative between the United States and Israel and has become a model for successful bilateral research and development collaboration.\n**(2)**\nSince its inception, the BIRD Foundation has approved over 1,000 projects with a total investment exceeding $500 million, generating over $10 billion in sales.\n**(3)**\nIn the past decade, approximately 30 percent of the projects approved by the BIRD Foundation have been related to health, biotechnology, life sciences, medical devices, diagnostics, and telemedicine.\n**(4)**\nThe United States and Israel have successfully expanded the activities of the Bird Foundation into dedicated programs targeting specific industrial needs, including energy, cyber, and homeland security.\n**(5)**\nThe United States and Israel signed a health, medical, and scientific cooperation agreement on January 4, 2016, which is designed to foster collaboration in various health-related areas.\n**(6)**\nIn 2020, Congress allocated $2 million to establish a bilateral collaboration program with the Israel for the development of health-related technologies.\n#### 3. Establishment of BIRD Health Program\n##### (a) Establishment\n**(1) In general**\nThe Secretary of Health and Human Services shall enter into a cooperative agreement to establish a bilateral research and innovation program (in this Act referred to as the BIRD Health Program ) to facilitate and coordinate efforts between the United States and Israel to expand and enhance collaboration on\u2014\n**(A)**\nthe development of healthcare products and services; and\n**(B)**\nthe delivery of such products and services to individuals in need.\n**(2) Coordination**\nThe Secretary of Health and Human Services shall carry out this subsection in coordination with the Secretary of Commerce and the Executive Director of the BIRD Foundation.\n**(3) Applicability of requirements**\nThe authority provided by this subsection shall be subject to any applicable requirements of law and any applicable agreements or understandings between the United States and Israel.\n##### (b) Program administration, goals, and components\nThe cooperation agreement referred to in subsection (a) shall provide for the following:\n**(1) Implementation partner**\nThe BIRD Health Program shall be administered by the BIRD Foundation, following the same model used for United States-Israel collaborations in energy, cyber, and homeland security.\n**(2) Governance**\nThe program shall be jointly governed by representatives from the Department of Health and Human Services and the Ministry of Health of Israel, who shall actively participate in defining focus areas and selecting projects to receive funding.\n**(3) Program goals**\nThe goals of the BIRD Health Program shall be\u2014\n**(A)**\nto facilitate joint research and development projects between United States and Israeli institutions, companies, and academic organizations in the field of health technologies;\n**(B)**\nto support the commercialization and deployment of innovative healthcare products and services, including\u2014\n**(i)**\nmedical devices and diagnostics;\n**(ii)**\npharmaceuticals and biological products;\n**(iii)**\ngenomics and personalized medicine;\n**(iv)**\ntelemedicine and digital health technologies;\n**(v)**\nartificial intelligence for healthcare applications;\n**(vi)**\ninfectious disease prevention;\n**(vii)**\nvaccine development; and\n**(viii)**\nepidemiological research; and\n**(C)**\nto strengthen health-related ecosystems by fostering United States-Israel partnerships in healthcare technology development.\n**(4) Program components**\n**(A) In general**\nThe BIRD Health Program shall provide funding for the following:\n**(i) Research and development**\nPrograms and activities for research and development, including\u2014\n**(I)**\njoint research projects between United States and Israeli institutions and companies;\n**(II)**\npromoting collaboration in areas such as medical device technology, pharmaceuticals (including biological products, genomics, and innovative digital health care solutions) and health care systems management (including a special focus on early-stage clinical trials);\n**(III)**\nwith respect to biological products, supporting\u2014\n**(aa)**\ninnovation;\n**(bb)**\nprocess optimization; and\n**(cc)**\nthe development of advanced manufacturing techniques that can enhance productivity, reduce costs, and improve product quality; and\n**(IV)**\nwork toward developing a framework for sharing health data for research purposes with the Ministry of Health of Israel.\n**(ii) Innovation and startup ecosystem**\nPrograms and activities for health-related ecosystems, including\u2014\n**(I)**\nfostering collaboration between United States and Israeli startup companies and other companies in the healthcare sector;\n**(II)**\nfacilitating innovative technology acceptance by the marketplace;\n**(III)**\nfacilitating mechanisms for technology transfer and joint venture opportunities; and\n**(IV)**\nsupporting innovation hubs to accelerate the development and commercialization of United States healthcare technologies in the Israeli market, including encouraging cybersecurity standards for sharing data, promoting patient privacy, and encouraging research.\n**(iii) Health care system strengthening**\nPrograms and activities for health care system strengthening, including facilitating sharing best practices, knowledge, and skills in areas such as clinical care and health care management.\n**(B) Telemedicine and digital health cooperation**\nThe BIRD Health Program shall provide funding for programs and activities for telemedicine and digital health cooperation for establishing initiatives\u2014\n**(i)**\nto enhance telemedicine infrastructure;\n**(ii)**\nto promote interoperability between United States and Israeli health care systems; and\n**(iii)**\nto facilitate collaboration on digital health technologies, data analytics, and cybersecurity.\n**(C) Disease prevention initiatives**\nThe BIRD Health Program shall provide funding for collaborating in disease prevention, including joint efforts to combat infectious diseases, develop vaccines, and share epidemiological data.\n**(D) Biological product manufacturing**\nThe BIRD Health Program shall provide funding for\u2014\n**(i)**\npromoting biological product manufacturing;\n**(ii)**\nestablishing joint manufacturing facilities for biological products in facilities in the United States that leverage the strengths and expertise of both countries;\n**(iii)**\npursuing accelerated development of life-saving treatments and new sources of nutrition that are both healthier and more available at an affordable cost; and\n**(iv)**\nsupply chain resilience through strategic collaboration to identify and develop contingency plans to mitigate biological product supply disruptions.\n**(5) Project selection criteria**\nProjects selected for funding under the BIRD Health program shall be evaluated based on\u2014\n**(A)**\ntechnical merit and innovation;\n**(B)**\ncommercial potential and economic impact;\n**(C)**\nrelevance to health priorities identified by both governments;\n**(D)**\nstrength of the United States-Israel partnership; and\n**(E)**\npotential to address unmet medical needs.\n#### 4. Funding and implementation\n##### (a) Funding\n**(1) Authorization of appropriations**\nThere is authorized to be appropriated to the Secretary of Health and Human Services to carry out this Act $10,000,000 for each of fiscal years 2026 through 2032.\n**(2) Administration of funds**\nSubject to the terms and conditions of the cooperative agreement referred to in section 3(a)(1), funds made available under this section shall be administered through the BIRD Foundation, with oversight from Secretary of Health and Human Services and the Secretary of Commerce.\n##### (b) Implementation timeline\n**(1) Program framework**\nNot later than 180 days after the date of enactment of this Act, the Secretary of Health and Human Services shall submit to Congress a report on the progress made in establishing the program framework.\n**(2) Proposals**\nNot later than one year after the date of establishment of the program framework, the BIRD Health Program shall begin accepting proposals and allocating funds for eligible projects.\n#### 5. Reporting and evaluation\n##### (a) Annual report to Congress\nNot later than one year after the date of enactment of this Act, and annually thereafter, the Secretary of Health and Human Services shall submit to Congress an annual report detailing the establishment and implementation of the BIRD Health Program, including\u2014\n**(1)**\nthe progress of funded projects and their impact on healthcare innovation;\n**(2)**\nthe economic and scientific benefits resulting from United States-Israel collaborations; and\n**(3)**\nany policy recommendations to enhance the effectiveness of the BIRD Health Program.\n##### (b) Program Review\nThe Secretary of Health and Human Services shall conduct, and submit to Congress, a comprehensive review of the success of the BIRD Health Program every three years, with recommendations for renewal or expansion.\n#### 6. Health technology defined\nIn this Act, the term health technology includes a medical device, pharmaceutical, digital health solution, diagnostic driven by artificial intelligence, and biologic.",
      "versionDate": "2025-07-16",
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
        "name": "Health",
        "updateDate": "2025-09-09T15:11:16Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4473ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BIRD Health Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-29T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "United States-Israel Bilateral Innovation for Research and Development in Health Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-29T05:53:21Z"
    },
    {
      "title": "BIRD Health Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-29T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to establish a bilateral research and innovation program to facilitate and coordinate efforts between the United States and Israel in certain health-related areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-29T05:48:17Z"
    }
  ]
}
```
