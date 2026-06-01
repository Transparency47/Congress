# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7801?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7801
- Title: Cloud LAB Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7801
- Origin chamber: House
- Introduced date: 2026-03-04
- Update date: 2026-04-02T18:04:39Z
- Update date including text: 2026-04-02T18:04:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2026-03-04: Introduced in House

## Actions

- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7801",
    "number": "7801",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "O000019",
        "district": "23",
        "firstName": "Jay",
        "fullName": "Rep. Obernolte, Jay [R-CA-23]",
        "lastName": "Obernolte",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Cloud LAB Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-02T18:04:39Z",
    "updateDateIncludingText": "2026-04-02T18:04:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T15:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MA"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "GA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7801ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7801\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2026 Mr. Obernolte (for himself, Mr. Khanna , Mr. Auchincloss , and Mr. McCormick ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo require the Director of the National Science Foundation to carry out a cloud laboratory network program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cloud Labs to Advance Biotechnology Act of 2026 or the Cloud LAB Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) Artificial intelligence**\nThe term artificial intelligence has the meaning given such term in section 5002 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 9401 ).\n**(2) Authorized researcher**\nThe term authorized researcher means an individual who has been appropriately authorized to access data generated by the cloud laboratories through a process established by the Director in establishing the cloud laboratory network.\n**(3) Biological data**\nThe term biological data means the information, including associated descriptors, derived from the structure, function, or process of a biological system that is either measured, collected, or aggregated for analysis.\n**(4) Cloud laboratory**\nThe term cloud laboratory means a physical laboratory that is equipped with research instrumentation and advanced robots that can be programmed and controlled remotely by scientists in order to conduct continuous experiments and collect associated data.\n**(5) Director**\nThe term Director means the Director of the National Science Foundation.\n**(6) Phase II cloud laboratory**\nThe term phase II cloud laboratory means a cloud laboratory funded by a grant awarded under section 3(c).\n**(7) Phase III cloud laboratory**\nThe term phase III cloud laboratory means a cloud laboratory funded by a grant awarded under section 3(d).\n**(8) Under Secretary**\nThe term Under Secretary means the Under Secretary of Commerce for Standards and Technology and Director of the National Institute of Standards and Technology.\n#### 3. Cloud laboratory network pilot program\n##### (a) Program established\n**(1) Authorization**\nThe Director, in consultation with the Secretary of Energy, and the Under Secretary, shall carry out a pilot program in accordance with this section that establishes a cloud laboratory network that helps to coordinate the activities of cloud laboratories established by the Director and cloud laboratories independently operated by other entities (such as private industry, government laboratories, and academic institutions), to further the purposes described in paragraph (3).\n**(2) Consultation**\nThe Director shall consult, to the greatest extent practicable, with other departments and agencies involved with cloud laboratories, and any government entities responsible for interagency coordination of biotechnology, such as that in the Executive Office of the President, to deduplicate efforts from different programs, and to increase awareness and connectivity of the cloud laboratory network established under subsection (b)(1).\n**(3) Purpose of the cloud laboratory network**\nThe cloud laboratory network described in paragraph (1) shall\u2014\n**(A)**\nserve the purpose of tracking and cataloging the different biotechnology capabilities at each cloud laboratory;\n**(B)**\nhelp researchers connect to the capabilities needed to pursue a line of research; and\n**(C)**\nprovide the opportunity for cloud laboratories to connect and collaborate on best practices, including data collection and data sharing, data standards, and needs.\n**(4) Cloud laboratory purposes**\nEach cloud laboratory supported under this section shall accomplish the following purposes:\n**(A)**\nGenerate high-quality biological data through automated experimentation that will be collected for use and analysis by authorized researchers for the purposes of training artificial intelligence models or other types of biological data analysis models.\n**(B)**\nProvide researchers access to high-quality experimental instrumentation and data collection for the purposes of advancing individual research projects.\n##### (b) Phase I of cloud laboratory network pilot program\n**(1) Establishment of the cloud laboratory network**\nNot later than 360 days after the date of enactment of this Act, the Director, in consultation with the Secretary of Energy and the Under Secretary, shall establish the cloud laboratory network as described in subsection (a)(1).\n**(2) Implementation plan**\nNot later than 360 days after the date of enactment of this Act, the Director, in consultation with the Secretary of Energy, the Under Secretary, and others as appropriate, shall prepare and submit an implementation plan to Congress that includes the following:\n**(A)**\nAn assessment of the state of public and private cloud laboratories in the United States, particularly cloud laboratories focused on biotechnology, as of the date of the report, including the number of cloud laboratories, the location of the cloud laboratories, and the financing or payment mechanism for each cloud laboratory.\n**(B)**\nAn implementation plan for a national cloud laboratory network and an associated grant program that includes a mechanism for deciding on the location of each cloud laboratory funded under the grant program in this section.\n**(C)**\nA plan to coordinate the network of cloud laboratories that are already established, in addition to those funded under this section.\n**(D)**\nA plan outlining how data generated through the cloud laboratories will be stored, published, and made available and accessible to authorized researchers as a public resource, including a plan to have the data made publicly available in a secure and accessible format.\n**(E)**\nA scheme for access to data generated through the cloud laboratories funded under this section and the payment or subscription model that will be required to access the cloud laboratory infrastructure and such data, which\u2014\n**(i)**\ndescribes how users can apply and use the infrastructure for the cloud laboratories funded under this section;\n**(ii)**\nallows users doing nonproprietary work to access such cloud laboratories at no or minimal cost; and\n**(iii)**\nincludes a request for information to industry to understand what companies would need in order to subscribe to such a data generation service.\n**(F)**\nAn outline of sample intellectual property agreements for the cloud laboratories funded under this section related to all data gathering and experimentation, which may include different agreements in order to further the different purposes described in subsection (a)(2).\n**(G)**\nA plan for engagement with industry and academic institutions that manage cloud laboratories to include them in the cloud laboratory network.\n**(H)**\nA plan for building in considerations related to cybersecurity, biosecurity, and research security from the beginning of development for each cloud laboratory.\n**(I)**\nThe estimated cost of carrying out the full pilot program establishing the cloud laboratory network broken down by year.\n**(3) Cloud laboratory advisory board**\n**(A) Consultation**\nIn preparing the implementation plan under paragraph (2), the Director shall consult with the advisory board established under this paragraph.\n**(B) Establishment**\nNot later than 180 days after the date of enactment of this Act, the Director shall establish, and lead, a cloud laboratory advisory board (referred to in this paragraph as the advisory board ).\n**(C) Members**\n**(i) Composition**\nThe advisory board shall consist of\u2014\n**(I)**\nemployees of the National Science Foundation and employees of such other Federal agencies as the Director determines appropriate;\n**(II)**\nacademic researchers in all areas of biotechnology, including computational biology, synthetic biology, cell biology, structural biology, robotics, and analytical chemistry;\n**(III)**\nresearchers and practitioners in the fields of biosafety, biosecurity, ethics, and relevant social science disciplines; and\n**(IV)**\nindustry representatives from different sectors of biotechnology, including health, agriculture, chemical production, and platform technologies.\n**(ii) Selection**\nThe selection and number of people on the advisory board shall be at the discretion of the Director.\n**(D) Duties**\nThe advisory board shall\u2014\n**(i)**\npropose biological data collection priorities through consultation with the biotechnology research community, including academia and private companies;\n**(ii)**\nadvise in ways that the cloud laboratories funded under this section are developed and expanded in such a way that maximizes usability across the disciplines of biotechnology while minimizing duplication across the network of cloud laboratories funded under this section;\n**(iii)**\nadvise on the definition of authorized researcher to ensure research security, but also allow access to all tiers of research and teaching institutions;\n**(iv)**\nproduce an annual report outlining all recommendations and actions that were taken over the course of the year; and\n**(v)**\nprovide guidance and recommendations to the Director regarding\u2014\n**(I)**\nensuring that appropriate safeguards are in place to prevent the misuse of cloud laboratories funded under this section; and\n**(II)**\nensuring the implementation of a rigorous cybersecurity scheme across the network of such cloud laboratories.\n**(E) Termination**\nThe advisory board shall terminate on the date that is 12 years after the date of enactment of this Act.\n##### (c) Phase II cloud laboratory awards\n**(1) Awards authorized**\nNot later than 2 years after the date of enactment of this Act, and subject to the availability of appropriations, the Director, in consultation with the Secretary of Energy, the Under Secretary, and the relevant individual in the Executive Office of the President responsible for coordinating interagency efforts related to biotechnology, shall, using the process developed in subsection (b)(2)(B), make grant awards, on a competitive basis, for the development and operation of not fewer than 2 cloud laboratories.\n**(2) Operational deadline**\nEach phase II cloud laboratory shall be fully operational by the date that is 3 years after the date of enactment of this Act.\n**(3) Duration**\nAn award under this subsection for a phase II cloud laboratory shall be for not less than an 8-year period.\n##### (d) Phase III cloud laboratory awards\n**(1) Awards authorized**\nNot later than 4 years after the date of enactment of this Act, and subject to the availability of appropriations, the Director, in consultation with the Secretary of Energy and the Under Secretary, shall make grant awards, on a competitive basis, for the development and operation of not fewer than 3 cloud laboratories.\n**(2) Relationship to phase II cloud laboratories**\nThe phase III cloud laboratories shall be separate, and in addition to, the phase II cloud laboratories.\n**(3) Duration**\nAn award under this subsection for a phase III cloud laboratory shall be for not less than a 6-year period.\n**(4) Award basis**\nIn making awards under this subsection, the Director shall utilize a similar competitive process as used for awards for phase II cloud laboratories, which may be adjusted based on lessons learned from the establishment of the phase II cloud laboratories.\n##### (e) Cloud laboratory pilot award program implementation reports\nBeginning 1 year after the date on which all awards are made for phase II cloud laboratories, and annually thereafter, the Director shall prepare and submit a report to Congress regarding the progress, including any successes, of all cloud laboratories supported under the pilot grant program under this section.\n##### (f) Sunset\nThis section shall cease to have effect on the date that is 12 years after the date of enactment of this Act.",
      "versionDate": "2026-03-04",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-04-02T18:04:38Z"
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
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7801ih.xml"
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
      "title": "To require the Director of the National Science Foundation to carry out a cloud laboratory network program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:34Z"
    },
    {
      "title": "Cloud LAB Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cloud LAB Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cloud Labs to Advance Biotechnology Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:19Z"
    }
  ]
}
```
